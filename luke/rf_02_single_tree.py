# A depth-3 decision tree first, so the model is readable before building the forest
# Needs: X_train, y_train, features, RANDOM_STATE
from sklearn.tree import DecisionTreeClassifier, plot_tree
import matplotlib.pyplot as plt

tree_model = DecisionTreeClassifier(max_depth=3, random_state=RANDOM_STATE)
tree_model.fit(X_train, y_train)

plt.figure(figsize=(20, 9))
plot_tree(tree_model, feature_names=features, class_names=["No goal", "Goal"],
          filled=True, rounded=True, proportion=True, fontsize=10)
plt.title("Decision tree (depth 3) trained on 2021/22–2024/25 shots")
plt.show()
