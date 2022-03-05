import pandas as pd
import numpy as np


df = pd.read_csv('a5.csv')
letters = {'آ', 'ئ', 'ا', 'ب', 'ت', 'ث', 'ج', 'ح', 'خ', 'د', 'ذ', 'ر', 'ز', 'س', 'ش', 'ص', 'ض', 'ط', 'ظ', 'ع', 'غ', 'ف', 'ق', 'ل', 'م', 'ن', 'ه', 'و', 'پ', 'چ', 'ژ', 'ک', 'گ', 'ی'}
replacements = {'آ':'ا'}

rand = np.random.randint(len(df))
answer = df.iloc[rand]
ans_list = list(answer)
for i in range(len(ans_list)):
    for k in replacements.keys():
        if ans_list[i] == k:
            ans_list[i] = replacements[k]

guess = input()
