'''
Fill each each function stub (i.e., replace the "pass") according to the
docstring. To run the unit tests make sure you are in the root
dir:assessment-day1. Then run the tests with the command "make test"
'''
import numpy as np
import pandas as pd
from scipy import stats
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

# Pandas / NumPy
def only_positive(arr):
    '''
    INPUT: 2 DIMENSIONAL NUMPY ARRAY
    OUTPUT: 2 DIMENSIONAL NUMPY ARRAY

    Return a numpy array containing only the rows from arr where all the values
    in that row are positive.

    E.g.  np.array([[1, -1, 2],
                    [3, 4, 2],
                    [-8, 4, -4]])
              ->  np.array([[3, 4, 2]])

    Use numpy methods to do this, full credit will not be awarded for a python
    for loop.
    '''
    pass



# Statistics
def calculate_t_test(sample1, sample2, type_I_error_rate):
    '''
    INPUT: NUMPY ARRAY, NUMPY ARRAY
    OUTPUT: FLOAT, BOOLEAN

    You are asked to evaluate whether the two samples come from a population
    with the same population mean.  Return a tuple containing the p-value for
    the pair of samples and True or False depending if the p-value is
    considered significant at the provided Type I Error Rate (i.e. false
    positive rate, i.e. alpha).
    '''
    pass


def calculate_clickthrough_prob(clicks_A, views_A, clicks_B, views_B):
    '''
    INPUT: INT, INT, INT, INT
    OUTPUT: FLOAT

    Calculate and return an estimated probability that SiteA performs better
    (has a higher click-through rate) than SiteB.

    Hint: Use Bayesian A/B Testing (use 'beta' from scipy.stats)
    '''
    pass


# Linear Regression
def linear_regression(X_train, y_train, X_test, y_test):
    '''
    INPUT: 2 DIMENSIONAL NUMPY ARRAY, NUMPY ARRAY
    OUTPUT: TUPLE OF FLOATS, FLOAT

    The R^2 statistic, also known as the coefficient of determination, is a
    popular measure of fit for a linear regression model.  If you need a
    refresher, this wikipedia page should help:

    https://en.wikipedia.org/wiki/Coefficient_of_determination

    Use the sklearn LinearRegression to find the best fit line for X_train and
    y_train. Calculate the R^2 value for X_test and y_test.

    Return a tuple of the coefficients and the R^2 value. Your returned data
    should be in this form:
    (12.3, 9.5), 0.567
    '''
    pass



# For each of these, your python function should return a string that is the
# SQL statement which answers the question.  
#
# For example:
#    
#    return "SELECT * FROM farmersmarkets;"
#
# You may want to test your queries using sqlite3 or postgresql.  Both
# databases - markets.sqlite (sqlite3) and markets.sql (postgreSQL) are in the
# dsi-assessment-day1/data directory.  Testing your queries with sqlite3 or
# postgresql is optional.  See the SQL instructions in the README.md if you
# want to do this.
#
# There are two tables in the database with these columns:
#
# statepopulations: state, pop2010, pop2000
#
# farmersmarkets: FMID, MarketName, Website, Street, City,
#    County, State, WIC, WICcash
#    (plus other columns we don't care about for this exercise)
#
# Note: FMID is a unique id for the farmers market.  WIC is a boolean varaible
# that indicates if the market accepts payments from the WIC government
# program.   WICCash is another boolean for a slightly different program.
# ---------------------------------------------------------------------------------------------------------

def windsor_markets():
    '''
    Return a SQL statement which gives the number of unique markets owned by the "Windsor"
    family (Hint: The Windsor name is in some of the columns)
    '''
    # Your code should look like this:
    # return '''SELECT * FROM universities;'''

    return '''your query here '''


def very_specific_market():
    '''
    Return a SQL statement which returns the specified county, zip & marketname for the
    farmers market that meets the following requirements: 
        - Within a state who's population from 2000 to 2010 has decreased
        - From the county with the 3rd highest total number of unique markets (by name)
        - 5th market ordered by name alphabetically in reverse (Z-->A)
    '''
    # Your code should look like this:
    # return '''SELECT * FROM universities;'''

    # NEED TO COMPLETE
    return '''your query here '''

