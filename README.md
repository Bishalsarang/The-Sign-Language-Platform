
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
Controls:
		Press 'n' to append current letter
		Press 'm' for space
		press 'd' to delete last letter from sentence
		press 's' to speak the translated sentence
		press 'c' to clear the sentence
		press ESC key to exit

** Confifuring paths to run ASL.ipynb**
1. Download datasets from [here](https://drive.google.com/open?id=15BypaqP5X10IiJSiPTpbNP5SDyYoO-xR) or create yout own
2. Modify TRAIN_DATA_PATH an TEST_DATA_PATH
3. Train the model
4. Your model is saved as withbgmodelv1.h5
5. Use the model to run translator.py by configuring the path in variables.py


