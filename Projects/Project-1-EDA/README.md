# ************************************************************************************
## Project 1: Data cleaning & EDA case study
# ************************************************************************************

For this project, you will be investigating data from a publically
available dataset focusing on Real-Time Continuous Glucose Monitor
use in patients with Type 1 Diabetes. As this is a public dataset
derived from a published Clinical Trial, the following disclaimer
applies in regard to the intent of use & results investigated while
using this dataset:

**The source of the data is the *The Juvenile Diabetes Research Foundation 
Continuous Glucose Monitoring Study Group*, but the analyses, content 
and conclusions presented herein are solely the responsibility of the authors 
and have not been reviewed or approved by the aforementioned study ownwers.**

Links to dataset & publication
- [data](xxx)
- [Publication 1: Outcomes for T1 patients with A1C <7%](https://diabetesjournals.org/care/article/32/8/1378/38871/The-Effect-of-Continuous-Glucose-Monitoring-in)
- [Publication 1: Outcomes for T1 patients with A1C ≥7%](https://www.nejm.org/doi/full/10.1056/NEJMoa0805017)

There is a notebook in the directory titled "EDA Project 1 Diabetes.ipynb" - This should help get
you started with importing the CGM & patient demo data, however this is plenty left to do!

Good luck!


## Data

A README is provided by the study owners along with the data for this publically
available dataset. The readme can be found in this project directory, under the /data folder 
[link](https://github.com/link). This dataset documentation contains all the information
that is necessary to understand what each file is, each data table contains and all features / 
explanations included in each table.

Data falls into 1 of 4 categories: (1) RT-CGM data, (2) Lab A1C values, (3) patient demographics & (4)  patient responses to surveys (questionnaires).

The *primary* tables you will utilize, generate new features from and calculate outcomes with are those with the: *tblADataRTCGM* pattern, relating to (1) CGM data. These tables contain EGVs (see diabetes & CGM background) collected at sample frequencies with CGM for all patients, with one record per one CGM reading. There are several files (see study overview), and glucose data for both groups, so you will find CGM data for: 
		
		1. Baseline - Both groups - blinded (patients in both cohorts wearing CGM, neither having access to EGVs / readings at any point, used to get patients assimialted to wearing devices)

		2. RTCGM group (treatment group) - first & second 26-week study period unblinded (patients wore CGM & can see EGVs via receiver or phone)

		3. Control group - first 26-week period (blinded - patients wore CGM, but did not get any data / readings, data only stored and analyzed retrospectively) & second 26-week period (patients continued to wear CGM, but could now see data coming in through receiver or phone)
		
This glucose data should be aggregated per person / cohort & used to compute glucose-driven outcomes like TIR,TAR, TBR, A1C, and correlated with other available data.

There are *many* other data types including patient demographics & responses to a wide array of surveys (income & insurance, hypo fear, complications, parents/caretakers, cost effectiveness, CGM satisfaction, etc - [see study readme](data/study_readme.md)). Data can all be connected using the **PtID** column that is present in all tables. There is a lot to explore, so take a look at the "coming up with your strategy" section below!


## Project Goal

The goal of this project is to apply the skills, knowledge & concepts
of data science to an investigation of outcomes derived from this dataset. There 
is an extensive amount of data to be examined, but the primary data that should
be used for measuring outcomes is stored in the files with "RTCGM" in the name. 
RT-CGM stands for Real Time Continuous Glucose Monitor & is the 
primary medical device / tool used today in diabetes management for patients with 
Type 1 diabetes and for many with Type 2 / other forms of diabetes. You will use 
this data & whatever supporting data that is provided to:

	1. Explore relationships between different demographical features,
    sub-groups & CGM-based outcomes.
	
	2. Generate your own questions & hypotheses on clinical outcomes and use 
	principles of statistics & data science to determine your conclusions
	
	3. Attempt to validate the findings of the study, using your findings from
	above and other means of statistical / DS analysis (Time permitting)
	
	4. Create a short presentation of your results


## Resources

- Publications - use the links above to provide context on the original study
protocol & outcomes
- Diabetes_CGM_background.md - a brief overview of contextual information 
on Diabets & Real-Time CGM use that will be helpful to understand while considering
your approach
- Study_Overview.md - a brief overview of the study protocol, data available
& limitations to help expedite the project

## Coming up with your strategy

However you decide to tackle this analysis you will want to
spend some time coming up with a strategy & formulating the questions you want to ask.
You do not need to write down specific questions, but rather ask yourself about what is
important to look at. For example:

- "What are some of the biggest differences between cohorts?"
- "What factors could most influence outcomes? Biological? Social Determinants?"
- "How does play a factor? Do patients adjust / change with respect to X over time?"
- "Are there any anomalies? What makes it/them anomalous?"
- "Are the primary findings reported in the publications reproducible?"


Even when you are a seasoned data scientist, you will need more than
a day to tackle each of these questions in a robust way, so scope here is important.

Some of the tools that may come in useful here, but are not limited to, include: 
- Statistics:
	- Mean, Median, Mode
	- Standard error / Standard deviation
	- Sampling (bootstrap)
	- Effect size, power, significance level, p-value
	- Correlation coefficients
	- Z/t tests
	- Confidence intervals
	
- Data manipulations & relationships
	- Pandas: .to_datetime(), .groupby(), .rolling(), .pivot_table()
	- Plots: histograms, scatter plots, bar plots, line plots, box plots

## Deliverables

As we are preparing not only for data science interviews, but also typical 
day-to-day workflows in a real data science position, we will introduce the concept of "Definition of Done". This is a standard practice used in data science to help us convey the stop-point at which we consider a project / task / workstream completed, in a way that is comprendible to others. For this project, a definition of done will
be written for you. In future projects, you will come up with this yourself.

### Definition of Done:
1. **Clean, commented & complete code is pushed to github**:
	- README on main page of directory specific to this project - very brief & presentable overview of project, resources used, disclaimer for public data
	    usage, 1-3 sentences of findings, links to slide deck with summary
	- Jupyter notebook with all EDA & outcomes
	- Any python files used for data cleaning, automation, or helper functions
	- Sections commented in notebook with Markdown & comments in py files
	
2. **Slide deck summarizing the project**. 
For the sake of time, we will keep this deck short
and only include the following:
	- Slide 1: Title slide
	- Slide 2: disclaimer on data usage & results (see top - copy and paste)
	- Slide 3: Background & study methods
	- Slide 4: Most interesting / important finding
	- Slide 5: Supplemental outcomes
	- Slide 6: Summary