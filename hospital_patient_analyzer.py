import pandas as pd
import datetime
df=pd.read_csv("hospital_patient_analyzer.csv")
print("The first five patinets are:",df.head(5))
print("The last five patients are:",df.tail(5))
print(df.shape)
print(df.dtypes)
print("The missing values in data frame are: ",df.isnull().sum())
print("The duplicated values in the data frame are:",df.duplicated().sum())

df["Age"]=pd.to_numeric(df['Age'],errors="coerce")
df["Treatment_Cost"]=pd.to_numeric(df["Treatment_Cost"],errors="coerce")

print("The mean age is",df["Age"].mean())
print("The minimum age is",df["Age"].min())
print("The max age is",df["Age"].max())   
print("The patient count is",df["Age"].count())
print("The average treatment cost is",df["Treatment_Cost"].mean())
print("The  max treatment cost is",df["Treatment_Cost"].max())
print("The  max treatment cost is",df["Treatment_Cost"].min())

print("unique value in gender coloumn are\n",df["Gender"].unique())
print("unique value in Department coloumn are\n",df["Department"].unique())
print("unique value in Diagnosis coloumn are\n",df["Diagnosis"].unique())
print("unique value in Ward coloumn are\n",df["Ward"].unique())
print("unique value in Insurance coloumn are\n",df["Insurance"].unique())
print("unique value in Patient_Status coloumn are\n",df["Patient_Status"].unique())

print("unique value in gender coloumn are\n",df["Gender"].value_counts(ascending=False))
print("unique value in Department coloumn are\n",df["Department"].value_counts(ascending=False))
print("unique value in Diagnosis coloumn are\n",df["Diagnosis"].value_counts(ascending=False))
print("unique value in Ward coloumn are\n",df["Ward"].value_counts(ascending=False))
print("unique value in Insurance coloumn are\n",df["Insurance"].value_counts(ascending=False))
print("unique value in Patient_Status coloumn are\n",df["Patient_Status"].value_counts(ascending=False))

df=df.drop_duplicates()
df.columns=df.columns.str.upper()
df["INSURANCE"]=df["INSURANCE"].astype(bool)
mean_age=df["AGE"].mean()
df["AGE"]=df["AGE"].fillna(mean_age)
print(df["AGE"].isnull().sum())
df["TREATMENT_COST"]=df["TREATMENT_COST"].fillna(0.00)

invalid_data = df[
    (df["AGE"] <= 0) | 
    (df["AGE"] > 100)&
    (df["TREATMENT_COST"])>=0
]
df=df.dropna(subset=["PATIENT_STATUS"])
print("Total patient in hosptial are:",df["AGE"].count())
print("Patient per department are: ",df.groupby("DEPARTMENT").size())
print("avg age per department: ",df.groupby("DEPARTMENT")["AGE"].mean())
print("Avg treatment cost per depertment",df.groupby("DEPARTMENT")["TREATMENT_COST"].mean())
print("Diagnosis",df["DIAGNOSIS"].value_counts())
print("Total treatment cost is: ",df["TREATMENT_COST"].sum())
print("Average treatment cost is: ",df["TREATMENT_COST"].mean())
print("Maximum treatment cost is: ",df["TREATMENT_COST"].max())
print("Minimum treatment cost is: ",df["TREATMENT_COST"].min())
print("Top 5 expensive patients are:",df["TREATMENT_COST"].value_counts(ascending=True))
print("Gender analysis",df.groupby("GENDER").size())
print("ward analysis",df.groupby("WARD").size())
df.to_csv("cleaned_patient_data.csv", index=False)