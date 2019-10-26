---
layout: wiki
---

Arithmetic rules can be used to enforce modeling constraints.
Many different types of constraints can be modeled, here are a few of the common types:

Let `Foo` be the binary predicate that we wish to put constraints on. (Constraints are not limited to only binary predicates.)

## Functional
A `Functional` constraint enforces the condition that for each possible constant c, the values of all groundings of `Foo(A, c)` sum to exactly 1.
```
Foo(A, +c) = 1 .
```
Note that the rule is unweighted (as indicated by the period at the end).

### Inverse Functional
Summing the first argument instead of the second one is often called `Inverse Functional`.
```
Foo(+c, A) = 1 .
```

## Partial Functional
A `Partial Functional` constraint is like a `Functional` one, except the values of all groundings of `Foo(A, c)` sum to 1 or less.
```
Foo(A, +c) <= 1 .
```

### Partial Inverse Functional
```
Foo(+c, A) <= 1 .
```