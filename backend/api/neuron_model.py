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
            os.makedirs('networkModel')
        self.model.save(f'networkModel\\model{len(self.classNames())}.h5')

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

#
# if __name__ == '__main__':
#     resnet = ResNetUltra('D:\\Github\\mlnet\\s\\s')
#     resnet.preProcessing()
#     resnet.netModel()
#     resnet.netBuild(1)
#     val = resnet.netPredict('train')
#     print(val)
#     print(resnet.classNames())
#     print(resnet.netSummary())
