---
layout: page
title: Publications
nav-title: Publications
order: 6
permalink: /pubs/
---

You can find all the PSL-related publications on the [LINQS Publications Page](https://linqs.soe.ucsc.edu/biblio).  
Below are some of PSL's key publications.

#### Overview
[Hinge-Loss Markov Random Fields And Probabilistic Soft Logic](https://linqs.soe.ucsc.edu/node/242)  
A fundamental challenge in developing high-impact machine learning technologies is balancing the need to model rich, structured domains with the ability to scale to big data.
Many important problem areas are both richly structured and large scale, from social and biological networks, to knowledge graphs and the Web, to images, video, and natural language.
In this paper, we introduce two new formalisms for modeling structured data, and show that they can both capture rich structure and scale to big data.
The first, hingeloss Markov random fields (HL-MRFs), is a new kind of probabilistic graphical model that generalizes different approaches to convex inference.
We unite three approaches from the randomized algorithms, probabilistic graphical models, and fuzzy logic communities, showing that all three lead to the same inference objective.
We then define HL-MRFs by generalizing this unified objective.
The second new formalism, probabilistic soft logic (PSL), is a probabilistic programming language that makes HL-MRFs easy to define using a syntax based on first-order logic.
We introduce an algorithm for inferring most-probable variable assignments (MAP inference) that is much more scalable than general-purpose convex optimization methods, because it uses message passing to take advantage of sparse dependency structures.
We then show how to learn the parameters of HL-MRFs.
The learned HL-MRFs are as accurate as analogous discrete models, but much more scalable.
Together, these algorithms enable HL-MRFs and PSL to model rich, structured data at scales not previously possible.

#### Weight Learning
[Hinge-loss Markov Random Fields: Convex Inference for Structured Prediction](https://linqs.soe.ucsc.edu/node/26)  
Graphical models for structured domains are powerful tools, but the computational complexities of combinatorial prediction spaces can force restrictions on models, or require approximate inference in order to be tractable.
Instead of working in a combinatorial space, we use hinge-loss Markov random fields (HL-MRFs), an expressive class of graphical models with log-concave density functions over continuous variables, which can represent confidences in discrete predictions.
This paper demonstrates that HLMRFs are general tools for fast and accurate structured prediction.
We introduce the first inference algorithm that is both scalable and applicable to the full class of HL-MRFs, and show how to train HL-MRFs with several learning algorithms.
Our experiments show that HL-MRFs match or surpass the predictive performance of state-of-the-art methods, including discrete models, in four application domains.

#### Online Inference
[Budgeted Online Collective Inference](https://linqs.soe.ucsc.edu/node/249)  
Updating inference in response to new evidence is a fundamental challenge in artificial intelligence.
Many real problems require large probabilistic graphical models, containing millions of interdependent variables.
For such large models, jointly updating the most likely (i.e., MAP) configuration of the variables each time new evidence is encountered can be infeasible, even if inference is tractable.
In this paper, we introduce budgeted online collective inference, in which the MAP configuration of a graphical model is updated efficiently by revising the assignments to a subset of the variables while holding others fixed.
The goal is to selectively update certain variables without sacrificing quality with respect to full inference.
To formalize the consequences of partially updating inference, we introduce the concept of inference regret.
We derive inference regret bounds for a class of graphical models with strongly-convex free energies.
These theoretical insights, combined with a thorough analysis of the optimization solver, motivate new approximate methods for efficiently updating the variable assignments under a budget constraint.
In experiments, we demonstrate that our algorithms can reduce inference time by 65% with accuracy comparable to full inference.

#### Latent Variables
[Paired-Dual Learning For Fast Training Of Latent Variable Hinge-Loss MRFs](https://linqs.soe.ucsc.edu/node/263)  
Latent variables allow probabilistic graphical models to capture nuance and structure in important domains such as network science, natural language processing, and computer vision.
Naive approaches to learning such complex models can be prohibitively expensive—because they require repeated inferences to update beliefs about latent variables—so lifting this restriction for useful classes of models is an important problem.
Hinge-loss Markov random fields (HL-MRFs) are graphical models that allow highly scalable inference and learning in structured domains, in part by representing structured problems with continuous variables.
However, this representation leads to challenges when learning with latent variables.
We introduce paired-dual learning, a framework that greatly speeds up training by using tractable entropy surrogates and avoiding repeated inferences.
Paired-dual learning optimizes an objective with a pair of dual inference problems.
This allows fast, joint optimization of parameters and dual variables.
We evaluate on social-group detection, trust prediction in social networks, and image reconstruction, finding that paired-dual learning trains models as accurate as those trained by traditional methods in much less time, often before traditional methods make even a single parameter update.

#### Topic Modeling
[Latent Topic Networks: A Versatile Probabilistic Programming Framework For Topic Models](https://linqs.soe.ucsc.edu/node/259)  
Topic models have become increasingly prominent text-analytic machine learning tools for research in the social sciences and the humanities.
In particular, custom topic models can be developed to answer specific research questions.
The design of these models requires a nontrivial amount of effort and expertise, motivating general-purpose topic modeling frameworks.
In this paper we introduce latent topic networks, a flexible class of richly structured topic models designed to facilitate applied research.
Custom models can straightforwardly be developed in our framework with an intuitive first-order logical probabilistic programming language.
Latent topic networks admit scalable training via a parallelizable EM algorithm which leverages ADMM in the M-step.
We demonstrate the broad applicability of the models with case studies on modeling influence in citation networks, and U.S. Presidential State of the Union addresses.
