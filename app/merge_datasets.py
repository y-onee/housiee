import pandas as pd

df_assessment = pd.read_csv('data/assessment.csv', dtype=str)
df_features = pd.read_csv('data/features.csv', dtype=str)

df_assessment_2026 = df_assessment[df_assessment['Tax Year'] == '2026']

df_assessment_2026 = df_assessment_2026[["Assessment Account Number", "Assessed Value","Taxable Assessed Value"]]
df_features_2026 = df_features[["Municipal Unit","Assessment Account Number","Civic City Name","Living Units","Year Built","Square Foot Living Area","Style","Bedrooms","Bathrooms","Under Construction","Construction Grade","Finished Basement","Garage"]]
    
merged = df_features_2026.merge(df_assessment_2026, on="Assessment Account Number", how="left")

merged.to_csv(
    "data/final_properties_with_2026_assessment.csv",
    index=False
)

print("Complete!")
print(
    "Missing assessments:",
    merged["Assessed Value"].isna().mean()
)