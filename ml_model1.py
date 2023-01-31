# first neural network with keras tutorial
from numpy import loadtxt
from tensorflow.python.keras.models import Sequential
from tensorflow.python.keras.layers import Dense


# load the training dataset
dataset = loadtxt('concrete_training_data.csv', delimiter=',')
# split into input (X) and output (y) variables
X = dataset[:,0:8]
y = dataset[:,8]

# define the keras model
model = Sequential()
model.add(Dense(12, input_shape=(8,), activation='relu'))
model.add(Dense(8, activation='relu'))
model.add(Dense(1, activation='relu'))

# compile the keras model
model.compile(loss='mean_squared_error', optimizer='adam')

# fit the keras model on the dataset
model.fit(X, y, epochs=150, batch_size=10)

# load the validation dataset
dataset = loadtxt('concrete_validation_data.csv', delimiter=',')
# split into input (X) and output (y) variables
A = dataset[:,0:8]
b = dataset[:,8]

# evaluate the keras model
_, accuracy = model.evaluate(A, b)
print('Accuracy: %.2f' % (accuracy*100))