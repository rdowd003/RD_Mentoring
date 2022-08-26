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
    return arr[arr[:,:] > 0]


def calculate_clickthrough_prob(clicks_A, views_A, clicks_B, views_B):
    '''
    INPUT: INT, INT, INT, INT
    OUTPUT: FLOAT

    Calculate and return an estimated probability that SiteA performs better
    (has a higher click-through rate) than SiteB.

    Hint: Use Bayesian A/B Testing (use 'beta' from scipy.stats)
    '''
    rv1 = stats.beta(1+clicks_A,1+views_A-clicks_A)
    rv2 = stats.beta(1+clicks_B,1+views_B-clicks_B)
    return sum(rv1>rv2)


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
    model = LinearRegression()
    model.fit(X_train, y_train)
    test_predicted = model.predict(X_test)
    score = r2_score(y_test,test_predicted)

    return ((model.coef_[1]),score)



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

    return '''SELECT count(distinct marketname) FROM farmersmarkets WHERE website like '%thewindsorfarmersmarket%';'''


def decreased_pop_markets():
    '''
    Return a SQL statement which gives the number of unique markets owned by the "Windsor"
    family (Hint: The Windsor name is in some of the columns)
    '''
    # Your code should look like this:
    # return '''SELECT * FROM universities;'''

    # NEED TO COMPLETE
    return '''SELECT zip,COUNT(DISTINCT marketname) FROM farmersmarkets JOIN statepopulations USING(state) WHERE pop2010 < pop2000);
49464|318;'''
