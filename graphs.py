import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import tweets as tw
import sentiment as sen
def clean_df(df):
    # Round the DF to one decimal places for plotting of data
    df = df.round({'subjectivity':1, 'polarity':1})

    return df


