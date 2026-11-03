# Final 500-tree model, scored on 2025/26 against Understat and a constant baseline
# Needs: grid_search, X_train, y_train, X_test, y_test, understat_xg_test, RANDOM_STATE
best = grid_search.best_params_
final_rf = RandomForestClassifier(n_estimators=500, max_depth=best["max_depth"],
                                  min_samples_leaf=best["min_samples_leaf"],
                                  max_features=best["max_features"],
                                  n_jobs=-1, random_state=RANDOM_STATE)
final_rf.fit(X_train, y_train)
test_xg = final_rf.predict_proba(X_test)[:, 1]

baseline = np.full(len(y_test), y_train.mean())   # every shot gets the training goal rate

# Output (2025/26): Brier 0.0789, log loss 0.2790
# Total xG: random forest 1063.4, Understat 1183.9, actual goals 1004
