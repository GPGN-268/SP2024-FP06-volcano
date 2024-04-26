import numpy as np
import pandas as pd

def get_year(date_str):
    '''
    Gets the year from a date-time string (DD-Mon-YYYY HH:MM:SS) <- this is the format of dates and times for the thermal data in this project.
    These date-time strings are indices in the dataframe that contains the thermal data.
    
    Input:
        date_str (str) - a date-time string in the form 'DD-Mon-YYYY HH:MM:SS'
        
    Returns:
        int - the year from the date-time string
    '''
    
    year = date_str[7:11]
    return int(year)

def get_month(date_str):
    '''
    Gets the month and year from a date-time string (DD-Mon-YYYY HH:MM:SS) <- this is the format of dates and times for the thermal data in this project.
    These date-time strings are indices in the dataframe that contains the thermal data.
    
    Input:
        date_str (str) - a date string in the form 'DD-Mon-YYYY HH:MM:SS'
        
    Returns:
        str - the month and year from the date string in the form 'Mon-YYYY'
    '''
    
    return date_str[3:11]

def check_different_month(df, date_str):
    '''
    Reads a date-time string (an index of the dataframe containing our thermal data), checking if the month is the same as the month of the previous string.
    This function is used in taking monthly averages of variables.
    
    Input:
        df (dataframe) - the dataframe containing date_str as its indices
        date_str (str) - a date string in the form 'DD-Mon-YYYY HH:MM:SS' that is an index in df
        
    Returns:
        Boolean - True if the month from date_str is different from the one before it in df, or if date_str is the first index of df
    '''
    
    return df.index.get_loc(date_str) == 0 or get_month(df.index[df.index.get_loc(date_str)]) != get_month(df.index[df.index.get_loc(date_str) - 1])

def check_different_year(df, date_str):
    '''
    Reads a date-time string (an index of the dataframe containing our thermal data), checking if the year is the same as the year of the previous string.
    This function is used in taking yearly averages of variables.
    Input:
        df (dataframe) - the dataframe containing date_str as its indices
        date_str (str) - a date string in the form 'DD-Mon-YYYY HH:MM:SS' that is an index in df
        
    Returns:
        Boolean - True if the year from date_str is different from the one before it in df, or if date_str is the first index of df
    '''
    
    return df.index.get_loc(date_str) == 0 or get_year(df.index[df.index.get_loc(date_str)]) != get_year(df.index[df.index.get_loc(date_str) - 1])

def monthly_avg(df, var):
    '''
    Calculates the mean of a chosen variable for each month during which thermal data were collected.
    
    Input:
        df (dataframe) - the dataframe containing the variable to average
        var (str) - the name of the variable to average. Must be a column name in df
        
    Returns:
        Series - the mean of var in each month, with months as indices
    '''
    
    A = {}
    for date_str in df.index:
        if(check_different_month(df, date_str)):
            var_list = [df[var][date_str]]
            c = 1
            m0 = get_month(date_str)
            m1 = get_month(df.index[df.index.get_loc(date_str) + c])
            while(m1 == m0):
                var_list.append(df[var][df.index[df.index.get_loc(date_str) + c]])
                if(df.index.get_loc(date_str)+c == len(df)-1):
                    break
                else:
                    m1 = get_month(df.index[df.index.get_loc(date_str) + c+1])
                    c += 1
            A[m0] = np.nanmean(var_list)
    monthly_avgs = pd.Series(A)
    return monthly_avgs

def yearly_avg(var):
    '''
    Calculates the mean of a chosen variable for each year during which thermal data were collected.
    
    Input:
        df (dataframe) - the dataframe containing the variable to average
        var (str) - the name of the variable to average. Must be a column name in df
        
    Returns:
        Series - the mean of var in each year, with months as indices
    '''
    
    A = {}
    for date_str in df.index:
        if(check_different_year(df, date_str)):
            var_list = [df[var][date_str]]
            c = 1
            y0 = get_year(date_str)
            y1 = get_year(df.index[df.index.get_loc(date_str) + c])
            while(y1 == y0):
                var_list.append(df[var][df.index[df.index.get_loc(date_str) + c]])
                if(df.index.get_loc(date_str)+c == len(df)-1):
                    break
                else:
                    y1 = get_year(df.index[df.index.get_loc(date_str) + c+1])
                    c += 1
            A[y0] = np.nanmean(var_list)
    yearly_avgs = pd.Series(A)
    return yearly_avgs

