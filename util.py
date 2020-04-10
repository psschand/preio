
#General functions

def checkNull(df, columnName, acceptableAmount):

    """

     # Run QA checks to confirm data population
    isNameValid = checkNull(df,'full_name',.9)
    isAgeValid = checkNull(df,'age',.9)
    isGenderValid = checkNull(df,'gender',1)

    :param df:
    :param columnName:
    :param acceptableAmount:
    :return:
    """
    acceptableQuality = False
    nullPercent = df[columnName].isnull().sum() / df[columnName].count()
    if nullPercent >= acceptableAmount:
        acceptableQuality = True

    return acceptableQuality


def swap_col(df,A,B):
    """

    :param df:
    :param A:
    :param B:
    :return:
    """
    df.loc[:, [B, A]] = df[[A, B]].to_numpy()

    return df

#Generic Functions for validation

def valid_date_format(date):
    """Validates a general date by making sure it is 8 digits long, are only digits and the year can only contain a 2 or 1 in the front (to exlude 0123,3000,4000)

    Args:
        date:str
    Returns:
        returns Boolean
    """
    if (len(date)==8 and date.isdigit() and (date[0]=="2" or date[0]=="1")):
        return True
    else:
        return False

def no_spaces(field):
    """Validates that there are no spaces in a string

    Args:
        field:str
    Returns:
        returns Boolean
    """
    if (' ' in field) == True:
        return(False)
    else:
        return(True)


def title_case(field):
    """Validates that as sting is title case
    Args:
        field:str
    Returns:
        returns Boolean
    """
    if (field.istitle()):
        return(True)
    else:
        return(False)


def is_greater_than(field,notgreaterthanthis):
    """Validates that a field length is not greater than the notgreaterthanthis value.

    Args:
        field:str
        notgreaterthanthis: int
    Returns:
        returns Boolean
    """
    if len(field) > notgreaterthanthis:
        return(False)
    else:
        return(True)
#Generic Functions for Normalisation

def normalize_date(date):
        """Removes non digits and joins numbers together

        Args:
            date:str
        Returns:
            returns str
        """
        whitelist = set('0123456789')
        normalized_date = ''.join(filter(whitelist.__contains__, date))
        return(str(normalized_date))

def remove_spaces(string):
        """Removes spaces

        Args:
            string:str
        Returns:
            returns str
        """
        string = string.replace(" ", "")
        return str(string)

def title_case(string):
         """makes string title case

         Args:
             string:str
         Returns:
             returns str
         """
         string = string.lower().title()
         return string

def remove_suffix(string):
          """Removes suffixes

          Args:
              string:str
          Returns:
              returns str
          """
          suffixes = ["Esq", "Ii", "Iii", "Iiii", "Iv", "Jnr", "Jr", "Sr"]
          string = string.replace(" ", "")
          string = string.replace(".", "")
          string = string.replace(",", "")
          for suffix in suffixes:
                  if(string.endswith(suffix)):
                          string = string[:-len(suffix)]
                          return(string)
          return(string)


#Generic Functions

def normalize_date(date):
        """Removes non digits and joins numbers together

        Args:
            date:str
        Returns:
            returns str
        """
        whitelist = set('0123456789')
        normalized_date = ''.join(filter(whitelist.__contains__, date))
        return(str(normalized_date))

def remove_spaces(string):
        """Removes spaces

        Args:
            string:str
        Returns:
            returns str
        """
        string = string.replace(" ", "")
        return str(string)

def title_case(string):
         """makes string title case

         Args:
             string:str
         Returns:
             returns str
         """
         string = string.lower().title()
         return string

def remove_suffix(string):
          """Removes suffixes

          Args:
              string:str
          Returns:
              returns str
          """
          suffixes = ["Esq", "Ii", "Iii", "Iiii", "Iv", "Jnr", "Jr", "Sr"]
          string = string.replace(" ", "")
          string = string.replace(".", "")
          string = string.replace(",", "")
          for suffix in suffixes:
                  if(string.endswith(suffix)):
                          string = string[:-len(suffix)]
                          return(string)
          return(string)
      
def print_hi():
    print("Hiyaa")      
