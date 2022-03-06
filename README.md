# toxicity_app_efrei ☠️
  
The goal of this project is to apply acquired knowledge in "Data Engineering" course at EFREI Paris in "Big Data and Machine Learning major".
Here, we developed a containerized and pipelined application accessible by a website asking you to fill an toxic sentence. With the user answer, a machine learning model on the backend will rate your toxicity between many class :
-toxic
-severe_toxic
-obscene
-threat
-insult
-identity_hate

For the deployment, we used Multibranch Pipeline from Jenkins. It aim is to test every feature branch before merge it in develop branch. After all, it create à pull request from develop to main to release it when user accept it.

## Requirements ⚙️ 

### Model 📊
  
Toxicity model used :
- https://huggingface.co/unitary/toxic-bert 
  
### Versions  🐍
  
- Python 3.7

## Start app from Docker Hub 🐳
 ```shell
 docker run -dp 5000:5000 clementbou/toxicity-app:latest
 ```
  
## Start in local 🚀

To start the project place yourself at the root of the project and be careful that docker is running. After it is running: 
```shell
  docker-compose up
```

## Access to the toxicity app website ❤️

Launch your browser with `localhost:5000` and enjoy!

## Stop ❌

Stop containers and remove containers, networks, volumes, and images created by your previous docker-compose up
```shell
  docker-compose down
```

NB: it's possible that you need administrator privileges, so just launch previous docker-compose commands with "sudo".

## Tests ✅

To launch tests you have to use a python 3.7 environment with the modules placed in requirements. At the root of the project launch:
```shell
  pip install -r requirements.txt
```

NB: use Anaconda environment if it's possible.

After it, you can launch all tests by using be sure to be in the good directory):
```shell
  python -m pytest .
```

## Jenkins pipeline ⚙️
- Install Jenkins from https://www.jenkins.io
- Go on http://localhost:8080 

There one multibranch pipeline :
- develop branch create merge request on main to generate a release
- feature-* build docker image, test it (with stress test an other) and if it is sucessful merge it on develop !

## Software used 🛠
  
_For the implementation of this project, we decided to use these different software:_  
* [Anaconda](https://www.anaconda.com/) - Python distribution platform  🐍
* [PyCharm](https://www.jetbrains.com/fr-fr/pycharm/) - IDE 💻
* [Docker](https://www.docker.com)-Containerization tool 🐳
* [Jenkins](https://www.jenkins.io)-Pipeline tool ⚙️
  
## Library versions 📦
  
**python :** 3.7
**pandas :** 1.3.4  
**flask :** 2.0.2
**vaderSentiment :** 3.3.2
**googletrans :** 3.1.0a0
  
## Authors ✍️
  
* **Cloé RICARD** _alias_ [@cloericard](https://github.com/cloericard)  
* **Clément BOULANGER** _alias_ [@ClementBou](https://github.com/ClementBou)
