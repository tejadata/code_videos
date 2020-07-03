# -*- coding: utf-8 -*-
"""
Created on Mon Jun 29 23:29:13 2020

@author: vishwateja.r
"""


import pandas as pd
import seaborn as sns

engine=(130,130,152,109,136,136,136,136,131,108,108,164,164,164)
price = (13495,16500,16500,13950,17450,15250,17710,18920,23875,16430,16925,20970,21105,24565)

d = {"engine":engine,"price":price}


data=pd.DataFrame(d)

data.corr()


sns.heatmap(data.corr(),annot=True)
