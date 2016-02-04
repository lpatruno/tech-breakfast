"""
Function to load the adult data set data and create the 0,1 class labels
"""
import pandas as pd


def load_df():
    """
    Returns the adult data set with 0,1 class labels in a pandas DataFrame
    """
    OBJECT = 'object'
    
    columns = ['age', 'workclass', 'fnlwgt', 'education', 'education-num', 
               'marital-status', 'occupation', 'relationship', 'race', 'sex', 
               'capital-gain', 'capital-loss', 'hours-per-week', 'native-country', 'label']
    
    categorical_data = {
            'workclass': OBJECT,
            'education': OBJECT,
            'marital-status': OBJECT,
            'occupation': OBJECT,
            'relationship': OBJECT,
            'race': OBJECT, 
            'sex': OBJECT, 
            'native-country': OBJECT, 
        }
    
    # Load the data as a dataframe, setting categorical columns to type object
    df = pd.read_csv('adult.data', names=columns, dtype=categorical_data, skipinitialspace=True)
    
    # Use 0 and 1 as class labels
    df.loc[ df['label'] == '<=50K', 'class'] = 0
    df.loc[ df['label'] == '>50K', 'class'] = 1
    
    # Force class data type to int
    df['class'] = df['class'].astype(int)
    
    # Drop the previous class label
    df.drop('label', axis=1, inplace=True)
    
    return df
    

if __name__ == '__main__':
    
    df = adult_data()
    print(df.describe())