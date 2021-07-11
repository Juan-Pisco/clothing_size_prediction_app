# Clothing Size Prediction App | Made by Juan David Pisco
## Project Summary
Predict your clothing size according to your height, age and weight in a intuitive Qt desktop app (Windows and Mac available) with the help of artificial intelligence to make your online purchases more secure and confident.

## Project Motivation 
* Buying clothes online is a headache for all people who are not sure about their size in a certain store, that's why with this app, the customer can be more confindent with a ML solution which recommends for the clothing size that best fits the cutsomer's body shape. The idea behind this is to sell the product to clothing stores and reinforce the training with data from new costumers so the model is more precise and related to each store. 
* Udacity's Data Science Nanodegree capstone project.

## Files Explanation
Files with their respective usage are:
* res (Folder): Contains logos and image resources used in the Qt app.
* clothing_size.pth: File containing the Pytorch Neural Network model.
* Data Analysis and Model Training: Notebook containing the data treatment and model's creation.
* final_test.csv: Dataset containing height, age, height and clothing size as columns. This dataset was used to train the model and was extracted from [this Kaggle post.](https://www.kaggle.com/tourist55/clothessizeprediction)
* main.py: Python code containing the app's logic and execution.
* requirements.txt: Result of pip freeze to install all the dependencies needed for running the app and the notebook.
* res.qrc: Resources special file for the Qt app.
* res_rc.py: Python encoding for showing the resources from res.qrc file in the app.
* screen.ui: QtDesigner file where the interface of the app is designed.

## Running instructions
Follow these instructions in order to run everything perfectly.
1. Install all the dependencies needed with `pip install -r requirements.txt`
2. To open the desktop app, run the `main.py` in your IDE of preference or get in the project's directory from the terminal and write:
`python main.py`
3. To open the notebook, run the `Data Analysis and Model Training.ipynb` notebook and run all the cells to get the model trained and the data preprocessed.





