# Features and train/test split by season (from the main notebook)
# Needs: df (cleaned shot data), RANDOM_STATE
target = "result"
excluded = ["result", "xg", "season", "team"]
features = [col for col in df.columns if col not in excluded]

train_seasons = ["2021/22", "2022/23", "2023/24", "2024/25"]
test_season = "2025/26"
train = df[df["season"].isin(train_seasons)]
test = df[df["season"] == test_season]

X_train, y_train = train[features], train[target]
X_test, y_test = test[features], test[target]
groups_train = train["season"]            # for leave-one-season-out CV
understat_xg_test = test["xg"]            # kept as a benchmark only

# Output: 34 features
# Training shots: 39657 | goal rate: 0.1097
# Test shots:      9483 | goal rate: 0.1059
