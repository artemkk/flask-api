# first neural network with keras tutorial
from keras.models import Sequential
from keras.layers import Dense
import matplotlib.pyplot as plt
import numpy
from sklearn.metrics import r2_score
from matplotlib import pyplot
import tensorflow as tf
from keras.utils import plot_model

# load the training and validation datasets
TrainingSet = numpy.genfromtxt("./raw-data/model-data-sets/concrete_training_data.csv", delimiter=",", skip_header=True)
ValidationSet = numpy.genfromtxt("./raw-data/model-data-sets/concrete_validation_data.csv", delimiter=",", skip_header=True)

# split into input (X) and output (y) variables
X1 = TrainingSet[:,0:8]
Y1 = TrainingSet[:,8]

X2 = ValidationSet[:,0:8]
Y2 = ValidationSet[:,8]

# define the keras model
model = Sequential()
model.add(Dense(12, input_shape=(8,), activation='relu'))
model.add(Dense(8, activation='relu'))
model.add(Dense(1, activation='relu'))

# compile the keras model
model.compile(loss='mean_squared_error', optimizer=tf.keras.optimizers.Adam(learning_rate=1e-6))

# Show model architecture
plot_model(model, to_file='model1_plot.png', show_shapes=True, show_layer_names=True)

# # fit the keras model on the dataset
# history = model.fit(X1, Y1, validation_data=(X2, Y2), epochs=250000, batch_size=100)

# # Calculate predictions
# PredTestSet = model.predict(X1)
# PredValSet = model.predict(X2)

# # Save predictions
# numpy.savetxt("trainresults1.csv", PredTestSet, delimiter=",")
# numpy.savetxt("valresults1.csv", PredValSet, delimiter=",")

# # Plot training history
# pyplot.plot(history.history['loss'], label='train')
# pyplot.plot(history.history['val_loss'], label='test')
# pyplot.legend()
# pyplot.show()

# # Plot actual vs prediction for training set
# TestResults = numpy.genfromtxt("trainresults1.csv", delimiter=",")
# plt.plot(Y1,TestResults,'ro')
# plt.title('Training Set Model 1')
# plt.xlabel('Actual')
# plt.ylabel('Predicted')
# plt.show()

# # Plot actual vs prediction for validation set
# ValResults = numpy.genfromtxt("valresults1.csv", delimiter=",")
# plt.plot(Y2, ValResults,'ro')
# plt.title('Validation Set Model 1')
# plt.xlabel('Actual')
# plt.ylabel('Predicted')
# plt.show()

# # Compute R-Square value for training set
# TestR2Value = r2_score(Y1, TestResults)
# print("Training Set Model 1 R-Square=", TestR2Value)

# # Compute R-Square value for validation set
# ValR2Value = r2_score(Y2, ValResults)
# print("Validation Set Model 1 R-Square=", ValR2Value)