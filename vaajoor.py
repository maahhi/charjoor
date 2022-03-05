import pandas as pd
import numpy as np


df = pd.read_csv('a5.csv')
rand = np.random.randint(len(df))
answer = df.iloc[rand]
letters = {'آ', 'ئ', 'ا', 'ب', 'ت', 'ث', 'ج', 'ح', 'خ', 'د', 'ذ', 'ر', 'ز', 'س', 'ش', 'ص', 'ض', 'ط', 'ظ', 'ع', 'غ', 'ف', 'ق', 'ل', 'م', 'ن', 'ه', 'و', 'پ', 'چ', 'ژ', 'ک', 'گ', 'ی'}
replacements = {'آ':'ا'}
