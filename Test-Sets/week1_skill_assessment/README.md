# WEEK 1 - Baseline Skills Assessment


Welcome to your first assessment!  This assessment will be used to gauge your strengths and weaknesses at the start so you can be provided with a better learning experience throughout mentorship.

This assessment has **two parts**: a coding part (`assessment.py`) and a math/concept part (`concepts.txt`). Once you complete the entire assessment, you will submit a pull request so that your work can be assessed. The questions for each topic section some questions are easy, some will be more challenging. That said, it is okay if you are unable to answer queston or are sure about your responses. You should refrain from relying entirely on external resources like books & notes, as much as possible so that it is an accurate assessment of the current state of your data science skills and knowledge.


### Python
Take this assessment using  **Python 3**.  To check which version of Python is installed natively, type `python --version` in the terminal. 

If you're running Anaconda's distribution of Python 2 natively and haven't made this environment before, it's easy to do though the download takes a few minutes.  In terminal type:
```
$ conda create -n py3 python=3 anaconda
```        
Only create the Python 3 environment if you **don't** have Python 3 installed.  Please ask for help if any of this is confusing or you're not sure.  


### SQL
The second part of the coding section asks for SQL queries on the markets SQL database.  The SQL queries that you will submit should be returned as python *strings* in the relevant functions in `assessment.py`.  However you may wish (it is not required) to test your queries in sqlite3 or postgreSQL first.

The databases (`markets.sqlite` for sqlite3, and `markets.sql` for postgreSQL) are located in the `data` directory. 


#### If you want to use sqlite3 (easiest)
Navigate to the `week1_skill_assessment/data` directory in terminal.  
At the terminal, type:
```
$ sqlite3 markets.sqlite
```
Now you can try your queries (using standard sql).

#### If you want to use postgreSQL
Navigate to the `week1_skill_assessment/data` directory in terminal.
The directions depend on your operating system (MacOs or Linux). 

##### Mac directions
On your Dock, go to Applications, find the Postgres.app icon and click it.
Then in the window that opens up click on "Open psql."  The psql terminal should open.  Then in that terminal create an empty markets database:  
```
# CREATE DATABASE markets;
# \q
```
Now load the provided file (`markets.sql`) into psql by typing in terminal:
```
$ psql markets < markets.sql
```
Now you should be able to open the database you just made:
```
$ psql markets
```
Now you can try your queries.

##### Linux directions
Create an empty markets database by typing these commands in terminal: 
```
$ sudo -i -u postgres
$ createdb markets
$ exit
```
Now load the provided file (`markets.sql`) into psql by typing in terminal:
```
$ psql markets < markets.sql
```
Now you should be able to open the database you just made:
```
$ psql markets
```
Now you can try your queries.  

Once again, testing these queries in sqlite3 or postgreSQL is *optional*.  These SQL instructions are provided for your convenience.

### Concepts
The last part of this assssment will be in a text file title "concepts.txt". You will write your responses out underneath each question. Please be as thorough as possible where necessary, and refrain from relying on the internet/books to answer these questions. It is okay if you do not know the answers, this provides us with a good understanding of where any skill & knowledge gaps are. 

________________________________________________________________________________________________________________________
# The Assessment

The repository has the following folder structure:

    assessment-day1
    ├── Makefile
    ├── README.md
    ├── src
    │   ├── __init__.py
    │   ├── assessment.py
    ├── data
    │   ├── alice.txt
    │   ├── markets.sqlite
    │   ├── markets.sql
    ├── test
    │   ├── __init__.py
    │   └── test_assessment.py
    └── concepts
        └── concepts.txt

There are 40 problems total in the assessment.  All the problems are worth the same number of points (3 pts).  
- 20 coding questions in `src/assessment.py`: 
    - 5 python fluency
    - 2 python challenge
    - 3 python statistics
    - 5 numpy/pandas/matplotlib
    - 5 sql fluency
- 25 math & conceptual questions in `concepts/concepts.txt`: 
    - 10 math, Statistics & probability
    - 10 machine learning & algorithms
    - 5 data tooling
- Case study test

**There are two parts to this assessment!  Please complete both!**

1. `src/assessment.py` contains function stubs for you to fill in. The goal is to make the tests pass. There are 12 problems in the file.

 * **Running Unit Tests**

 * This section (`src/assessment.py`) can be tested using the unit tests. You can run the tests with this command from the *root* directory (fork_repository_name/ )):    

    `py.test`

 * If you do not have py.test, you may see Import errors. Run the following commands in case you see such errors:    

    `pip3 install pytest`     

 * `.` refers to passing test, `E` is an error in the code and `F` is a failure. So something that looks like this: `....EFFFFFF` means 4 tests passed, one has an error and 6-11 fail.
 * It can be helpful to press enter a bunch of times between each time you run the test so that it's easy to find the beginning of your most recent results.    


2. The questions for the concepts portion of the assessment are in `concepts.txt`.
  There are no automated tests for this portion of the assessment.

* When you feel you have finished, submit a pull request.


Good luck!
