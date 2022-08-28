# ************************************************************************************
## Project 2: Machine Learning In Practice
# ************************************************************************************

For this project, you will apply your skills & knowledge in machine learning to some
interesting data. The goal of the next few weeks is to make sure that you can 
demonstrate your ability to conduct clean & informative exploratory data analyses
to inform your feature engineering, as well as an ability to drive the development
of a/some machine learning models. You will have several options to choose from to
complete this project. 

This next stage is also about defining your own goals. You
will be expected to derive a question or solution that you would like to address
using a machine learning model. This is an extremely important part of being
a data scientist. Often we are tasked with coming up with the question & the
solution, using data science. That is what you will do for this project!

## Option 1: Single, Optimized model
# ************************************************************************************
With this option, you will select a data source (see data_sources.txt, or select your 
own) & develop a model from scratch. You will conduct thorough exploratory analyses 
to better understand relationships between existing features & to better define your own
engineered features. Then, you will brak up your data into training, testing & validation
data, and proceed with testing multiple model architectures. The aim is to 
select one that performs the best before thorough optimization. You will then spend time 
optimizing hyperparameters with your model (regularization,parameter grid search, PCA, 
model score optimization,etc.). The goal is, at the end, to show a successful (highly
accurate) model & how it performs on the final hold-out data. 

Steps to complete
1. EDA
2. Train, test, validate split data
3. Try multiple model types
4. Optimize best performing model
5. Demonstrate final accuracy & summarize


## Option 2: Multiple Models of varying types, semi-optimized
# ************************************************************************************
For this option, you will spend ~1 week per model. You will still wnat to conduct some
exploratory data analyses & feature engineering at the start of each. However, each model
will have a different goal, but all using the same data. You will develop one semi-
optimized model focusing on prediction, one on classification, and a third of your 
choice. The third could be clustering, neural networks, time series, natural language
processing, etc.

### Steps

- (1) Conduct EDA for each model

- (2a) Develop Prediction Model
The bulk of the work in developing this model will involve data splitting, feature 
engineering & hyperparameter optimization. Ideally, this would involve conducting a 
grid-search operation. 

- (2b) Develop Classification Model
The bulk of the work in developing this model will be comparing various 
classification type models against one another (Logistic Reg, gradient boosted regressor, 
decision trees, SVM, etc.), with some time spent on optimizing the best general model. 

- (2c) Develop 3rd model
The bulk of the work in developing this model depend on which you choose, so once
you make this decision, we can discuss how time should be spent. 

- (3) Summarize results of each model


## Tips for Success
# ************************************************************************************
### Feature Engineering
When deciding on your approach to feature engineering, keep the following questions in
mind:

- How different is the scale of the features included?
- Are there categorical features that should be ordinal? Dummy?
- Do any of the features have redundant information?
- is there any new information that can be derived by combining 1 or more features?
- Am I providing the model with...
	- Enough information?
	- Too much information?
	- Redundant information?



### Modeling
- Does the data need to be scaled/standardized?
- Am I using a model prone to bias?
- Am I exposing the model to enough variabiltiy in training data?
- Am I fitting a model to noise?
- Which model type is the best for this data?



## Definition of Done
# ************************************************************************************
-  **Clean, commented & complete code is pushed to github**:
	- README on main page of directory specific to this project - very brief & presentable overview of project, resources used, disclaimer for public data
	    usage, 1-3 sentences of findings, links to slide deck with summary
	- Jupyter notebook with all EDA & outcomes
	- Any python files used for data cleaning, automation, or helper functions
	- Sections commented in notebook with Markdown & comments in py files