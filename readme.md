# Installation
Install all requirements via ```pip install -r requirements.txt```

# Task 1 Gather Data
Data can be gathered via ```python3 gather-data.py``` and is saved to the folder ``data``.

**Press button 1 on the M5Stack to start the measurement.**

The data can also be: 

- resampled with ```resample.py```
- downsampled with ```downsample.py```

# Task 2 Fitness Trainer

Start the fitness trainer via ```python3 src/fitness-trainer.py```.

- press SPACE to start 
- press Q to quit the code


Some extra feedback about the decisions is printed in the terminal to the user.

### File Naming Disclaimer
When workign with pyhton usually underscores are used when naming files. But since in the assignment the filename was given i kept them here. Hence there is some inconsistency in the file naming.


## Data 
Overall the data seems to be too less for an accurate model. Hence one should download all data from the trainingset repository and train its model with those.

### Disclaimer
Overall the program works. But the data i am using is not very accurate, hence my model had a accuracy of only 82 %. This could be due to my leg injury, since i can neither do complete jumingjacks nor run and had to improvise them.

**resampled_data:**
```
----------------
Model Accuracy: 0.82
----------------
```

**downsampled_data:**
```
----------------
Model Accuracy: 0.7866 
----------------
```

**The Accuracy should normaly at least be above 90%.**

Problems: 
- The current model predicts to many jumpngjacks (representated as 0)

## Measurement Problems
The measured data seems to be not correctly captured. Many rows in a row contained the same values which seems to be not realsitic. Therefore some adjustmenst werde made:

- since a large amount of data has been captured, the data has been resampled with ``resample.py`` which can be found in the folder ``resampled_data``
- **since there were many duplicate rows I created a scipt to downsample these data so there are no more duplicates (``donwsample.py``). The downsampled data can be found in the ``downsampled_data`` folder.**
- if in the resampled_data or any other data NaN values appeard, then these rows are deleted (see activity_recognizer.py)
