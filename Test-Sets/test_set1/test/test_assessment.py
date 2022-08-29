'''
Unit tests for Assessment 1
Usage: from week1 skills assessment directory run: make test
Updated for Python 3 10/28/17
'''

import unittest as unittest
import sqlite3 as sql
import numpy as np
import pandas as pd
from solutions import src_solutions as a


def run_sql_query(db, command):
    if not command:
        return []
    con = sql.connect(db)
    c = con.cursor()
    data = c.execute(command)
    return [d for d in data]
    con.close()


class TestAssessment1(unittest.TestCase):

    def test_only_positive(self):
        arr = np.array([[1, 2, 3], [4, -5, -6], [-7, 8, 9], [10, 11, 12]])
        result = a.only_positive(arr)
        self.assertIsInstance(result, np.ndarray)
        self.assertEqual(result.tolist(), [[1, 2, 3], [10, 11, 12]])


    def test_calculate_t_test(self):
        data = np.genfromtxt('data/t_test.csv')
        results = a.calculate_t_test(data[:, 0], data[:, 1], 0.001)
        self.assertIsNotNone(results)
        self.assertTrue(len(results), 2)
        self.assertAlmostEqual(results[0], 0.00023790996, 10)
        self.assertTrue(results[1])


    def test_calculate_clickthrough_prob(self):
        result = a.calculate_clickthrough_prob(450, 56000, 345, 49000)
        self.assertIsInstance(result, float)


    def test_linear_regression_model(self):
        df = pd.read_csv('data/lin_reg.csv')
        X = df[['A', 'B']].values
        y = df['C'].values
        X_train = X[:25]
        y_train = y[:25]
        X_test = X[25:]
        y_test = y[25:]
        results = a.linear_regression(X_train, y_train, X_test, y_test)
        self.assertIsNotNone(results)
        self.assertEqual(len(results), 2)
        coeffs, r2 = results
        self.assertAlmostEqual(r2, 0.773895, 6)
        self.assertAlmostEqual(coeffs[0], 13.815259, 6)
        self.assertAlmostEqual(coeffs[1], 85.435835, 6)



    def test_windsor_markets(self):
        result = run_sql_query('Test-Sets/test_set1/data/markets.sqlite', a.windsor_markets())
        self.assertEqual(result, 2)


    def test_very_specific_market(self):
        result = run_sql_query('Test-Sets/test_set1/data/markets.sqlite', a.very_specific_market())
        answer = set([u"Oakland", u"48220", u"Royal Town Farmer's Market"])
        self.assertEqual(set([x[0] for x in result]), answer)





if __name__ == '__main__':
    unittest.main()
