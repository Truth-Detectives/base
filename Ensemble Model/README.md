# Ensemble Model using Stacking Classifier
*This model uses MLPClassifier, GaussianNB, Logistic Regression, GradientBosstingClassifer and AdaBoostClassifer as estimator models. AdaBoostClassifier was also used as the meta_model for this notebook. The estimator models and meta_model was used to initialise a StackingClassifier, which was then trained and tested on the derived singfake_bilibili_audio_feature.csv dataset.*

## Table of Contents
- Requirements
- Installation
- How to run notebook
- Test_Size
- Estimator Models
- Meta_Model
- StackingClassifier Initialisation

## Requirements
*The package requirements for this notebook is as follows:*
[scikit-learn](https://scikit-learn.org/stable/install.html)
[pandas](https://pypi.org/project/pandas/)
[numpy](https://pypi.org/project/numpy/)
[seaborn](https://pypi.org/project/seaborn/)
[matplotlib](https://pypi.org/project/matplotlib/)


## Installation
### Install scikit-learn library

```bash
python -m venv sklearn-env
sklearn-env\Scripts\activate
pip install -U scikit-learn
```
### Install pandas

```bash
pip install pandas
```

### Install numpy

```bash
pip install numpy
```
### Install seaborn

```bash
pip install seaborn
```

### Install matplotlib

```bash
pip install matplotlib
```
## How to run notebook
*In order to run the segments of code. The user must click the necessary cell and then click the play button in the top navigation bar.*

## Test_Size

```python
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.65, random_state=42)
```

## Estimator Models

```python
models=[
    ('mlp',MLPClassifier(hidden_layer_sizes=(50,50),max_iter=1000, random_state=42)),
    ('nb',GaussianNB()),
    ('lr',LogisticRegression(penalty='l2', max_iter=1000,random_state=42,solver='liblinear')),
    ('gbc', GradientBoostingClassifier(n_estimators=500, learning_rate=0.01, max_depth=3,random_state=42)),
    ('ada', AdaBoostClassifier(n_estimators=500, random_state=42))
]
```

## Meta_Model

```python
meta_model = AdaBoostClassifier(n_estimators=500, random_state=42)
```

## StackingClassifier Initialisation

```python
stack = StackingClassifier(estimators=models,final_estimator=meta_model,cv=5)
```