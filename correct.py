import pandas as pd 


def cols_to_strip_commas(df, columns):
    """Strip commas from selected dataframe columns.

    Args: 
        df: Pandas dataframe.
        columns: List of columns to convert.

    Returns: 
        Original dataframe with converted column data.
    """

    for col in columns:
        df[col] = df[col].str.replace(',','')
        
    return df


def cols_to_drop(df, columns):
    """Drop selected columns and return dataframe.

    Args: 
        df: Pandas dataframe.
        columns: List of columns to drop.

    Returns: 
        Original dataframe without dropped columns.
    """

    for col in columns:
        df.drop([col], axis=1, inplace=True) 

    return df


def col_names_to_lower(df):
    """Convert column names to lowercase and return dataframe.

    Args: 
        df: Pandas dataframe.

    Returns: 
        Original dataframe with converted column data.
    """

    return df.columns.str.lower()


def cols_to_rename(df, dictionary):
    """Drop selected columns and return dataframe.
    
    Args: 
        df: Pandas dataframe.
        dictionary: {'old_name1': 'new_name1', 'old_name2': 'new_name2'}

    Returns: 
        Original dataframe without dropped columns.
    """

    df.rename(dictionary, axis=1, inplace=True)

    return df