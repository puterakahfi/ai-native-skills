---
name: refactoring
description: Structured code refactoring without behavior change — name the smell, green tests first, small independent steps, one refactoring type per commit. Covers extract method/class, move, rename, decompose conditional, replace pattern.
license: MIT
metadata:
  ai-native-skills.version: 1.0.0
  ai-native-skills.author: puterakahfi
  ai-native-skills.type: skill
  ai-native-skills.implements: ai-native-core/contracts/skills/software-engineering/refactoring.contract.yaml
---

# Refactoring

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

## Common Refactorings

### Extract Method

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

### Extract Class (God Class)

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

### Replace Conditional with Polymorphism

```php
// Before — Conditional Complexity smell
public function getShippingRate(string $type, Shipment $shipment): Money
{
    return match($type) {
        'flat'         => Money::of(999, 'USD'),
        'weight'       => Money::of($shipment->weight() * 50, 'USD'),
        'zone'         => $this->zoneRates[$shipment->zone()],
        default        => throw new UnknownShippingTypeException($type),
    };
}

// After — Replace with Polymorphism (Strategy pattern)
interface ShippingCalculator {
    public function calculate(Shipment $shipment): Money;
}

class FlatRateCalculator implements ShippingCalculator { ... }
class WeightBasedCalculator implements ShippingCalculator { ... }
class ZoneBasedCalculator implements ShippingCalculator { ... }
```

### Introduce Parameter Object

```php
// Before — Long Parameter List smell
public function createReport(
    string $userId,
    DateTimeImmutable $from,
    DateTimeImmutable $to,
    string $format,
    bool $includeArchived
): Report { ... }

// After — Introduce Parameter Object
class ReportQuery {
    public function __construct(
        public readonly string $userId,
        public readonly DateTimeImmutable $from,
        public readonly DateTimeImmutable $to,
        public readonly string $format = 'pdf',
        public readonly bool $includeArchived = false,
    ) {}
}

public function createReport(ReportQuery $query): Report { ... }
```

### Extract Value Object (Primitive Obsession)

```php
// Before — string for email, no validation, no behavior
public function register(string $email, string $password): User { ... }

// After — Value Object
final class Email {
    private string $value;

    public function __construct(string $value) {
        if (!filter_var($value, FILTER_VALIDATE_EMAIL)) {
            throw new InvalidEmailException($value);
        }
        $this->value = strtolower($value);
    }

    public function toString(): string { return $this->value; }
    public function equals(Email $other): bool { return $this->value === $other->value; }
}

public function register(Email $email, Password $password): User { ... }
```

---

## Refactoring Checklist

Before starting:
- [ ] Code smell named explicitly?
- [ ] Tests green before first change?
- [ ] Refactoring goal stated (not "clean up" but "extract X to Y")?

During:
- [ ] One refactoring type per commit?
- [ ] Tests run after every step?
- [ ] No new features added?
- [ ] No bugs fixed (create separate ticket)?

After:
- [ ] Tests still green?
- [ ] Coverage not decreased?
- [ ] Code smell resolved?
- [ ] Commit messages say `refactor(scope): description`?
