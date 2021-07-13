import requests
import json
import numpy as np
import pandas as pd
import streamlit as st

response = requests.get("https://indexapi.aws.merqurian.com/index?type=test%2Cprod")
#response2 = requests.get("https://indexapi.aws.merqurian.com/index/94e276c8-dab7-41b8-8a5d-64f7778276d0/metrics/price_return/data")
#displayData = {}
data = json.loads(response.text)
#data2 = json.loads(ressponse2.text)
url = ''
dataList = []
print('Total number of apis to be called ', len(data['results']))
loopCount=0
for result in data['results']:
    loopCount = loopCount + 1
    #print(result['id'])
    #print(result['name'])
    id = result['id']
    name = result['name']
    url = requests.get("https://indexapi.aws.merqurian.com/index/" + result['id'] + "/metrics/price_return/data")
    data3 = json.loads(url.text)
    result2 = data3['results']
    newLength = len(result2) - 1
    lastObject = result2[newLength]
    date = lastObject['id']
    #print(date)
    metrics = lastObject['metrics']
    priceObject = metrics[0]
    priceReturn = priceObject['value']
    #print(priceReturn)
    #print()
    table = {}
    for variable in ["id", "name", "priceReturn", "date"]:
        table[variable] = eval(variable)
    dataList.append(table)
    #print(loopCount, table)
    #print(dataList)

header = st.beta_container()
dataset = st.beta_container()

with header:
    st.title("Test")

with dataset:
    st.header("MerQube Indices")
    st.write(pd.DataFrame(dataList))







