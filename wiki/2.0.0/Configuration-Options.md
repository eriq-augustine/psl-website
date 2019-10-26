---
layout: wiki
---

***Key***:            pairedduallearner.warmuprounds  
***Type***:           int  
***Default Value***:  0  
***Module***:         psl-core  
***Defining Class***: org.linqs.psl.application.learning.weight.em.PairedDualLearner  
***Description***:    Key for Integer property that indicates how many rounds of paired-dual learning to run before beginning to update the weights (parameter K in the ICML paper)  

***Key***:            pairedduallearner.admmsteps  
***Type***:           int  
***Default Value***:  1  
***Module***:         psl-core  
***Defining Class***: org.linqs.psl.application.learning.weight.em.PairedDualLearner  
***Description***:    Key for Integer property that indicates how many steps of ADMM to run for each inner objective before each gradient step (parameter N in the ICML paper)  

***Key***:            hardem.adagrad  
***Type***:           boolean  
***Default Value***:  false  
***Module***:         psl-core  
***Defining Class***: org.linqs.psl.application.learning.weight.em.HardEM  
***Description***:    Key for Boolean property that indicates whether to use AdaGrad subgradient scaling, the adaptive subgradient algorithm of John Duchi, Elad Hazan, Yoram Singer (JMLR 2010). If TRUE, will override other step scheduling options (but not scaling).  

***Key***:            bernoullimeanfieldem.mpeinit  
***Type***:           boolean  
***Default Value***:  true  
***Module***:         psl-core  
***Defining Class***: org.linqs.psl.application.learning.weight.em.BernoulliMeanFieldEM  
***Description***:    Key for Boolean property. If true, the mean field will be reinitialized via MPE inference at each round. If false, each mean will be initialized to 0.5 before the first round.  

***Key***:            em.iterations  
***Type***:           int  
***Default Value***:  10  
***Module***:         psl-core  
***Defining Class***: org.linqs.psl.application.learning.weight.em.ExpectationMaximization  
***Description***:    Key for positive int property for the number of iterations of expectation maximization to perform  

***Key***:            em.resetschedule  
***Type***:           boolean  
***Default Value***:  true  
***Module***:         psl-core  
***Defining Class***: org.linqs.psl.application.learning.weight.em.ExpectationMaximization  
***Description***:    Key for Boolean property that indicates whether to reset step-size schedule for each EM round. If TRUE, schedule will be VotedPerceptron#STEP_SIZE_KEY at start of each round. If FALSE, schedule will smoothly decrease across rounds, i.e., the schedule will be 1/ (round number * num steps + step number). This property has no effect if VotedPerceptron#STEP_SCHEDULE_KEY is false.  

***Key***:            em.storeweights  
***Type***:           boolean  
***Default Value***:  false  
***Module***:         psl-core  
***Defining Class***: org.linqs.psl.application.learning.weight.em.ExpectationMaximization  
***Description***:    Key for Boolean property that indicates whether to store weights along entire optimization path  

***Key***:            em.tolerance  
***Type***:           double  
***Default Value***:  1e-3  
***Module***:         psl-core  
***Defining Class***: org.linqs.psl.application.learning.weight.em.ExpectationMaximization  
***Description***:    Key for positive double property for the minimum absolute change in weights such that EM is considered converged  

***Key***:            votedperceptron.augmentloss  
***Type***:           boolean  
***Default Value***:  false  
***Module***:         psl-core  
***Defining Class***: org.linqs.psl.application.learning.weight.maxlikelihood.VotedPerceptron  
***Description***:    Key for boolean property for whether to add loss-augmentation for online large margin  

***Key***:            votedperceptron.l2regularization  
***Type***:           double  
***Default Value***:  0.0  
***Module***:         psl-core  
***Defining Class***: org.linqs.psl.application.learning.weight.maxlikelihood.VotedPerceptron  
***Description***:    Key for positive double property scaling the L2 regularization (\lambda / 2) * ||w||^2  

***Key***:            votedperceptron.l1regularization  
***Type***:           double  
***Default Value***:  0.0  
***Module***:         psl-core  
***Defining Class***: org.linqs.psl.application.learning.weight.maxlikelihood.VotedPerceptron  
***Description***:    Key for positive double property scaling the L1 regularization \gamma * |w|  

***Key***:            votedperceptron.stepsize  
***Type***:           double  
***Default Value***:  1.0  
***Module***:         psl-core  
***Defining Class***: org.linqs.psl.application.learning.weight.maxlikelihood.VotedPerceptron  
***Description***:    Key for positive double property which will be multiplied with the objective gradient to compute a step.  

***Key***:            votedperceptron.schedule  
***Type***:           boolean  
***Default Value***:  true  
***Module***:         psl-core  
***Defining Class***: org.linqs.psl.application.learning.weight.maxlikelihood.VotedPerceptron  
***Description***:    Key for Boolean property that indicates whether to shrink the stepsize by a 1/t schedule.  

***Key***:            votedperceptron.scalegradient  
***Type***:           boolean  
***Default Value***:  true  
***Module***:         psl-core  
***Defining Class***: org.linqs.psl.application.learning.weight.maxlikelihood.VotedPerceptron  
***Description***:    Key for Boolean property that indicates whether to scale gradient by number of groundings  

***Key***:            votedperceptron.averagesteps  
***Type***:           boolean  
***Default Value***:  true  
***Module***:         psl-core  
***Defining Class***: org.linqs.psl.application.learning.weight.maxlikelihood.VotedPerceptron  
***Description***:    Key for Boolean property that indicates whether to average all visited weights together for final output.  

***Key***:            votedperceptron.numsteps  
***Type***:           int  
***Default Value***:  25  
***Module***:         psl-core  
***Defining Class***: org.linqs.psl.application.learning.weight.maxlikelihood.VotedPerceptron  
***Description***:    Key for positive integer property. VotedPerceptron will take this many steps to learn weights.  

***Key***:            votedperceptron.nonnegativeweights  
***Type***:           boolean  
***Default Value***:  true  
***Module***:         psl-core  
***Defining Class***: org.linqs.psl.application.learning.weight.maxlikelihood.VotedPerceptron  
***Description***:    Key for boolean property. If true, only non-negative weights will be learned.  

***Key***:            maxspeudolikelihood.bool  
***Type***:           boolean  
***Default Value***:  false  
***Module***:         psl-core  
***Defining Class***: org.linqs.psl.application.learning.weight.maxlikelihood.MaxPseudoLikelihood  
***Description***:    Boolean property. If true, MaxPseudoLikelihood will treat RandomVariableAtoms as boolean valued. Note that this restricts the types of contraints supported.  

***Key***:            maxspeudolikelihood.numsamples  
***Type***:           int  
***Default Value***:  10  
***Module***:         psl-core  
***Defining Class***: org.linqs.psl.application.learning.weight.maxlikelihood.MaxPseudoLikelihood  
***Description***:    Key for positive integer property. MaxPseudoLikelihood will sample this many values to approximate the integrals in the marginal computation.  

***Key***:            maxspeudolikelihood.constrainttolerance  
***Type***:           double  
***Default Value***:  1e-5  
***Module***:         psl-core  
***Defining Class***: org.linqs.psl.application.learning.weight.maxlikelihood.MaxPseudoLikelihood  
***Description***:    Key for constraint violation tolerance  

***Key***:            maxspeudolikelihood.minwidth  
***Type***:           double  
***Default Value***:  1e-2  
***Module***:         psl-core  
***Defining Class***: org.linqs.psl.application.learning.weight.maxlikelihood.MaxPseudoLikelihood  
***Description***:    Key for positive double property. Used as minimum width for bounds of integration.  

***Key***:            maxmargin.tolerance  
***Type***:           double  
***Default Value***:  1e-3  
***Module***:         psl-core  
***Defining Class***: org.linqs.psl.application.learning.weight.maxmargin.MaxMargin  
***Description***:    Key for double property, cutting plane tolerance  

***Key***:            maxmargin.slackpenalty  
***Type***:           double  
***Default Value***:  1  
***Module***:         psl-core  
***Defining Class***: org.linqs.psl.application.learning.weight.maxmargin.MaxMargin  
***Description***:    Key for double property, slack penalty C, where objective is ||w|| + C (slack)  

***Key***:            maxmargin.maxiter  
***Type***:           int  
***Default Value***:  500  
***Module***:         psl-core  
***Defining Class***: org.linqs.psl.application.learning.weight.maxmargin.MaxMargin  
***Description***:    Key for positive integer, maximum number of constraints to add to quadratic program  

***Key***:            maxmargin.nonnegativeweights  
***Type***:           boolean  
***Default Value***:  true  
***Module***:         psl-core  
***Defining Class***: org.linqs.psl.application.learning.weight.maxmargin.MaxMargin  
***Description***:    Key for boolean property. If true, only non-negative weights will be learned.  

***Key***:            maxmargin.scalenorm  
***Type***:           NormScalingType  
***Default Value***:  NormScalingType.NONE  
***Module***:         psl-core  
***Defining Class***: org.linqs.psl.application.learning.weight.maxmargin.MaxMargin  
***Description***:    Key for NormScalingType enum property. Determines type of norm scaling MaxMargin will use in its objective.  

***Key***:            maxmargin.squareslack  
***Type***:           boolean  
***Default Value***:  false  
***Module***:         psl-core  
***Defining Class***: org.linqs.psl.application.learning.weight.maxmargin.MaxMargin  
***Description***:    Key for SquareSlack boolean property. Determines whether to penalize slack linearly or quadratically.  

***Key***:            minnormprog.conicprogramsolver  
***Type***:           ConicProgramSolverFactory  
***Default Value***:  new HomogeneousIPMFactory()  
***Module***:         psl-core  
***Defining Class***: org.linqs.psl.application.learning.weight.maxmargin.MinNormProgram  
***Description***:    Key for ConicProgramSolverFactory or String property. Should be set to a ConicProgramSolverFactory (or the binary name of one). The ConicReasoner will use this ConicProgramSolverFactory to instantiate a ConicProgramSolver.  

***Key***:            frankwolfe.tolerance  
***Type***:           double  
***Default Value***:  1e-5  
***Module***:         psl-core  
***Defining Class***: org.linqs.psl.application.learning.weight.maxmargin.FrankWolfe  
***Description***:    Key for double property, cutting plane tolerance  

***Key***:            frankwolfe.maxiter  
***Type***:           int  
***Default Value***:  500  
***Module***:         psl-core  
***Defining Class***: org.linqs.psl.application.learning.weight.maxmargin.FrankWolfe  
***Description***:    Key for positive integer, maximum iterations  

***Key***:            frankwolfe.averageweights  
***Type***:           boolean  
***Default Value***:  false  
***Module***:         psl-core  
***Defining Class***: org.linqs.psl.application.learning.weight.maxmargin.FrankWolfe  
***Description***:    Key for boolean property. If true, algorithm will output average weights when learning exceeds maximum number of iterations.  

***Key***:            frankwolfe.nonnegativeweights  
***Type***:           boolean  
***Default Value***:  true  
***Module***:         psl-core  
***Defining Class***: org.linqs.psl.application.learning.weight.maxmargin.FrankWolfe  
***Description***:    Key for boolean property. If true, only non-negative weights will be learned.  

***Key***:            frankwolfe.normalize  
***Type***:           boolean  
***Default Value***:  true  
***Module***:         psl-core  
***Defining Class***: org.linqs.psl.application.learning.weight.maxmargin.FrankWolfe  
***Description***:    Key for boolean property. If true, loss and gradient will be normalized by number of labels.  

***Key***:            frankwolfe.regparam  
***Type***:           double  
***Default Value***:  1  
***Module***:         psl-core  
***Defining Class***: org.linqs.psl.application.learning.weight.maxmargin.FrankWolfe  
***Description***:    Key for double property, regularization parameter \lambda, where objective is \lambda*||w|| + (slack)  

***Key***:            l1maxmargin.balanceloss  
***Type***:           LossBalancingType  
***Default Value***:  LossBalancingType.NONE  
***Module***:         psl-core  
***Defining Class***: org.linqs.psl.application.learning.weight.maxmargin.L1MaxMargin  
***Description***:    Key for LossBalancingType enum property. Determines the type of loss balancing MaxMargin will use. @see LossBalancingType  

***Key***:            weightlearning.reasoner  
***Type***:           ReasonerFactory  
***Default Value***:  new ADMMReasonerFactory()  
***Module***:         psl-core  
***Defining Class***: org.linqs.psl.application.learning.weight.WeightLearningApplication  
***Description***:    Key for Factory or String property. <p> Should be set to a ReasonerFactory or the fully qualified name of one. Will be used to instantiate a Reasoner. <p> This reasoner will be used when constructing ground models for weight learning, unless this behavior is overriden by a subclass.  

***Key***:            lazympeinference.reasoner  
***Type***:           ReasonerFactory  
***Default Value***:  new ADMMReasonerFactory()  
***Module***:         psl-core  
***Defining Class***: org.linqs.psl.application.inference.LazyMPEInference  
***Description***:    Key for Factory or String property. <p> Should be set to a ReasonerFactory or the fully qualified name of one. Will be used to instantiate a Reasoner.  

***Key***:            lazympeinference.maxrounds  
***Type***:           int  
***Default Value***:  100  
***Module***:         psl-core  
***Defining Class***: org.linqs.psl.application.inference.LazyMPEInference  
***Description***:    Key for int property for the maximum number of rounds of inference.  

***Key***:            mpeinference.reasoner  
***Type***:           ReasonerFactory  
***Default Value***:  new ADMMReasonerFactory()  
***Module***:         psl-core  
***Defining Class***: org.linqs.psl.application.inference.MPEInference  
***Description***:    Key for Factory or String property. <p> Should be set to a ReasonerFactory or the fully qualified name of one. Will be used to instantiate a Reasoner.  

***Key***:            LTNmaxspeudolikelihood.bool  
***Type***:           boolean  
***Default Value***:  false  
***Module***:         psl-core  
***Defining Class***: org.linqs.psl.application.topicmodel.LatentTopicNetworkMaxPseudoLikelihood  
***Description***:    Boolean property. If true, MaxPseudoLikelihood will treat RandomVariableAtoms as boolean valued. Note that this restricts the types of contraints supported.  

***Key***:            LTNmaxspeudolikelihood.numsamples  
***Type***:           int  
***Default Value***:  10  
***Module***:         psl-core  
***Defining Class***: org.linqs.psl.application.topicmodel.LatentTopicNetworkMaxPseudoLikelihood  
***Description***:    Key for positive integer property. MaxPseudoLikelihood will sample this many values to approximate the integrals in the marginal computation.  

***Key***:            LTNmaxspeudolikelihood.constrainttolerance  
***Type***:           double  
***Default Value***:  1e-5  
***Module***:         psl-core  
***Defining Class***: org.linqs.psl.application.topicmodel.LatentTopicNetworkMaxPseudoLikelihood  
***Description***:    Key for constraint violation tolerance  

***Key***:            LTNmaxspeudolikelihood.minwidth  
***Type***:           double  
***Default Value***:  1e-2  
***Module***:         psl-core  
***Defining Class***: org.linqs.psl.application.topicmodel.LatentTopicNetworkMaxPseudoLikelihood  
***Description***:    Key for positive double property. Used as minimum width for bounds of integration.  

***Key***:            CONFIG_PREFIX + ".lowerboundepsilon"  
***Type***:           double  
***Default Value***:  1e-6  
***Module***:         psl-core  
***Defining Class***: org.linqs.psl.application.topicmodel.reasoner.admm.LatentTopicNetworkADMMReasoner  
***Description***:    Key for positive double property. Minimum value that theta and phi parameters are allowed to take, enforced by clipping the consensus variables to this.  

***Key***:            latentTopicNetworks.hingeLossTheta  
***Type***:           boolean  
***Default Value***:  true  
***Module***:         psl-core  
***Defining Class***: org.linqs.psl.application.topicmodel.LatentTopicNetwork  
***Description***:    Key for Boolean property indicating whether to use a hinge-loss MRF to model theta.  

***Key***:            latentTopicNetworks.hingeLossPhi  
***Type***:           boolean  
***Default Value***:  false  
***Module***:         psl-core  
***Defining Class***: org.linqs.psl.application.topicmodel.LatentTopicNetwork  
***Description***:    Key for Boolean property indicating whether to use a hinge-loss MRF to model phi.  

***Key***:            latentTopicNetworks.numIterations  
***Type***:           int  
***Default Value***:  200  
***Module***:         psl-core  
***Defining Class***: org.linqs.psl.application.topicmodel.LatentTopicNetwork  
***Description***:    Key for positive integer property indicating the number of EM iterations to perform.  

***Key***:            latentTopicNetworks.numBurnIn  
***Type***:           int  
***Default Value***:  0  
***Module***:         psl-core  
***Defining Class***: org.linqs.psl.application.topicmodel.LatentTopicNetwork  
***Description***:    Key for positive integer property indicating the number of vanilla LDA EM iterations to perform before using hinge losses in the M step.  

***Key***:            latentTopicNetworks.numTopics  
***Type***:           int  
***Default Value***:  20  
***Module***:         psl-core  
***Defining Class***: org.linqs.psl.application.topicmodel.LatentTopicNetwork  
***Description***:    Key for positive integer property indicating the number of EM iterations to perform.  

***Key***:            latentTopicNetworks.alpha  
***Type***:           double  
***Default Value***:  1.01  
***Module***:         psl-core  
***Defining Class***: org.linqs.psl.application.topicmodel.LatentTopicNetwork  
***Description***:    Key for positive double property, the Dirichlet prior hyperparameter alpha.  

***Key***:            latentTopicNetworks.beta  
***Type***:           double  
***Default Value***:  1.01  
***Module***:         psl-core  
***Defining Class***: org.linqs.psl.application.topicmodel.LatentTopicNetwork  
***Description***:    Key for positive double property, the Dirichlet prior hyperparameter beta.  

***Key***:            latentTopicNetworks.weightLearning  
***Type***:           boolean  
***Default Value***:  false  
***Module***:         psl-core  
***Defining Class***: org.linqs.psl.application.topicmodel.LatentTopicNetwork  
***Description***:    Key for Boolean property indicating whether to perform pseudo-likelihood weight learning in the EM loop.  

***Key***:            latentTopicNetworks.firstWLearningIter  
***Type***:           int  
***Default Value***:  50  
***Module***:         psl-core  
***Defining Class***: org.linqs.psl.application.topicmodel.LatentTopicNetwork  
***Description***:    Key for positive integer property indicating the number of EM iterations to perform before performing weight learning.  

***Key***:            latentTopicNetworks.WLearningGap  
***Type***:           int  
***Default Value***:  10  
***Module***:         psl-core  
***Defining Class***: org.linqs.psl.application.topicmodel.LatentTopicNetwork  
***Description***:    Key for positive integer property indicating the number of EM iterations to between weight learning steps.  

***Key***:            latentTopicNetworks.initMStepToLDAtheta  
***Type***:           boolean  
***Default Value***:  false  
***Module***:         psl-core  
***Defining Class***: org.linqs.psl.application.topicmodel.LatentTopicNetwork  
***Description***:    Key for Boolean property indicating whether to initialize the ADMM variables to LDA, for theta. The alternative is to initialize at the previous iteration. LDA initialization may be best in high dimensions, while previous iteration initialization may be best with strong weights.  

***Key***:            latentTopicNetworks.initMStepToLDAphi  
***Type***:           boolean  
***Default Value***:  true  
***Module***:         psl-core  
***Defining Class***: org.linqs.psl.application.topicmodel.LatentTopicNetwork  
***Description***:    Key for Boolean property indicating whether to initialize the ADMM variables to LDA, for phi. The alternative is to initialize at the previous iteration. LDA initialization may be best in high dimensions, while previous iteration initialization may be best with strong weights.  

***Key***:            latentTopicNetworks.saveDir  
***Type***:           String  
***Default Value***:  ""  
***Module***:         psl-core  
***Defining Class***: org.linqs.psl.application.topicmodel.LatentTopicNetwork  
***Description***:    Key for string property indicating the directory to save intermediate topic models (if empty, do not save them).  

***Key***:            LTNmaxspeudolikelihood.bool  
***Type***:           boolean  
***Default Value***:  false  
***Module***:         psl-core  
***Defining Class***: org.linqs.psl.application.topicmodel.LatentTopicNetworkMaxPseudoLikelihood_Naive  
***Description***:    Boolean property. If true, MaxPseudoLikelihood will treat RandomVariableAtoms as boolean valued. Note that this restricts the types of contraints supported.  

***Key***:            LTNmaxspeudolikelihood.numsamples  
***Type***:           int  
***Default Value***:  10  
***Module***:         psl-core  
***Defining Class***: org.linqs.psl.application.topicmodel.LatentTopicNetworkMaxPseudoLikelihood_Naive  
***Description***:    Key for positive integer property. MaxPseudoLikelihood will sample this many values to approximate the integrals in the marginal computation.  

***Key***:            LTNmaxspeudolikelihood.constrainttolerance  
***Type***:           double  
***Default Value***:  1e-5  
***Module***:         psl-core  
***Defining Class***: org.linqs.psl.application.topicmodel.LatentTopicNetworkMaxPseudoLikelihood_Naive  
***Description***:    Key for constraint violation tolerance  

***Key***:            LTNmaxspeudolikelihood.minwidth  
***Type***:           double  
***Default Value***:  1e-2  
***Module***:         psl-core  
***Defining Class***: org.linqs.psl.application.topicmodel.LatentTopicNetworkMaxPseudoLikelihood_Naive  
***Description***:    Key for positive double property. Used as minimum width for bounds of integration.  

***Key***:            uaiformatreasoner.task  
***Type***:           Task  
***Default Value***:  Task.MPE  
***Module***:         psl-core  
***Defining Class***: org.linqs.psl.reasoner.bool.UAIFormatReasoner  
***Description***:    Key for Task enum property which is reasoner task to perform.  

***Key***:            uaiformatreasoner.seed  
***Type***:           int  
***Default Value***:  0  
***Module***:         psl-core  
***Defining Class***: org.linqs.psl.reasoner.bool.UAIFormatReasoner  
***Description***:    Key for integer property which is random seed for reasoner  

***Key***:            booleanmaxwalksat.maxflips  
***Type***:           int  
***Default Value***:  50000  
***Module***:         psl-core  
***Defining Class***: org.linqs.psl.reasoner.bool.BooleanMaxWalkSat  
***Description***:    Key for positive integer property that is the maximum number of flips to try during optimization  

***Key***:            booleanmaxwalksat.noise  
***Type***:           double  
***Default Value***:  (double) 1 / 100  
***Module***:         psl-core  
***Defining Class***: org.linqs.psl.reasoner.bool.BooleanMaxWalkSat  
***Description***:    Key for double property in [0,1] that is the probability of randomly perturbing an atom in a randomly chosen potential  

***Key***:            booleanmcsat.numsamples  
***Type***:           int  
***Default Value***:  2500  
***Module***:         psl-core  
***Defining Class***: org.linqs.psl.reasoner.bool.BooleanMCSat  
***Description***:    Key for length of Markov chain  

***Key***:            booleanmcsat.numburnin  
***Type***:           int  
***Default Value***:  500  
***Module***:         psl-core  
***Defining Class***: org.linqs.psl.reasoner.bool.BooleanMCSat  
***Description***:    Number of burn-in samples  

***Key***:            ad3reasoner.algorithm  
***Type***:           Algorithm  
***Default Value***:  Algorithm.AD3  
***Module***:         psl-core  
***Defining Class***: org.linqs.psl.reasoner.bool.AD3Reasoner  
***Description***:    Key for Algorithm enum property which is inference algorithm to use.  

***Key***:            conicreasoner.conicprogramsolver  
***Type***:           ConicProgramSolverFactory  
***Default Value***:  new HomogeneousIPMFactory()  
***Module***:         psl-core  
***Defining Class***: org.linqs.psl.reasoner.conic.ConicReasoner  
***Description***:    Key for org.linqs.psl.config.Factory or String property. Should be set to a org.linqs.psl.optimizer.conic.ConicProgramSolverFactory (or the binary name of one). The ConicReasoner will use this org.linqs.psl.optimizer.conic.ConicProgramSolverFactory to instantiate a org.linqs.psl.optimizer.conic.ConicProgramSolver, which will then be used for inference.  

***Key***:            admmreasoner.maxiterations  
***Type***:           int  
***Default Value***:  25000  
***Module***:         psl-core  
***Defining Class***: org.linqs.psl.reasoner.admm.ADMMReasoner  
***Description***:    Key for int property for the maximum number of iterations of ADMM to perform in a round of inference  

***Key***:            admmreasoner.stepsize  
***Type***:           double  
***Default Value***:  1  
***Module***:         psl-core  
***Defining Class***: org.linqs.psl.reasoner.admm.ADMMReasoner  
***Description***:    Key for non-negative double property. Controls step size. Higher values result in larger steps.  

***Key***:            admmreasoner.epsilonabs  
***Type***:           double  
***Default Value***:  1e-5  
***Module***:         psl-core  
***Defining Class***: org.linqs.psl.reasoner.admm.ADMMReasoner  
***Description***:    Key for positive double property. Absolute error component of stopping criteria.  

***Key***:            admmreasoner.epsilonrel  
***Type***:           double  
***Default Value***:  1e-3  
***Module***:         psl-core  
***Defining Class***: org.linqs.psl.reasoner.admm.ADMMReasoner  
***Description***:    Key for positive double property. Relative error component of stopping criteria.  

***Key***:            admmreasoner.stopcheck  
***Type***:           int  
***Default Value***:  1  
***Module***:         psl-core  
***Defining Class***: org.linqs.psl.reasoner.admm.ADMMReasoner  
***Description***:    Key for positive integer. The number of ADMM iterations after which the termination criteria will be checked.  

***Key***:            admmreasoner.numthreads  
***Type***:           int  
***Default Value***:  Runtime.getRuntime().availableProcessors()  
***Module***:         psl-core  
***Defining Class***: org.linqs.psl.reasoner.admm.ADMMReasoner  
***Description***:    Key for positive integer. Number of threads to run the optimization in.  

***Key***:            executablereasoner.executable  
***Type***:             
***Default Value***:    
***Module***:         psl-core  
***Defining Class***: org.linqs.psl.reasoner.ExecutableReasoner  
***Description***:    Key for String property which is path to reasoner executable. This is the rare PSL property that is mandatory to specify.  

***Key***:            atomeventframework.activation  
***Type***:           double  
***Default Value***:  0.01  
***Module***:         psl-core  
***Defining Class***: org.linqs.psl.model.atom.AtomEventFramework  
***Description***:    ; Key for double property in (0,1]. Activation events will be generated for RandomVariableAtoms when they meet or exceed this threshold.  

***Key***:            blocksolver.maxcgiter  
***Type***:           int  
***Default Value***:  1000000  
***Module***:         psl-core  
***Defining Class***: org.linqs.psl.optimizer.conic.ipm.solver.BlockSolver  
***Description***:    Key for integer property. The BlockSolver will throw an exception if the conjugate gradient solver completes this many iterations without solving the normal system.  

***Key***:            blocksolver.cgreltol  
***Type***:           double  
***Default Value***:  10e-10  
***Module***:         psl-core  
***Defining Class***: org.linqs.psl.optimizer.conic.ipm.solver.BlockSolver  
***Description***:    Key for double property. The conjugate gradient solver will terminate as converged if the residual is less than this value times the initial residual.  

***Key***:            blocksolver.cgabstol  
***Type***:           double  
***Default Value***:  10e-50  
***Module***:         psl-core  
***Defining Class***: org.linqs.psl.optimizer.conic.ipm.solver.BlockSolver  
***Description***:    Key for double property. The conjugate gradient solver will terminate as converged if the residual is less than this value.  

***Key***:            blocksolver.cgdivtol  
***Type***:           double  
***Default Value***:  10e5  
***Module***:         psl-core  
***Defining Class***: org.linqs.psl.optimizer.conic.ipm.solver.BlockSolver  
***Description***:    Key for double property. The BlockSolver will throw an exception if the conjugate graident solver reaches an iterate whose residual is at least this value times the initial residual.  

***Key***:            blocksolver.preconditionerterms  
***Type***:           int  
***Default Value***:  1  
***Module***:         psl-core  
***Defining Class***: org.linqs.psl.optimizer.conic.ipm.solver.BlockSolver  
***Description***:    Key for non-negative integer property. The BlockSolver preconditions the Schur's complement matrix by a truncated series summation. Higher values generally result in fewer conjugate gradient iterations, but each iteration is more time consuming.  

***Key***:            cgsolver.maxcgiter  
***Type***:           int  
***Default Value***:  1000000  
***Module***:         psl-core  
***Defining Class***: org.linqs.psl.optimizer.conic.ipm.solver.ConjugateGradient  
***Description***:    Key for integer property. The ConjugateGradient solver will throw an exception if the conjugate gradient solver completes this many iterations without solving the normal system.  

***Key***:            cgsolver.cgreltol  
***Type***:           double  
***Default Value***:  10e-10  
***Module***:         psl-core  
***Defining Class***: org.linqs.psl.optimizer.conic.ipm.solver.ConjugateGradient  
***Description***:    Key for double property. The ConjugateGradient solver will terminate as converged if the residual is less than this value times the initial residual.  

***Key***:            cgsolver.cgabstol  
***Type***:           double  
***Default Value***:  10e-50  
***Module***:         psl-core  
***Defining Class***: org.linqs.psl.optimizer.conic.ipm.solver.ConjugateGradient  
***Description***:    Key for double property. The ConjugateGradient solver will terminate as converged if the residual is less than this value.  

***Key***:            cgsolver.cgdivtol  
***Type***:           double  
***Default Value***:  10e5  
***Module***:         psl-core  
***Defining Class***: org.linqs.psl.optimizer.conic.ipm.solver.ConjugateGradient  
***Description***:    Key for double property. The ConjugateGradient solver will throw an exception if the conjugate graident solver reaches an iterate whose residual is at least this value times the initial residual.  

***Key***:            cgsolver.preconditioner  
***Type***:           PreconditionerFactory  
***Default Value***:  new IdentityPreconditionerFactory()  
***Module***:         psl-core  
***Defining Class***: org.linqs.psl.optimizer.conic.ipm.solver.ConjugateGradient  
***Description***:    Key for Factory or String property. Should be set to a PreconditionerFactory or the fully qualified name of one. Will be used to instantiate a DoublePreconditioner.  

***Key***:            ppipm.threadpoolsize  
***Type***:           int  
***Default Value***:  1  
***Module***:         psl-core  
***Defining Class***: org.linqs.psl.optimizer.conic.ipm.ParallelPartitionedIPM  
***Description***:      

***Key***:            hipm.dualize  
***Type***:           boolean  
***Default Value***:  true  
***Module***:         psl-core  
***Defining Class***: org.linqs.psl.optimizer.conic.ipm.HomogeneousIPM  
***Description***:    Key for boolean property. If true, the IPM will dualize the conic program before solving it. The IPM will substitute the results back into the original problem, so this should only affect the computational cost of #solve(ConicProgram), not the quality of the solution. @see Dualizer  

***Key***:            hipm.infeasibilitythreshold  
***Type***:           double  
***Default Value***:  10e-8  
***Module***:         psl-core  
***Defining Class***: org.linqs.psl.optimizer.conic.ipm.HomogeneousIPM  
***Description***:    Key for double property. The IPM will consider the problem primal, dual, or gap feasible if the primal, dual, or gap infeasibility is less than its value, respectively.  

***Key***:            hipm.gapthreshold  
***Type***:           double  
***Default Value***:  10e-6  
***Module***:         psl-core  
***Defining Class***: org.linqs.psl.optimizer.conic.ipm.HomogeneousIPM  
***Description***:    Key for double property. The IPM will iterate until the duality gap is less than its value.  

***Key***:            hipm.tauthreshold  
***Type***:           double  
***Default Value***:  10e-8  
***Module***:         psl-core  
***Defining Class***: org.linqs.psl.optimizer.conic.ipm.HomogeneousIPM  
***Description***:    Key for double property. The IPM will multiply its value by another value and consider tau small if tau is less than that product.  

***Key***:            hipm.muthreshold  
***Type***:           double  
***Default Value***:  10e-8  
***Module***:         psl-core  
***Defining Class***: org.linqs.psl.optimizer.conic.ipm.HomogeneousIPM  
***Description***:    Key for double property. The IPM will consider mu small if mu is less than its value times the initial mu.  

***Key***:            hipm.beta  
***Type***:           double  
***Default Value***:  10e-8  
***Module***:         psl-core  
***Defining Class***: org.linqs.psl.optimizer.conic.ipm.HomogeneousIPM  
***Description***:    Key for double property in (0,1). The IPM will stay in a neighborhood of the central path, the size of which is defined by its value. Larger values correspond to smaller neighborhoods.  

***Key***:            hipm.delta  
***Type***:           double  
***Default Value***:  0.5  
***Module***:         psl-core  
***Defining Class***: org.linqs.psl.optimizer.conic.ipm.HomogeneousIPM  
***Description***:    Key for double property in [0,1]. The IPM will use its value to determine how aggressively to minimize the objective (versus to follow the central path). Lower values correspond to more aggressive strategies.  

***Key***:            hipm.normalsolver  
***Type***:           NormalSystemSolverFactory  
***Default Value***:  new CholeskyFactory()  
***Module***:         psl-core  
***Defining Class***: org.linqs.psl.optimizer.conic.ipm.HomogeneousIPM  
***Description***:    Key for Factory or String property. Should be set to a NormalSystemSolverFactory or the fully qualified name of one. Will be used to instantiate a NormalSystemSolver.  

***Key***:            ipm.initfeasible  
***Type***:           boolean  
***Default Value***:  true  
***Module***:         psl-core  
***Defining Class***: org.linqs.psl.optimizer.conic.ipm.IPM  
***Description***:    Key for boolean property. If true, the IPM will initialize the conic program to a feasible point before solving it. @see FeasiblePointInitializer  

***Key***:            ipm.dualize  
***Type***:           boolean  
***Default Value***:  true  
***Module***:         psl-core  
***Defining Class***: org.linqs.psl.optimizer.conic.ipm.IPM  
***Description***:    Key for boolean property. If true, the IPM will dualize the conic program before solving it. The IPM will substitute the results back into the original problem, so this should only affect the computational cost of #solve(ConicProgram), not the quality of the solution. @see Dualizer  

***Key***:            ipm.dualitygapthreshold  
***Type***:           double  
***Default Value***:  0.0001  
***Module***:         psl-core  
***Defining Class***: org.linqs.psl.optimizer.conic.ipm.IPM  
***Description***:    Key for double property. The IPM will iterate until the duality gap is less than its value.  

***Key***:            ipm.infeasibilitythreshold  
***Type***:           double  
***Default Value***:  10e-8  
***Module***:         psl-core  
***Defining Class***: org.linqs.psl.optimizer.conic.ipm.IPM  
***Description***:    Key for double property. The IPM will iterate until the primal and dual infeasibilites are each less than its value. @see ConicProgram#getPrimalInfeasibility() @see ConicProgram#getDualInfeasibility()  

***Key***:            cgipm.maxcgiter  
***Type***:           int  
***Default Value***:  1000000  
***Module***:         psl-core  
***Defining Class***: org.linqs.psl.optimizer.conic.ipm.cg.ConjugateGradientIPM  
***Description***:    Key for integer property. The ConjugateGradientIPM will throw an exception if the conjugate gradient solver completes this many iterations without solving the normal system.  

***Key***:            cgipm.cgreltol  
***Type***:           double  
***Default Value***:  1e-10  
***Module***:         psl-core  
***Defining Class***: org.linqs.psl.optimizer.conic.ipm.cg.ConjugateGradientIPM  
***Description***:    Key for double property. The conjugate gradient solver will terminate as converged if the residual is less than this value times the initial residual.  

***Key***:            cgipm.cgabstol  
***Type***:           double  
***Default Value***:  1e-50  
***Module***:         psl-core  
***Defining Class***: org.linqs.psl.optimizer.conic.ipm.cg.ConjugateGradientIPM  
***Description***:    Key for double property. The conjugate gradient solver will terminate as converged if the residual is less than this value.  

***Key***:            cgipm.cgdivtol  
***Type***:           double  
***Default Value***:  1e5  
***Module***:         psl-core  
***Defining Class***: org.linqs.psl.optimizer.conic.ipm.cg.ConjugateGradientIPM  
***Description***:    Key for double property. The ConjugateGradientIPM will throw an exception if the conjugate graident solver reaches an iterate whose residual is at least this value times the initial residual.  

***Key***:            rdbmsdatastore.valuecolumn  
***Type***:           String  
***Default Value***:  truth  
***Module***:         psl-core  
***Defining Class***: org.linqs.psl.database.rdbms.RDBMSDataStore  
***Description***:    Key for String property for the name of the value column in the database.  

***Key***:            rdbmsdatastore.confidencecolumn  
***Type***:           String  
***Default Value***:  confidence  
***Module***:         psl-core  
***Defining Class***: org.linqs.psl.database.rdbms.RDBMSDataStore  
***Description***:    Key for String property for the name of the confidence column in the database.  

***Key***:            rdbmsdatastore.partitioncolumn  
***Type***:           String  
***Default Value***:  partition  
***Module***:         psl-core  
***Defining Class***: org.linqs.psl.database.rdbms.RDBMSDataStore  
***Description***:    Key for String property for the name of the partition column in the database.  

***Key***:            rdbmsdatastore.usestringids  
***Type***:           boolean  
***Default Value***:  true  
***Module***:         psl-core  
***Defining Class***: org.linqs.psl.database.rdbms.RDBMSDataStore  
***Description***:    Key for boolean property of whether to use RDBMSUniqueStringID as a UniqueID.  