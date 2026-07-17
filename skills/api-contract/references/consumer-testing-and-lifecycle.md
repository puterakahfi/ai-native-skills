# API Contract — Consumer Testing, Errors, Deprecation & CI Gates

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
