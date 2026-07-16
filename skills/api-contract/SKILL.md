---
name: api-contract
description: Design, enforce, and version API contracts between services — OpenAPI spec, consumer-driven contract testing, breaking change detection, versioning strategy, and deprecation lifecycle.
version: 1.0.0
author: puterakahfi
license: MIT
type: skill
implements: ai-native-core/contracts/skills/domain-architecture/api-contract.contract.yaml
related_skills: [service-design, event-driven-design, security-review]
---

# API Contract

## The Core Rule

```
An API contract is a promise to consumers.
Breaking it without notice = breaking trust.

Contract-first design:
  1. Design the contract (spec)
  2. Generate tests from the contract
  3. Implement against the tests
  4. Never ship a breaking change without a version bump
```

---

## Contract-First Design

Write the spec before writing implementation. The spec IS the contract.

```yaml
# openapi: 3.0.3
# orders-api.yaml

openapi: 3.0.3
info:
  title: Order API
  version: 1.0.0

paths:
  /orders:
    post:
      operationId: placeOrder
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/PlaceOrderRequest'
      responses:
        '201':
          description: Order placed
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/OrderResponse'
        '422':
          description: Validation error
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'

components:
  schemas:
    PlaceOrderRequest:
      type: object
      required: [customerId, items]
      properties:
        customerId:
          type: string
          format: uuid
        items:
          type: array
          minItems: 1
          items:
            $ref: '#/components/schemas/OrderItem'

    ErrorResponse:
      type: object
      required: [code, message]
      properties:
        code:
          type: string
        message:
          type: string
        details:
          type: array
          items:
            type: object
```

---

## Versioning Strategy

### URL versioning (recommended for REST)
```
/v1/orders    ← stable, consumers depend on this
/v2/orders    ← new version, breaking changes here
```

### Header versioning
```
Accept: application/vnd.myapi.v2+json
```

### Rules:
- **MAJOR** version bump = breaking change
- **MINOR** = backward-compatible addition (new optional field, new endpoint)
- **PATCH** = bug fix, documentation only

---

## Breaking vs Non-Breaking Changes

### Breaking (requires MAJOR version bump)
```
❌ Remove a field from response
❌ Rename a field
❌ Change field type (string → integer)
❌ Make optional field required
❌ Remove an endpoint
❌ Change HTTP method of endpoint
❌ Change error response schema
❌ Change authentication scheme
```

### Non-Breaking (safe to ship in MINOR)
```
✅ Add new optional field to response
✅ Add new optional field to request
✅ Add new endpoint
✅ Add new enum value (if consumer uses allowAdditionalValues)
✅ Expand validation (loosen constraints)
```

---

## Consumer-Driven Contract Testing

Consumers define what they expect. Provider must satisfy all consumers.

```
Consumer (ShippingService) defines:
  - I call GET /orders/{id}
  - I expect: { id, status, items[], shippingAddress }
  - I do NOT care about: billingAddress, discount

Provider (OrderService) must:
  - Return at minimum what ShippingService expects
  - Not remove fields ShippingService uses
  - Run ShippingService's contract test in CI
```

### Using Pact (consumer-driven contract testing)

```javascript
// Consumer side — ShippingService defines expectation
const { like, eachLike } = Matchers;

await provider.addInteraction({
  state: 'order ORD-001 exists',
  uponReceiving: 'a request for order details',
  withRequest: {
    method: 'GET',
    path: '/orders/ORD-001',
  },
  willRespondWith: {
    status: 200,
    body: {
      id: like('ORD-001'),
      status: like('CONFIRMED'),
      items: eachLike({ productId: like('PRD-1'), quantity: like(2) }),
    },
  },
});
```

```php
// Provider side — OrderService verifies it satisfies consumer
// Run in CI: php artisan pact:verify --consumer=ShippingService
```

---

## Error Response Standard

All APIs must return consistent error schema:

```json
{
  "code": "VALIDATION_ERROR",
  "message": "Request validation failed",
  "details": [
    {
      "field": "items",
      "message": "must have at least 1 item"
    }
  ],
  "requestId": "req_abc123",
  "timestamp": "2026-07-16T10:00:00Z"
}
```

**HTTP status codes:**
| Status | Use For |
|---|---|
| 200 | Success |
| 201 | Created |
| 204 | Success, no body |
| 400 | Bad request (client error, fixable) |
| 401 | Unauthenticated |
| 403 | Unauthorized (authenticated but no permission) |
| 404 | Not found |
| 409 | Conflict (duplicate, state conflict) |
| 422 | Validation error (semantic, not syntactic) |
| 429 | Rate limited |
| 500 | Server error (never expose internals) |

---

## Deprecation Lifecycle

```
1. Announce in changelog + API docs
2. Add Deprecation header to responses:
   Deprecation: true
   Sunset: Sat, 01 Jan 2027 00:00:00 GMT
   Link: </v2/orders>; rel="successor-version"

3. Minimum notice period: product_defined (typically 3-6 months)
4. Monitor consumer usage — do not sunset while consumers active
5. Remove only after all consumers migrated
```

---

## Gate: Breaking Change Detection in CI

```bash
# Using oasdiff — detect breaking changes between versions
oasdiff breaking api/v1/orders.yaml api/v2/orders.yaml

# Output:
# [ERR] DELETE /orders/{id}/cancel - endpoint removed (breaking)
# [ERR] response body property 'total' removed (breaking)
# [WARN] response body property 'discount' added (non-breaking)
```

Add to CI pipeline — fail on breaking change in same major version.

---

## API Design Checklist

Before publishing an API:
- [ ] OpenAPI spec written before implementation?
- [ ] Versioning strategy declared?
- [ ] All endpoints documented (request + response + errors)?
- [ ] Error responses follow consistent schema?
- [ ] Contract tests exist for every known consumer?
- [ ] Breaking change detection in CI pipeline?
- [ ] Deprecation policy documented?
- [ ] No internal implementation details exposed?
- [ ] Authentication scheme documented?
- [ ] Rate limiting documented?
