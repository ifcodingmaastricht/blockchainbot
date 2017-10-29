from database import Database
#db = Database()
#db.connect()
#sampleData = db.getSampleData()
#print(sampleData)




import numpy as np
import matplotlib.pyplot as plt
from sklearn import svm, datasets
# import some data to play with

iris = datasets.load_iris()

X = iris.data[:, :2] # we only take the first two features. We could

 # avoid this ugly slicing by using a two-dim dataset
y = iris.target
print(type(y))
print(type(X))
print(type(X[0]))
#print("X:")
#print(X)
#print("y:")
#print(y)

X = np.array([np.array([5.1,3.5]), np.array([7.,3.2]), np.array([3.1,2.7])])
y = np.array([1,2,3])

#X = np.array(sampleData)
#X[2:2,:2] = X[2:2,:2]
#for i in range(len(X)):
#    X[]= X[i][2] - 1508399262
#y = np.ones(len(sampleData))
#for i in range(0, int(len(sampleData)/3)):
#    y[i] = 2
#for i in range(int(len(sampleData)/3), int(len(sampleData)/3)*2):
#    y[i] = 3
#y = y.astype(int)
#y.sort()
#print(type(y))
#print("X:")
##print(X)
#print("y:")
#print(y)


# we create an instance of SVM and fit out data. We do not scale our
# data since we want to plot the support vectors
C = 1.0 # SVM regularization parameter
svc = svm.SVC(kernel='linear', C=100,gamma=0.1).fit(X, y)


#print("SVC has ran")
##plt.plot(X[0])
#plt.scatter(X[:, 0], X[:, 1], c=y, cmap=plt.cm.Paired)

#plt.show()

# create a mesh to plot in
x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
h = (x_max / x_min)/100
xx, yy = np.meshgrid(np.arange(x_min, x_max, h),
np.arange(y_min, y_max, h))

plt.subplot(1, 1, 1)
Z = svc.predict(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)
plt.contourf(xx, yy, Z, cmap=plt.cm.Paired, alpha=0.8)
plt.scatter(X[:, 0], X[:, 1], c=y, cmap=plt.cm.Paired)
plt.xlabel('Sepal length')
plt.ylabel('Sepal width')
plt.xlim(xx.min(), xx.max())
plt.title('SVC with linear kernel')
plt.show()
