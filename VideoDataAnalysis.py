import pandas as pd, numpy as np
import matplotlib as mlt
#%%
# import datasets
games = pd.read_csv('Datasets/vgsales.csv')
#view top 5 rows
games.head()

#%%
games.dtypes
#%%
#Describe the genres
games.Genre.describe()
#%%
#Value counts for each type of genre
games.Genre.value_counts()
#%%
games.Platform.value_counts()
games.Year.value_counts()
games.Publisher.value_counts()

#%%
type(games.Genre.value_counts())

#%%
#top value counts
games.Genre.value_counts().head(5)

#%%
#various types of games
#to generate list
games.Genre.unique()
#%%
#no of unique columns
games.Genre.nunique()


#%%
# generate cross tabular of genre and year
pd.crosstab(games.Genre,games.Year)
#%%
#describe the sales
games.Global_Sales.describe()
#%%
games.Global_Sales.mean()
#%%
#std dev
games.Global_Sales.std()
#%%
games.Year.plot(kind='hist')
#%%
games.Genre.value_counts().plot(kind='bar')

#%%
