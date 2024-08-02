# Vegetable Identifier

This project uses the NVIDIA Jetson AI to identify different types of vegetables and fruits

![image of a vegetable](https://github.com/user-attachments/assets/dc1b424a-83c1-4051-aaef-f463614df979)

  ## THE MODEL

This model was trained using jetson inference's image recognition program. More details on this model can be found [on this page](https://github.com/dusty-nv/jetson-inference/blob/master/docs/imagenet-example-python-2.md ). It uses the resnet-18 model, which was retrained with ([this](https://www.kaggle.com/datasets/misrakahmed/vegetable-image-dataset)) dataset that contains 15000 training images.

A folder containing test images is included in this repository which the model will be able recognize as some of the following:

_(The vegetable types this model can detect are)_
* Bean
* Bitter Gourd
* Bottle Gourd
* Brinjal
* Broccoli
* Cabbage
* Capsicum
* Carrot
* Cauliflower
* Cucumber
* Papaya
* Potato
* Pumpkin
* Radish
* Tomato

## Running this project

A tutorial on how to use this model can be found [here](). (Note: VSCode and a jetson-inference library is required in order to run this code)

1: Clone the repository by running this command
```sh
git clone https://github.com/MrSunnyboiii/Vegetable-Detection
```

2: Move into the project folder
```sh
cd Vegetable-Detection
```

3: Run the python script by including an image of the vegetable you want to identify (Ex: test-images/0001.jpg)
```sh
python3 vegetables.py path/to/file/here
```
