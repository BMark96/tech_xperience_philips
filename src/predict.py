import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import ImageDataGenerator

test_dir_in = '/data'
model_file_in = '/model/model_philips.h5'
predictions_file_out = '/prediction/prediction.txt'

model = load_model(model_file_in)

data_generator = ImageDataGenerator(
    rescale=1./255
)
test_generator = data_generator.flow_from_directory(
    directory=test_dir_in,
    target_size=(224,224),
    color_mode="rgb",
    batch_size=1,
    class_mode="categorical",
    shuffle=False,
    seed=42
)

n_steps_test = test_generator.n / test_generator.batch_size
index_map =  {0: 'shaver', 1: 'smart-baby-bottle', 2: 'toothbrush', 3: 'wake-up-light'}
labels = test_generator.classes
filenames = test_generator.filenames

test_generator.reset()
probabilities = model.predict_generator(
    generator=test_generator,
    steps=n_steps_test,
    verbose=1
)
predicted = np.argmax(probabilities, axis=1)

print('Predictions:')
with open(predictions_file_out, 'w') as predictions_file:
    for i in range(len(filenames)):
        line = filenames[i].split('/')[1] + ' – ' + index_map[predicted[i]] + '\n'
        print(line)
        predictions_file.write(line)