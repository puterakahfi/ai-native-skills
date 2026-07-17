# Refactoring — Smells, Core Rules & Primary Refactorings

## The Core Rule

```
Refactoring = behavior-preserving transformation.

Two hats:
  Hat 1: Refactoring  — change structure, tests stay green, no new features
  Hat 2: Adding feature — add behavior, structure stays (mostly) stable

Never wear both hats at once.
```

---

## When to Refactor

**Triggered by code smells — name the smell before fixing:**

| Smell | Signal | Refactoring |
|---|---|---|
| Long Method | Method > 20 lines, hard to name | Extract Method |
| God Class | Class > 300 lines, 10+ responsibilities | Extract Class, Move Method |
| Feature Envy | Method uses another class's data more than its own | Move Method |
| Duplicate Code | Same logic in 2+ places | Extract Method, Pull Up Method |
| Long Parameter List | 4+ parameters | Introduce Parameter Object |
| Primitive Obsession | String for email, int for money | Extract Value Object |
| Conditional Complexity | Nested if/else, switch on type | Replace Conditional with Polymorphism |
| Dead Code | Unused methods/variables | Remove Dead Code |
| Shotgun Surgery | One change requires edits in 10 files | Move Method, Inline Class |
| Anemic Model | Entity with only getters, logic scattered in services | Move logic into entity |

---

## Step 0: Green Before You Start

```bash
# Run full suite — must be green before any refactoring
php artisan test        # Laravel
npm test                # Node
pytest                  # Python

# If red → fix tests first, then refactor
# Never refactor a broken codebase
```

**Gate: tests green before step 1.**

---

## Step 1: Name the Smell

```
# Wrong — vague
"This code is messy, let me clean it up"

# Right — named
"Code smell: Long Method — processOrder() is 87 lines with 3 levels of nesting.
Refactoring: Extract Method — extract payment validation to validatePayment(),
inventory check to checkInventory(), notification to notifyCustomer()"
```

---

## Step 2: Small, Independent Steps

Each step must be independently verifiable — run tests after each.

```
# Extract Method — step by step

Step 1: Identify the block to extract
Step 2: Create new method with descriptive name
Step 3: Copy block to new method
Step 4: Replace original block with method call
Step 5: Run tests → green?
Step 6: Commit

# One commit per refactoring type
git commit -m "refactor(order): extract validatePayment from processOrder"
git commit -m "refactor(order): extract checkInventory from processOrder"
git commit -m "refactor(order): extract notifyCustomer from processOrder"
```

---

## Extract Method

```php
// Before — Long Method smell
public function processOrder(Order $order): void
{
    // validate payment
    if ($order->total() <= 0) throw new InvalidAmountException();
    if (!$order->paymentToken()) throw new MissingPaymentException();
    if ($this->payments->isBlacklisted($order->customerId())) throw new BlockedCustomerException();

    // check inventory
    foreach ($order->items() as $item) {
        if (!$this->inventory->isAvailable($item->productId(), $item->qty())) {
            throw new InsufficientStockException($item->productId());
        }
    }

    // process
    $this->payments->charge($order->total(), $order->paymentToken());
    $this->inventory->reserve($order->items());
    $this->notifications->orderConfirmed($order->customerId());
}

// After — Extract Method
public function processOrder(Order $order): void
{
    $this->validatePayment($order);
    $this->checkInventory($order);
    $this->payments->charge($order->total(), $order->paymentToken());
    $this->inventory->reserve($order->items());
    $this->notifications->orderConfirmed($order->customerId());
}

private function validatePayment(Order $order): void
{
    if ($order->total() <= 0) throw new InvalidAmountException();
    if (!$order->paymentToken()) throw new MissingPaymentException();
    if ($this->payments->isBlacklisted($order->customerId())) throw new BlockedCustomerException();
}

private function checkInventory(Order $order): void
{
    foreach ($order->items() as $item) {
        if (!$this->inventory->isAvailable($item->productId(), $item->qty())) {
            throw new InsufficientStockException($item->productId());
        }
    }
}
```

---

## Extract Class (God Class)

```php
// Before — God Class smell: UserService does everything
class UserService {
    public function register() { ... }
    public function login() { ... }
    public function sendPasswordReset() { ... }   // ← email concern
    public function validateEmailFormat() { ... }  // ← validation concern
    public function calculateLoyaltyPoints() { ... } // ← loyalty concern
}

// After — Extract Class
class UserService {
    public function register() { ... }
    public function login() { ... }
}

class PasswordResetService {
    public function sendReset() { ... }
}

class LoyaltyService {
    public function calculatePoints() { ... }
}
```
