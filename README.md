# capstone-MNIST-sign-language
This is my capstone project where I built a sign language interpreter using Keras (Tensorflow backend).

### A couple of notes before we start:
- My models were trained on publicly available MNIST sign language data provided on Kaggle. This data is located in the file named "mnist_data".
- Jupyter notebooks starting with the word "scratchpad" in the name are the primary files I've worked out of. Please read the markdown cells in each section before running the cells. Otherwise, some cells may take a while (approximately 30 minutes) to process.
- "scratchpad_models.ipynb" is the notebook I ran all my models out of. The best performers were saved as .h5 files.
- "scratchpad-all-except-modeling.ipynb" is the notebook where I tested all my code before entering it in a neat and clean format ("demo-png-to-pred.ipynb") to create the .py file.

### Training My Model
First I trained my model on the train data, then tested it on the test data. I measured success based on accuracy. My goal was to achieve a 95% or greater accuracy rate. Since the data is essentially a dataframe of pictures represented as pixels, I did not have to worry about missing data. Once I trained my model, I made many tweaks until I reached my target accuracy rate. When I looked at the 5% that was misclassified, I noticed that there were some trends:

Letter | Number Misclassified	| Misclassed as
--- | --- | ---
  T	     |       82	    |            X,L
  S	      |      62	|ME
  N	       |     49	|UAQ
  G	        |    41	|TPQ
  M	        |    31	|N
  U	         |   22	|KR
  R	          |  21	|VU
  K	           | 21	|Y
  H	    |        20	|G
  D	     |       12	|AX
  V	      |      10	|WU
  Q	       |     8	|M
  Y	        |    3	|P


### Testing My Model on Other Data
Once my model reached over 95% accuracy in its predictions, I tested it on even more data that it had never seen before. This was data I personally collected for the purpose of training a model on a larger, more diverse data set. Unfortunately, the model had an accuracy rate of 0% on this new data, which led me to dig a 

### To run the demo:
- All .py files are in the locations required to run the file.
- To run the demo, use "demo-png-to-pred.py" in your Command line. It uses data from the file "demo_data".
