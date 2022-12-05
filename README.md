# What is this project?
This is Transfer Learning project implemented on Django+Vue. We implemented background processes via Celery+Rabbitmq3

# Why do we need it?
The concept of the project is to automate the prelearning phases in neural network (including scrapping of the images, their storage, and preprocessing them).

# Do we used Neural Networks?
Yes, we used the transfer learning method. We took **Resnet50** (convolution neural network based on 50 layers: 48 conv2d, max pooling and averaging layers) trained on **Imagenet** and Flattened our custom network to improve the weights and biases of the network.

# What is the work process?
The work process of our application as follows:
1. We scrap images from Yandex search tool and download it to our local repository (implemented as a background process of our application).
2. We generate neural model (we have class for the model in our django-backend) and train based on this input.
3. User can input image in the web interface
4. This image is verified by the model
5. User gets the correct prediction of what is the image (what object is illustrated on it).

## Screenshots
*Would be provided later.
