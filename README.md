# Group Sprint 1: Probabilistic Expected Goals ($xG$) Modeling & Spatial Analysis

## Project Group & Equity Statement

- **Don Athipozhiyil** (25% Contribution)
- **Dylan Sharpe** (25% Contribution)
- **Luke Chinoy** (25% Contribution)
- **Pietro Neill** (25% Contribution)

*Equity Statement:* All team members contributed equally (25% each) across conceptual design, mathematical modeling, code implementation, and reporting. Detailed individual working histories are documented in member-specific subdirectories.

---

## Project Overview & Objectives

The goal of this project is to investigate how effectively different supervised machine learning approaches estimate the conditional probability of a football shot resulting in a goal ($xG_i = P(Y_i=1 \mid X_i)$). 

We address three primary objectives:
1. **Model Development:** Formulate and train four distinct machine learning architectures (Logistic Regression, Gradient Boosting, Random Forest, and a Neural Network) alongside baseline null models.
2. **Probabilistic Model Evaluation:** Compare out-of-sample predictive performance on unseen data using strictly proper scoring rules (Brier Score and Log Loss) alongside discrimination metrics (ROC-AUC).
3. **Spatial Analysis & Application:** Apply the superior probabilistic model to evaluate spatial shooting performance, examining shot quality heatmaps and identifying team-level over/underperformance relative to actual goals.

---

## Repository Structure & Reading Order

To review the project analysis, follow the structured reading order below:

### 1. Preparation & Setup
Ensure the required dependencies are installed before executing notebooks.

- **Python Requirements:** Run `pip install -r requirements.txt` (utilising Python 3.9+).
- **R Requirements:** R and RStudio (with Pandoc) are required to knit `.Rmd` files. Missing R packages install automatically on execution.
- **Data Dependencies:** All necessary data is pre-processed and included in `data/shots_cleaned.csv`. Data collection scripts in individual folders do not need to be re-run unless reproducing raw scrapes.

### 2. Data Directory (`data/`)
1. `data/understat_shots.csv`: Raw historical shot data scraped from Understat.
2. `data/shots_cleaned.csv`: Fully cleaned, feature-engineered, and one-hot encoded dataset used across all models.
3. `data/statsbomb_shots_all.csv`: Initial candidate dataset evaluated during exploratory analysis; retained for comparative data-suitability benchmarking.

### 3. Main Report (`report/`)
The primary project submission is structured sequentially within the `report/` folder:

1. `01_introduction.ipynb`: Problem formulation, mathematical framework of $xG$, proper scoring rules, and baseline specifications.
2. `02_data_processing.ipynb`: Feature engineering, data scrubbing, encoding, and chronological split formulation.
3. `03_logistic_regression.ipynb`: Model implementation 1 – Baseline parametric model.
4. `04_gradient_boosting.ipynb`: Model implementation 2 – Tree-based ensemble with hyperparameter tuning.
5. `05_random_forest.ipynb`: Model implementation 3 – Bagged decision trees.
6. `06_neural_networks.html`: Model implementation 4 – Multi-layer perceptron trained in R (`06_neural_networks.Rmd` source available in `dylan/`).
7. `07_comparison_and_analysis.ipynb`: Comparative evaluation using strictly proper scoring rules, reliability diagrams, and out-of-sample test results.
8. `08_heatmaps.ipynb`: Spatial application – Generating team-level spatial shot heatmaps and evaluating goal output against expected probabilities.

---

## Data & Methodological Framework

### Data Splits
To prevent data leakage and evaluate real-world generalisability, we implemented a **chronological split** rather than random sampling:

| Split Set | Seasons | Function |
| :--- | :--- | :--- |
| **Training** | 2021/22 – 2023/24 | Parameter fitting & feature selection |
| **Validation** | 2024/25 | Hyperparameter tuning & model selection |
| **Testing** | 2025/26 | Final out-of-sample evaluation |

---

## Environment & Requirements

### Python Dependencies
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

### R Dependencies
```R
nnet
tidyverse
readr
knitr
```

---

## Documentation & Individual Working Directories

Each group member maintained an individual directory documenting exploratory iterations, raw data pipelines, and model prototyping:

- `don/`: Exploratory data cleaning pipelines, feature extraction scripts, and initial logistic regression implementations.
- `dylan/`: Web scraping utilities (`understat_download`, `statsbomb_download`), dataset comparison analysis, and R Neural Network (`.Rmd` and knitted `.html`).
- `luke/`: Random forest parameter tuning, spatial pitch plotting functions, and heat map generation scripts.
- `pietro/`: Gradient boosting pipeline development, hyperparameter search grids, and introductory mathematical formulations.

---

## References

1. Colman, J. (2025) *What is xG in football and how does it work?* BBC Sport. Available at: https://www.bbc.co.uk/sport/football/articles/cgrqd18q0rgo
2. Understat (2026) *Understat: Advanced Football Statistics*. Available at: https://understat.com
3. Sumpter, D. and Andrzejewski, A. (2022) *Plotting shot location*, Soccermatics. Available at: https://soccermatics.readthedocs.io/en/latest/gallery/lesson2/plot_xGModelFit.html#plotting-shot-location
