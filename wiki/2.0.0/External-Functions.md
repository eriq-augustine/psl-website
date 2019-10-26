---
layout: wiki
---

Customized functions can be created be implementing the `ExternalFunction` interface.
The getValue() method should return a value in [0, 1].
```
public class MyStringSimilarity implements ExternalFunction {
   @Override
   public int getArity() {
      return 2;
   }

   @Override
   public ConstantType[] getArgumentTypes() {
      return [ConstantType.String, ConstantType.String].toArray();
   }

   @Override
   public double getValue(ReadOnlyDatabase db, Constant... args) {
      return args[0].toString().equals(args[1].toString()) ? 1.0 : 0.0;
   }
}
```

A function comparing the similarity between two entities or text can then be declared as follows:
```
model.add function: MyStringSimilarity, implementation: new MyStringSimilarity();
```

A function can be used in the same manner as a predicate in rules:
```
Name(P1, N1) & Name(P2, N2) & MyStringSimilarity(N1, N2) -> SamePerson(P1, P2)
```