# imports
from keras.models import Sequential
from keras.layers import Dense
from sklearn.metrics import r2_score
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt
import numpy
from keras.optimizers import Adam
from matplotlib import pyplot
from keras.callbacks import EarlyStopping
from keras.utils.vis_utils import plot_model
from keras import regularizers

def define_model():

    l2_dim = 0.001 

    # Create model
    model = Sequential()
    model.add(Dense(128, activation="relu", input_dim=8, kernel_regularizer=regularizers.l2(l2_dim)))
    model.add(Dense(32, activation="relu", kernel_regularizer=regularizers.l2(l2_dim)))
    model.add(Dense(8, activation="relu", kernel_regularizer=regularizers.l2(l2_dim)))

    # Since the regression is performed, a Dense layer containing a single neuron with a linear activation function.
    # Typically ReLu-based activation are used but since it is performed regression, it is needed a linear activation.
    model.add(Dense(1, activation="linear"))

    # Compile model: The model is initialized with the Adam optimizer and then it is compiled.
    model.compile(loss='mean_squared_error', optimizer=Adam(learning_rate=1e-6, decay=1e-3 / 20))

    return model

def execute_model(training_set, validation_set):

    # region Pull Data

    # Split into input (X) and output (Y) variables
    X1 = training_set[:,0:8]
    Y1 = training_set[:,8]

    X2 = validation_set[:,0:8]
    Y2 = validation_set[:,8]
    # endregion

    # Patient early stopping
    es = EarlyStopping(monitor='val_loss', mode='min', verbose=1, patience=130)

    # Fit the model
    model = define_model()
    history = model.fit(X1, Y1, validation_data=(X2, Y2), epochs=10000000, batch_size=125, verbose=2, callbacks=[es])

    # region Display
    # Calculate predictions
    PredTestSet = model.predict(X1)
    PredValSet = model.predict(X2)

    # Save predictions
    numpy.savetxt("trainresults2.csv", PredTestSet, delimiter=",")
    numpy.savetxt("valresults2.csv", PredValSet, delimiter=",")

    # Show model architecture
    plot_model(model, to_file='model_plot2.png', show_shapes=True, show_layer_names=True)

    # Plot training history
    pyplot.plot(history.history['loss'], label='train')
    pyplot.plot(history.history['val_loss'], label='test')
    pyplot.title('Training History')
    pyplot.legend()
    pyplot.show()

    # Plot actual vs prediction for training set
    TestResults = numpy.genfromtxt("trainresults2.csv", delimiter=",")
    plt.plot(Y1,TestResults,'ro')
    plt.title('Training Set Model 2')
    plt.xlabel('Actual')
    plt.ylabel('Predicted')
    plt.show()

    # Plot actual vs prediction for validation set
    ValResults = numpy.genfromtxt("valresults2.csv", delimiter=",")
    plt.plot(Y2, ValResults,'ro')
    plt.title('Validation Set Model 2')
    plt.xlabel('Actual')
    plt.ylabel('Predicted')
    plt.show()

    # Compute R-Square value for training set
    TestR2Value = r2_score(Y1,TestResults)
    print("Training Set Model 2 R-Square=", TestR2Value)

    # Compute R-Square value for validation set
    ValR2Value = r2_score(Y2, ValResults)
    print("Validation Set Model 2 R-Square=", ValR2Value)

    # Compute MSE for validation set
    ValMSEValue = mean_squared_error(Y2, ValResults)
    print("Validation Set Model 2 MSE=", ValMSEValue)
    # endregion

    return