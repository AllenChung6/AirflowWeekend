import pandas as pd
import numpy as np
import matplotlib


def nutrition_script():
    data = pd.read_csv('/Users/allenc/PyCharmProjects/AirflowWeekend/airflow-proj-files/NutritionalFacts.csv',
                       encoding='ISO-8859-1')
    # Food and Serving, Calories, Total Fat, sodium, Total Carbohydrates, dietary Fibers, Protein, Sugars, Saturated Fat, Cholesterol
    # data3: dataframe with specified columns only
    data3 = data[['Food and Serving', 'Calories', 'Total Fat', 'Sodium',
                  'Total Carbo-hydrate', 'Dietary Fiber', 'Protein', 'Sugars', 'Saturated Fat', 'Chole-sterol']]
    # replace NaN values with 0.0 value
    data3.fillna(0.0, inplace=True)
    # Check dataframe for al NaN values
    data3.isna().sum()
    data3.loc[[0]]
    # Append first row data with column data (unit meaures)
    data3.columns = data3.columns + data3.iloc[0, :]
    data3.iloc[1:, ]
    # Remove unnamed Data
    data3.columns = data3.columns.str.rstrip("Unnamed: 0_level_1")
    # Remove first row
    data3 = data3.iloc[1:, :]
    # Convert column values with numeric datatypes to Float
    data3['Calories'] = data3['Calories'].astype('float')
    data3['Total Fat(g)'] = data3['Total Fat(g)'].astype('float')
    data3['Sodium(g)'] = data3['Sodium(g)'].astype('float')
    data3['Total Carbo-hydrate(g)'] = data3['Total Carbo-hydrate(g)'].astype('float')
    data3['Dietary Fiber(g)'] = data3['Dietary Fiber(g)'].astype('float')
    data3['Protein(g)'] = data3['Protein(g)'].astype('float')
    data3['Sugars(g)'] = data3['Sugars(g)'].astype('float')
    data3['Saturated Fat(%DV)'] = data3['Saturated Fat(%DV)'].astype('float')
    data3['Chole-sterol(%DV)'] = data3['Chole-sterol(%DV)'].astype('float')
    # Show all records in Dataframe
    pd.set_option("display.max_rows", None, "display.max_columns", None)
    data3.to_csv('/Users/allenc/PyCharmProjects/AirflowWeekend/airflow-proj-files/output_file.csv')
    # Sort values by alphabet
    # Alphabetized = data3.sort_values(by=['Food and Serving'], ascending=True)
    # Sort by Calories numbers from High to Low
    # Calories = data3.sort_values(by=['Calories'], ascending=False)
    # Sort foods by the amount of Protein from High to low
    # Protein = data3.sort_values(by=['Protein(g)'], ascending=False)


