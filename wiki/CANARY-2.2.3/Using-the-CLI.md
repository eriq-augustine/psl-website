---
layout: wiki
---

PSL provides a Command Line Interface.
The CLI is the easiest interface to PSL and handles most situations where you do not need additional customization.

## Setup

PSL requires that you have [Java installed](Prerequisites.md). 

## Running your first program
Let's first download the files for our example program, run it and see what it does! 

In this program, we'll use information about known locations of some people, know people know, and what people like to infer who knows each other. We'll first run the program and see the output. We will be working from the command line so open up your shell or terminal.

### Get the code
As with the other PSL examples, you can find all the code in our [psl-examples repository](https://github.com/linqs/psl-examples).
We will be using the `simple-acquaintances` example.

```
git clone https://github.com/linqs/psl-examples.git
cd psl-examples/simple-acquaintances/cli
```

### Run your first PSL program

All the required commands are contained in the `run.sh` script.
However, the commands are very simple and can also be run individually.

The PSL jar will be fetched automatically.
You can also select what version of PSL if fetched/used at the top of this script.

You should now see output that looks like this (note that the order of the output lines may differ): 
```
Running PSL Inference
0    [main] INFO  org.linqs.psl.cli.Launcher  - Loading data
81   [main] INFO  org.linqs.psl.cli.Launcher  - Data loading complete
81   [main] INFO  org.linqs.psl.cli.Launcher  - Loading model
159  [main] INFO  org.linqs.psl.cli.Launcher  - Model loading complete
159  [main] INFO  org.linqs.psl.cli.Launcher  - Starting inference
224  [main] INFO  org.linqs.psl.application.inference.MPEInference  - Grounding out model.
320  [main] INFO  org.linqs.psl.application.inference.MPEInference  - Beginning inference.
420  [main] INFO  org.linqs.psl.reasoner.admm.ADMMReasoner  - Optimization completed in 404 iterations. Primal res.: 0.022839682, Dual res.: 6.607145E-4
420  [main] INFO  org.linqs.psl.application.inference.MPEInference  - Inference complete. Writing results to Database.
447  [main] INFO  org.linqs.psl.application.inference.MPEInference  - Results committed to database.
457  [main] INFO  org.linqs.psl.cli.Launcher  - Inference Complete
461  [main] INFO  org.linqs.psl.cli.Launcher  - Starting discrete evaluation
472  [main] INFO  org.linqs.psl.cli.Launcher  - Discrete evaluation results for KNOWS -- Accuracy: 0.5961538461538461, Error: 21.0, Positive Class Precision: 0.7333333333333333, Positive Class Recall: 0.6285714285714286, Negative Class Precision: 0.4090909090909091, Negative Class Recall: 0.5294117647058824,
472  [main] INFO  org.linqs.psl.cli.Launcher  - Discrete evaluation complete
```

### Where are the prediction?
By default, the PSL examples output the results into the `inferred-predicates` directory.
The results for this program will looks something like:
```
$ cat inferred-predicates/KNOWS.txt | sort
'Alex'	'Arti'	0.9966862201690674
'Alex'	'Ben'	0.5923290848731995
'Alex'	'Dhanya'	0.48786869645118713
< ... 50 rows omitted for brevity ...>
'Steve'	'Elena'	0.49548637866973877
'Steve'	'Jay'	0.614285409450531
'Steve'	'Sabina'	0.5133784413337708
```

### What did it do?
Now that we've run our first program that performs link prediction to infer who knows who, let's understand the steps that we went through to infer the unknown values: defining the underlying model, providing data to the model, and running inference to classify the unknown values.

#### Defining a Model
A model in PSL is a set of logic-like rules. 

The model is defined inside a text file with the format `.psl`. We describe this model in the file `simple-acquaintances.psl`.
Let's have a look at the rules that make up our model: 
```
20: Lived(P1, L) & Lived(P2, L) & (P1 != P2) -> Knows(P1, P2) ^2
5: Lived(P1, L1) & Lived(P2, L2) & (P1 != P2) & (L1 != L2) -> !Knows(P1, P2) ^2
10: Likes(P1, L) & Likes(P2, L) & (P1 != P2) -> Knows(P1, P2) ^2
5: Knows(P1, P2) & Knows(P2, P3) & (P1 != P3) -> Knows(P1, P3) ^2
Knows(P1, P2) = Knows(P2, P1) .
5: !Knows(P1, P2) ^2
```
The model is expressing the intuition that people who have lived in the same location or like the same thing may know each other.
The integer values at the beginning of rules indicate the weight of the rule.
Intuitively, this tells us the relative importance of satisfying this rule compared to the other rules.
The `^2` at the end of the rules indicates that the hinge-loss functions based on groundings of these rules are squared, for a smoother tradeoff.
For a full description of rule syntax, see the [Rule Specification](Rule-Specification.md).
For more details on hinge-loss functions and squared potentials, see the publications on our [PSL webpage](http://psl.linqs.org). 

#### Loading the Data
PSL rules consist of predicates. The names of the predicates used in our model and possible substitutions of these predicates with actual entities from our network are defined inside the file `simple-acquaintances.data`.
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
We are aware of some instances of people knowing each other, but wish to infer the other instances `Knows` an open predicate.

In the `observations` section, for each predicate for which we have observations, we specify the name of the tab-separated file containing the observations.
For example, `knows_obs.txt` and `lived_obs.txt` specifies which people know each other and where some of these people live, respectively.

The `targets` section specifies a `.txt` file that, for each open predicate, lists all substitutions of that predicate that we wish to infer.
In `knows_targets.txt`, we specify the pairs of people for whom we wish to infer.

The `truth` section specifies a `.txt` file that provides a set of ground truth observations for each open predicate.
Here, we give the actual values for the `Knows` predicate for all the people in the network as training labels. We describe the the general data loading scheme in more detail in the sections below.

More advanced features of the `.data` file can be found on the [CLI Data File Format](CLI-Data-File-Format.md) page.

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

A `closed` predicate is a predicate whose values are always observed.
For example, the `knows` predicate from the simple example is closed because we fully observe the entire network of people that know one another.
On the other hand, an `open` predicate is a predicate where some values may be observed, but some values are missing and thus, need to be inferred.

As shown above, then create your `observations:`, `targets:` and `truth:` sections that list the names of files that specify the observed values for predicates, values you want to infer for open predicates, and observed ground truth values for open predicates.

For all predicates, all possible substitutions should be specified either in the target files or in the observation files.
The observations files should contain the known values for all closed predicates and can contain some of the known values for the open predicates.
The target files tell PSL which substitutions of the open predicates it needs to infer.
Target files cannot be specified for closed predicates as they are fully observed.

The truth files provide training labels in order learn the weights of the rules directly from data.
This is similar to learning the weights of coefficients in a logistic regression model from training data.

## Running Inference

Run inference with the general command:
```sh
java -jar psl-cli.jar --infer --model [name of model file].psl --data [name of data file].data
```

When we run inference, the inferred values are outputted to the screen.
If you want to write the outputs to a file and use the inferred values in various ways downstream, you can use:
```sh
java -jar psl-cli.jar --infer --model [name of model file].psl --data [name of data file].data --output [directory to write output files]
```

Values for all predicates will be output as tab-separated files in the specified output directory.

With the inferred values, some downstream tasks that you can perform are:
   - if you have a gold standard set of labels, you can evaluate your model by computing standard metrics like accuracy, AUC, F1, etc.
   - you may want to use the predicted outputs of PSL as inputs for another model.
   - you may want to visualize the predicted values and use the outputs of PSL as inputs to a data visualization program.