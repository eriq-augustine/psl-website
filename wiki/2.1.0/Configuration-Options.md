---
layout: wiki
---

***Key***:            admmmemorytermstore.internalstore  
***Type***:           String  
***Default Value***:  org.linqs.psl.reasoner.term.MemoryTermStore  
***Module***:         psl-core  
***Defining Class***: org.linqs.psl.reasoner.admm.term.ADMMTermStore  
***Description***:    Initial size for the memory store.  

***Key***:            admmreasoner.epsilonabs  
***Type***:           float  
***Default Value***:  1e-5f  
***Module***:         psl-core  
***Defining Class***: org.linqs.psl.reasoner.admm.ADMMReasoner  
***Description***:    Absolute error component of stopping criteria. Should be positive.  

***Key***:            admmreasoner.epsilonrel  
***Type***:           float  
***Default Value***:  1e-3f  
***Module***:         psl-core  
***Defining Class***: org.linqs.psl.reasoner.admm.ADMMReasoner  
***Description***:    Relative error component of stopping criteria. Should be positive.  

***Key***:            admmreasoner.initialconsensusvalue  
***Type***:           String  
***Default Value***:  InitialValue.RANDOM.toString()  
***Module***:         psl-core  
***Defining Class***: org.linqs.psl.reasoner.admm.ADMMReasoner  
***Description***:    The starting value for consensus variables. Values should come from the InitialValue enum.  

***Key***:            admmreasoner.initiallocalvalue  
***Type***:           String  
***Default Value***:  InitialValue.RANDOM.toString()  
***Module***:         psl-core  
***Defining Class***: org.linqs.psl.reasoner.admm.ADMMReasoner  
***Description***:    The starting value for local variables. Values should come from the InitialValue enum.  

***Key***:            admmreasoner.maxiterations  
***Type***:           int  
***Default Value***:  25000  
***Module***:         psl-core  
***Defining Class***: org.linqs.psl.reasoner.admm.ADMMReasoner  
***Description***:    The maximum number of iterations of ADMM to perform in a round of inference.  

***Key***:            admmreasoner.objectivebreak  
***Type***:           boolean  
***Default Value***:  true  
***Module***:         psl-core  
***Defining Class***: org.linqs.psl.reasoner.admm.ADMMReasoner  
***Description***:    Stop if the objective has not changed since the last logging period (see LOG_PERIOD).  

***Key***:            admmreasoner.stepsize  
***Type***:           float  
***Default Value***:  1.0f  
***Module***:         psl-core  
***Defining Class***: org.linqs.psl.reasoner.admm.ADMMReasoner  
***Description***:    Step size. Higher values result in larger steps. Should be positive.  

***Key***:            admmtermgenerator.invertnegativeweights  
***Type***:           boolean  
***Default Value***:  false  
***Module***:         psl-core  
***Defining Class***: org.linqs.psl.reasoner.admm.term.ADMMTermGenerator  
***Description***:    If true, then invert negative weight rules into their positive weight counterparts (negate the weight and expression).  

***Key***:            arithmeticrule.delim  
***Type***:           String  
***Default Value***:  ;  
***Module***:         psl-core  
***Defining Class***: org.linqs.psl.model.rule.arithmetic.AbstractArithmeticRule  
***Description***:    The delimiter to use when building summation substitutions. Make sure the value for this key does not appear in ground atoms that use a summation.  

***Key***:            booleanmaxwalksat.maxflips  
***Type***:           int  
***Default Value***:  50000  
***Module***:         psl-core  
***Defining Class***: org.linqs.psl.reasoner.bool.BooleanMaxWalkSat  
***Description***:    Key for positive integer property that is the maximum number of flips to try during optimization  

***Key***:            booleanmaxwalksat.noise  
***Type***:           double  
***Default Value***:  0.01  
***Module***:         psl-core  
***Defining Class***: org.linqs.psl.reasoner.bool.BooleanMaxWalkSat  
***Description***:    Key for double property in [0,1] that is the probability of randomly perturbing an atom in a randomly chosen potential  

***Key***:            booleanmcsat.numburnin  
***Type***:           int  
***Default Value***:  500  
***Module***:         psl-core  
***Defining Class***: org.linqs.psl.reasoner.bool.BooleanMCSat  
***Description***:    Number of burn-in samples  

***Key***:            booleanmcsat.numsamples  
***Type***:           int  
***Default Value***:  2500  
***Module***:         psl-core  
***Defining Class***: org.linqs.psl.reasoner.bool.BooleanMCSat  
***Description***:    Key for length of Markov chain  

***Key***:            categoricalevaluator.categoryindexes  
***Type***:             
***Default Value***:    
***Module***:         psl-core  
***Defining Class***: org.linqs.psl.evaluation.statistics.CategoricalEvaluator  
***Description***:    The index of the arguments in the predicate (delimited by colons).  

***Key***:            categoricalevaluator.defaultpredicate  
***Type***:             
***Default Value***:    
***Module***:         psl-core  
***Defining Class***: org.linqs.psl.evaluation.statistics.CategoricalEvaluator  
***Description***:    The default predicate to use when none are supplied.  

***Key***:            categoricalevaluator.representative  
***Type***:             
***Default Value***:    
***Module***:         psl-core  
***Defining Class***: org.linqs.psl.evaluation.statistics.CategoricalEvaluator  
***Description***:    The representative metric. Default to accuracy. Must match a string from the RepresentativeMetric enum.  

***Key***:            continuousevaluator.representative  
***Type***:             
***Default Value***:    
***Module***:         psl-core  
***Defining Class***: org.linqs.psl.evaluation.statistics.ContinuousEvaluator  
***Description***:    The representative metric. Default to MSE. Must match a string from the RepresentativeMetric enum.  

***Key***:            continuousrandomgridsearch.maxlocations  
***Type***:           int  
***Default Value***:  250  
***Module***:         psl-core  
***Defining Class***: org.linqs.psl.application.learning.weight.search.grid.ContinuousRandomGridSearch  
***Description***:    The max number of locations to search.  

***Key***:            discreteevaluator.representative  
***Type***:             
***Default Value***:    
***Module***:         psl-core  
***Defining Class***: org.linqs.psl.evaluation.statistics.DiscreteEvaluator  
***Description***:    The representative metric. Default to F1. Must match a string from the RepresentativeMetric enum.  

***Key***:            discreteevaluator.threshold  
***Type***:             
***Default Value***:    
***Module***:         psl-core  
***Defining Class***: org.linqs.psl.evaluation.statistics.DiscreteEvaluator  
***Description***:    The truth threshold.  

***Key***:            em.iterations  
***Type***:           int  
***Default Value***:  10  
***Module***:         psl-core  
***Defining Class***: org.linqs.psl.application.learning.weight.em.ExpectationMaximization  
***Description***:    Key for positive int property for the number of iterations of expectation maximization to perform  

***Key***:            em.tolerance  
***Type***:           double  
***Default Value***:  1e-3  
***Module***:         psl-core  
***Defining Class***: org.linqs.psl.application.learning.weight.em.ExpectationMaximization  
***Description***:    Key for positive double property for the minimum absolute change in weights such that EM is considered converged  

***Key***:            executablereasoner.cleanupinput  
***Type***:           boolean  
***Default Value***:  true  
***Module***:         psl-core  
***Defining Class***: org.linqs.psl.reasoner.ExecutableReasoner  
***Description***:    Key for boolean property for whether to delete the input file to external the reasoner on close.  

***Key***:            executablereasoner.cleanupoutput  
***Type***:           boolean  
***Default Value***:  true  
***Module***:         psl-core  
***Defining Class***: org.linqs.psl.reasoner.ExecutableReasoner  
***Description***:    Key for boolean property for whether to delete the output file to external the reasoner on close.  

***Key***:            executablereasoner.executablepath  
***Type***:             
***Default Value***:    
***Module***:         psl-core  
***Defining Class***: org.linqs.psl.reasoner.ExecutableReasoner  
***Description***:    Key for int property for the path of the executable.  

***Key***:            gridsearch.weights  
***Type***:           String  
***Default Value***:  0.001:0.01:0.1:1:10  
***Module***:         psl-core  
***Defining Class***: org.linqs.psl.application.learning.weight.search.grid.GridSearch  
***Description***:    A comma-separated list of possible weights. These weights should be in some sorted order.  

***Key***:            guidedrandomgridsearch.explorelocations  
***Type***:           int  
***Default Value***:  10  
***Module***:         psl-core  
***Defining Class***: org.linqs.psl.application.learning.weight.search.grid.GuidedRandomGridSearch  
***Description***:    The number of initial seed locations to explore based off of whichever ones score the best.  

***Key***:            guidedrandomgridsearch.seedlocations  
***Type***:           int  
***Default Value***:  25  
***Module***:         psl-core  
***Defining Class***: org.linqs.psl.application.learning.weight.search.grid.GuidedRandomGridSearch  
***Description***:    The number of locations to initially search.  

***Key***:            hardem.adagrad  
***Type***:           boolean  
***Default Value***:  false  
***Module***:         psl-core  
***Defining Class***: org.linqs.psl.application.learning.weight.em.HardEM  
***Description***:    Key for Boolean property that indicates whether to use AdaGrad subgradient scaling, the adaptive subgradient algorithm of John Duchi, Elad Hazan, Yoram Singer (JMLR 2010). If TRUE, will override other step scheduling options (but not scaling).  

***Key***:            hyperband.basebracketsize  
***Type***:           int  
***Default Value***:  10  
***Module***:         psl-core  
***Defining Class***: org.linqs.psl.application.learning.weight.search.Hyperband  
***Description***:    The base number of weight configurations for each brackets.  

***Key***:            hyperband.numbrackets  
***Type***:           int  
***Default Value***:  4  
***Module***:         psl-core  
***Defining Class***: org.linqs.psl.application.learning.weight.search.Hyperband  
***Description***:    The number of brackets to consider. This is computed in vanilla Hyperband.  

***Key***:            hyperband.survival  
***Type***:           int  
***Default Value***:  4  
***Module***:         psl-core  
***Defining Class***: org.linqs.psl.application.learning.weight.search.Hyperband  
***Description***:    The proportion of configs that survive each round in a brancket.  

***Key***:            inference.groundrulestore  
***Type***:           String  
***Default Value***:  org.linqs.psl.application.groundrulestore.MemoryGroundRuleStore  
***Module***:         psl-core  
***Defining Class***: org.linqs.psl.application.inference.InferenceApplication  
***Description***:    The class to use for ground rule storage.  

***Key***:            inference.reasoner  
***Type***:           String  
***Default Value***:  org.linqs.psl.reasoner.admm.ADMMReasoner  
***Module***:         psl-core  
***Defining Class***: org.linqs.psl.application.inference.InferenceApplication  
***Description***:    The class to use for a reasoner.  

***Key***:            inference.termgenerator  
***Type***:           String  
***Default Value***:  org.linqs.psl.reasoner.admm.term.ADMMTermGenerator  
***Module***:         psl-core  
***Defining Class***: org.linqs.psl.application.inference.InferenceApplication  
***Description***:    The class to use for term generator. Should be compatible with REASONER_KEY and TERM_STORE_KEY.  

***Key***:            inference.termstore  
***Type***:           String  
***Default Value***:  org.linqs.psl.reasoner.admm.term.ADMMTermStore  
***Module***:         psl-core  
***Defining Class***: org.linqs.psl.application.inference.InferenceApplication  
***Description***:    The class to use for term storage. Should be compatible with REASONER_KEY.  

***Key***:            initialweighthyperband.internalwla  
***Type***:           String  
***Default Value***:  MaxLikelihoodMPE.class.getName()  
***Module***:         psl-core  
***Defining Class***: org.linqs.psl.application.learning.weight.search.InitialWeightHyperband  
***Description***:    The internal weight learning application (WLA) to use. Should actually be a VotedPerceptron.  

***Key***:            lazyatommanager.activation  
***Type***:           double  
***Default Value***:  0.01  
***Module***:         psl-core  
***Defining Class***: org.linqs.psl.database.atom.LazyAtomManager  
***Description***:    The minimum value an atom must take for it to be activated. Must be a flot in (0,1].  

***Key***:            lazymaxlikelihoodmpe.maxgrowrounds  
***Type***:           int  
***Default Value***:  100  
***Module***:         psl-core  
***Defining Class***: org.linqs.psl.application.learning.weight.maxlikelihood.LazyMaxLikelihoodMPE  
***Description***:    Key for int property for the maximum number of rounds of lazy growing.  

***Key***:            lazympeinference.maxrounds  
***Type***:           int  
***Default Value***:  100  
***Module***:         psl-core  
***Defining Class***: org.linqs.psl.application.inference.LazyMPEInference  
***Description***:    Key for int property for the maximum number of rounds of inference.  

***Key***:            maxpiecewisepseudolikelihood.numsamples  
***Type***:           int  
***Default Value***:  100  
***Module***:         psl-core  
***Defining Class***: org.linqs.psl.application.learning.weight.maxlikelihood.MaxPiecewisePseudoLikelihood  
***Description***:    Key for positive integer property. MaxPiecewisePseudoLikelihood will sample this many values to approximate the expectations.  

***Key***:            maxspeudolikelihood.bool  
***Type***:           boolean  
***Default Value***:  false  
***Module***:         psl-core  
***Defining Class***: org.linqs.psl.application.learning.weight.maxlikelihood.MaxPseudoLikelihood  
***Description***:    Boolean property. If true, MaxPseudoLikelihood will treat RandomVariableAtoms as boolean valued. Note that this restricts the types of contraints supported.  

***Key***:            maxspeudolikelihood.minwidth  
***Type***:           double  
***Default Value***:  1e-2  
***Module***:         psl-core  
***Defining Class***: org.linqs.psl.application.learning.weight.maxlikelihood.MaxPseudoLikelihood  
***Description***:    Key for positive double property. Used as minimum width for bounds of integration.  

***Key***:            maxspeudolikelihood.numsamples  
***Type***:           int  
***Default Value***:  10  
***Module***:         psl-core  
***Defining Class***: org.linqs.psl.application.learning.weight.maxlikelihood.MaxPseudoLikelihood  
***Description***:    Key for positive integer property. MaxPseudoLikelihood will sample this many values to approximate the integrals in the marginal computation.  

***Key***:            memorytermstore.initialsize  
***Type***:           int  
***Default Value***:  5000  
***Module***:         psl-core  
***Defining Class***: org.linqs.psl.reasoner.term.MemoryTermStore  
***Description***:    Initial size for the memory store.  

***Key***:            optimalcover.blockadvantage  
***Type***:           double  
***Default Value***:  100.0  
***Module***:         psl-core  
***Defining Class***: org.linqs.psl.database.rdbms.OptimalCover  
***Description***:    The cost for a blocking predicate is divided by this.  

***Key***:            optimalcover.joinadvantage  
***Type***:           double  
***Default Value***:  2.0  
***Module***:         psl-core  
***Defining Class***: org.linqs.psl.database.rdbms.OptimalCover  
***Description***:    The cost for a JOIN.  

***Key***:            pairedduallearner.admmsteps  
***Type***:           int  
***Default Value***:  1  
***Module***:         psl-core  
***Defining Class***: org.linqs.psl.application.learning.weight.em.PairedDualLearner  
***Description***:    Key for Integer property that indicates how many steps of ADMM to run for each inner objective before each gradient iteration (parameter N in the ICML paper)  

***Key***:            pairedduallearner.warmuprounds  
***Type***:           int  
***Default Value***:  0  
***Module***:         psl-core  
***Defining Class***: org.linqs.psl.application.learning.weight.em.PairedDualLearner  
***Description***:    Key for Integer property that indicates how many rounds of paired-dual learning to run before beginning to update the weights (parameter K in the ICML paper)  

***Key***:            parallel.numthreads  
***Type***:           int  
***Default Value***:  Runtime.getRuntime().availableProcessors()  
***Module***:         psl-core  
***Defining Class***: org.linqs.psl.util.Parallel  
***Description***:      

***Key***:            persistedatommanager.throwaccessexception  
***Type***:           boolean  
***Default Value***:  true  
***Module***:         psl-core  
***Defining Class***: org.linqs.psl.database.atom.PersistedAtomManager  
***Description***:    Whether or not to throw an exception on illegal access. Note that in most cases, this indicates incorrectly formed data. This should only be set to true when the user understands why these exceptions are thrown in the first place and the grounding implications of not having the atom initially in the database.  

***Key***:            random.seed  
***Type***:           int  
***Default Value***:  4  
***Module***:         psl-core  
***Defining Class***: org.linqs.psl.util.RandUtils  
***Description***:      

***Key***:            randomgridsearch.maxlocations  
***Type***:           int  
***Default Value***:  150  
***Module***:         psl-core  
***Defining Class***: org.linqs.psl.application.learning.weight.search.grid.RandomGridSearch  
***Description***:    The max number of locations to search.  

***Key***:            rankingevaluator.representative  
***Type***:             
***Default Value***:    
***Module***:         psl-core  
***Defining Class***: org.linqs.psl.evaluation.statistics.RankingEvaluator  
***Description***:    The representative metric. Default to F1. Must match a string from the RepresentativeMetric enum.  

***Key***:            rankingevaluator.threshold  
***Type***:             
***Default Value***:    
***Module***:         psl-core  
***Defining Class***: org.linqs.psl.evaluation.statistics.RankingEvaluator  
***Description***:    The truth threshold.  

***Key***:            ranksearch.scalingfactors  
***Type***:           String  
***Default Value***:  1:2:10:100  
***Module***:         psl-core  
***Defining Class***: org.linqs.psl.application.learning.weight.search.grid.RankSearch  
***Description***:    A comma-separated list of scaling factors.  

***Key***:            rdbmsdatabase.optimalcover  
***Type***:           boolean  
***Default Value***:  false  
***Module***:         psl-core  
***Defining Class***: org.linqs.psl.database.rdbms.RDBMSDatabase  
***Description***:    Use optimal cover grounding.  

***Key***:            votedperceptron.averagesteps  
***Type***:           boolean  
***Default Value***:  false  
***Module***:         psl-core  
***Defining Class***: org.linqs.psl.application.learning.weight.VotedPerceptron  
***Description***:    Key for Boolean property that indicates whether to average all visited weights together for final output.  

***Key***:            votedperceptron.clipnegativeweights  
***Type***:           boolean  
***Default Value***:  true  
***Module***:         psl-core  
***Defining Class***: org.linqs.psl.application.learning.weight.VotedPerceptron  
***Description***:    If true, then weight will not be allowed to go negative (clipped at zero).  

***Key***:            votedperceptron.cutobjective  
***Type***:           boolean  
***Default Value***:  false  
***Module***:         psl-core  
***Defining Class***: org.linqs.psl.application.learning.weight.VotedPerceptron  
***Description***:    If true, then cut the step size in half whenever the objective increases.  

***Key***:            votedperceptron.inertia  
***Type***:           double  
***Default Value***:  0.00  
***Module***:         psl-core  
***Defining Class***: org.linqs.psl.application.learning.weight.VotedPerceptron  
***Description***:    The inertia that is used for adaptive step sizes. Should be in [0, 1).  

***Key***:            votedperceptron.l1regularization  
***Type***:           double  
***Default Value***:  0.0  
***Module***:         psl-core  
***Defining Class***: org.linqs.psl.application.learning.weight.VotedPerceptron  
***Description***:    Key for positive double property scaling the L1 regularization \gamma * |w|  

***Key***:            votedperceptron.l2regularization  
***Type***:           double  
***Default Value***:  0.0  
***Module***:         psl-core  
***Defining Class***: org.linqs.psl.application.learning.weight.VotedPerceptron  
***Description***:    Key for positive double property scaling the L2 regularization (\lambda / 2) * ||w||^2  

***Key***:            votedperceptron.numsteps  
***Type***:           int  
***Default Value***:  25  
***Module***:         psl-core  
***Defining Class***: org.linqs.psl.application.learning.weight.VotedPerceptron  
***Description***:    Key for positive integer property. VotedPerceptron will take this many steps to learn weights.  

***Key***:            votedperceptron.scalegradient  
***Type***:           boolean  
***Default Value***:  true  
***Module***:         psl-core  
***Defining Class***: org.linqs.psl.application.learning.weight.VotedPerceptron  
***Description***:    Key for Boolean property that indicates whether to scale gradient by number of groundings  

***Key***:            votedperceptron.scalestepsize  
***Type***:           boolean  
***Default Value***:  true  
***Module***:         psl-core  
***Defining Class***: org.linqs.psl.application.learning.weight.VotedPerceptron  
***Description***:    If true, then scale the step size down by the iteration.  

***Key***:            votedperceptron.stepsize  
***Type***:           double  
***Default Value***:  0.2  
***Module***:         psl-core  
***Defining Class***: org.linqs.psl.application.learning.weight.VotedPerceptron  
***Description***:    Key for positive double property which will be multiplied with the objective gradient to compute a step.  

***Key***:            votedperceptron.zeroinitialweights  
***Type***:           boolean  
***Default Value***:  false  
***Module***:         psl-core  
***Defining Class***: org.linqs.psl.application.learning.weight.VotedPerceptron  
***Description***:    If true, then start all weights at zero for learning.  

***Key***:            weightlearning.evaluator  
***Type***:           String  
***Default Value***:  ContinuousEvaluator.class.getName()  
***Module***:         psl-core  
***Defining Class***: org.linqs.psl.application.learning.weight.WeightLearningApplication  
***Description***:    An evalautor capable of producing a score for the current weight configuration. Child methods may use this at their own discrection. This is only used for logging/information, and not for gradients.  

***Key***:            weightlearning.groundrulestore  
***Type***:           String  
***Default Value***:  MemoryGroundRuleStore.class.getName()  
***Module***:         psl-core  
***Defining Class***: org.linqs.psl.application.learning.weight.WeightLearningApplication  
***Description***:    The class to use for ground rule storage.  

***Key***:            weightlearning.randomweights  
***Type***:           boolean  
***Default Value***:  false  
***Module***:         psl-core  
***Defining Class***: org.linqs.psl.application.learning.weight.WeightLearningApplication  
***Description***:    Randomize weights before running. The randomization will happen during ground model initialization.  

***Key***:            weightlearning.reasoner  
***Type***:           String  
***Default Value***:  ADMMReasoner.class.getName()  
***Module***:         psl-core  
***Defining Class***: org.linqs.psl.application.learning.weight.WeightLearningApplication  
***Description***:    The class to use for inference.  

***Key***:            weightlearning.termgenerator  
***Type***:           String  
***Default Value***:  ADMMTermGenerator.class.getName()  
***Module***:         psl-core  
***Defining Class***: org.linqs.psl.application.learning.weight.WeightLearningApplication  
***Description***:    The class to use for term generator. Should be compatible with REASONER_KEY and TERM_STORE_KEY.  

***Key***:            weightlearning.termstore  
***Type***:           String  
***Default Value***:  ADMMTermStore.class.getName()  
***Module***:         psl-core  
***Defining Class***: org.linqs.psl.application.learning.weight.WeightLearningApplication  
***Description***:    The class to use for term storage. Should be compatible with REASONER_KEY.