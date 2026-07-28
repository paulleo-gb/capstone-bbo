# Black Box Optimisation (BBO) Capstone Project
## Project Overview
Goal of this project is to iteratively find the maximum output for eight different black-box functions. They are called black-box functions because the internals of each function is unknown. We feed input to the functions, the functions processes the inputs and gives the output.
For the next week, inputs and outputs of the previous week is then added to the original inputs and outputs and fed into the functions. Functions processes this input and gives the result back.
This cycle is repeated for each of the 8 functions for 13 weeks.

I used Bayesian optimisation strategy which is used to find the maximum and minimum of complex black-box functions.
Components of Bayesian optimisation used:

Surrogate model - Builds a probabilistic model, Gaussian Process, that approximates the function.

Acquistic function - Balances exploration and exploitation

## Repository Structure

data – contains the input files that provides the data for each week's each function on which the experimentation is done. initial_outputs.npy contains the output of previous weeks.

```
data
|
|__ function_1
    |
    |__ week_01
        |
        |__ initial_inputs.npy
        |__ initial_outputs.npy
```
notebooks - contains Jupyter notebooks, one each for each week and each function. Each notebook contains the code to set up the model, experiment and display the results.

```
notebooks
|
|__ function_1
    |
    |__ week_01
        |
        |__ week01_function1.jpynb
```

utilities - contains utility methods that is used across the Jupyter notebooks

```
utilities
|
|__ common_functions.py
```

## Documentation
- [Model Card](ModelCard.md) 

## Inputs and Outputs
Each black-box function accepts a vector of continuous numeric inputs and returns a single scalar value.  
Input data for each function range from 2 dimensions up to 8 dimensions  
Function-1: 2D  
Function-2: 2D  
Function-3: 3D  
Function-4: 4D  
Function-5: 4D  
Function-6: 5D  
Function-7: 6D  
Function-8: 8D  

Output: Each function returns a scalar number. It can be positive or negative. Higher the values better are the results.

## Technologies
<ul>
  <li>Jupyter note books</li>
  <li>Python</li>
  <li>NumPy</li>
  <li>SciPy</li>
  <li>Scikit-Learn</li>
  <li>Matplotlib</li>
  <li>sklearn</li>
  <li>pathlib</li>
</ul>


