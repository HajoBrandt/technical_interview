import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def Clean_Start_Age_Range(start_age_range):
    average_start_dates = []
    for range in start_age_range.tolist():
        if range == "Younger than 5 years":
            average_start_dates.append(2.5)
        elif range == "Older than 64 years":
            average_start_dates.append(64)
        elif type(range) == float:
            average_start_dates.append(None)
        else:
            clean_range = range.replace(" years", "")
            start_date = int(clean_range.split(" - ")[0])
            end_date = int(clean_range.split(" - ")[1])
            date_difference = (end_date - start_date) / 2
            average_start_dates.append(end_date - date_difference)
    return average_start_dates

def Convert_Age_Range(age):
    match age:
        case 0:
            return "Younger than 5 years"
        case 5:
            return "5 - 10 years"
        case 11:
            return "11 - 17 years"
        case 18:
            return "18 - 24 years"
        case 25:
            return "25 - 34 years"
        case 35:
            return "35 - 44"
        case 45:
            return "45 - 54 years"
        case 55:
            return "55 - 64 years"
        case 64:
            return "Older than 64 years"

def Calculate_Mean_Of_Age1stCode_Per_Country():
    raw_survey_results = pd.read_csv("data/survey_results_public.csv")
    relevant_columns = raw_survey_results[["Country", "Age1stCode"]]
    relevant_columns.to_excel('cleaned_output/cleaned_data.xlsx')
    relevant_columns.loc[:, "Age1stCode"] = Clean_Start_Age_Range(relevant_columns["Age1stCode"])
    avg_by_country = relevant_columns.groupby("Country")["Age1stCode"].mean()
    return avg_by_country

def Append_GDP_To_Dataframe(avg_by_country):
    gdp = pd.read_excel("data/gdp.xlsx", keep_default_na=False)
    gdp = gdp.replace('', np.nan)
    merged_df = pd.merge(avg_by_country, gdp, left_on='Country', right_on='Country Name')
    merged_df.rename(columns={'2021': 'GDP'}, inplace=True)
    merged_df['Age1stCode'], merged_df['Country Name'] = merged_df['Country Name'], merged_df['Age1stCode']
    merged_df = merged_df.rename(columns={'Age1stCode': 'Country Name', 'Country Name': 'Age1stCode'})
    
    merged_df.to_excel('cleaned_output/cleaned_data_average.xlsx')
    return merged_df

def Append_Lowest_Age_Range_Per_Country(base_data):
    raw_survey_results = pd.read_csv("data/survey_results_public.csv")
    relevant_columns = raw_survey_results[["Country", "Age1stCode"]]
    relevant_columns['Age1stCode'] = relevant_columns['Age1stCode'].str.extract('(\d+)', expand=False)
    relevant_columns['Age1stCode'].replace('Younger than 5 years', '0', inplace=True)
    relevant_columns['Age1stCode'].replace('Older than 64', '64', inplace=True)
    relevant_columns['Age1stCode'] = pd.to_numeric(relevant_columns['Age1stCode'], errors='coerce')
    lowest_age_range = relevant_columns.groupby('Country')['Age1stCode'].min()
    merged_df = base_data.merge(lowest_age_range, left_on='Country Name', right_index=True)
    merged_df.rename(columns={'Age1stCode': 'Lowest_Range'}, inplace=True)
    merged_df.to_excel("cleaned_output/cleaned_data_average_and_range.xlsx")

def Generate_Plot_Based_On_Table(merged_df):
    print(f"De correlatiecoëfficiënt is {merged_df['GDP'].corr(merged_df['Age1stCode'])}")
    plt.scatter(merged_df['Age1stCode'], merged_df['GDP'])
    plt.xlabel('Age First Code')
    plt.ylabel('GDP')
    plt.title('Relationship Between GDP and Age First Code')
    plt.savefig("results/result.png")

def Define_Relationship_Between_Age1stCode_Per_Country_And_GDP():
    Mean_Of_Age1stCode_Per_Country = Calculate_Mean_Of_Age1stCode_Per_Country()
    base_data = Append_GDP_To_Dataframe(Mean_Of_Age1stCode_Per_Country)
    Append_Lowest_Age_Range_Per_Country(base_data)
    Generate_Plot_Based_On_Table(base_data)

if __name__ == '__main__':
    Define_Relationship_Between_Age1stCode_Per_Country_And_GDP()







