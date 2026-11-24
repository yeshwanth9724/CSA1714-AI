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
