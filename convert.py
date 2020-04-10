import pandas as pd


def cols_to_slugify(df, columns):
    """Slugify selected column values and return dataframe.

    Args: 
        df: Pandas dataframe.
        columns: List of columns to convert.

    Returns: 
        Original dataframe with converted column data.
    """

    for col in columns:
        df[col] = df[col].str.replace('[^0-9a-zA-Z]+', '_', regex=True)

    return df


def cols_to_float(df, columns):
    """Convert selected column values to float and return dataframe.

    Args: 
        df: Pandas dataframe.
        columns: List of columns to convert.

    Returns: 
        Original dataframe with converted column data.
    """

    for col in columns:
        df[col] = df[col].astype(float)

    return df


def cols_to_int(df, columns):
    """Convert selected column values to int and return dataframe.

    Args: 
        df: Pandas dataframe.
        columns: List of columns to convert.

    Returns: 
        Original dataframe with converted column data.
    """

    for col in columns:
        df[col] = df[col].astype(int)

    return df


def cols_to_datetime(df, columns):
    """Convert selected column values to datetime and return dataframe.

    Args: 
        df: Pandas dataframe.
        columns: List of columns to convert.

    Returns: 
        Original dataframe with converted column data.
    """

    for col in columns:
        df[col] = pd.to_datetime(df[col])

    return df


def cols_to_negative(df, columns):
    """Convert selected column values to negative and return dataframe.

    Args: 
        df: Pandas dataframe.
        columns: List of columns to convert.

    Returns: 
        Original dataframe with converted column data.
    """

    for col in columns:
        df[col] = df[col] * -1

    return df


def num_to_Cat(df, column, labels, bins):
    """

    :return:
    """
    try:
        df[column] = pd.cut(df[column], bins=bins, labels=labels)
    except Exception as e:
        print("Unexpected error :", e)
        raise ValueError()

    return df


def cat_to_cat(df, column, dict):
    """
     non-exhaustive mapping : retains the existing variables for non-matches,  add fillna

    :param df:
    :param column:
    :param dict:
    :return:
    """
    try:
        df[column] = df[column].map(dict)
    except Exception as e:
        print("Unexpected error :", e)
        raise ValueError()

    return df
