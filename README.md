# Mati 🧿

This project is my first exploration of using computer vision and LLMs, as well as observing the incredible power that can come from combining them. 

After studying ROS, I was brainstorming the possible applications of robotics when I had an idea: robotic seeing-eye dogs! Currently, it involves years of training for dogs to become a guide dog [(source)](https://www.cnib.ca/en/blog/inside-scoop-what-it-takes-train-guide-dog?region=bc#:~:text=Each%20dog%20that%20comes%20into,involves%20three%20years%20of%20training), but what if we could use robots instead? This would reduce training time and also make them accessible to people unable to take care of an animal.

The [demo](https://www.youtube.com/watch?v=HxpIs5khI1I) available here is meant to serve as a “proof of concept” and show how this idea may be fully actualized. 

# Explanation

Currently, this project uses [Yolov5](https://github.com/ultralytics/yolov5) (with some modifications for our purposes) to scan a setting with the computer’s webcam for ~5 unique items. Upon scanning the setting, it then queries the [HuggingFace LLM](https://huggingface.co/), listing the items and then asking where am I? Using the [gTTS](https://pypi.org/project/gTTS/) python library, it will say the query and then the response from the LLM, hopefully giving an accurate description to the user.

# Setup

If you want to try the program out for yourself, make sure to:

* Download the code from this GitHub repo
* Within the project directory run ``` $ pip install -r requirements.txt``` to install the required dependencies for the library
>[!NOTE]
>You may want to create a virtual environment first so that these libraries do not disturb your 
existing dependencies
* Create an account at [HuggingFace](https://huggingface.co/) and modify the .env file to have your API key (go to the settings in your HuggingFace account and then create a new API key)
* Run the script in your terminal with ```$ python Mati.py ``` and show your webcam around the room!
