'''
Fill each each function stub (i.e., replace the "pass") according to the
docstring. To run the unit tests make sure you are in the root
dir:assessment-day1. Then run the tests with the command "make test"
'''
import numpy as np
import pandas as pd
from collections import Counter


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
    return Counter(string)


	    

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
    
    return {v: k for k, v in d.items()}



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
    # I had to look up the open syntax
    f = open(filename, 'r')
    data = f.read()
    lines = len(f.readlines())
    words = len(data.split(' '))
    chars = len(data)

    return (lines, words, chars)



# ---------------------------------------------------------------------------------------------------------
# Python Challenge
# ---------------------------------------------------------------------------------------------------------


# Medium hard
from sklearn.metrics import f1_score
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
    preds = np.array(preds)
    actual = np.array(actual)
    tp = (preds==actual)&(actual==1)
    fp = (preds!=actual)&(actual==0)
    tn = (preds==actual)&(actual==0)
    fn = (preds!=actual)&(actual==1)
    
    recall = np.round(tp/(tp+fn),2)
    precision = np.round(tp/(tp+fp),2)
    accuracy = np.round((tp + tn)/len(preds),2)

    return precision,recall,accuracy


# Note: This one is very challenging & not particularly short (it's okay if you do not get this)
def num_to_word_string(number):
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
    my_dict = {10:'ten', 11:'twenty'}

    pass
    if number>=1 and number<=1000:
        a = ['','one','two','three','four','five','six','seven','eight','nine','ten',
         'eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen',
         'eighteen','nineteen','twenty ','thirty ','fourty ','fifty ','sixty ','seventy ','eighty ','ninty ']
        if number<=20:
            if number%10==0: return a[number]
            else: return a[number]
        elif number<100:
            b=number-20
            r=b%10
            b//=10
            return a[20+b]+a[r]
        elif number<1000:
            if number%100==0:
                b=number//100
                return a[b]+' hundred'
            else:
                r=number%100
                b=number//100
                if r<=20:
                    return a[b]+' hundred'+' and '+a[r]
                else:
                    r=r-20
                    d=r//10
                    r%=10
                    return a[b]+' hundred'+' and '+a[20+d]+a[r]
        elif number==1000:
            return 'one thousand'
        else:
            return -1   


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
    return (a * 0.5)/a


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
    total_reward = 0
    keys = list(reward_dict.keys())
    run_dtns = np.random.random(size=runs)
    for index,dtn in enumerate(run_dtns):
        if dtn < episilon:
            choice = np.random.choice(keys)
            total_reward += reward_dict[choice][index]
        else:
            temp_rewards = [reward_dict[key][index] for key in keys]
            total_reward += max(temp_rewards)


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
    return np.matmul(np.full((rows, cols), scalar), matrixA)



def data_frame_easy(df, colA, colB, colC):
    '''
    INPUT: DATAFRAME, STR, STR, STR
    OUTPUT: None

    Insert a column (colC) into the dataframe that is the sum of colA and colB.
    Assume that df contains columns colA and colB and that these are numeric.
    '''
    df[colC] = df[colA] + df[colB]
    


def data_frame_med(df, colA, win, min_val):
    '''
    INPUT: DATAFRAME, STR, INT, INT
    OUTPUT: None

    Insert a column (colB) into the dataframe that computes a rolling sum on
    colA, with a window size (win) and a minimum (min_val) number of
    values in the window required to compute the rolling sum
    '''
    # I don't think i've ever done this so I had to look this up
    df['colB'] = df[colA].rolling(win, min_periods=min_val).sum()


def data_frame_hard(df, colA, colB, function_x):
    '''
    INPUT: DATAFRAME, STR, STR, STR
    OUTPUT: None

    Insert a column (colC) into the dataframe that maps function_x, which takes
    colA & colB as input.
    '''
    df['colC'] = df.apply(lambda x: function_x(x[colA], x[colB]), axis=1)



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
    return '''SELECT state, sum(case when wic = 'Y' then 1 when wiccash = 'Y' then 1 else 0 end) AS wictrue FROM farmersmarkets GROUP BY 1;'''
    # Your code should look like this:
    # return '''SELECT * FROM universities;'''


def state_population_gain():
    '''
    Return a SQL statement which gives the 10 states with the highest
    population gain from 2000 to 2010.
    '''
    return '''SELECT state, (pop2010 - pop2000) AS change FROM statepopulations ORDER BY change DESC LIMIT 10;'''
    
    # Your code should look like this:
    # return '''SELECT * FROM universities;'''


def farmers_wine_and_honey():
    '''
    Return a SQL statement which gives the name of the county
    with the greatest number of cities that sell wine & honey,
    and the count of cities.
    '''
    
    return '''SELECT county, COUNT(city) as num_cities FROM farmersmarkets GROUP BY county ORDER BY num_cities DESC LIMIT 1;'''

    
    # Your code should look like this:
    # return '''SELECT * FROM universities;'''


def mad_cheese_markets():
    '''
    Return a SQL statement which returns the state, county with the 
    most amount of farmers markets that sell cheese, and have at least
    20+ markets selling cheese
    '''

    return '''SELECT state,county,count(distinct fmid) c FROM farmersmarkets WHERE cheese = 'Y' GROUP BY 1 HAVING c > 20 ORDER BY c DESC LIMIT 3;'''
    # Your code should look like this:
    # return '''SELECT * FROM universities;''' 


