import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from scipy.stats import linregress



def draw_plot():

    df = pd.read_csv("epa-sea-level.csv")
    df.fillna(method="ffill", inplace=True)

    lin = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
   
    fit_line = lin.slope*df["Year"] + lin.intercept
    plt.scatter(df["Year"],df["CSIRO Adjusted Sea Level"],label="CSIRO Adjusted Sea Level")
    plt.plot(df["Year"],fit_line,label="best fit line",color="red")
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.title("Rise in Sea Level")
    plt.legend()

    return plt.gca()

def draw_predict():

    df = pd.read_csv("epa-sea-level.csv")
    df.fillna(method="ffill", inplace=True)

    df_new = df[df["Year"]>=2000]
    lin2 = linregress(df_new["Year"],df_new["CSIRO Adjusted Sea Level"])

    predict = np.arange(2000,2051)
    fit_line2 = (lin2.slope * predict) + lin2.intercept

    plt.scatter(df_new["Year"],df_new["CSIRO Adjusted Sea Level"],label="CSIRO Adjusted Sea Level")
    plt.plot(predict,fit_line2,label="best fit line",color="orange")
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.title("Sea Level Rise predictions to 2050")
    plt.legend()

    return plt.gca()

