# Refactoring — Advanced Patterns & Checklist

## Replace Conditional with Polymorphism

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

---

## Introduce Parameter Object

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

---

## Extract Value Object (Primitive Obsession)

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
