curl -X 'POST' \
  'http://localhost:10007/predict' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "Account_Balance": 1,
  "Duration_of_Credit_monthly": 12,
  "Payment_Status_of_Previous_Credit": 2,
  "Purpose": 2,
  "Credit_Amount": 5000,
  "Value_Savings_Stocks": 1,
  "Length_of_current_employment": 2,
  "Instalment_per_cent": 4,
  "Sex_Marital_Status": 2,
  "Guarantors": 1,
  "Duration_in_Current_address": 3,
  "Most_valuable_available_asset": 2,
  "Age_years": 25,
  "Concurrent_Credits": 1,
  "Type_of_apartment": 1,
  "No_of_Credits_at_this_Bank": 1,
  "Occupation": 1,
  "No_of_dependents": 1,
  "Telephone": 1,
  "Foreign_Worker": 1
}'

curl -X 'POST' \
  'http://localhost:10007/predict' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "Account_Balance": 1,
  "Duration_of_Credit_monthly": 4,
  "Payment_Status_of_Previous_Credit": 18,
  "Purpose": 4,
  "Credit_Amount": 0,
  "Value_Savings_Stocks": 1028,
  "Length_of_current_employment": 1,
  "Instalment_per_cent": 3,
  "Sex_Marital_Status": 4,
  "Guarantors": 2,
  "Duration_in_Current_address": 1,
  "Most_valuable_available_asset": 3,
  "Age_years": 1,
  "Concurrent_Credits": 36,
  "Type_of_apartment": 3,
  "No_of_Credits_at_this_Bank": 2,
  "Occupation": 2,
  "No_of_dependents": 3,
  "Telephone": 1,
  "Foreign_Worker": 1
}'

curl -X 'POST' \
  'http://localhost:10007/predict' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "Account_Balance": 1,
  "Duration_of_Credit_monthly": 4,
  "Payment_Status_of_Previous_Credit": 36,
  "Purpose": 4,
  "Credit_Amount": 3,
  "Value_Savings_Stocks": 3342,
  "Length_of_current_employment": 5,
  "Instalment_per_cent": 5,
  "Sex_Marital_Status": 4,
  "Guarantors": 3,
  "Duration_in_Current_address": 1,
  "Most_valuable_available_asset": 2,
  "Age_years": 3,
  "Concurrent_Credits": 51,
  "Type_of_apartment": 3,
  "No_of_Credits_at_this_Bank": 2,
  "Occupation": 1,
  "No_of_dependents": 3,
  "Telephone": 1,
  "Foreign_Worker": 2
}'