# Error and Failure Types | 错误和失败类型

## API Reference

Navigation failure and error types.

### NavigationFailureType

Enumeration of navigation failure types.

**Types:**
```typescript
enum NavigationFailureType {
  aborted = 4,
  cancelled = 8,
  duplicated = 16
}
```

### NavigationFailure

Type for navigation failures.

**Properties:**
- `type`: NavigationFailureType
- `from`: Route location navigation started from
- `to`: Route location navigation was going to

### Example: Handling Navigation Failures

```javascript
router.push('/home').catch((err) => {
  if (err.name === 'NavigationDuplicated') {
    // Handle duplicate navigation
  } else if (err.name === 'NavigationAborted') {
    // Handle aborted navigation
  } else if (err.name === 'NavigationCancelled') {
    // Handle cancelled navigation
  }
})
```

### Key Points

- Navigation methods return Promises
- Failures are caught in `.catch()` handlers
- Different failure types indicate different scenarios
- Can check failure type to handle appropriately
