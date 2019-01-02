
# Sign-Language-Platform
ASL translator using CNN


Requirements:

 





**Configuring paths for creating a CNN Model**
1. Download ASL datasets from [here](https://www.kaggle.com/grassknoted/asl-alphabet).
2. Make folder *datasets* in root directory of the notebook 
3. Inside datasets make subfolders *test_data* and *train_data*
4. Extract files from downloaded compressed files and put the contents into respective directories.
  The folder structure for both test_data and train_data should look like this
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
