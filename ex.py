import pandas as pd
import numpy as np

# Example Dataset (Pandas DataFrame)
data = {
    'Outlook': ['Sunny', 'Sunny', 'Overcast', 'Rain', 'Rain', 'Rain', 'Overcast', 'Sunny', 'Sunny', 'Rain', 'Sunny', 'Overcast', 'Overcast', 'Rain'],
    'Temperature': ['Hot', 'Hot', 'Hot', 'Mild', 'Cool', 'Cool', 'Cool', 'Mild', 'Mild', 'Mild', 'Hot', 'Mild', 'Mild', 'Hot'],
    'Humidity': ['High', 'High', 'High', 'High', 'High', 'Low', 'Low', 'High', 'Low', 'Low', 'Low', 'Low', 'High', 'High'],
    'Wind': ['Weak', 'Strong', 'Weak', 'Weak', 'Weak', 'Weak', 'Strong', 'Weak', 'Weak', 'Strong', 'Strong', 'Weak', 'Strong', 'Strong'],
    'PlayTennis': ['No', 'No', 'Yes', 'Yes', 'Yes', 'No', 'Yes', 'Yes', 'Yes', 'No', 'Yes', 'Yes', 'Yes', 'No']
}

df = pd.DataFrame(data)

# Helper Functions

# 1. Calculate the Entropy of a Dataset
def entropy(data):
    value_counts = data.value_counts()
    total = len(data)
    ent = 0
    for count in value_counts:
        prob = count / total
        ent -= prob * np.log2(prob)
    return ent

# 2. Calculate the Information Gain for a particular feature
def information_gain(data, feature, target):
    total_entropy = entropy(data[target])
    value_counts = data[feature].value_counts()
    weighted_entropy = 0
    for value, count in value_counts.items():
        subset = data[data[feature] == value]
        weighted_entropy += (count / len(data)) * entropy(subset[target])
    return total_entropy - weighted_entropy

# 3. ID3 Algorithm to build a decision tree
def id3(data, features, target):
    # Base case: if all examples have the same label, return that label
    if len(data[target].unique()) == 1:
        return data[target].iloc[0]
    
    # Base case: if there are no more features to split on, return the most common label
    if len(features) == 0:
        return data[target].mode()[0]
    
    # Find the feature with the highest information gain
    gains = {feature: information_gain(data, feature, target) for feature in features}
    best_feature = max(gains, key=gains.get)
    
    # Create a decision tree node
    tree = {best_feature: {}}
    
    # Recur for each value of the best feature
    for value in data[best_feature].unique():
        subtree = id3(data[data[best_feature] == value], [f for f in features if f != best_feature], target)
        tree[best_feature][value] = subtree
    
    return tree

# 4. Function to classify a new sample using the decision tree
def classify(tree, sample):
    if isinstance(tree, dict):
        feature = list(tree.keys())[0]
        value = sample[feature]
        return classify(tree[feature][value], sample)
    return tree

# Build the decision tree using the ID3 algorithm
target = 'PlayTennis'
features = ['Outlook', 'Temperature', 'Humidity', 'Wind']
tree = id3(df, features, target)

# Print the decision tree
print("Decision Tree:")
print(tree)

# Classify a new sample
sample = {'Outlook': 'Sunny', 'Temperature': 'Mild', 'Humidity': 'Low', 'Wind': 'Strong'}
prediction = classify(tree, sample)
print(f"\nPrediction for sample {sample}: {pre
diction}")
