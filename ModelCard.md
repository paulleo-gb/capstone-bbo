<h3>Model Name: Black Box Optimisation </h3>
<h3>Type: Bayesian Optimisation </h3>
<h3>Version: 1.0 </h3>
</p>
<hr/>

## Intended use
It is suitable for parameter optimisation, performance maximisation under unknown functional relationship. This approach is intended to identify the maximum values of eight unknown, or “black box”, functions.
</p>

## What tasks is it suitable for?
The task involves eight synthetic functions whose internal workings are not visible. Because the relationship between inputs and outputs is unknown, the approach must rely on observed data rather than direct knowledge of each function.
</p>

## Optimisation goal
The goal is to find input values that produce the highest possible output for each function, using the available dataset to guide the search.
</p>

## What use cases should be avoided?
- Very high dimensional optimisation <br/> - because GP struggles in high dimensions due to the curse of dimensionality.
- Functions of thousands of parameters <br/> - because BO is intended for hyperparameters, not millions of trainable parameters
</p>

## Details
- Fit a surrogate model: <br/>I selected a surrogate model to approximate the objective function.
- Use a Gaussian process surrogate: <br/>I used a Gaussian process (GP), a common surrogate model that provides predictions together with uncertainty estimates.
- Define an acquisition function: <br/>I defined an acquisition function to guide the search for new points.
- Select acquisition strategies: <br/>I used common acquisition functions, including Expected Improvement (EI) and Upper Confidence Bound (UCB). These functions helped determine where to query next by balancing the surrogate model’s predictions with its uncertainty estimates.
- Run the optimisation loop: <br/> I selected new points suggested by the acquisition functions for each query. After each query, I updated the surrogate model with the new input–output pair.
- Set the iteration schedule:<br/> I ran the optimisation for a fixed number of iterations across the 7-week period, using an equal number of queries each week.
- Record the best result:<br/> After completing the queries, I recorded the best-performing input–output pair: the input that produced the highest output. This record supports benchmarking and future analysis.
</p>

## Performance
- Performance metrics:<br/> Performance was evaluated using the highest output value identified during the optimisation process. Week-by-week improvements were tracked as additional query points were evaluated.
- Strategy assessment:<br/> Visual inspection of optimisation progress, together with comparisons of outputs across rounds, was used to assess the effectiveness of the strategy.
- Benchmarking approach:<br/> Because the true functions were hidden, performance was measured relative to previous results rather than against a known ground truth.
</p>

## Assumptions and limitations
### Assumptions
- Local Smoothness:<br/> We assume the objective function obeys the Matern kernel's prior (i.e., small changes in input results in small changes in output.
- Stationarity:<br/> It is assumed that the function logic doesn’t change over the 13 rounds.
### Limitations
- Curse of Dimensionality:<br/> Performance in 6D–8D functions is significantly limited by the query budget.
- Local Optima:<br/> The current strategy prevents the model from discovering better output if they lie far from the current best point, which may result in the model being converge prematurely.
</p>

## Ethical considerations
- Transparency:<br/> All decision logic, code and data are maintained in open Jupyter notebooks and .npy files to maintain transparency.
- Data Privacy:<br/> This framework processes purely numerical objective values; no personal or sensitive data is involved in this framework.
- Bias:<br/> The model is "biased" only by its kernel choice and prior, which are explicitly stated.

