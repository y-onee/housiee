import pandas as pd

df_assessment = pd.read_csv('data/raw/assessment.csv', dtype=str)
df_features = pd.read_csv('data/raw/features.csv', dtype=str)

df_all_2026 = df_assessment[df_assessment['Tax Year'] == '2026']

df_assessment_2026 = df_all_2026[["Assessment Account Number", "Assessed Value"]]
df_taxable_2026 = df_all_2026[["Assessment Account Number", "Taxable Assessed Value"]]
df_features_2026 = df_features[["Municipal Unit","Assessment Account Number","Civic City Name","Living Units","Year Built","Square Foot Living Area","Style","Bedrooms","Bathrooms","Under Construction","Construction Grade","Finished Basement","Garage"]]
    
merged_assessed = df_features_2026.merge(df_assessment_2026, on="Assessment Account Number", how="left")
merged_taxable = df_features_2026.merge(df_taxable_2026, on="Assessment Account Number", how="left")

merged_assessed.to_csv(
    "data/processed/final_properties_with_2026_assessment.csv",
    index=False
)

merged_taxable.to_csv(
    "data/processed/final_properties_with_2026_taxable.csv",
    index=False
)

print("Complete!")
print(
    "Missing assessments:",
    merged_assessed["Assessed Value"].isna().mean()
)