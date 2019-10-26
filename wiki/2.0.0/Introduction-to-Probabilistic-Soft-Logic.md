---
layout: wiki
---

Probabilistic soft logic (PSL) is a general purpose language for modeling probabilistic and relational domains. It is applicable to a variety of machine learning problems, such as link prediction and ontology alignment. PSL combines the strengths of two powerful theories -- [first-order logic](https://en.wikipedia.org/wiki/First-order_logic), with its ability to succinctly represent complex phenomena, and [probabilistic graphical models](https://en.wikipedia.org/wiki/Graphical_model), which capture the uncertainty and incompleteness inherent in real-world knowledge. More specifically, PSL uses "soft" logic as its logical component and [Markov networks](http://en.wikipedia.org/wiki/Markov_random_field) as its statistical model. 

In "soft" logic, logical constructs need not be strictly `false (0)` or `true (1)`, but can take on values between 0 and 1 inclusively. For example, in logical formula `similarNames(X, Y) => sameEntity(X, Y)` (which encodes the belief that if two people `X` and `Y` have similar names, then they are likely the same person),  the truth value of `similarNames(X, Y)` and that of the entire formula lie in the range [0, 1]. The logical operators `and (^)`, `or (v)` and `not (~)` are defined using the [Lukasiewicz t-norms](http://en.wikipedia.org/wiki/%C5%81ukasiewicz_logic), i.e., 
```
A ^ B = max{A + B - 1, 0}
A v B = min{A + B, 1}
~A = 1 - A
```

(Note that if the values of `A` and `B` are restricted to be false or true, then the logical operators work as they are conventionally defined.) PSL provides an interface in the [Groovy](http://groovy-lang.org) programming language for users to declaratively encode their knowledge of a particular domain in soft logic. 

These logical formulas become the features of a Markov network. Each feature in the network is associated with a weight, which determines its importance in the interactions between features. Weights can be specified manually or learned from evidence data using PSL's suite of learning algorithms. PSL also provides sophisticated inference techniques for finding the most likely answer (i.e. the MAP state) to a user's query. The "softening" of the logical formulas allows us to cast the inference problem as a polynomial-time optimization, rather than a (much more difficult NP-hard) combinatorial one. (See [LP relaxation](http://en.wikipedia.org/wiki/LP_relaxation) for more details.)

For more details on PSL, please refer to the paper [Hinge-Loss Markov Random Fields and Probabilistic Soft Logic](https://arxiv.org/abs/1505.04406).