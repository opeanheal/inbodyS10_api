import pandas as pd
import numpy as np
from classes.Bio import Bio

class BioData():

  def __init__(self, path):
    self.path = path
    self.df = self.read_S10_file()
  
  def read_S10_file(self):
    df = pd.read_csv(self.path)
    return df

  def filter(self, filter_by_id):
    df = self.df[['1.DATE&TIMES','2.ID']]
    filtered = df.loc[df['2.ID'] == filter_by_id]
    return filtered

  def list(self):
    return self.df[['1.DATE&TIMES', '2.ID']]

  def list_by_name(self):
    return np.array(self.list().sort_values(by=['2.ID']))

  def list_by_index(self):
    return np.array(self.list().sort_index().reset_index())

  def to_dictionary(self, index):
    return self.df.iloc[[index]].to_dict('records')[0]

  def create_array_of_bios(self, indexes):# indexes is an array of indexes
      return [Bio(self.to_dictionary(i)) for i in indexes]