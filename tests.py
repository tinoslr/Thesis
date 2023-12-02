import pandas as pd 
import numpy as numpy
import matplotlib.pyplot as plt 
import matplotlib as mpl
mpl.style.use('ggplot')
import seaborn as sns

s = pd.Series([8888 , 7777 ,5555, 33333])
s.index = ["Berlin","Karlsruhe","Köln","Bonn"]
s.name = 'Population'
print(s)