import pandas as pd
import numpy as np


def cols_to_log(df, columns):
    """Transform column data with log and return new columns of prefixed data.

    For us with data where the column values do not include zeroes.

    Args: 
        df: Pandas dataframe.
        columns: List of columns to transform.

    Returns: 
        Original dataframe with additional prefixed columns.
    """

    for col in columns:
        df['log_'+col] = np.log(df[col])

    return df


def cols_to_log1p(df, columns):
    """Transform column data with log+1 and return new columns of prefixed data. 
    
    For use with data where the column values include zeroes. 

    Args: 
        df: Pandas dataframe.
        columns: List of columns to transform.

    Returns: 
        Original dataframe with additional prefixed columns.
    """

    for col in columns:
        df['log1p_'+col] = np.log(df[col]+1)

    return df


def cols_to_log_max_root(df, columns):
    """Convert data points to log values using the maximum value as the log max and return new columns of prefixed data. 
    
    For use with data where the column values include zeroes. 

    Args: 
        df: Pandas dataframe.
        columns: List of columns to transform.

    Returns: 
        Original dataframe with additional prefixed columns.
    """

    for col in columns:
        log_max = np.log(df[col].max())
        df['logmr_'+col] = df[col] ** (1 / log_max)

    return df


def cols_to_tanh(df, columns):
    """Transform column data with hyperbolic tangent and return new columns of prefixed data. 
    
    Args: 
        df: Pandas dataframe.
        columns: List of columns to transform.

    Returns: 
        Original dataframe with additional prefixed columns.
    """

    for col in columns:
        df['tanh_'+col] = np.tanh(df[col])

    return df


def cols_to_sigmoid(df, columns):
    """Convert data points to values between 0 and 1 using a sigmoid function and return new columns of prefixed data. 
    
    Args: 
        df: Pandas dataframe.
        columns: List of columns to transform.

    Returns: 
        Original dataframe with additional prefixed columns.
    """
    
    for col in columns:
        e = np.exp(1)
        y = 1 / (1+e**(-df[col]))
        df['sig_'+col] = y

    return df


def cols_to_cube_root(df, columns):
    """Convert data points to their cube root value so all values are between 0-1 and return new columns of prefixed data. 
    
    Args: 
        df: Pandas dataframe.
        columns: List of columns to transform.

    Returns: 
        Original dataframe with additional prefixed columns.
    """
    
    for col in columns:
        df['cube_root_'+col] = df[col] ** (1/3)

    return df


def cols_to_cube_root_normalize(df, columns):
    """Convert data points to their normalized cube root value so all values are between 0-1 and return new columns of prefixed data. 
    
    Args: 
        df: Pandas dataframe.
        columns: List of columns to transform.

    Returns: 
        Original dataframe with additional prefixed columns.
    """
    
    for col in columns:
        df['cube_root_'+col] = (df[col] - df[col].min()) / (df[col].max() - df[col].min()) ** (1/3)

    return df

def cols_to_percentile(df, columns):
    """Convert data points to their percentile linearized value and return new columns of prefixed data. 
    
    Args: 
        df: Pandas dataframe.
        columns: List of columns to transform.

    Returns: 
        Original dataframe with additional prefixed columns.
    """
    for col in columns:
        df['pc_lin_'+col] = df[col].rank(method='min').apply(lambda x: (x-1) / len(df[col])-1)

    return df


def cols_to_normalize(df, columns):
    """Convert data points to values between 0 and 1 and return new columns of prefixed data.
    
    Args: 
        df: Pandas dataframe.
        columns: List of columns to transform.

    Returns: 
        Original dataframe with additional prefixed columns.
    """
    
    for col in columns:
        df['norm_'+col] = (df[col] - df[col].min()) / (df[col].max() - df[col].min())

    return df


def cols_to_log1p_normalize(df, columns):
    """Transform column data with log+1 normalized and return new columns of prefixed data. 
    
    For use with data where the column values include zeroes. 

    Args: 
        df: Pandas dataframe.
        columns: List of columns to transform.

    Returns: 
        Original dataframe with additional prefixed columns.
    """

    for col in columns:
        df['log1p_norm_'+col] = np.log((df[col] - df[col].min()) / (df[col].max() - df[col].min())+1)

    return df


def cols_to_one_hot(df, columns):
    """One hot encode column values and return new prefixed columns.
    
    Args: 
        df: Pandas dataframe.
        columns: List of columns to transform.

    Returns: 
        Original dataframe with additional prefixed columns.
    """
    
    for col in columns:
        encoding = pd.get_dummies(df[col], prefix=col)
        df = pd.concat([df, encoding], axis=1)
        
    return df


def cols_to_reduce_uniques(df, column_threshold_dict):
    """Reduce the number of unique values by creating a column of X values and the rest marked "Others".
    
    Args: 
        df: Pandas dataframe.
        columns: Dictionary of column and threshold, i.e. {'col1' : 1000, 'col2' : 3000}

    Returns: 
        Original dataframe with additional prefixed columns. The most dominant values in the column will
        be assigned their original value. The less dominant results will be assigned to Others, which can
        help visualise and model data in some cases.
    """
    
    for key, value in column_threshold_dict.items():
            counts = df[key].value_counts()
            others = set(counts[counts < value].index)
            df['reduce_'+key] = df[key].replace(list(others), 'Others')
            
    return df


def get_grouped_stats(df, group, column):
    """Group by a column and return summary statistics for a given column in new columns.

    Args:
        df: Pandas dataframe.
        group: Column name to groupby
        column: Column to summarise.

    Returns:
        Original dataframe with new column containing previous value of named column.

    """

    df['mean_' + column] = df.groupby([group])[column].transform('mean')
    df['median_' + column] = df.groupby([group])[column].transform('median')
    df['std_' + column] = df.groupby([group])[column].transform('std')
    df['max_' + column] = df.groupby([group])[column].transform('max')
    df['min_' + column] = df.groupby([group])[column].transform('min')

    return df


def get_previous_value(df, group, column, name):
    """Group by a column and return the previous value of another column and assign value to a new column.

    Args:
        df: Pandas dataframe.
        group: Column name to groupby
        column: Column value to return.
        name: Name for new column.

    Returns:
        Original dataframe with new column containing previous value of named column.

    """
    df[name] = df.groupby([group])[column].shift().notnull().astype(int)
    return df


def get_dates(df, date_column):
    """Converts a given date to various formats and returns an updated dataframe.

    Args:
        df: Pandas dataframe.
        columns: List of columns to transform.

    Returns:
        Original dataframe with additional date columns.
    """

    df['day'] = df[date_column].dt.strftime("%d")  # Day of month with leading zero
    df['month'] = df[date_column].dt.strftime("%m")  # Month of year with leading zero
    df['year'] = df[date_column].dt.strftime("%Y")  # Full numeric four digit year
    df['year_month'] = df[date_column].dt.strftime("%Y%m")  # Full numeric four digit year plus month
    df['week_number'] = df[date_column].dt.strftime("%U")  # Week number with leading zero
    df['day_number'] = df[date_column].dt.strftime("%j")  # Day number with leading zero
    df['day_name'] = df[date_column].dt.strftime("%A")  # Day name, i.e. Sunday
    df['month_name'] = df[date_column].dt.strftime("%B")  # Month name, i.e. January
    df['mysql_date'] = df[date_column].dt.strftime("%Y-%d-%m")  # MySQL date, i.e. 2020-30-01

    return df

