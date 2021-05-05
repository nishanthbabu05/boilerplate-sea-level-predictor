import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress


def draw_plot():
    # Read data from file
    df=pd.read_csv('epa-sea-level.csv')
    df_n=df.loc[df['Year']>=2000]
    x=pd.Series(list(range(1880, 2051)))
    y=pd.Series(list(range(2000, 2051)))
    res = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    re=linregress(df_n['Year'], df_n['CSIRO Adjusted Sea Level'])
    p=res.intercept + res.slope*x
    q=re.intercept + re.slope*y

    # Create scatter plot
    plt.scatter( data=df,x='Year', y='CSIRO Adjusted Sea Level')
    plt.xticks(pd.Series(list(range(1850, 2100,25)),dtype='float'))

    # Create first line of best fit   
    
    plt.plot(x,p,'b')
    


    # Create second line of best fit    
    
    plt.plot(y,q,'r')


    # Add labels and title
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.title("Rise in Sea Level")
    

    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
