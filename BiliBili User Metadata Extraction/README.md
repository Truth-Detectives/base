# Singfake dataset and Logistic Regression
*This folder contains the files used to acquire bilibili user data*
# Table of contents
- Requirements
- Installation
- Using the API

# Requirements

## For BiliBili API
*In order to run the bilibilitest.py file these libraries are required:*
[asyncio](https://pypi.org/project/asyncio/)
[bilibili API](https://pypi.org/project/bilibili-api-python/)
[pandas](https://pypi.org/project/pandas/)

# Installation

## Install bilibili API
```bash
pip install bilibili-api-python
```
## Install asyncio
```bash
pip install asyncio
```

## Install pandas

```bash
pip install pandas
```


## Using the API
*The bilibili API was used to get user data such as amount of folllowers, user ID and usernames from bilibili links. In order to fetch such data a credential class must be initalized. This class uses browser cookie data for GET, POST operation as well as verification.*
```python
SESSDATA = ""
BILI_JCT = ""
BUVID3 = ""
```
```python
 cred = Credential(sessdata=SESSDATA, bili_jct=BILI_JCT, buvid3=BUVID3)
```
*This credential is then used along with the video bvid to retrieve video data.*