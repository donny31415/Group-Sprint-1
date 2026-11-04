# Group Sprint 1: Expected Goals (xG) Modelling and Analysis

## 1. Project Group and Equity Statement

- **Don Athipozhiyil** – 25% contribution
- **Dylan Sharpe** – 25% contribution
- **Luke Chinoy** – 25% contribution
- **Pietro Neill** – 25% contribution

**Equity statement:** All four members contributed equally to the project, with an agreed contribution of 25% each. Contributions included data exploration and preparation, mathematical and statistical modelling, implementation, model evaluation, spatial analysis and report development. Individual working histories, including exploratory work and model development, are documented in the corresponding member directories.

## 2. Project Overview and Objectives

Expected goals (xG) is a measure of the probability that a particular football shot results in a goal. Rather than classifying each shot directly as a goal or a non-goal, an xG model estimates the conditional probability of a goal given the available information about the shot.

The aim of this project is to investigate how effectively different supervised machine learning approaches can estimate this probability. We use historical shot-level data from Understat to develop and compare four models, before examining how their predictions can be used to analyse shooting performance.

The project has four main objectives:

1. **Model development:** Implement and investigate four modelling approaches: logistic regression, gradient boosting, random forest and a neural network. We also establish a constant base-rate model as a baseline for comparison.
2. **Probabilistic evaluation:** Compare the models using the Brier score and log loss, which assess the quality of predicted probabilities, alongside ROC-AUC, which measures their ability to distinguish between goals and non-goals.
3. **Benchmarking and robustness:** Evaluate all models on an unseen season and compare their predictions against Understat's existing xG estimates. We consider calibration and uncertainty when interpreting differences in performance.
4. **Spatial and team-level analysis:** Use the predicted probabilities to examine patterns in shot quality across the pitch and compare aggregated expected goals with actual goal output.

An important part of the project is considering what makes a model effective for this particular problem. A model that ranks shots well does not necessarily produce accurate probabilities, and a high classification accuracy does not necessarily indicate good xG predictions. We therefore consider the strengths and limitations of the evaluation metrics alongside the model results.

## 3. Repository Structure and Reading Order

The `report/` directory contains the main project submission. The notebooks and rendered analysis should be read in the following order.

### 3.1 Preparation and setup

Before running the analysis, install the required Python packages using:

```bash
pip install -r requirements.txt
```

Python 3.9 or later is recommended.

The neural network analysis was implemented in R. R and the required R packages are needed to rerun the source analysis. RStudio and Pandoc are required to knit the R Markdown file into HTML. The rendered HTML output is included in the report directory so that the analysis and results can be reviewed without running the R code.

The cleaned dataset used by the models is included in `data/shots_cleaned.csv`. The raw data and exploratory dataset comparisons are also retained in the data directory. The individual analysis folders contain additional development work and scripts.

### 3.2 Main report reading order

| Order | File | Purpose |
|---|---|---|
| 1 | `01_introduction.ipynb` | Introduces the xG prediction problem, research objectives, mathematical framework and evaluation metrics. |
| 2 | `02_data_processing.ipynb` | Explains the data selection, cleaning, feature engineering, encoding and chronological data split. |
| 3 | `03_logistic_regression.ipynb` | Develops the logistic regression model and evaluates its predictions. |
| 4 | `04_gradient_boosting.ipynb` | Implements gradient boosting, including model development and hyperparameter tuning. |
| 5 | `05_random_forest.ipynb` | Develops the random forest model and investigates its predictive performance. |
| 6 | `06_neural_networks.html` | Presents the neural network implementation in R, including model selection, training and evaluation. The corresponding R Markdown source is available in `dylan/`. |
| 7 | `07_comparison_and_analysis.ipynb` | Compares the four models and the external benchmark using common test data, scoring metrics and calibration analysis. |
| 8 | `08_heatmaps.ipynb` | Applies the model predictions to spatial analysis, generating shot heatmaps and examining team-level expected goals against actual goals. |

The report is intended to be read sequentially. The introduction establishes the prediction problem and evaluation framework, the data-processing notebook explains how the modelling dataset was prepared, and the subsequent notebooks develop the individual models. The comparison and spatial analysis notebooks then bring the results together.

### 3.3 Data directory (`data/`)

The data directory contains the datasets used and considered during the project.

1. `data/understat_shots.csv` – Raw historical shot data obtained from Understat.
2. `data/shots_cleaned.csv` – Cleaned, feature-engineered and encoded dataset used for model development and evaluation.
3. `data/statsbomb_shots_all.csv` – An alternative dataset considered during the initial exploratory analysis and retained as part of the data-suitability investigation.

The data-processing notebook documents the steps taken to prepare the final modelling dataset. This includes the handling of missing values, feature selection, encoding and the removal of variables that could introduce data leakage.

## 4. Data and Methodological Framework

### 4.1 Prediction target

Each observation represents an individual football shot. The response variable is binary:

$$
Y_i =
\begin{cases}
1, & \text{if shot } i \text{ results in a goal},\\
0, & \text{otherwise}.
\end{cases}
$$

The models estimate the conditional probability

$$
p_i = \mathbb{P}(Y_i=1\mid X_i),
$$

where $X_i$ represents the available shot characteristics and contextual information.

Understat's existing xG estimates are retained separately for benchmarking and are not used as explanatory variables in the independently developed models.

### 4.2 Chronological data split

We use a chronological split rather than randomly sampling observations. This reflects the intended application of the models: using previous seasons to predict outcomes in a later season.

| Dataset | Seasons | Purpose |
|---|---|---|
| **Training** | 2021/22–2023/24 | Fit model parameters. |
| **Validation** | 2024/25 | Compare models and make modelling decisions, including hyperparameter selection. |
| **Testing** | 2025/26 | Evaluate final predictions on an unseen season. |

The test season is kept separate from model fitting and model selection. Where appropriate, the final model is refitted using the training and validation data before producing predictions for the test season.

This approach provides a more realistic assessment of performance on future data than a random split across seasons. It also means that the models are evaluated under possible changes in the distribution of shots between seasons.

### 4.3 Performance evaluation

We use three main metrics:

- **Brier score:** Measures the mean squared difference between predicted probabilities and observed outcomes. It is a strictly proper scoring rule, with lower values indicating better probabilistic predictions.
- **Log loss:** Measures the negative log-likelihood of the observed outcomes under the predicted probabilities. It penalises confident incorrect predictions particularly heavily, with lower values indicating better performance.
- **ROC-AUC:** Measures the ability of a model to rank goal-scoring shots above non-goal shots. A value of 0.5 represents random ranking and a value of 1 represents perfect ranking.

The Brier score and log loss assess the quality of the probabilities themselves, whereas ROC-AUC assesses discrimination. We use all three because performance under one metric does not necessarily imply strong performance under the others.

The constant base-rate model provides a baseline for assessing whether the machine learning models gain predictive value from the shot-level features. Understat's xG estimates provide an additional external benchmark.

## 5. Environment and Requirements

### 5.1 Python dependencies

The main Python analysis uses the following packages:

```text
numpy
pandas
matplotlib
seaborn
scikit-learn
xgboost
mplsoccer==1.5.1
jupyter
```

Install the dependencies from the repository root:

```bash
pip install -r requirements.txt
```

### 5.2 R dependencies

The neural network analysis uses R and the following packages:

```R
nnet
tidyverse
readr
knitr
```

R and Pandoc are required to reproduce the knitted HTML output from the R Markdown source. Any additional package requirements are documented in the relevant source file.

### 5.3 Reproducing the analysis

The report notebooks should be run in the order listed in Section 3.2, since later stages depend on the cleaned data and, where applicable, the predictions generated by earlier stages.

The cleaned dataset is provided in `data/shots_cleaned.csv`, so the raw data collection process does not need to be repeated to run the modelling analysis. If the data-processing stage is rerun, the resulting dataset should be checked against the version used by the model notebooks to ensure that the observations and feature definitions remain consistent.

The neural network analysis is provided as a rendered HTML file alongside its R Markdown source. The HTML file can be opened directly to inspect the model development and results without installing R.

Any manual steps or changes to file paths required to reproduce individual analyses should be followed as documented in the relevant notebook.

## 6. Individual Working Directories

Each group member maintained an individual directory containing development work, exploratory analysis and model implementation. These directories provide evidence of the work carried out during the project and show how the individual contributions were incorporated into the final report.

- **`don/`** – Exploratory data cleaning, feature extraction and logistic regression model development.
- **`dylan/`** – Data collection and scraping utilities, comparison of candidate datasets, and the neural network implementation in R, including its R Markdown source and rendered HTML output.
- **`luke/`** – Random forest development, parameter tuning, spatial plotting functions and heatmap generation.
- **`pietro/`** – Gradient boosting development, hyperparameter investigation and introductory mathematical formulations.

The individual directories retain relevant exploratory work as well as the final implementations. The main `report/` directory contains the consolidated analysis used for assessment.

## 7. References

1. Colman, J. (2025). *What is xG in football and how does it work?* BBC Sport. Available at: https://www.bbc.co.uk/sport/football/articles/cgrqd18q0rgo
2. Understat (2026). *Understat: Advanced Football Statistics*. Available at: https://understat.com
3. Sumpter, D. and Andrzejewski, A. (2022). *Plotting shot location*. Soccermatics. Available at: https://soccermatics.readthedocs.io/en/latest/gallery/lesson2/plot_xGModelFit.html#plotting-shot-location

Additional references and package documentation are provided in the relevant notebooks where they are used.
