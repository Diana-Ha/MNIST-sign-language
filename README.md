# MNIST-sign-language
This is my capstone project where I built a sign language interpreter using Keras (Tensorflow backend).

### A couple of notes before we start:
- My models were trained on publicly available MNIST sign language data provided on Kaggle. This data is located in the file named "mnist_data".
- Jupyter notebooks starting with the word "scratchpad" in the name are the primary files I've worked out of. Please read the markdown cells in each section before running the cells. Otherwise, some cells may take a while (approximately 30 minutes) to process.
- "scratchpad_models.ipynb" is the notebook I ran all my models out of. The best performers were saved as .h5 files.
- "scratchpad-all-except-modeling.ipynb" is the notebook where I tested all my code before entering it in a neat and clean format ("demo-png-to-pred.ipynb") to create the .py file.

### Training My Model
First I trained my model on the train data, then tested it on the test data. I measured success based on accuracy. My goal was to achieve a 95% or greater accuracy rate. Since the data is essentially a dataframe of pictures represented as pixels, I did not have to worry about missing data. Once I trained my model, I made many tweaks until I reached my target accuracy rate. When I looked at the 5% that was misclassified, I noticed that there were some trends:

Letter	|Number Misclassified	|Misclassed as	|% of Total Misclassified
--- | --- | --- | ---
T	|82	|XL	|21%
S	|62	|ME	|16%
N	|49	|UAQ	|13%
G	|41	|TPQ	|11%
M	|31	|N	|8%
U |22	|KR	|6%
R	|21	|VU	|5%
K |21	|Y	|5%
H	|20	|G	|5%
D	|12	|AX	|3%
V	|10	|WU	|3%
Q	|8	|M	|2%
Y	|3	|P	|1%

Since the concentration of misclassified letters were T, S, N, and G, I converted some of these rows of pixels back into an actual image and noticed that for some of the images the pixelation (lack of granularity) made it difficult to determine the letter even with the naked eye. I believe this issue can be resolved with a larger dataset to train on. 

### Testing My Model on Other Data
Once my model reached over 95% accuracy in its predictions, I tested it on even more data that it had never seen before. This was data I personally collected for the purpose of training a model on a larger, more diverse data set. Unfortunately, the model had an accuracy rate of 0% on this new data, which led me to dig a bit deeper on the data the model was orginally trained on. One issue I found was that the original training data only had one skin tone (my new test data had a range of skin tones). Another issue I found was that the original training data did not have as many variations in angles as my new test data (meaning my test data had a larger range of hand motion). I believe this issue will be resolved if I retrain my model with a more diverse data set.

### Next Steps
I will train a new model on a larger, more diverse data set and attempt to make the demo a real-time translator.
For more details, please review the file "ASL.pdf".

### To run the demo:
- All .py files are in the locations required to run the file.
- To run the demo, use "demo-png-to-pred.py" in your Command line. It uses data from the file "demo_data".
