from copyreg import constructor
import pandas as pd
import numpy as np
import matplotlib

class driver:
  def __init__(self):
    self.df = pd.read_csv('./data/GlobalLandTemperaturesByCountry.csv')

  def explore_data(self):
    # Drop null data
    self.cleanData = self.df['AverageTemperature'].dropna(how='any')
    print(self.cleanData.head())
    # print('---------------------------')
    # print('Rows: ' + str(self.df.shape[0]) + ' - Columns: ' + str(self.df.shape[1]))
    # print('---------------------------')
    # print('---------------------------')
    # print(self.df['AverageTemperature'].isnull().values.any())
    # print(self.df['AverageTemperature'].isnull().sum())
    # print('Mean: ')
    print(self.df.mean())

  
dr = driver()

dr.explore_data()
  
