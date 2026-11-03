# Group Sprint 1: Expected Goals (xG) Models

## Project Group

- Don Athipozhiyil
- Dylan Sharpe
- Luke Chinoy
- Pietro Neill

## Research question

**By exploring different xG models, how can we assess where on the pitch teams are under/over performing?**

Expected goals (xG) gives every shot a probability of being scored, based on factors such as where it was taken from and how it was taken [1]. Comparing the goals a team actually scores with its xG shows whether it is finishing better or worse than the quality of its chances suggests.

We built four classification models to predict whether a shot is scored, using Premier League shot data from Understat [2]. Each model was trained on the 2021/22 to 2024/25 seasons and tested on the same 2025/26 season, then scored with Brier score, log loss and ROC-AUC. The neural network performed best, so we used its predictions to create attacking and defensive xG heat maps for every Premier League team in 2025/26 [3].

## Reading order

### Data

The data is in the `data/` directory and should be read in this order:

1. `understat_shots.csv`: the original shot data collected from Understat
2. `shots_cleaned.csv`: the cleaned and processed data used by every model

### Report

All report content is in the `report/` directory and should be read in this order:

1. `01_Introduction.ipynb`
2. `02_data_processing.ipynb`
3. `03_logistic_regression.ipynb`
4. `04_Gradient_Boosting.ipynb`
5. `05_random_forest.ipynb`
6. `06_neural_networks`
7. `07_comparison_and_analysis.ipynb`
8. `08_heatmaps.ipynb`

The introduction and data processing should be read first. The four model notebooks (03 to 06) can be read in any order. The comparison and analysis notebook brings the models together and includes our conclusions, and the heat maps notebook uses the best model (the neural network) to look at where each team over- and underperforms.

### Results

The `results/` directory holds each model's xG predictions for the 2025/26 season, the performance analysis table, and the attacking and defensive heat map images.

## Requirements

The Python notebooks use the packages listed below:

- numpy
- pandas
- matplotlib
- seaborn
- scikit-learn
- xgboost
- mplsoccer (version 1.5.1, as 1.6.0 does not run on Python 3.9)
- jupyter

The R neural network model uses:

- nnet
- tidyverse
- readr
- knitr

## Who did what

- **Don**: data cleaning and processing, logistic regression model
- **Dylan**: neural network model in R
- **Luke**: random forest model, heat maps
- **Pietro**: gradient boosting model

## Evidence

Our working is shown in our own directories:

- `don/`
- `dylan/`
- `luke/`
- `pietro/`

The final models and analysis were brought together in the `report/` directory.

## References

1. Colman, J. (2025) *What is xG in football and how does it work?* BBC Sport, September 2025. Available at: https://www.bbc.co.uk/sport/football/articles/cgrqd18q0rgo
2. Understat (2026) *Understat: Advanced Football Statistics*. Available at: https://understat.com
3. Sumpter, D. and Andrzejewski, A. (2022) *Plotting shot location*, Soccermatics. Available at: https://soccermatics.readthedocs.io/en/latest/gallery/lesson2/plot_xGModelFit.html#plotting-shot-location
