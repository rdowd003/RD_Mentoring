'''
Fill each each function stub (i.e., replace the "pass") according to the
docstring. To run the unit tests make sure you are in the root
dir:assessment-day1. Then run the tests with the command "make test"
'''
import numpy as np
import pandas as pd
import collections


# ---------------------------------------------------------------------------------------------------------
# Python Fluency 
# ---------------------------------------------------------------------------------------------------------

def count_characters(string):
    '''
    INPUT: STRING
    OUTPUT: DICT (with counts of each character in input string)

    Return a dictionary which contains
    a count of the number of times each character appears in the string.
    Characters which with a count of 0 should not be included in the
    output dictionary.
    '''
    pass
    # Insert code here

	    

def invert_dictionary(d):
    '''
    INPUT: DICT
    OUTPUT: DICT (of sets of input keys indexing the same input values
                  indexed by the input values)

    Given a dictionary d, return a new dictionary with d's values
    as keys and the value for a given key being
    the set of d's keys which shared the same value.
    e.g. {'a': 2, 'b': 4, 'c': 2} => {2: {'a', 'c'}, 4: {'b'}}
    '''
    pass
    # Insert code here



def word_count(filename):
    '''
    INPUT: STRING
    OUTPUT: INT, INT, INT (a tuple with line, word,
                           and character count of named INPUT file)

    The INPUT filename is the name of a text file.
    The OUTPUT is a tuple containting (in order)
    the following stats for the text file:
      1. number of lines
      2. number of words (broken by whitespace)
      3. number of characters
    '''

    pass
    # Insert code here


# ---------------------------------------------------------------------------------------------------------
# Python Challenge
# ---------------------------------------------------------------------------------------------------------


# Medium hard
def classifier_eval(preds,actual):
    '''
    INPUT: LISTS
    OUTPUT: TUPLE 

    The INPUT is:
        - Preds: List len(n) of 1s and zeros reflecting prediction labels output by model
        - actual List len(n) of 1s and zeros reflecting actual data point labels 
    The OUTPUT is a Tuple with classifier scorig metrics rounded to the nearest 1/10 th, in the following order:
        - precision
        - recall
        - accuracy
    For example:
        - INPUT
            - preds  = [0,0,0,1,0,0,0,0,0,1,0,0,1,1]
            - actual = [1,0,0,1,0,1,0,0,0,1,1,0,1,0]
        - OUTPUT: 
            return (precision,recall,accuracy)
                precision = 0.95
                recall = 0.83
                accuracy = 0.85

    '''

    pass
    # Insert code here 


# Note: This one is very challenging & not particularly short (it's okay if you do not get this)
def num_to_word_string(n):
    '''
    INPUT: INTEGER
    OUTPUT: STRING 

    The INPUT is aninteger of ANY size.
    The OUTPUT is a string version of the word in English.
    For example:
        - INPUT = 1,342
        - OUTPUT: One thousand three hundred and forty two"
    Note: Do not worry about punctuation & capitalization
    '''

    pass
    # Insert code here   


# ---------------------------------------------------------------------------------------------------------
# Statistics & Probability
# ---------------------------------------------------------------------------------------------------------


def cookie_jar(a, b):
    '''
    INPUT: FLOAT (probability of drawing a chocolate cooking from Jar A),
            FLOAT (probability of drawing a chocolate cooking from Jar B)
    OUTPUT: FLOAT (conditional probability that cookie was drawn from Jar A
                   given that a chocolate cookie was drawn)

    There are two jars of cookies.
    Each has chocolate and peanut butter cookies.
    INPUT 'a' is the fraction of cookies in Jar A which are chocolate
    INPUT 'b' is the fraction of cookies in Jar B which are chocolate
    A jar is chosen at random and a cookie is drawn.
    The cookie is chocolate.
    Return the probability that the cookie came from Jar A.
    '''
    pass
    # Insert code here


def mab_slots(reward_dict,episilon,seed,runs):
    '''
    INPUT: 
        - df: dictionary
        - episilon: INTEGER
        - seed: INTEGER
        - runs: INTEGER
    OUTPUT: 
        - INTEGER

    Implement a simple multi-armed bandit testing algorithm for a set of fake
    slot machines. There will be 3 slot machines, and the deciding threshold
    will be (episilon). The function will accept a pyton dictionary where each
    key represents the slot machine name and the values are a list of rewards
    representing the reward gain from that machine for each run. The goal is to 
    return the total sum reward after all trial runs

    INPUT:
        - reward_dict: rows = reward, columns = slot machine
        e.g.: d = {'S1':[0,5,4,6,3],
                   'S2:[1,10,11,4,3],
                   'S3':[2,5,7,2,31]}
        - episilon: value between 0 & 1 (e.g. 0.20)
        - seed: value between 1 and 100 (e.g. 4) to set numpy random seed
        - runs: total number of runs (loops to iterate) - e.g.: 100
    OUTPUT:
        - total_reward: sum of rewards from each run after total runs

    Note: Assume `runs` ≤ len of lists per slot machine
    Hint: value < epislon = random, else greedy
    '''

    np.random.seed(seed)
    # Insert code here


# ---------------------------------------------------------------------------------------------------------
# Pandas, NumPy & MatplotLib
# ---------------------------------------------------------------------------------------------------------


def array_work(rows, cols, scalar, matrixA):
    '''
    INPUT: INT, INT, INT, NUMPY ARRAY
    OUTPUT: NUMPY ARRAY
    (of matrix product of r-by-c matrix of "scalar"'s time matrixA)

    Create matrix of size (rows, cols) with elements initialized to the scalar
    value. Right multiply that matrix with the passed matrixA (i.e. AB, not
    BA).  Return the result of the multiplication.  You needn't check for
    matrix compatibililty, but you accomplish this in a single line.

    E.g., array_work(2, 3, 5, [[3, 4], [5, 6], [7, 8]])
           [[3, 4],      [[5, 5, 5],
            [5, 6],   *   [5, 5, 5]]
            [7, 8]]
    '''
    pass
    # Insert code here



def data_frame_easy(df, colA, colB, colC):
    '''
    INPUT: DATAFRAME, STR, STR, STR
    OUTPUT: None

    Insert a column (colC) into the dataframe that is the sum of colA and colB.
    Assume that df contains columns colA and colB and that these are numeric.
    '''
    pass
    # Insert code here


def data_frame_med(df, colA, win, min_val):
    '''
    INPUT: DATAFRAME, STR, STR, STR
    OUTPUT: None

    Insert a column (colB) into the dataframe that computes a rolling sum on
    colA, with a window size (win) and a minimum (min_val) number of
    values in the window required to compute the rolling sum
    '''
    pass
    # Insert code here


def data_frame_hard(df, colA, colB, function_x):
    '''
    INPUT: DATAFRAME, STR, STR, STR
    OUTPUT: None

    Insert a column (colC) into the dataframe that maps function_x, which takes
    colA & colB as input.
    '''
    pass
    # Insert code here



# ---------------------------------------------------------------------------------------------------------
# SQL SECTION
# ---------------------------------------------------------------------------------------------------------

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

def markets_per_state():
    '''
    Return a SQL statement which gives the states and a count of the number of
    markets for each state which take WIC or WICcash.
    '''

    pass
    # Your code should look like this:
    # return '''SELECT * FROM universities;'''


def state_population_gain():
    '''
    Return a SQL statement which gives the 10 states with the highest
    population gain from 2000 to 2010.
    '''

    pass
    # Your code should look like this:
    # return '''SELECT * FROM universities;'''


def farmers_wine_and_honey():
    '''
    Return a SQL statement which gives the name of the county
    with the greatest number of cities that sell wine & honey,
    and the count of cities.
    '''

    pass
    # Your code should look like this:
    # return '''SELECT * FROM universities;'''


def mad_cheese_markets():
    '''
    Return a SQL statement which returns the state, county with the 
    most amount of farmers markets that sell cheese, and have at least
    20+ markets selling cheese
    '''

    return '''select state,county,count(distinct fmid) c from farmersmarkets where cheese = 'Y' group by 1 having c > 20 order by c desc limit 3;'''
    # Your code should look like this:
    # return '''SELECT * FROM universities;''' 


