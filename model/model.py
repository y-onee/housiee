import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.discriminant_analysis import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from pygam import LinearGAM, s

df = pd.read_csv('data/processed/final_properties_with_2026_assessment.csv', dtype=str)

feature_cols = ["Municipal Unit","Assessment Account Number","Civic City Name","Living Units","Year Built","Square Foot Living Area","Style","Bedrooms","Bathrooms","Under Construction","Construction Grade","Finished Basement","Garage"]

X = df[feature_cols]

y = df["Assessed Value"].str.replace(',', '').astype(float)

categorical_cols = ["Municipal Unit", "Civic City Name", "Style", "Under Construction", "Construction Grade", "Finished Basement", "Garage"]

numeric_cols = [col for col in feature_cols if col not in categorical_cols and col != "Assessment Account Number"]

preprocessor = ColumnTransformer(
    transformers=[
        ('num', StandardScaler(), numeric_cols),
        ('cat', OneHotEncoder(handle_unknown='ignore'), categorical_cols)
    ]
)

gam = LinearGAM(
    sum([s(i) for i in range(len(numeric_cols))]).fit(preprocessor.fit_transform(X), y)
)
