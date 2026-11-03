# Basic forest with starting settings, scored out-of-bag
# Needs: X_train, y_train, train, RANDOM_STATE
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import brier_score_loss, log_loss
import numpy as np

rf_basic = RandomForestClassifier(n_estimators=300, min_samples_leaf=20,
                                  oob_score=True, n_jobs=-1, random_state=RANDOM_STATE)
rf_basic.fit(X_train, y_train)
oob_xg = rf_basic.oob_decision_function_[:, 1]   # each shot predicted only by trees that did not see it

print("Different xG values given:", len(np.unique(oob_xg)))
print("OOB Brier score:", round(brier_score_loss(y_train, oob_xg), 4))
print("OOB log loss:   ", round(log_loss(y_train, oob_xg), 4))
print("Understat Brier on the same shots:", round(brier_score_loss(y_train, train["xg"]), 4))

# Output: 39657 different xG values (the single tree gave 8)
# OOB Brier 0.0803 | OOB log loss 0.2818 | Understat Brier 0.0757
