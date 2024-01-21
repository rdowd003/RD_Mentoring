# ************************************************************************************
## Project 1: Diabetes & CGM background
# ************************************************************************************

## Terminology

The terminology below should be used as context to better develop hypotheses and consider
which factors / data points are most important in 

### Diabetes Types
|Term|Definition|Notes|
|----|----------|-----|
|Glucose|Endogenous molecule used as the primary analyte for monitoring Diabetes||
|Insulin|Endogenous molecule used by the body to regulate endogenous glucose system|Used in various forms of treatment for diabetes|
|Diabetes Mellitus|An endocrine disorder affecting the insulin-producing (beta) cells of the pancreas|Multiple forms with various causes, and varying levels of curability|
|Type 1 Diabetes (T1D)|An autoimmune form of Diabetes involving (typically) a complete inability to produce insulin & regulate endogenous glucose|Is not caused by, nor can be controlled by diet/exercise. Requires the administration of both short-acting (fast) & long (fast) acting Insulin to regulate endogenous glucose levels 24/7. Non-treatable, typically relies on CGM for monitoring & considered "Insulin dependent"|
|Type 2 Diabetes (T2D)|A genetic & behaviorally driven form of diabetes caused by excessive & uncontrolled endogneous glucose|People with T2D are typically less healthy and need support controlling glucose. Typically follows a diagnosis of "pre-diabetes". First treated behaviorally (diet/exercise), followed by medication (Sulfionoreas (fix spelling) / Metformin / other, and can ultimately develop into "Insulin dependent" stage if left untreated.|
|Other forms of Diabetes|Diabetes can take on other forms of diabetes, including: "Gestational Diabetes (GDM)", "Late Adult Diabetes A (LADA)", etc.| Can be brought on by pregnancy (short lasting), major life/body changes (surgery, viral infection, etc), and other behavioral actions|


### Glucose Monitoring
|Term|Definition|Notes|
|----|----------|-----|
|Glucose Monitoring | The measurement of subcutaneous glucose | Multiple methods, see below|
|Single Measurement Blood Glucose (SMBG, aka "finger prick")|Use of a needle to "prick" skin on finger to pull blood, placed on test strip for measurement of subq glucose|Until CGM (below), this was the industry & medical standard for measuring glucose. This can be done at home with simple needles & test strips|
|Continuous Glucose Monitor (CGM)| A medical device comprising of an implanted wire sensor measuring glucose, and a bluetooth transmitter sending glucose data points to remote device|'Receivers" were the first connected devices used, while nowadays, CGM devices can connect to mobile phones, both, or other medical devices|
|Real-time (rt)CGM|A CGM device that monitors in "real-time"|Does not require user action, can collect samples at a constant frequency & consistently send to device via bluetooth at similar rate. Dexcom = 5 minute intervals|
|Intermittent-Scanning (is)CGM|CGM devices that rely on near-field-detection ("scanning", or swiping phone past implanted receiver)|Typically considered inferior to rtCGM, becoming less common|
|Yellow Standard Instruments (YSI)|An instrument used to measure glucose in-lab glucose values, used as a standard value / ground-truth for determining accuracy of CGM devices|Matched-pair analyses used to determine same-time glucose measurements from CGM & blood-draw-YSI|
|Euglycemia|Well controlled endogenous glucose. Typically refers to non-diabetes, in the range of 80-140 mg/dl|Can refer to instaneous (single) measurement, episodic, or long-term. Typical classification for people without diabetes|
|Hyperglycemia|Glucose that is above euglycemic levels, typically in the range of 180-400 mg/dl| Can refer to instaneous (single) measurement, episodic, or long-term. Not considered emergent risk, but commorbid with many long-term medical issues. Typical concern for people with T2D|
|Hypoglycemia|Glucose that is below euglycemic levels, typically in the range of 40-80 mg/dl| Can refer to instaneous (single) measurement, episodic, or long-term. Episodes of hypoglycemia are considered dangerous, and create a more emergent risk (often requiring immediate administration of glucagon/sugar) and can lead to black-out/death if unresolved quickly. Typical concern for people with T1D. Can also happen to people without diabetes (heavy exertion/exercise & low-sugar/calories intake)|
|Blinded CGM Use|A CGM user is wearing a CGM device (sensor implanted), however they are not in possession of a receiver or mobile device that is connected to the transmitter and are thus unable to see the data / EGV readings| This is commonly used in clinical studies with CGM devices to compare the value of CGM (seeing, interpreting the data as a patient) against non-use, while ensuring that device wear in itself is not a confounding factor|
Unblinded CGM Use|Opposite of blinded, user wearing a CGM device has access to data and can see readings streamed to receiver/phone at predictable interviews|Typical use of CGM|
|Insulin pump|A medical device with implanted needle used to programtically administrate Insulin to user|Now being used in conjunction with CGM devices, or integrated for AID (below)|
| Automated Insulin Delivery System (AID)|An integrated & algorithm-driven system that used closed-loop feedback to determine frequency & dose of automated Insulin delivery basedon CGM reading|Cool data science application!|



### Glucose-driven Measurements
|Term|Definition|Notes|
|----|----------|-----|
|Estimated Glucose Value (EGV)|Estimation of endogenous glucose levels via measurement of subcutaneous glucose with CGM in units of mg/dl|Standard range of readable glucose is 39mg/dl-401 mg/dl. Algorithm used to provide EGV from subq reading|
|Hemoglobin (hb)A1C|Lab-only measurement (tested at Dr/clinic), typically at 3-month intervals|Was former standard of care indicator for state of diabetes, used by physicians & diabetes educators to plan with patient and ammend on-going treatment plans. NO direct calculation for A1C <--> TIR. A1C ≤ 5% is considered well-controlled, <7% is moderate, 7-10% is moderate, ≥10% considered poor control|
|Glucose Management Index (GMI)|A value derived from EGVs used to *approximate* hbA1C (not considered equivalent)|Used for research & management purposes between visits. [Guide to calculating here]()|
|Time in Range (TIR)|Time per measurement period with measured glucose values between 80-140 mg/dl|Considered new standard indicator for diabetes management, monitoring & outcomes. Typically calculated as a % of day, or daily avg % TIR. Requires 10-14 days worth of glucose values to accurately calculate|
Time above Range (TAR)|Time per measurement period with measured glucose values > 180 mg/dl (Level 1) or > 250 mg/dl (Level 2)|Considered new standard indicator for diabetes management, monitoring & outcomes. Typically calculated as a % of day, or daily avg % TIR. Requires 10-14 days worth of glucose values to accurately calculate|
Time below Range (TBR)|Time per measurement period with measured glucose values < 70 mg/dl, or below 54 mg/dl|Considered new standard indicator for diabetes management, monitoring & outcomes. Typically calculated as a % of day, or daily avg % TIR. Requires 10-14 days worth of glucose values to accurately calculate. Many devices like CGM or Insulin pumps have alert to warn user when glucose is (dangerously) low|
|Coefficient of Variation (CV)|A measurement of variability in glucose levels, calculated from CGM-measured EGVs|CV ≤ 0.36 (36%) is clinical goal. Several other metrics trying to calculate variation exist in clinical research as well, in particular: MAGE|
|Diabetes Risk Measurements|Low Blood Glucose Indicator (LBGI), High Blood Glucose Indicator (HBGI), Average Daily Risk Range (ADRR), etc.|Mostly used in clinical research - might be worth looking into for this project!|
|Ambulatory Glucose Profile (AGP)|A profile of diabetes management indicators used to determine success over a given period|clincal goal / recommendations: TIR ≥ 70%, TA180 ≥ 25%, TA250 ≥ 5%, TB70 ≥ 4%, TB54 ≥ 1% - based on [American Diabetes Association (ADA) 2022 standards of care](insert link here)|


## Other Notes / Background
- Type 1 diabetes typically onsets early in life, is untreatable, and forces dependency on Insulin
- Type 2 diabetes average onset is younger adult (T2D onset in children becoming more common), avg age ~30-50
- Now understood that diabetes is *very* dynamic disorder and management success + risk change frequently. CGM has helped mitigate this issue 