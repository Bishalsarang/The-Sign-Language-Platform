
# Sign-Language-Platform
ASL translator using CNN


Requirements:
Python 3.6 64 bit (Python 3.7 is not officially supported by tensorflow)

For Anaconda Users:
 You can download and import the virtual environment file to anoconda environment ["tensorflow_env.yml"](https://github.com/sarangbishal/ASL-translator/blob/master/tensorflow_env.yml) which install all the libraries neeeded for project.
 
Other users can install all requirements from "requirements.txt" file
```
pip install -r requirements.txt
```
 
**Configuring paths to run the translator:**
1. Download pre-trained model from [here](https://drive.google.com/open?id=1s3h2tr_nE53-zIKFMTvvMP35Th3VWbsY)
2.  Modify MODEL_PATH from variables.py

**Running  translator.py**
After installing all the requirements in your system environment or virtual environment run the translator directly 
Download [model](https://drive.google.com/open?id=1tMwCNFbdmStjGNwdDnAG8y-vCm44SO2V) and set MODEL_PATH
Usage:
1. Translate from webcam
```
python translator.py 
```


