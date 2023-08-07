column_names = ['SHORTNESS OF BREATH', 'EXPECTORATION', 'DIABETES', 'TYPE OF SMOKER',
                'CIGARETTE/BIDI/GANJA', 'ALCOHOL USE', 'mMRC GRADE',
                '(FEV1 PRE BD) %PRED', '(FEV1/FVC POST BD ) L/SEC']

# Define the mapping dictionary for each categorical column
categorical_mapping = {
    'SHORTNESS OF BREATH': {'NO': 0, 'YES': 1},
    'EXPECTORATION': {'NO': 0, 'YES': 1},
    'DIABETES': {'NO': 0, 'YES': 1},
    'TYPE OF SMOKER': {'NON SMOKER': 0, 'EX SMOKER': 1, 'CURRENT SMOKER': 2, 'PASSIVE SMOKER': 3},
    'CIGARETTE/BIDI/GANJA': {'CIGARETTE': 0, 'BIDI': 1, 'GANJA': 2, 'BIOMASS FUEL': 3, 'NONE': 4},
    'ALCOHOL USE': {'NO': 0, 'YES': 1},
}

categorical_features = ['SHORTNESS OF BREATH', 'EXPECTORATION','DIABETES', 'TYPE OF SMOKER', 'CIGARETTE/BIDI/GANJA', 'ALCOHOL USE']
numerical_features = ['mMRC GRADE', '(FEV1 PRE BD) %PRED', '(FEV1/FVC POST BD ) L/SEC']

# Output Excel file
output_file = 'data_output.xlsx'
