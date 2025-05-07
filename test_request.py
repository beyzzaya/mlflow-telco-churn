import requests

url = "http://127.0.0.1:8000/predict"
headers = {"Content-Type": "application/json"}

payload = {
    "columns": [
        "gender", "SeniorCitizen", "Partner", "Dependents", "tenure",
        "PhoneService", "PaperlessBilling", "MonthlyCharges", "TotalCharges",
        "NEW_Engaged", "NEW_noProt", "NEW_Young_Not_Engaged", "NEW_TotalServices",
        "NEW_FLAG_ANY_STREAMING", "NEW_FLAG_AutoPayment", "NEW_AVG_Charges",
        "NEW_Increase", "NEW_AVG_Service_Fee", "MultipleLines_No phone service",
        "MultipleLines_Yes", "InternetService_Fiber optic", "InternetService_No",
        "OnlineSecurity_No internet service", "OnlineSecurity_Yes",
        "OnlineBackup_No internet service", "OnlineBackup_Yes",
        "DeviceProtection_No internet service", "DeviceProtection_Yes",
        "TechSupport_No internet service", "TechSupport_Yes",
        "StreamingTV_No internet service", "StreamingTV_Yes",
        "StreamingMovies_No internet service", "StreamingMovies_Yes",
        "Contract_One year", "Contract_Two year",
        "PaymentMethod_Credit card (automatic)", "PaymentMethod_Electronic check",
        "PaymentMethod_Mailed check", "NEW_TENURE_YEAR_1-2 Year",
        "NEW_TENURE_YEAR_2-3 Year", "NEW_TENURE_YEAR_3-4 Year",
        "NEW_TENURE_YEAR_4-5 Year", "NEW_TENURE_YEAR_5-6 Year"
    ],
    "data": [[
        0, 0, 1, 0, -1.27, 0, 1, -1.32, -0.99,
        0, 1, 1, 0, 0, 0, -1.52, -2.58, 1.11,
        1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 1, 0, 0,
        
        0, 0, 0, 0, 0
    ]]
}

response = requests.post(url, json=payload, headers=headers)
print(response.status_code)
print(response.json())