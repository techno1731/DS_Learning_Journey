#!/usr/bin/env python3

import csv
import pandas as pd
import numpy as np
import statsmodels.api as sm
from statsmodels.graphics.gofplots import qqplot
import seaborn as sns
import collections
import itertools
from matplotlib import pyplot as plt


def get_data(path):
    df = pd.read_csv(path)
    return df


def clean_data(df):
    # Remove duplicate rows
    df.drop_duplicates(inplace=True)
    # Remove rows with duplicated imdb_id
    df.drop_duplicates(subset='imdb_id', inplace=True)
    # Remove columns that have high number of missing values
    # or do not add value to the investigation
    df.drop(columns=['homepage',
                     'tagline',
                     'keywords',
                     'overview', 
                     'production_companies'], inplace=True)
    # Remove rows with missing values
    df.dropna(inplace=True)
    # Remove rows where revenue or budget is unknown, i.e., 0  
    df.drop(df[df['revenue'] == 0.0].index, inplace=True)
    df.drop(df[df['budget'] == 0.0].index, inplace=True)
    return df


def simple_moving_average(df, name_new_col, target_col_num, window=10):
    df[name_new_col] = df.iloc[:,target_col_num].rolling(window=window).mean()
    return df


def exploratory_analysis(df, target):
    print('\nBasic Exploratory Information\n')
    print(f'\nDataFrame Information:\n{df.info()}\n\nDataFrame Head(5):\n{df.head(5)}')
    print(f'\n\n{target} is chosen as the independent variable and the target\
     will be to find what are the varibles that influence it.\n')
    print(f"\nBasic Statistical Information for {target}\n\
            \nMax: {np.amax(df[target])}\
            \nMin: {np.amin(df[target])}\
            \nRange: {np.ptp(df[target])}\
            \nMean: {np.mean(df[target])}\
            \nMedian: {np.median(df[target])}\
            \nMode: {df[target].mode()}\
            \nVariance: {np.var(df[target])}\
            \nStandard Deviation: {np.std(df[target])}\
            \nSkew: {df[target].skew()}\
            \nPercentiles 25, 50, 75 and 95: {np.percentile(df[target], [25, 50, 75, 95])}\
            \nInterquantile Range: {np.percentile(df[target], 75) - np.percentile(df[target], 25)}")
    #Distribution of target variable
    plt.figure(f'Distribution of {target}')
    sns.distplot(df[target], bins=100, kde=False)
    return None

def correlation_visual(df):
    correlation = df.corr()
    figure = plt.figure('Correlation')
    sns.heatmap(correlation, vmin=-1, vmax=1, 
                cmap='coolwarm', annot=True, linewidths=0.5)
    return correlation


def normality_test(df, target):
    qqplot(df[target], line='s')
    return None


def main():
    # Generate DataFrame from CSV file
    path =r'tmdb-movies.csv'
    target = 'revenue_adj'
    df_imdb = clean_data(get_data(path))
    # EDA
    exploratory_analysis(df_imdb, target)
    # question 1
    print('\nWhat are the five most successful movies by revenue_adj: \n')
    print(df_imdb[['original_title','release_year',
                   'revenue_adj']].sort_values(by='revenue_adj', ascending=False).head(5))
    # question 2
    print('\nWhat are the top genres in regards to number of movies made?\n')
    top_genres = collections.Counter(itertools.chain.from_iterable(genre.split('|') for genre in df_imdb['genres'])).most_common()
    for i in range(5):
        print(f"{i+1}°: {top_genres[i]}")
    # qestion 3
    print('\nIs there a correlation between the revenue, and the budget,\
    runtime or vote_avg \n')
    # data aggregation for question 3 
    revenue_col_num = 15
    budget_col_num = 14
    moving_average_revenue = 'sma_revenue'
    moving_average_budget = 'sma_budget'
    df_imdb = simple_moving_average(df_imdb, moving_average_revenue, revenue_col_num)
    df_imdb = simple_moving_average(df_imdb, moving_average_budget, budget_col_num)
    # visual comparison grid for inspecting correlations
    correlation = correlation_visual(df_imdb)
    # Visual normality test for y - can we perform linear parametric regression?
    normality_test(df_imdb, target)
    print(f'{target} does not have gaussian form, thus parametric regression\
    is not easily implemented.')
    # Show all plots
    plt.show()
    return df_imdb

if __name__ == "__main__":
    main()
