---
layout: wiki
---

[Arithmetic rules](Rule-Specification.md#arithmetic-rules) can be used to enforce modeling constraints.
Many different types of constraints can be modeled, this page show a few of the common types.

For these examples, let `Foo` be the binary predicate that we wish to put constraints on.
(Constraints are not limited to only binary predicates.)

## Functional
A **Functional** constraint enforces the condition that for each possible constant `c`,
the values of all groundings of `Foo(A, c)` sum to exactly 1.
```
Foo(A, +c) = 1 .
```
Note that the rule is unweighted (as indicated by the period at the end).

### Inverse Functional
Summing the first argument instead of the second one is often called **Inverse Functional**.
There are no semantic differences between functional and inverse functional constraints.
```
Foo(+c, A) = 1 .
```

## Partial Functional
A **Partial Functional** constraint is like a functional one, except the value of all groundings of `Foo(A, c)` sum to 1 or less.
```
Foo(A, +c) <= 1 .
```

### Partial Inverse Functional
```
Foo(+c, A) <= 1 .
```