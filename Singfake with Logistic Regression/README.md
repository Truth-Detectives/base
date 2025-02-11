# Singfake dataset and Logistic Regression
*This folder contains the files used to acquire bilibili video data and the notebook used to run that data against the logistic regression model in order to detect AI generated videos*
# Table of contents
- Requirements
- Resources
- Installation
- Using the API
- Running the notebook
- Logistic Regression

# Requirements

## For BiliBili API
*In order to run the bilibilitest.py file these libraries are required:*
[asyncio](https://pypi.org/project/asyncio/)
[bilibili API](https://pypi.org/project/bilibili-api-python/)
[pandas](https://pypi.org/project/pandas/)

## For Logistic Regression
*In order for all components of the notebook to run these libraries are required:*
[scikit-learn](https://scikit-learn.org/stable/install.html)
[pandas](https://pypi.org/project/pandas/)
[numpy](https://pypi.org/project/numpy/)
[seaborn](https://pypi.org/project/seaborn/)
[matplotlib](https://pypi.org/project/matplotlib/)

# Resources
*The dataset that is used in this notebook is:* [singfake dataset](https://singfake.org/)

# Installation

## Install bilibili API
```bash
pip install bilibili-api-python
```
## Install asyncio
```bash
pip install asyncio
```
## Install scikit-learn library

```bash
python -m venv sklearn-env
sklearn-env\Scripts\activate
pip install -U scikit-learn
```
## Install pandas

```bash
pip install pandas
```

## Install numpy

```bash
pip install numpy
```

## Install seaborn

```bash
pip install seaborn
```

## Install matplotlib

```bash
pip install matplotlib
```

## Using the API
*The bilibili API was used to get video data such as amount of views, likes and comments from bilibili links. In order to fetch such data a credential class must be initalized. This class uses browser cookie data for GET, POST operation as well as verification.*
```python
SESSDATA = ""
BILI_JCT = ""
BUVID3 = ""
```
```python
 cred = Credential(sessdata=SESSDATA, bili_jct=BILI_JCT, buvid3=BUVID3)
```
*This credential is then used along with the video bvid to retrieve video data.*
*Getting the bvid:*
```python
def get_bvid(url):
    
    str_ar = url.split('/')
    bvid_url = str_ar[4]
    alt_id = bvid_url.split('?')
    bvid_id = alt_id[0]
    
    return bvid_id
```
*Retrieving video data*
```python
async def get_stats(id,cred,i,df):
    
    await asyncio.sleep(1) 
    
    vid_data = video.Video(bvid=id, credential=cred)
    
    try:
        vid_info = await vid_data.get_info()
    except:
        print("no data")
        stats = [{'view': 0,'like':0,'reply':0}]
    else:
        stats = vid_info['stat']
        df.loc[i,['views']] = stats['view']
        df.loc[i,['likes']] = stats['like']
        df.loc[i,['comments']] = stats['reply']
        print(stats['view'])
        
        
    return stats
```

## Running the notebook
*In order to run the segments of code. The user must click the necessary cell and then click the play button in the top navigation bar.*

## Logistic Regression

*The new dataset containing view, like and comment counts is now ran against the logistic regression model. Firstly the data was read into to a dataframe, pdata*
```python
pdata = pd.read_csv('singfake_updated_dataset.csv', skiprows=1, names=col_names)
```
*The data was then separated into the feature data and the y data which will be our real or fake values.*
```python
feat_col = ['views','likes','comments']

X = pdata[feat_col] 
y = pdata.bonafide_or_spoof
```
*The data was then separated into trainins and testing sets at a test size of 0.25 and a random state of 42*
```python
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)
```
*The model was then initalized with a max_iter value of 200 and a random state of 42*
```python
lrmodel = LogisticRegression(max_iter=200,random_state=42)
```
*The model was then trained and the y prediction values was generated.*
```python
lrmodel.fit(X_train, y_train)

y_pred = lrmodel.predict(X_test)
```
*The accuracy and classification report was then generated as well as the confusion matrix and the AUC-ROC curve.*
