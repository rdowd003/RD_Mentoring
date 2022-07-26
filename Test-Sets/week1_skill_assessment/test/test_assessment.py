'''
Unit tests for Assessment 1
Usage: from week1 skills assessment directory run: make test
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

def function_x(a,b):
    return a+b


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


    def test_data_frame_easy(self):
        df = pd.DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6]})
        colA, colB, colC = ('a', 'b', 'c')
        a.data_frame_easy(df, colA, colB, colC)
        self.assertTrue(colC in df.columns.tolist())
        self.assertEqual(df[colC].tolist(), [5, 7, 9])


    def test_data_frame_med(self):
        df = pd.DataFrame({'a': [1, 2, 3, 4, 5, 6]})
        colA, colB = ('a','b')
        win = 3
        min_val = 2
        a.data_frame_med(df, colA, win=win,min_val=min_val)
        self.assertTrue(colB in df.columns.tolist())
        self.assertEqual([str(x) for x in df[colB].tolist()], ['nan','3.0','6.0','9.0','12.0','15.0'])


    def test_data_frame_hard(self):
        df = pd.DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6]})
        colA, colB, colC = ('a', 'b', 'c')
        a.data_frame_hard(df, colA, colB, function_x)
        self.assertTrue(colC in df.columns.tolist())
        self.assertEqual(df[colC].tolist(), [5, 7, 9])


    def test_classifier_eval(self):
        pred_labels = [0,0,0,1,0,0,0,0,0,1,0,0,1,1]
        true_labels = [1,0,0,1,0,1,0,0,0,1,1,0,1,0]
        tp = np.sum(np.logical_and(pred_labels == 1, true_labels == 1))
        tn = np.sum(np.logical_and(pred_labels == 0, true_labels == 0))
        fp = np.sum(np.logical_and(pred_labels == 1, true_labels == 0))
        fn = np.sum(np.logical_and(pred_labels == 0, true_labels == 1))
        precison, recall, accuracy = a.classifier_eval(pred_labels,true_labels)
        self.assertEqual(precison,np.round(((tp)/(tp+fp)),2))
        self.assertEqual(recall,np.round(((tp)/(tp+fn)),2))
        self.assertEqual(accuracy,np.round(((tp+tn)/(tp+tn+fp+fn)),2))


    def test_num_to_word_string(self):
        s = 245
        str_actual = "two hundred and forty five"
        output = a.num_to_word_string(s)
        self.assertTrue(type(output)==str)
        self.assertEqual(output, str_actual) 


    def test_mab_slots(self)  :
        d = {'a': [0, 1, 2, 3], 'b': [4, 5, 6, 7], 'c': [0, 1, 4, 2]}
        eps = 0.2
        seed = 22
        runs = 3
        result = mab(d,eps,seed,runs)
        total_reward = a.mab_slots(d,eps,seed,runs)
        self.assertEqual(result, total_reward)


    def test_markets_per_state(self):
        result = run_sql_query('Test-Sets/week1_skill_assessment/data/markets.sqlite', a.markets_per_state())
        california, maine = None, None
        for item in result:
            if item[0] == 'California':
                california = item[1]
            if item[0] == 'Maine':
                maine = item[1]
        self.assertEqual(california, 332)


    def test_state_population_gain(self):
        result = run_sql_query('Test-Sets/week1_skill_assessment/data/markets.sqlite', a.state_population_gain())
        answer = set([u'Georgia', u'Colorado', u'Florida', u'Washington', u'Virginia', u'North Carolina', u'Arizona', \
                      u'California', u'Nevada', u'Texas'])
        self.assertEqual(set([x[0] for x in result]), answer)

    
    def test_farmers_wine_and_honey(self):
        result = run_sql_query('Test-Sets/week1_skill_assessment/data/markets.sqlite', a.farmers_wine_and_honey())
        for item in result:
            if item[0] == 'Middlesex':
                cities = item[1]
        self.assertEqual(cities, 23)


    def test_mad_cheese_markets(self):
        result = run_sql_query('Test-Sets/week1_skill_assessment/data/markets.sqlite', a.mad_cheese_markets())
        for item in result:
            if item[0] == 'New York':
                ny = item[1]
            if item[0] == 'California':
                ca = item[1]
            if item[0] == 'Massachusetts':
                ma = item[1]
        self.assertEqual(ny, 'Westchester')
        self.assertEqual(ca, 'Sutter')
        self.assertEqual(ma, 'Middlesex')





def mab(reward_dict,e,s,r):
    np.random.seed(s)
    total_reward = 0
    keys = list(reward_dict.keys())
    run_dtns = np.random.random(size=r)
    for index,dtn in enumerate(run_dtns):
        if dtn < e:
            choice = np.random.choice(keys)
            total_reward += reward_dict[choice][index]
        else:
            temp_rewards = [reward_dict[key][index] for key in keys]
            total_reward += max(temp_rewards)

    return total_reward







if __name__ == '__main__':
    unittest.main()
