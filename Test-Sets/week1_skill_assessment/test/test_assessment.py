'''
Unit tests for Assessment 1
Usage: from main assessment-day1 directory run: make test
Updated for Python 3 10/28/17
'''

import unittest as unittest
import sqlite3 as sql
import numpy as np
import pandas as pd
from src import assessment as a


def run_sql_query(db, command):
    if not command:
        return []
    con = sql.connect(db)
    c = con.cursor()
    data = c.execute(command)
    return [d for d in data]
    con.close()

class TestAssessment1(unittest.TestCase):

    def test_count_characters(self):
        string = "abafdcggfaabe"
        answer = {"a": 4, "b": 2, "c": 1, "d": 1, "e": 1, "f": 2, "g": 2}
        result = a.count_characters(string)
        self.assertEqual(result, answer)


    def test_invert_dictionary(self):
        d = {"a": 4, "b": 2, "c": 1, "d": 1, "e": 1, "f": 2, "g": 2}
        result = {4: {'a'}, 2: {'b', 'f', 'g'}, 1: {'c', 'd', 'e'}}
        self.assertEqual(a.invert_dictionary(d), result)


    def test_word_count(self):
        self.assertEqual(a.word_count('data/alice.txt'), (17, 1615, 8449))


    def test_cookie_jar(self):
        self.assertEqual(a.cookie_jar(0.2, 0.6), 0.25)


    def test_array_work(self):
        matrixA = np.array([[-4, -2],
                            [ 0, -3],
                            [-4, -1],
                            [-1,  1],
                            [-3,  0]])
        answer1 = np.array([[-24, -24, -24],
                           [-12, -12, -12],
                           [-20, -20, -20],
                           [  0,   0,   0],
                           [-12, -12, -12]])
        result1 = a.array_work(2, 3, 4, matrixA)
        self.assertTrue(np.all(answer1 == result1))

        answer2 = np.array([[-36, -36],
                            [-18, -18],
                            [-30, -30],
                            [  0,   0],
                            [-18, -18]])
        result2 = a.array_work(2, 2, 6, matrixA)
        self.assertTrue(np.all(answer2 == result2))


    def test_data_frame_work(self):
        df = pd.DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6]})
        colA, colB, colC = ('a', 'b', 'c')
        a.data_frame_work(df, colA, colB, colC)
        self.assertTrue(colC in df.columns.tolist())
        self.assertEqual(df[colC].tolist(), [5, 7, 9])


    def test_markets_per_state(self):
        result = run_sql_query('data/markets.sqlite', a.markets_per_state())
        california, maine = None, None
        for item in result:
            if item[0] == 'California':
                california = item[1]
            if item[0] == 'Maine':
                maine = item[1]
        self.assertEqual(california, 340)
        self.assertEqual(maine, 37)


    def test_state_population_gain(self):
        result = run_sql_query('data/markets.sqlite', a.state_population_gain())
        answer = set([u'Georgia', u'Colorado', u'Florida', u'Washington', u'Virginia', u'North Carolina', u'Arizona', \
                      u'California', u'Nevada', u'Texas'])
        self.assertEqual(set([x[0] for x in result]), answer)


if __name__ == '__main__':
    unittest.main()
