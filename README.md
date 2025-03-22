![Stars](https://img.shields.io/github/stars/harshbg/Sign-Language-Interpreter-using-Deep-Learning.svg?style=social)
![Forks](https://img.shields.io/github/forks/harshbg/Sign-Language-Interpreter-using-Deep-Learning.svg?style=social)
![GitHub contributors](https://img.shields.io/github/contributors/harshbg/Sign-Language-Interpreter-using-Deep-Learning.svg)
![Language](https://img.shields.io/github/languages/top/harshbg/Sign-Language-Interpreter-using-Deep-Learning.svg)
[![GitHub](https://img.shields.io/github/license/harshbg/Sign-Language-Interpreter-using-Deep-Learning.svg)](https://choosealicense.com/licenses/mit)
[![HitCount](http://hits.dwyl.io/harshbg/Sign-Language-Interpreter-using-Deep-Learning.svg)](http://hits.dwyl.io/harshbg/Sign-Language-Interpreter-using-Deep-Learning)


# Sign Language Interpreter using Deep Learning
> A sign language interpreter using live video feed from the camera. 
The project was completed in 24 hours as part of HackUNT-19, the University of North Texas's annual Hackathon. You can view the project demo on [YouTube](https://link.harshgupta.com/acd72). 

## Table of contents
* [General info](#general-info)
* [Screenshots](#screenshots)
* [Demo](#demo)
* [Technologies and Tools](#technologies-and-tools)
* [Setup](#setup)
* [Process](#process)
* [Code Examples](#code-examples)
* [Features](#features)
* [Status](#status)
* [Contact](#contact)

## General info

The theme at HACK UNT 19 was to use technology to improve accessibility by finding a creative solution to benefit the lives of those with a disability. 
We wanted to make it easy for 70 million deaf people across the world to be independent of translators for there daily communication needs, so we designed the app to work as a personal translator 24*7 for the deaf people.

## Demo
![Example screenshot](./img/demo4.gif)



![Example screenshot](./img/demo2.gif)



![Example screenshot](./img/demo3.gif)


**The entire demo of the project can be found on [YouTube](https://link.harshgupta.com/acd72).**


## Screenshots

![Example screenshot](./img/Capture1.PNG)
![Example screenshot](./img/Capture.PNG)

## Technologies and Tools
* Python 
* TensorFlow
* Keras
* OpenCV

## Setup

* Use comand promt to setup environment by using install_packages.txt and install_packages_gpu.txt files. 
 
`pyton -m pip r install_packages.txt`

This will help you in installing all the libraries required for the project.

## Process

* Run `set_hand_histogram.py` to set the hand histogram for creating gestures. 
* Once you get a good histogram, save it in the code folder, or you can use the histogram created by us that can be found [here](https://github.com/harshbg/Sign-Language-Interpreter-using-Deep-Learning/blob/master/Code/hist).
* Added gestures and label them using OpenCV which uses webcam feed. by running `create_gestures.py` and stores them in a database. Alternately, you can use the gestures created by us [here](https://github.com/harshbg/Sign-Language-Interpreter-using-Deep-Learning/tree/master/Code).
* Add different variations to the captured gestures by flipping all the images by using `Rotate_images.py`.
* Run `load_images.py` to split all the captured gestures into training, validation and test set. 
* To view all the gestures, run `display_gestures.py` .
* Train the model using Keras by running `cnn_model_train.py`.
* Run `final.py`. This will open up the gesture recognition window which will use your webcam to interpret the trained American Sign Language gestures. 
