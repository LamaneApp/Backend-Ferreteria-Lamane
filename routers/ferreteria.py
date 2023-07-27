import pandas as pd

def read_file(file):
    dataFrame = pd.read_excel(file)
    lectura = dataFrame.to_dict()