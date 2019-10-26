---
layout: wiki
---

The job of a Weight Learning Application is to **use data** to learn the weights of each rule in a PSL model.   

##Syntax
In weight learning we follow the structure below:
```
<WeightLearningApplication> weightLearner =
      new <WeightLearningApplication>(<model>, <targetDatabase>, <groundTruthDatabase>, <config>);
```

- `<model>` is the model specified by your PSL program. 
- `<targetDatabase>` is a database which contains all of the atoms for which you would like to infer values. When you create this database, the target predicate will be open. 
- `<groundTruthDatabase>` is a database which contains the known values of the atoms for which you are inferring values in the targetDatabase. When you create this database the predicates should be closed. 
- `<config>` is your [config bundle](Configuration.md). 

Weight Learning Applications include:
- `LazyMaxLikelihoodMPE`
- `L1MaxMargin`
- `MaxLikelihoodMPE`
- `MaxPseudoLikelihood`