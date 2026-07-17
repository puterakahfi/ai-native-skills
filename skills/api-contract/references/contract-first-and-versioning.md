# API Contract — Contract-First Design, Versioning & Breaking Changes

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
