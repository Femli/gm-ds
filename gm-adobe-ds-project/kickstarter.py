#pip3 install pandas
#pip3 install matplotlib
#pip3 install scikit-learn
import pandas as pd
import numpy as np
import matplotlib as plt
from pathlib import Path

dataset = "DSI_kickstarterscrape_dataset.csv"
dataset_path = Path(dataset).resolve()
#print(dataset_path)

df = pd.read_csv(dataset, encoding="ISO-8859-1", engine="python")
df.head(10)
df.dtypes

#isolating the pledged column
df["pledged"].head(10)
pledged = df["pledged"]

#getting the average pledge across all kickstarter projects
#pledged = pledged.to_numpy()
#avg_pledge = sum(pledged) / len(pledged)
#print(avg_pledge)
pledged.describe()
pledged.mean()

#exploring the kickstarter projects and their backers
df[["name", "backers"]].head(10)
backers = df["backers"]
backers.head(10)
backers.describe()

#looking into the distribution of backers
backers.plot() #all exisiting values in the dataset
backers.plot.box() #visualizing distribution - extremely skewed to the right
backers.plot.hist(bins=50)

#looking into the distribution of durations
df["duration"].describe()
df["duration"].plot.box()
df["duration"].plot.hist(bins=50)

#looking into successful kickstarter projects
df["status"].value_counts()
df["status"].value_counts().plot.bar()
#important columns that provide insight on successful projects
imp = ["status", "category", "location", "funded percentage", "funded date", "updates", "duration", "pledged"]
#focusing only on projects that were successful
df_imp = df[imp].loc[df["status"] == "successful"]
df_imp.head(10)

#top 10 successful locations
df_imp["location"].value_counts().iloc[0:10]
df_imp["location"].value_counts().iloc[0:10].sort_values().plot.barh()
#duration for most successful projects
df_imp["duration"].plot.hist(bins=50) #vs df["duration"].plot.hist() -- have identical distributions
df_imp["duration"].plot.box()
df_imp["duration"].describe()
#most successful categories
df_imp["category"].value_counts()
df_imp["category"].value_counts().sort_values().plot.barh()
#most successful months
df_months = df_imp["funded date"].str.split(expand=True)[2]; df_months.head(5)
df_months.count()
df_months.value_counts().sort_values().plot.barh()
#an_ind = df_imp["funded date"].isin(jan)
#most successful pledge goals
df_imp["pledged"].describe(); df_imp["pledged"].mode()
df_imp["pledged"].plot.box()
df_imp["pledged"].plot.hist(bins=100)
df_imp["pledged"].plot.hist(logy=True, bins=100) #scaling the graph logirthimcally
#df_imp["pledged"].plot.hist(xlim=[df_imp["pledged"].quantile(0.25), df_imp["pledged"].quantile(0.75)], bins=500) #removing outliers
df_imp["pledged"].plot(xlim=[0, df_imp["pledged"].quantile(0.75)]) #removing outliers

pld_cnt = df_imp["pledged"].value_counts()
pld_cnt.iloc[0:10].plot.bar()
