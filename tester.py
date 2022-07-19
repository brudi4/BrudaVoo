import pandas as pd

names=['chlorhexidine', 'cyntomycin', 'afobazol']
counts=[15, 18, 7]

def create_medications(names, counts):
    medications = pd.Series(
        index=names, 
        data=counts)
    return medications

medication_list = create_medications(names, counts)

def get_percent(medications_list, medication_name):
    return(medications_list.loc[medication_name] * 100 /sum(medications_list))

print(get_percent(medication_list,'cyntomycin'))