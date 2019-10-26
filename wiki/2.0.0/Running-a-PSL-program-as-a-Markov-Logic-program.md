---
layout: wiki
---

PSL includes implementations of [Markov Logic](http://www.cs.washington.edu/homes/pedrod/papers/mlj05.pdf) inference algorithms. You can use them in your inference and learning applications by setting the following [configuration](configuration.md) options. Note that these implementations do not support all constraints allowed in PSL. If your program's constraint set does not decompose over atoms, (i.e., each atom participates in at most one constraint), then they will throw exceptions.

### Inference

MPEInference and LazyMPEInference can use MaxWalkSat (MPE inference) and MC-Sat (marginal inference) with the following configuration options. Marginal probabilities will be set as the atoms' truth values.

```
# Sets MPEInference to perform Markov Logic MPE inference
<bundle>.mpeinference.reasoner = org.linqs.psl.reasoner.bool.BooleanMaxWalkSatFactory
# Sets MPEInference to perform Markov Logic marginal inference
<bundle>.mpeinference.reasoner = org.linqs.psl.reasoner.bool.BooleanMCSatFactory

# Sets LazyMPEInference to perform Markov Logic MPE inference
<bundle>.lazympeinference.reasoner = org.linqs.psl.reasoner.bool.BooleanMaxWalkSatFactory
# Sets LazyMPEInference to perform Markov Logic marginal inference
<bundle>.lazympeinference.reasoner = org.linqs.psl.reasoner.bool.BooleanMCSatFactory
```

### Weight Learning

Weight learning that uses a reasoner for MPE inference as a subroutine (e.g., MaxLikelihoodMPE, LazyMaxLikelihoodMPE) can also use Markov Logic MPE inference.

```
<bundle>.weightlearning.reasoner = org.linqs.psl.reasoner.bool.BooleanMaxWalkSatFactory
```

MaxPseudoLikelihood also supports Markov Logic weight learning.

```
<bundle>.maxpseudolikelihood.bool = true
```