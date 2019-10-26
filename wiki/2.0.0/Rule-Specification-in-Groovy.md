---
layout: wiki
---

Models in Groovy support three different ways to specify rules:

## In-Line Syntax
Rules can be specified using the natural Groovy syntax and the add() method for models.
The rule weight and squaring must be specified as additional arguments.
Both may be left off to specify an unweighted rule.
```groovy
model.add(
   rule: ( Likes(A, 'Dogs') & Likes(B, 'Dogs') ) >> Friends(A, B),
   weight: 5.0,
   squared: true
);
```

Because the in-line syntax must be a subset of Groovy syntax, the following operator variants are not supported:
- `&&`
- `||`
- `->`
- `<<`
- `<-`
- `!`  
Note that there are supported variants for all unsupported operators.
**Arithmetic rules** are **not** supported with the in-line syntax.

## String Syntax
```groovy
model.add(
   rule: "( Likes(A, 'Dogs') & Likes(B, 'Dogs') ) >> Friends(A, B)",
   weight: 5.0,
   squared: true
);

// Produces the same rule as above.
model.add(
   rule: "5.0: ( Likes(A, 'Dogs') && Likes(B, 'Dogs') ) -> Friends(A, B) ^2"
);

// An unweighted (constraint) variant of the above rule.
model.add(
   rule: "( Likes(A, 'Dogs') && Likes(B, 'Dogs') ) -> Friends(A, B)"
);

// An arithmetic constraint.
model.add(
   rule: "Likes(A, +B) = 1 ."
);
```

Rules can also be specified directly as a string.
Because they are not limited by the Groovy syntax, all operators are available.
A rule that specifies a weight and squaring in the string may not also pass "weight" and "squared" arguments.

## Bulk String Syntax
```groovy
// Load multiple rules from a single string.
model.addRules("""
   1: ( Likes(A, 'Dogs') & Likes(B, 'Dogs') ) >> Friends(A, B) ^2
   Likes(A, +B) = 1 .
""");

// Load multiple rules from a file.
model.addRules(new FileReader("myRules.txt"));
```

The addRules() method may be used add multiple rules at a time, each rule on its own line.
A `String` or `Reader` may be passed.
Each rule must be fully specified with respects to weights and squaring.

## Constraints
Constraints are specified as unweighted arithmetic rules.
So all you need to do is make an arithmetic rule and either explicitly specify that it is unweighted (using the period syntax), or not specify a weight.

```groovy
// An unweighted rule (constraint) explicitly specified with a period.
model.add(
   rule: "Likes(A, +B) = 1 ."
);

// An unweighted rule (constraint) implicitly specified by not adding a weight.
model.add(
   rule: "Likes(A, +B) = 1"
);