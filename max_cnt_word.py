import pandas as pd
import re

df = pd.DataFrame

data = []
with open('movies.csv') as f:
    for i, line in enumerate(f):
        if i > 0:
            title = line.strip().split(',')
            result = re.findall(r'[a-z]+',title[1].lower())
            for word in result:
                data.append(word.lower())
                
df = pd.DataFrame(data, columns=['word'])
df['cnt'] = 1

d = df.groupby('word').sum('cnt')

max_word = d.cnt.max()

d.loc[d['cnt'] == max_word]

-- результат 
the 1540