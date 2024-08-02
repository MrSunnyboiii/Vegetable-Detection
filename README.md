# Vegetable Identifier

This project uses the NVIDIA Jetson AI to identify different types of vegetables

![image of a vegetable](https://github.com/user-attachments/assets/dc1b424a-83c1-4051-aaef-f463614df979)

## The Algorithm

The model is retrained from the resnet-18 model, using a dataset of over 5000 images ([Found here]([https://www.kaggle.com/datasets/misrakahmed/vegetable-image-dataset])). The model was retrained using jetson inference's built-in retraining system. More details on the process can be found [here](https://github.com/dusty-nv/jetson-inference/blob/master/docs/pytorch-cat-dog.md).

The python file utilizes the .onnx file to recognize an image that the user inputs. A few test images are also included.

This vegetable types this model can detect are:
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

[View a video explanation here]()

1: Be sure the jetson inference library is installed on your system

2: Clone the repository by running this command
```sh
git clone [https://github.com/MrSunnyboiii/Vegetable-Detection]
```

3: Move into the project folder
```sh
cd VeggieIdentifier
```

4: Run the python script
```sh
python3 vegetables.py path/to/file/here
```
