# Tuning with leave-one-season-out cross-validation (32 combinations x 4 folds)
# Needs: X_train, y_train, groups_train, RANDOM_STATE
from sklearn.model_selection import GridSearchCV, LeaveOneGroupOut

param_grid = {
    "max_depth": [5, 10, 15, None],
    "min_samples_leaf": [10, 25, 50, 100],
    "max_features": ["sqrt", 0.5],
}
grid_search = GridSearchCV(
    estimator=RandomForestClassifier(n_estimators=200, random_state=RANDOM_STATE),
    param_grid=param_grid, cv=LeaveOneGroupOut(),
    scoring={"log_loss": "neg_log_loss", "brier": "neg_brier_score"},
    refit="log_loss", return_train_score=True, n_jobs=-1)
grid_search.fit(X_train, y_train, groups=groups_train)

# Output: best settings max_depth=10, min_samples_leaf=50, max_features=0.5
# Best CV log loss 0.2821 | std across the 4 held-out seasons 0.0061
