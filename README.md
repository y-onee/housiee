# Housing Cost Prediction ML Project

## Project Overview

This repository contains a machine learning project aimed at predicting housing costs based on property characteristics and location data. By leveraging historical assessment values and detailed property features, the project builds predictive models to estimate housing prices, which can assist buyers, sellers, and analysts in understanding market trends.

## Problem Statement

Housing prices are influenced by numerous factors including property features, location, and market conditions. This project focuses on developing a robust ML pipeline that integrates diverse property data to accurately predict housing costs, enabling data-driven decision making in real estate.

## Data Sources

The project utilizes two primary raw datasets as inputs:

1. **Residential Dwelling Characteristics**  
   Contains detailed property features such as number of bedrooms, bathrooms, square footage, and building structure.

   🔗 https://www.thedatazone.ca/Assessment/Residential-Dwelling-Characteristics/a859-xvcs/about_data

2. **Assessed Value and Taxable Assessed Value History**  
   Contains historical and current assessment values for properties, including 2026 assessment data.

   🔗 https://www.thedatazone.ca/Assessment/Assessed-Value-and-Taxable-Assessed-Value-History/bt58-qu28/about_data

These datasets are combined and processed as part of the feature engineering pipeline.

## Feature Engineering

Key steps in feature engineering include:

- Filtering assessment data to focus on the target year (e.g., 2026)
- Merging property features with corresponding assessment values
- Creating derived features such as price per square foot, age of property, and location-based indicators
- Handling missing values and encoding categorical variables

## Model Approach

The project explores various regression models to predict housing costs, including:

- Linear Regression
- Random Forest Regressor
- Gradient Boosting Machines

Model performance is evaluated using metrics such as RMSE and R², with hyperparameter tuning applied to optimize results.

## Project Structure

- `data/` - Raw and processed datasets
- `notebooks/` - Jupyter notebooks for exploratory data analysis and model experiments
- `src/` - Source code for data processing, feature engineering, and modeling
- `models/` - Saved trained models and evaluation results
- `README.md` - Project documentation

## How to Run

1. Clone the repository
2. Ensure Python 3.8+ is installed
3. Create and activate a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
5. Run data processing scripts to prepare datasets
6. Train models using provided scripts or notebooks
7. Evaluate and analyze model performance

## Notes

- This project assumes access to the raw datasets linked above; users should download and place them in the `data/raw/` directory.
- The pipeline is modular, allowing easy updates as new data or features become available.
- Future enhancements may include incorporating additional location-based data and deploying the model as a web service.
