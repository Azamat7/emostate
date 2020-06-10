# EmoState: IE481 Data Visualization Project

## Description  

A folder ```project/client/templates/``` has all the html files that are rendered. There are three main pages: ```outdoor_activity.html```, ```app_usage.html```, ```recommendation.html```. All inherits ```base.html```, in which most of design attributes are set. Each page mainly consists of plotly python code converted to be embedded into html & js file.  



## How to run  

It would be useful to use virtual environment, so here are commands to create and activate it (Windows users may want to use different commands)

Create a virtual environment:
```bash
virtualenv env
```

Then, activate it:
```bash
source env/bin/activate
```

Install the requirements:
```bash
pip install -r requirements.txt
```

Set the development configs:
```bash 
APP_SETTINGS="project.server.config.DevelopmentConfig"
```

Run the app:
```bash 
python app.py
```

App is accessible at: [emostate.herokuapp.com](https://emostate.herokuapp.com/)
