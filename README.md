# 🏥 Hospital Patient Analyzer

A beginner-friendly **Pandas data analysis project** that explores, cleans, and analyzes hospital patient data.

The dataset is intentionally **unclean**, containing missing values, duplicate records, inconsistent text formatting, invalid numeric values, and invalid dates. The purpose of the project is to practice real-world data cleaning and analysis using Python Pandas.

## 🎯 Project Objective

The main objective of this project is to learn how to work with an unclean healthcare dataset and extract useful information from it.

The project focuses on:

* Exploring the dataset
* Finding missing values
* Detecting duplicate records
* Identifying inconsistent data
* Cleaning numerical and categorical data
* Handling invalid values
* Analyzing patients by department, diagnosis, gender, ward, and status
* Analyzing treatment costs
* Finding useful patterns from the data

## 📁 Dataset

The dataset contains approximately **200 patient records**.

### Columns

| Column           | Description               |
| ---------------- | ------------------------- |
| `Patient_ID`     | Unique patient identifier |
| `First_Name`     | Patient's first name      |
| `Last_Name`      | Patient's last name       |
| `Age`            | Patient age               |
| `Gender`         | Patient gender            |
| `Department`     | Hospital department       |
| `Diagnosis`      | Patient diagnosis         |
| `Doctor`         | Assigned doctor           |
| `Ward`           | Patient ward              |
| `Admission_Date` | Patient admission date    |
| `Treatment_Cost` | Cost of treatment         |
| `Insurance`      | Insurance status          |
| `Patient_Status` | Current patient status    |

## 🧹 Data Cleaning

The dataset was intentionally created with problems that commonly occur in real-world datasets.

The project practices:

* Detecting missing values
* Handling missing values
* Finding duplicate records
* Removing duplicates
* Removing unnecessary spaces
* Standardizing text values
* Converting columns to numeric data types
* Handling invalid numeric values
* Converting date values
* Detecting invalid ages
* Detecting invalid treatment costs
* Checking inconsistent categorical values

## 📊 Data Exploration

The project explores:

* First five records
* Last five records
* Number of rows and columns
* Column names
* Data types
* Missing-value counts
* Duplicate records
* Unique values
* Frequency of categorical values

## 📈 Data Analysis

After cleaning the dataset, the project can be used to analyze:

### Patient Analysis

* Total number of patients
* Average patient age
* Minimum and maximum age
* Patient count by gender
* Patient count by department
* Patient count by ward
* Patient count by patient status

### Department Analysis

Using `groupby()`:

* Number of patients per department
* Average age per department
* Average treatment cost per department
* Highest-cost department
* Most occupied department

### Diagnosis Analysis

* Most common diagnosis
* Top 5 diagnoses
* Number of patients for each diagnosis

### Treatment Cost Analysis

* Total treatment cost
* Average treatment cost
* Minimum treatment cost
* Maximum treatment cost
* Top 5 patients by treatment cost

### Insurance Analysis

* Insured vs uninsured patients
* Number of patients by insurance status
* Average treatment cost based on insurance status

### Ward Analysis

* Number of patients in each ward
* Average treatment cost by ward
* Most occupied ward

### Age Group Analysis

Patients can be grouped into:

* Children: 0–18
* Young Adults: 19–40
* Middle Age: 41–60
* Seniors: 61+

The project can then compare patient counts and treatment costs between age groups.

## 🧠 Pandas Concepts Practiced

```text
read_csv()
head()
tail()
shape
columns
dtypes
isnull()
sum()
duplicated()
drop_duplicates()
fillna()
astype()
pd.to_numeric()
to_datetime()
unique()
value_counts()
mean()
min()
max()
count()
sort_values()
groupby()
Boolean filtering
Creating new columns
```

## 📂 Project Structure

```text
Hospital-Patient-Analyzer/
│
├── hospital_patient_analyzer.py
├── hospital_patient_analyzer.csv
└── README.md
```

## 🚀 What I Learned

Through this project, I practiced how to work with an intentionally messy dataset using Pandas.

The main concepts I improved were:

1. Loading CSV data
2. Exploring DataFrames
3. Checking data types
4. Finding missing values
5. Detecting duplicate records
6. Cleaning categorical data
7. Converting data types
8. Handling invalid values
9. Filtering data
10. Sorting data
11. Using `groupby()`
12. Using `value_counts()`
13. Creating calculated columns
14. Performing basic statistical analysis
15. Extracting useful information from raw data

## 🔮 Future Improvements

Possible future improvements include:

* Adding Matplotlib visualizations
* Creating charts for department and diagnosis analysis
* Creating a hospital dashboard
* Adding monthly admission analysis
* Analyzing treatment cost trends
* Adding more patient records
* Exporting the cleaned dataset
* Creating an interactive dashboard

## 👨‍💻 Author

**Ashutosh Adhikari**

This project was created as part of my learning journey with **Python, Pandas, and Data Analysis**.
