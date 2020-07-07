import matplotlib.pyplot as plt # plotting
import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import seaborn as sns #Analyticalplots

df = pd.read_csv(r"C:\Users\SIDDHARTH GOEL\OneDrive\Desktop\InternShips\Data\datasets_heart.csv")

#Looking at the data set.
df.head()
df.info()
df.describe()

Row, Col = df.shape
print(f'There are {Row} rows and {Col} columns')

#Grouping data baased on usable features.
dat = df[["age","sex","trestbps","fbs","thalach","chol","restecg","target"]]


#Changing columns name for better understanding.
dat.columns=["Age","Sex","Rest BP","Fast Sugar Levels","Heart Rates","Serum Cholestrol","Rest ECG","Target"]
dat.sample(5)

Row, Col = dat.shape
print(f'There are {Row} rows and {Col} columns')
#
#
#
#Analysis of the data.
sns.lmplot(x="Rest BP", y="Heart Rates",hue= "Target", data=dat)
sns.lmplot(x="Age",y="Serum Cholestrol",hue="Target",data=dat)

df["trestbps"].unique()


sns.lmplot(x="trestbps", y="thalach", hue="sex", data=df)

# filter with chol,target is not 1 and trestbps less than 170
chol = dat[(dat['Serum Cholestrol']<200) &(dat['Target']==1) & (dat['Rest BP']<160)]
#
#
#
#Plotting Histogramns 
for col in dat.columns:
    plt.hist(dat[col], bins = dat[col].nunique())
    plt.title(col)
    plt.show()

#Plotting corelational datasets
def plotCorrelationMatrix(df, graphWidth):
    filename = df
    df = df.dropna('columns') # drop columns with NaN
    df = df[[col for col in df if df[col].nunique() > 1]] # keep columns where there are more than 1 unique values
    if df.shape[1] < 2:
        print(f'No correlation plots shown: The number of non-NaN or constant columns ({df.shape[1]}) is less than 2')
        return
    corr = df.corr()
    plt.figure(num=None, figsize=(graphWidth, graphWidth), dpi=80, facecolor='w', edgecolor='k')
    corrMat = plt.matshow(corr, fignum = 1)
    plt.xticks(range(len(corr.columns)), corr.columns, rotation=90)
    plt.yticks(range(len(corr.columns)), corr.columns)
    plt.gca().xaxis.tick_bottom()
    plt.colorbar(corrMat)
    plt.title(f'Correlation Matrix for {filename}', fontsize=15)
    plt.show()

plotCorrelationMatrix(dat, 8)
