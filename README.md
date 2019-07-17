# Alexa-skill
A program that receives requests from a custom Alexa skill and runs appropriate functions.

## This project contains
* Usage of a flask web server
* Scalable design that allows for more Alexa intents to be added easily
* Type-checking and Type hints
* Basic unittests

## What I learned
* How to interface with the Alexa skill system
* Formatting json requests

## Installation
Install the requirements
```
$ pip install -r requirements.txt
$ python main.py
 ```
More setup is required to create an Alexa skill and the program will need to be deployed. Alternatively use ngrok to create a https server tunnel for development.