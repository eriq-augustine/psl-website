---
layout: wiki
---

PSL provides a Command Line Interface.
The CLI is the easiest interface to PSL and handles most situations where you do not need additional customization.

## Setup

PSL requires that you have [Java installed](Prerequisites.md). 

The PSL jar file `psl-cli-CANARY.jar` already contains all required PSL libraries that you need to be able to run your PSL programs. You can find a current snapshot of this `.jar` file from our [resources directory](https://linqs-data.soe.ucsc.edu/maven/repositories/psl-releases/org/linqs/psl-cli/CANARY/psl-cli-CANARY.jar) until we finalize our v2.0 release.

In this page we will be using the `CANARY` build, but you may use any PSL jar that is at least version 2.0.0.

## Running your first program
Let's first download the files for our example program, run it and see what it does! 

In this program, we'll use information about known locations of some people, know people know, and what people like to infer who knows each other. We'll first run the program and see the output. We will be working from the command line so open up your shell or terminal.

### Get the code
As with the other PSL examples, you can find all the code in our [psl-examples repository](https://bitbucket.org/linqs/psl-examples).
We will be using the `easy` `link prediction` example.

```
git clone https://bitbucket.org/linqs/psl-examples.git
cd psl-examples/link_prediction/easy/cli
```

### Run your first PSL program

All the required commands are contained in the `run.sh` script.
However, the commands are very simple and can also be run individually.
You only need to fetch the jar (done in the setup steps above) and run PSL.
```
wget https://linqs-data.soe.ucsc.edu/maven/repositories/psl-releases/org/linqs/psl-cli/CANARY/psl-cli-CANARY.jar
java -jar psl-cli-CANARY.jar -infer -model simple_lp.psl -data simple_lp.data
```

You should now see output that looks like this (note that the order of the output lines may differ): 
```
0    [main] INFO  org.linqs.psl.config.ConfigManager  - PSL configuration psl.properties file not found. Only default values will be used unless additional properties are specified.
6    [main] INFO  org.linqs.psl.config.ConfigManager  - No value found for option cli.dbpath. Returning default of /tmp/cli.
19   [main] INFO  org.linqs.psl.config.ConfigManager  - No value found for option cli.dbpath. Returning default of /tmp/cli.
133  [main] INFO  org.linqs.psl.config.ConfigManager  - No value found for option cli.rdbmsdatastore.valuecolumn. Returning default of truth.
134  [main] INFO  org.linqs.psl.config.ConfigManager  - No value found for option cli.rdbmsdatastore.confidencecolumn. Returning default of confidence.
134  [main] INFO  org.linqs.psl.config.ConfigManager  - No value found for option cli.rdbmsdatastore.partitioncolumn. Returning default of partition.
150  [main] INFO  org.linqs.psl.config.ConfigManager  - Found value true for option cli.rdbmsdatastore.usestringids.
154  [main] INFO  org.linqs.psl.cli.Launcher  - data:: loading:: ::starting
208  [main] WARN  org.linqs.psl.database.rdbms.RDBMSDataStoreMetadata  - Determining max partition, no partitions found null
260  [main] INFO  org.linqs.psl.cli.Launcher  - data:: loading:: ::done
260  [main] INFO  org.linqs.psl.cli.Launcher  - model:: loading:: ::starting
320  [main] INFO  org.linqs.psl.cli.Launcher  - model:: loading:: ::done
335  [main] INFO  org.linqs.psl.cli.Launcher  - operation::infer ::starting
336  [main] INFO  org.linqs.psl.config.ConfigManager  - Found value org.linqs.psl.reasoner.admm.ADMMReasonerFactory@34a0ee3f for option cli.mpeinference.reasoner.
339  [main] INFO  org.linqs.psl.config.ConfigManager  - No value found for option cli.admmreasoner.maxiterations. Returning default of 25000.
339  [main] INFO  org.linqs.psl.config.ConfigManager  - No value found for option cli.admmreasoner.stepsize. Returning default of 1.0.
339  [main] INFO  org.linqs.psl.config.ConfigManager  - No value found for option cli.admmreasoner.epsilonabs. Returning default of 1.0E-5.
339  [main] INFO  org.linqs.psl.config.ConfigManager  - No value found for option cli.admmreasoner.epsilonrel. Returning default of 0.001.
339  [main] INFO  org.linqs.psl.config.ConfigManager  - No value found for option cli.admmreasoner.stopcheck. Returning default of 1.
340  [main] INFO  org.linqs.psl.config.ConfigManager  - No value found for option cli.admmreasoner.numthreads. Returning default of 8.
345  [main] INFO  org.linqs.psl.application.inference.MPEInference  - Grounding out model.
463  [main] INFO  org.linqs.psl.application.inference.MPEInference  - Beginning inference.
647  [main] INFO  org.linqs.psl.reasoner.admm.ADMMReasoner  - Optimization completed in  662 iterations. Primal res.: 0.022740805753995307, Dual res.: 5.499541249718983E-4
647  [main] INFO  org.linqs.psl.application.inference.MPEInference  - Inference complete. Writing results to Database.
669  [main] INFO  org.linqs.psl.cli.Launcher  - operation::infer inference:: ::done
KNOWS('Alex', 'Jay') = 0.6563306840338842
KNOWS('Steve', 'Ben') = 0.44100447478155413
< ... 50 rows omitted for brevity ...>
KNOWS('Sabina', 'Arti') = 0.7194742867561412
KNOWS('Dhanya', 'Elena') = 0.3682973941849134
KNOWS('Elena', 'Sabina') = 0.3287882658219531
```

### What did it do?
Now that we've run our first program that performs link prediction to infer who knows who, let's understand the steps that we went through to infer the unknown values: defining the underlying model, providing data to the model, and running inference to classify the unknown values.

#### Defining a Model
A model in PSL is a set of logic-like rules. 

The model is defined inside a text file with the format `.psl`. We describe this model in the file `simple_lp.psl`.
Let's have a look at the rules that make up our model: 
```
20:    Lived(P1,L) & Lived(P2,L) & P1!=P2   -> Knows(P1,P2) ^2
5:     Lived(P1,L1) & Lived(P2,L2) & P1!=P2 & L1!=L2  -> !Knows(P1,P2) ^2
10:    Likes(P1,L) & Likes(P2,L) & P1!=P2  -> Knows(P1,P2) ^2
5:     Knows(P1,P2) & Knows(P2,P3) & P1!=P3 -> Knows(P1,P3) ^2
10000: Knows(P1,P2) -> Knows(P2,P1) ^2
5:     !Knows(P1,P2) ^2
```
The model is expressing the intuition that people who have lived in the same location or like the same thing may know each other.
The integer values at the beginning of rules indicate the weight of the rule.
Intuitively, this tells us the relative importance of satisfying this rule compared to the other rules.
The `^2` at the end of the rules indicates that the hinge-loss functions based on groundings of these rules are squared, for a smoother tradeoff.
For more details on hinge-loss functions and squared potentials, see the publications on our [PSL webpage](http://psl.linqs.org). 

#### Loading the Data
PSL rules consist of predicates. The names of the predicates used in our model and possible substitutions of these predicates with actual entities from our network are defined inside the file `simple_lp.data`.
Let's have a look:
```
predicates:
  Knows/2: open
  Likes/2: closed
  Lived/2: closed

observations:
  Knows : ../data/knows_obs.txt
  Lived : ../data/lived_obs.txt
  Likes : ../data/likes_obs.txt

targets:
  Knows : ../data/knows_targets.txt

truth:
  Knows : ../data/knows_truth.txt
```
In the `predicate` section, we list all the predicates that will be used in rules that define the model.
The keyword `open` indicates that we want to infer some substitutions of this predicate while `closed` indicates that this predicate is fully observed.
I.e. all substitutions of this predicate have known values and will behave as evidence for inference. 

For our simple example, we fully observe where people have lived and what things they like (or dislike).
Thus, `Likes` and `Lived` are both closed predicates.
We are aware of some instances of people knowing each other, but wish to infer the other insatnces `Knows` an open predicate.

In the `observations` section, for each predicate for which we have observations, we specify the name of the `.txt` file containing the observations.
For example, `knows_obs.txt` and `lived_obs.txt` specifies which people know each other and where some of these people live, respectively.

The `targets` section specifies a `.txt` file that, for each open predicate, lists all substitutions of that predicate that we wish to infer.
In `knows_targets.txt`, we specify the pairs of people for whom we wish to infer.

The `truth` section specifies a `.txt` file that provides a set of ground truth observations for each open predicate.
Here, we give the actual values for the `Knows` predicate for all the people in the network as training labels. We describe the the general data loading scheme in more detail in the sections below.

#### Inferring the Missing Values

When we run the `java -jar psl-cli-CANARY.jar -infer -model simple_lp.psl -data simple_lp.data` command with the `-infer` flag, PSL's inference engine substitutes values from the data files into the rules of the model and runs inference on the targets.

## Writing PSL Rules

To create a PSL model, you should define a set of rules in a `.psl` file.
Let's go over the basic syntax to write rules. Consider this very general rule form:
```
w: P(A,B) & Q(B,C) -> R(A,C) ^2
```

The first part of the rule, `w`, is an integer value that specifies the weight of the rule.
In this example, `P`, `Q` and `R` are predicates.
Logical rules consist of the rule "body" and rule "head."
The body of the rule appears before the `->` which denotes logical implication.
The body can have one or more predicates conjuncted together with the `&` that denotes logical conjunctions.
The head of the rule should be a single predicate.
The predicates that appear in the body and head can be any combination of open and closed predicate types.

The [Rule Specification](Rule-Specification.md) page contains the full syntax for PSL rules.

## Organizing your Data 
In a `.data` file, you should first define your `predicates:` as shown in the above example.
Use the `open` and `closed` keywords to characterize each predicate. 

An `closed` predicate is a predicate whose values are always observed.
For example, the `knows` predicate from the simple example is closed because we fully observe the entire network of people that know one another.
On the other hand, an `open` predicate is a predicate where some values may be observed, but some values are missing and thus, need to be inferred.  

As shown above, then create your `observations:`, `targets:` and `truth:` sections that list the names of `.txt` files that specify the observed values for predicates, values you want to infer for open predicates and observed ground truth values for open predicates. 

For all predicates, all possible substitutions should be specified either in the target files or in the observation files.
The observations files should contain the known values for all closed predicates and can contain some of the known values for the open predicates.
The target files tell PSL which substitutions of the open predicates it needs to infer.
Target files cannot be specified for closed predicates as they are fully observed. 

The truth files provide training labels in order learn the weights of the rules directly from data.
This is similar to learning the weights of coefficients in a logistic regression model from training data.
Weight learning is described below in greater detail.

## Running Inference

Run inference with the general command:

`java -jar psl-cli-CANARY.jar -infer -model [name of model file].psl -data [name of data file].data`

When we run inference, the inferred values are outputted to the screen as shown for our example above.
If you want to write the outputs to a file and use the inferred values in various ways downstream, you can use:

`java -jar psl-cli-CANARY.jar -infer -model [name of model file].psl -data [name of data file].data -output [directory to write output files]`

Values for all predicates will be output as `.csv` files in the specified output directory.

With the inferred values, some downstream tasks that you can perform are:
- if you have a gold standard set of labels, you can evaluate your model by computing standard metrics like accuracy, AUC, F1, etc.
- you may want to use the predicted outputs of PSL as inputs for another model.
- you may want to visualize the predicted values and use the outputs of PSL as inputs to a data visualization program.