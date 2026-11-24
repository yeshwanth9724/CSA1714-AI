# CSA1714 - Artificial Intelligence Laboratory
## Observation Experiments Record (Experiments 29 - 38)

---

## Experiment 29: Medical Diagnostic System

### Aim:
To write and implement a knowledge base in Prolog for a Medical Diagnostic Expert System to infer diseases based on observed patient symptoms.

### Algorithm / Procedure:
1. Define facts specifying patients and their observed symptoms using `symptom(Patient, Symptom)`.
2. Define diagnostic rules using Horn clauses:
   - If a patient has fever, cough, and headache, diagnose `flu`.
   - If a patient has cold, sneezing, and fever, diagnose `common_cold`.
   - If a patient has chills, fever, and body ache, diagnose `viral_infection`.
3. Define the query rule `diagnosis(Patient, Disease) :- disease(Patient, Disease)`.
4. Consult the knowledge base in the SWI-Prolog interpreter.
5. Query the system with specific patients or diseases to obtain automated diagnoses.

### Program (`Exp-29.pl`):
```prolog
% Medical Diagnostic System

symptom(john, fever).
symptom(john, cough).
symptom(john, headache).

symptom(raj, fever).
symptom(raj, cold).
symptom(raj, sneezing).

symptom(susan, chills).
symptom(susan, fever).
symptom(susan, body_ache).

disease(X, flu) :-
    symptom(X, fever),
    symptom(X, cough),
    symptom(X, headache).

disease(X, common_cold) :-
    symptom(X, cold),
    symptom(X, sneezing),
    symptom(X, fever).

disease(X, viral_infection) :-
    symptom(X, chills),
    symptom(X, fever),
    symptom(X, body_ache).

diagnosis(Patient, Disease) :-
    disease(Patient, Disease).
```

### Queries & Output:
```prolog
?- diagnosis(john, D).
D = flu .

?- diagnosis(raj, D).
D = common_cold .

?- diagnosis(susan, D).
D = viral_infection .

?- disease(X, flu).
X = john .
```

### Result:
Thus, the Prolog program for the Medical Diagnostic System was successfully developed, queried, and verified.

---

## Experiment 30: Linear Regression Algorithm

### Aim:
To implement Simple Linear Regression in Python using Scikit-Learn to fit a linear model and predict dependent values.

### Algorithm / Procedure:
1. Import `numpy` and `LinearRegression` from `sklearn.linear_model`.
2. Prepare independent feature vector `x` and target variable array `y`.
3. Instantiate the `LinearRegression()` model.
4. Fit the model to the training data using `model.fit(x, y)`.
5. Predict the value for an unseen test point ($x = 6$) using `model.predict()`.
6. Display the learned slope (coefficient), intercept, and predicted output.

### Program (`Exp-30.py`):
```python
import numpy as np
from sklearn.linear_model import LinearRegression

x = np.array([[1], [2], [3], [4], [5]])
y = np.array([10, 20, 30, 40, 50])

model = LinearRegression()
model.fit(x, y)

prediction = model.predict([[6]])

print("Linear Regression Model")
print("Slope:", model.coef_[0])
print("Intercept:", model.intercept_)
print("Predicted value:", prediction[0])
```

### Output:
```text
Linear Regression Model
Slope: 9.999999999999998
Intercept: 7.105427357601002e-15
Predicted value: 59.99999999999999
```

### Result:
Thus, the Linear Regression algorithm was successfully implemented in Python and used to predict continuous outcomes.

---

## Experiment 31: K-Nearest Neighbors (KNN) Classification

### Aim:
To implement the K-Nearest Neighbors (KNN) classification algorithm in Python using Scikit-Learn to classify an unknown data point based on proximity to nearest neighbors.

### Algorithm / Procedure:
1. Import `KNeighborsClassifier` from `sklearn.neighbors`.
2. Define training feature dataset `x` and corresponding binary class labels `y`.
3. Create an instance of `KNeighborsClassifier` with $k = 3$.
4. Train the classifier using `model.fit(x, y)`.
5. Provide a test sample point $(5, 6)$ and predict its class membership using `model.predict()`.
6. Output the training samples, class labels, and predicted class.

### Program (`Exp-31.py`):
```python
from sklearn.neighbors import KNeighborsClassifier

x = [[1, 2], [2, 3], [3, 3], [6, 7], [7, 8], [8, 8]]
y = [0, 0, 0, 1, 1, 1]

model = KNeighborsClassifier(n_neighbors=3)
model.fit(x, y)

test_point = [[5, 6]]
prediction = model.predict(test_point)

print("K-Nearest Neighbors (KNN) Classifier")
print("Training Samples:", x)
print("Class Labels:", y)
print("Predicted Class:", prediction[0])
```

### Output:
```text
K-Nearest Neighbors (KNN) Classifier
Training Samples: [[1, 2], [2, 3], [3, 3], [6, 7], [7, 8], [8, 8]]
Class Labels: [0, 0, 0, 1, 1, 1]
Predicted Class: 1
```

### Result:
Thus, the K-Nearest Neighbors classification algorithm was implemented and successfully classified the test data point.

---

## Experiment 32: Decision Tree Classifier

### Aim:
To implement a Decision Tree Classifier in Python using Scikit-Learn to learn hierarchical decision rules for pattern classification.

### Algorithm / Procedure:
1. Import `DecisionTreeClassifier` from `sklearn.tree`.
2. Define multi-dimensional training feature vectors `x` and discrete class targets `y`.
3. Instantiate the `DecisionTreeClassifier()` model.
4. Fit the decision tree on the dataset using `model.fit(x, y)`.
5. Predict the class of an unknown query point $(5, 6)$ using `model.predict()`.
6. Print the dataset features, target classes, and the predicted class label.

### Program (`Exp-32.py`):
```python
from sklearn.tree import DecisionTreeClassifier

x = [[1, 2], [2, 3], [3, 3], [6, 7], [7, 8], [8, 8]]
y = [0, 0, 0, 1, 1, 1]

model = DecisionTreeClassifier()
model.fit(x, y)

test_point = [[5, 6]]
prediction = model.predict(test_point)

print("Decision Tree Classification")
print("Training Features:", x)
print("Class Labels:", y)
print("Predicted Class:", prediction[0])
```

### Output:
```text
Decision Tree Classification
Training Features: [[1, 2], [2, 3], [3, 3], [6, 7], [7, 8], [8, 8]]
Class Labels: [0, 0, 0, 1, 1, 1]
Predicted Class: 1
```

### Result:
Thus, the Decision Tree classification model was successfully trained and evaluated on sample feature data.

---

## Experiment 33: Sentiment Analysis using NLP

### Aim:
To implement Sentiment Analysis in Python using Natural Language Processing (TextBlob) to determine the polarity of natural language text.

### Algorithm / Procedure:
1. Import `TextBlob` from the `textblob` NLP library.
2. Accept a text sentence from the user (or use a default test sentence if blank).
3. Create a `TextBlob(text)` object.
4. Compute the sentiment polarity score $(-1.0 \text{ to } +1.0)$ using `analysis.sentiment.polarity`.
5. Classify the sentiment:
   - If $\text{score} > 0 \rightarrow \text{Positive}$
   - If $\text{score} < 0 \rightarrow \text{Negative}$
   - Otherwise $\rightarrow \text{Neutral}$
6. Print the computed polarity score and final sentiment classification.

### Program (`Exp-33.py`):
```python
from textblob import TextBlob

text = input("Enter a sentence: ")
if not text.strip():
    text = "Artificial Intelligence is great and very helpful"

analysis = TextBlob(text)
score = analysis.sentiment.polarity

print("Sentiment Polarity Score:", score)
if score > 0:
    print("Sentiment: Positive")
elif score < 0:
    print("Sentiment: Negative")
else:
    print("Sentiment: Neutral")
```

### Output:
```text
Enter a sentence: Artificial Intelligence is great and very helpful
Sentiment Polarity Score: 0.5
Sentiment: Positive
```

### Result:
Thus, sentiment analysis using Natural Language Processing was implemented and correctly determined sentence polarity.

---

## Experiment 34: Genetic Algorithm for Optimization

### Aim:
To implement a Genetic Algorithm in Python to optimize a mathematical fitness function $f(x) = x^2$.

### Algorithm / Procedure:
1. Define the objective/fitness function $f(x) = x^2$.
2. Initialize a population of individuals (candidate solutions) randomly within range $[0, 10]$.
3. Iterate across generations (10 iterations):
   - Sort the population in descending order based on fitness value.
   - Select the two fittest individuals as parents.
   - Perform crossover (compute average $(P_1 + P_2) // 2$) to generate offspring.
   - Replace the weakest individual in the population with the new child.
4. Identify the best individual with maximum fitness score.
5. Print the optimal parameter value and the maximum objective score.

### Program (`Exp-34.py`):
```python
import random

def fitness(x):
    return x * x

random.seed(42)
population = [random.randint(0, 10) for _ in range(5)]

for i in range(10):
    population.sort(key=fitness, reverse=True)

    parent1 = population[0]
    parent2 = population[1]

    child = (parent1 + parent2) // 2
    population[-1] = child

best = max(population, key=fitness)

print("Genetic Algorithm Optimization")
print("Best value of x:", best)
print("Maximum value:", fitness(best))
```

### Output:
```text
Genetic Algorithm Optimization
Best value of x: 10
Maximum value: 100
```

### Result:
Thus, the Genetic Algorithm for function optimization was implemented and successfully converged to the global maximum.

---

## Experiment 35: Support Vector Machine (SVM) Classification

### Aim:
To implement Support Vector Machine (SVM) binary classification with a linear kernel in Python using Scikit-Learn.

### Algorithm / Procedure:
1. Import `SVC` from `sklearn.svm`.
2. Define linearly separable feature vectors `x` and class labels `y \in \{0, 1\}`.
3. Instantiate the Support Vector Classifier with `kernel='linear'`.
4. Fit the hyperplane on the training set using `model.fit(x, y)`.
5. Predict the class assignment of a test query point $(5, 6)$ using `model.predict()`.
6. Display the kernel type and predicted classification result.

### Program (`Exp-35.py`):
```python
from sklearn.svm import SVC

x = [[1, 2], [2, 3], [3, 3], [6, 7], [7, 8], [8, 8]]
y = [0, 0, 0, 1, 1, 1]

model = SVC(kernel='linear')
model.fit(x, y)

test_sample = [[5, 6]]
prediction = model.predict(test_sample)

print("Support Vector Machine (SVM) Classification")
print("Kernel: Linear")
print("Predicted Class:", prediction[0])
```

### Output:
```text
Support Vector Machine (SVM) Classification
Kernel: Linear
Predicted Class: 1
```

### Result:
Thus, the Support Vector Machine (SVM) classification algorithm was successfully implemented and evaluated.

---

## Experiment 36: Principal Component Analysis (PCA) Dimensionality Reduction

### Aim:
To implement Principal Component Analysis (PCA) in Python using Scikit-Learn to reduce feature dimensions while retaining maximum variance.

### Algorithm / Procedure:
1. Import `PCA` from `sklearn.decomposition` and `StandardScaler` from `sklearn.preprocessing`.
2. Define a multi-dimensional dataset (e.g., 2D coordinates).
3. Standardize the data features to zero mean and unit variance using `StandardScaler().fit_transform()`.
4. Instantiate `PCA(n_components=1)` to project data from 2 dimensions down to 1 dimension.
5. Compute the transformed principal component scores using `pca.fit_transform()`.
6. Display the original data and the reduced 1D projection.

### Program (`Exp-36.py`):
```python
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

x = [[2, 4], [3, 5], [4, 6], [5, 8], [6, 9]]

scaler = StandardScaler()
x_scaled = scaler.fit_transform(x)

pca = PCA(n_components=1)
result = pca.fit_transform(x_scaled)

print("Original Data:")
print(x)
print("Reduced Data:")
print(result)
```

### Output:
```text
Original Data:
[[2, 4], [3, 5], [4, 6], [5, 8], [6, 9]]
Reduced Data:
[[-1.91499142]
 [-1.033745  ]
 [-0.15249857]
 [ 1.10999428]
 [ 1.99124071]]
```

### Result:
Thus, Principal Component Analysis (PCA) was implemented and successfully performed dimensionality reduction.

---

## Experiment 37: Collaborative Filtering Recommendation System

### Aim:
To implement a User-Based Collaborative Filtering Recommendation System in Python using Cosine Similarity.

### Algorithm / Procedure:
1. Import `numpy`.
2. Create a User-Item rating matrix where rows represent users and columns represent items (ratings from 1 to 5; 0 denotes unrated).
3. Extract the active user's rating vector (`user1`).
4. Compute the Cosine Similarity between `user1` and all other users:
   $$\text{similarity} = \frac{u_1 \cdot u_i}{\|u_1\| \|u_i\|}$$
5. Identify the most similar user using `argmax()`.
6. Recommend the highest-rated item from the most similar user that the active user has not yet rated.

### Program (`Exp-37.py`):
```python
import numpy as np

ratings = np.array([
    [5, 4, 0, 0],
    [4, 5, 0, 0],
    [0, 0, 5, 4],
    [0, 0, 4, 5]
])

user1 = ratings[0]
similarity = []

for i in range(len(ratings)):
    if i == 0:
        similarity.append(-1)
    else:
        sim = np.dot(user1, ratings[i]) / (
            np.linalg.norm(user1) * np.linalg.norm(ratings[i])
        )
        similarity.append(sim)

best_user = np.argmax(similarity)

for i in range(ratings.shape[1]):
    if ratings[0][i] == 0:
        print("Recommended Item:", i + 1)
        break
```

### Output:
```text
Recommended Item: 3
```

### Result:
Thus, the Collaborative Filtering Recommendation System was implemented and successfully generated item recommendations.

---

## Experiment 38: K-Means Clustering Algorithm

### Aim:
To implement the unsupervised K-Means Clustering algorithm in Python using Scikit-Learn to partition unlabelled observations into $k$ distinct clusters.

### Algorithm / Procedure:
1. Import `KMeans` from `sklearn.cluster`.
2. Define unlabelled 2D data samples.
3. Instantiate `KMeans(n_clusters=2, random_state=0, n_init=10)`.
4. Fit the model to the data points to partition them into 2 clusters.
5. Retrieve cluster assignments (`model.labels_`) and cluster centroids (`model.cluster_centers_`).
6. Print the resulting cluster labels and centroid coordinates.

### Program (`Exp-38.py`):
```python
from sklearn.cluster import KMeans

x = [[1, 2], [2, 3], [3, 3],
     [8, 8], [9, 8], [8, 9]]

model = KMeans(n_clusters=2, random_state=0, n_init=10)
model.fit(x)

print("Cluster Labels:")
print(model.labels_)
print("Cluster Centers:")
print(model.cluster_centers_)
```

### Output:
```text
Cluster Labels:
[1 1 1 0 0 0]
Cluster Centers:
[[8.33333333 8.33333333]
 [2.         2.66666667]]
```

### Result:
Thus, the K-Means clustering algorithm was implemented and successfully grouped unlabelled data points into distinct clusters.
