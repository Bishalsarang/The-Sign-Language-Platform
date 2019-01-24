
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
 



**Configuring paths for creating a CNN Model**
1. Download ASL datasets from [here](https://www.kaggle.com/grassknoted/asl-alphabet).
2. Make folder *datasets* in root directory of the notebook 
3. Inside datasets make subfolders *test_data* and *train_data*
4. Extract files from downloaded compressed files and put the contents into respective directories.
  The folder structure for both test_data and train_data should look like this
 5. Modify variable:
   NUM_OF_TRAIN IMAGES = 3000 * 28 if you're using datasets from the above link or modify accordingly
 
<pre>
├───test_data
   ├───A
   ├───B
   ├───C
   ├───D
   ├───E
   ├───F
   ├───G
   ├───H
   ├───I
   ├───J
   ├───K
   ├───L
   ├───M
   ├───N
   ├───nothing
   ├───O
   ├───P
   ├───Q
   ├───R
   ├───S
   ├───space
   ├───T
   ├───U
   ├───V
   ├───W
   ├───X
   ├───Y
   └───Z
</pre>

**Configuring paths to run the translator:**
1. Download pre-trained model from [here](https://drive.google.com/file/d/12h1QmfUwd2sJyyk-0xobRSgJN9BxXblZ/view?usp=sharing)
2.  Modify IMG_PATH and MODEL_PATH
3. Run the translator.ipynb notebook 



**Running  translator.py**
After installing all the requirements in your system environment or virtual environment run the translator directly 
```
python translator.py
```
