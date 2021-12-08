# sentiment-analysis_efrei 💌
  
The goal of this project is to apply acquired knowledge in "Data Engineering" course at EFREI Paris in "Big Data and Machine Learning major".
Here, we developed a containerized application accessible by a website asking "How you feel ?" to the user. With the user answer, a machine learning model on the backend tries to classify user feelings between :
-Positive
-Negative
-Neutral

Some tests have been made to validate the app quality.

## Requirements ⚙️ 

### DataSet 📊
  
DataSet for evaluation of Vader model https://www.kaggle.com/abhi8923shriv/sentiment-analysis-dataset :  
- test.csv  
  
### Versions  🐍
  
- Python 3.7
  
## Start 🚀

To start the project place yourself at the root of the project and be careful that docker is running. After it is running: 
```shell
  docker-compose up
```

## Access to the sentiment analysis website ❤️

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

After it, you can launch all tests by using:
```shell
  python -m pytest .
```

## Software used 🛠
  
_For the implementation of this project, we decided to use these different software:_  
* [Anaconda](https://www.anaconda.com/) - Python distribution platform  🐍
* [PyCharm](https://www.jetbrains.com/fr-fr/pycharm/) - IDE 💻
* [Docker](https://www.docker.com)-Containerization tool 🐳
  
## Library versions 📦
  
**python :** 3.7
**pandas :** 1.3.4  
**flask :** 2.0.2
**vaderSentiment :** 3.3.2
**googletrans :** 3.1.0a0
  
## Authors ✍️
  
* **Cloé RICARD** _alias_ [@cloericard](https://github.com/cloericard)  
* **Clément BOULANGER** _alias_ [@ClementBou](https://github.com/ClementBou)
