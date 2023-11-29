#Librerías
#!pip install nfl-data-py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# import nfl_data_py as nfl
import seaborn as sns
import warnings
import os
from scipy.stats import chi2_contingency
warnings.filterwarnings("ignore")
# ----------
# Functions
def colums_lower(df):
        df.columns = df.columns.str.lower()
        return df
        #Limpieza de datos

# ----------