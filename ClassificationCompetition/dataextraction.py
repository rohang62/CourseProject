import numpy as np
import pandas as pd
import json

def extract_data(filename):
    data = []
    with open(filename,'r') as file:
        for line in file:
            data.append(line)
    return data

def parse_json(data, train):
    df = None
    if train:
        df = pd.DataFrame(columns = ['label', 'response'])
    else:
        df = pd.DataFrame(columns = ['id', 'response'])
    for i in data:
        dict = json.loads(i)
        l = list(dict.values())
        context = l.pop()
#         context_s = context[0]
#         for i in range(1, min(len(context), 2)):
#             context_s += " " + context[i]
#         l[1] += " " + context_s
        tmp = pd.DataFrame([l], columns = list(df.columns))
        df = df.append(tmp)
    return df
