import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df_census = pd.read_csv(r"C:\Users\donna\Documents\Python\Demographic_Analyzer\adult.data.csv")

    #establish repetitive variables
    ttl_records = len(df_census)
    advanced_are = df_census['education'].isin(['Bachelors', 'Masters', 'Doctorate']) 
    advanced_degrees = df_census[advanced_are] 
    no_advanced_degree = df_census[~advanced_are] 
    over_50K = df_census['salary'] == '>50K' 
    over_50K_mask = df_census[over_50K] 

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df_census['race'].value_counts()
    
    # What is the average age of men?
    average_age_men = round(df_census.loc[df_census['sex'] == 'Male', 'age'].mean(),1)
   
    # What is the percentage of people who have a Bachelor's degree?
    percentage_bachelors = round((len(df_census.loc[df_census['education'] == 'Bachelors'] ) / ttl_records) * 100 ,1)
   
    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    higher_education = len(advanced_degrees.loc[advanced_degrees['salary'] == '>50K'])
    lower_education = len(no_advanced_degree.loc[no_advanced_degree['salary'] == '>50K'])
   
    # percentage with salary >50K
    higher_education_rich = round((len(advanced_degrees.loc[advanced_degrees['salary'] == '>50K'] )/ len(advanced_degrees)) * 100,1)
    lower_education_rich = round((len(no_advanced_degree.loc[no_advanced_degree['salary'] == '>50K'] ) / len(no_advanced_degree)) * 100,1)
    
    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df_census['hours-per-week'].min()
    
    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    num_min_workers = len(over_50K_mask[over_50K_mask['hours-per-week'] == min_work_hours])
    rich_percentage = round((len(over_50K_mask[over_50K_mask['hours-per-week'] == min_work_hours]))   / (len(df_census[df_census['hours-per-week'] == min_work_hours])) * 100,1)
   
    # What country has the highest percentage of people that earn >50K?
    highest_earning_country = ((over_50K_mask['native-country'].value_counts()) /  (df_census['native-country'].value_counts())).idxmax()
    highest_earning_country_percentage = round((over_50K_mask['native-country'].value_counts()/  df_census['native-country'].value_counts()).max() * 100, 1)

    # Identify the most popular occupation for those who earn >50K in India.
    top_IN_occupation = over_50K_mask[over_50K_mask['native-country'] == 'India']['occupation'].value_counts().idxmax()
    

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }