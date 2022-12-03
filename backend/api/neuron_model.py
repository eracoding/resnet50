import os
import matplotlib.pyplot as plt
import numpy as np
import PIL
import tensorflow as tf
import pathlib
import cv2


class ResNetUltra:
    def __init__(self, data_path):
        self.data_dir = pathlib.Path(data_path)
        self.train_ds = ''
        self.val_ds = ''
        self.model = ''
        self.history = ''

    def preProcessing(self):
        img_height, img_width = 180, 180
        batch_size = 32
        self.train_ds = tf.keras.preprocessing.image_dataset_from_directory(
            self.data_dir,
            validation_split=0.2,
            subset="training",
            seed=123,
            image_size=(img_height, img_width),
            batch_size=batch_size
        )

        self.val_ds = tf.keras.preprocessing.image_dataset_from_directory(
            self.data_dir,
            validation_split=0.2,
            subset="validation",
            seed=123,
            image_size=(img_height, img_width),
            batch_size=batch_size
        )

    def classNames(self):
        return self.train_ds.class_names

    def resNet50(self):
        resnet = tf.keras.applications.ResNet50(include_top=False,
                                                input_shape=(180, 180, 3),
                                                pooling='avg', classes=len(self.classNames()),
                                                weights='imagenet')
        # frozing the learning

        for layer in resnet.layers:
            layer.trainable = False

        return resnet

    def netModel(self):
        model = tf.keras.models.Sequential()

        model.add(self.resNet50())
        model.add(tf.keras.layers.Flatten())
        model.add(tf.keras.layers.Dense(512, activation='relu'))
        model.add(tf.keras.layers.Dense(len(self.classNames()), activation='softmax'))
        self.model = model

    def netSummary(self):
        return self.model.summary()

    def netBuild(self, epochs):
        self.model.compile(optimizer=tf.keras.optimizers.Adam(learning_rate=0.001),
                           loss='sparse_categorical_crossentropy',
                           metrics=['accuracy'])

        self.history = self.model.fit(
            self.train_ds,
            validation_data=self.val_ds,
            epochs=epochs
        )
        if not os.path.isdir('networkModels'):
            os.makedirs('networkModels')
        try:
            self.model.save(f'networkModels\\model{len(self.classNames())}.h5')
        except Exception:
            pass

    def netPredict(self, classname, path_netmodel='', gimage=''):
        if not self.model:
            self.model = tf.keras.models.load_model(path_netmodel)
        if not gimage:
            image = cv2.imread(str(list(self.data_dir.glob(f"{classname}\\*"))[0]))
        else:
            image = cv2.imread(str(gimage))
        image_resized = cv2.resize(image, (180, 180))
        image = np.expand_dims(image_resized, axis=0)
        return self.model.predict(image)


# if __name__ == '__main__':
#     resnet = ResNetUltra('D:\\Github\\mlnet\\s\\s')
#     resnet.preProcessing()
#     resnet.netModel()
#     resnet.netBuild(1)
#     val = resnet.netPredict('train')
#     print(val)
#     print(resnet.classNames())
#     print(resnet.netSummary())

# OUTPUT:
#
# 166/166 [==============================] - 289s 2s/step - loss: 0.4203 - accuracy: 0.8694 - val_loss: 0.2592 - val_accuracy: 0.9127
# 1/1 [==============================] - 1s 897ms/step
# [[4.1363939e-09 9.0778469e-09 2.1127456e-11 2.0578107e-10 1.4327614e-09
#   7.6505891e-08 3.6456026e-07 5.9547375e-07 9.9999666e-01 2.2360964e-06]]
# ['bicycle', 'gazelle', 'horse', 'lawn mower', 'ski', 'snowboard', 'tipper', 'tractor', 'train', 'truck']
# Model: "sequential"
# _________________________________________________________________
#  Layer (type)                Output Shape              Param #
# =================================================================
#  resnet50 (Functional)       (None, 2048)              23587712
#
#  flatten (Flatten)           (None, 2048)              0
#
#  dense (Dense)               (None, 512)               1049088
#
#  dense_1 (Dense)             (None, 10)                5130
#
# =================================================================
# Total params: 24,641,930
# Trainable params: 1,054,218
# Non-trainable params: 23,587,712
# _________________________________________________________________
# None