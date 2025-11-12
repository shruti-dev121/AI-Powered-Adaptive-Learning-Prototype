from sklearn.linear_model import LogisticRegression
import numpy as np

# Level mapping
level_map = {"Easy": 0, "Medium": 1, "Hard": 2}
rev_map = {0: "Easy", 1: "Medium", 2: "Hard"}

# Simulated training data
X_train = np.array([
    [1.0, 2.0, 0],
    [0.33, 3.0, 1],
    [0.66, 1.5, 1],
    [0.8, 2.0, 1],
    [0.5, 2.5, 2],
])
y_train = np.array([1, 0, 1, 2, 1])

# Train ML model
model = LogisticRegression(multi_class='multinomial', max_iter=200)
model.fit(X_train, y_train)

def update_difficulty_ml(current_level, last_results, last_times):
    """Predict next difficulty using ML model."""
    if len(last_results) < 3:
        return current_level
    
    accuracy = sum(last_results[-3:]) / 3
    avg_time = sum(last_times[-3:]) / 3
    current_level_num = level_map[current_level]

    next_level_num = model.predict([[accuracy, avg_time, current_level_num]])[0]
    next_level = rev_map[next_level_num]

    print(f"Based on your performance, your level for next quiz is {next_level}")
    return next_level
