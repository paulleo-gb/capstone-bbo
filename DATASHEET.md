## Motivation
This dataset was developed for learning and experimenting Bayesian Black Box Optimisation as part of the Capstone project. Aim is to try and evaluate how different optimisation strategies will behave for different functions, which are expensive to evaluate, internals are unknown and accessible only through queries, when the budget is constrained.
<br/>
  
## Composition
This dataset contains eight synthetic black box functions of varying dimensionality ranging from 2 dimensions to 8 dimensions.
```
data
|
|__ initial_data
    |
    |__ function_1
        |
        |__initial_inputs.npy
        |__ initial_outputs.npy

```
This initial data is used for the first iteration. Further data are stored in the respectively named folders

```
data
|
|__ function_1
    |
    |__ week-01
        |
        |__initial_inputs.npy
        |__ initial_outputs.npy

```
<br/>
  
## Collection process

### Query generation
- start with the initial data provided
- apply Bayesian Optimisation using Gaussian ProcessEach week and find the output
- submit the output
- receive a new set of input data for each function for the next iteration
- use all the input data (initial data + new input data received) for the next iteraion and find the output
- submit the output
- decisions around strategy for the next query submission are considered and updates to surrogate models and acquiisition functions are made based on this (e.g., exploration or exploitation approaches)
  
### Strategies
Data points were generated iteratively using Bayesian Optimisation technique
- Exploration in rounds 1 to 3
- Balance between exploraion and exploitation in rounds 4 to 6
- Exploitation from round 7 

### Time frame
Over a time frame of 7 weeks, one query per week, per function

<br/>

## Preprocessing and uses
I haven't applied any transformation to the input and output data.

### Intended uses
- To study and evaluate strategies under limited conditions
- Analyse the trade-offs between exploration and exploitation
- Assess black-box optimisation concepts

### Inappropriate uses
- Generalisation to other domains without their own adaptation
- Decision-making without human oversight
- This data is not intended for demographic or societal impact analysis
  
<br/>

## Distribution and maintenance
The data is hosted in a public GitHub repository and is part of the capstone project. It is intended for academic, non-commercial use. Maintained by the author.
