import pandas as pd
import numpy as np
import  pickle
import random
from constants import *


# DF to store Patient Data
database = pd.DataFrame(columns=column_names)

#  Load SVM Model
pickle_in = open('svm_classifier.pkl', "rb")
classifier = pickle.load(pickle_in)

# Load StandardScaler
with open('scaler.pkl', 'rb') as scaler_file:
    scaler = pickle.load(scaler_file)


def predictGoldGrade(data):
    # Scale the data
    X_scaled = preprocessData(data)
    # Use model (pkl file) to predict gold grade
    prediction = int(classifier.predict(X_scaled)[0])
    data['Gold Grade'] = prediction
    # Add data to our database (excelsheet)
    add_data_to_excel(data)
    return prediction

def map_categorical_values(data, mapping_dict):
    mapped_data = data.copy()
    for column, mapping in mapping_dict.items():
        mapped_data[column] = mapped_data[column].replace(mapping)
    return mapped_data

def array_to_dataframe(input_array):
    data_dict = dict(zip(column_names, input_array))
    data_dict_copy = data_dict
    data_df = pd.DataFrame(data_dict, index=[0])
    return data_df

def preprocessData(data):
    # Create an array of required data
    patientData = [
        data['SHORTNESS OF BREATH'].upper(),
        data['EXPECTORATION'].upper(),
        data['DIABETES'].upper(),
        data['TYPE OF SMOKER'].upper(),
        data['CIGARETTE/BIDI/GANJA'].upper(),
        data['ALCOHOL USE'].upper(),
        data['mMRC GRADE'],
        data['(FEV1 PRE BD) %PRED'],
        data['(FEV1/FVC POST BD ) L/SEC'],
    ]
    df = array_to_dataframe(patientData)
    # Map the data accoding to training data
    X = map_categorical_values(df, categorical_mapping)
    X_scaled = scaler.transform(X)
    return X_scaled

    
def add_data_to_excel(data_dict):
    print("*******************************")
    data_dict.pop('Cat Values')
    # print(data_dict)
    try:
        # Read the existing Excel file (if it exists)
        try:
            existing_df = pd.read_excel(output_file)
        except FileNotFoundError:
            existing_df = pd.DataFrame()

        # Create a DataFrame from the new data
        new_data_df = pd.DataFrame(data_dict, index=[0])

        # Append the new data to the existing DataFrame
        combined_df = existing_df.append(new_data_df, ignore_index=True)

        # Write the combined DataFrame to the Excel file
        combined_df.to_excel(output_file, index=False)

        print(f'Data added and written to {output_file}')
    except Exception as e:
        print(f'Error: {e}')


# new_data = {
#     'Name': ['New Person'],
#     'AGE': [30],
#     'GENDER': ['Female'],
#     'WEIGHT IN KGS': [65.0],
#     'HEIGHT IN CM': [160.0],
#     'SHORTNESS OF BREATH': ['No'],
#     'EXPECTORATION': ['No'],
#     'DIABETES': ['No'],
#     'TYPE OF SMOKER': ['Non-Smoker'],
#     'CIGARETTE/BIDI/GANJA': ['NONE'],
#     'ALCOHOL USE': ['No'],
#     'mMRC GRADE': [1],
#     '(FEV1 PRE BD) %PRED': [90.0],
#     '(FEV1/FVC POST BD ) L/SEC': [75.0],
#     'Gold Grade': [1]
# }

# # Call the function with the corrected example data
# add_data_to_excel(new_data)