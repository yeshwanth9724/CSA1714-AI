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
