from prettytable import PrettyTable

data = [
    {"Gender": "Male", "HeightCm": 171, "WeightKg": 96 },
    { "Gender": "Male", "HeightCm": 161, "WeightKg": 85 },
    { "Gender": "Male", "HeightCm": 180, "WeightKg": 77 },
    { "Gender": "Female", "HeightCm": 166, "WeightKg": 62},
    {"Gender": "Female", "HeightCm": 150, "WeightKg": 70},
    {"Gender": "Female", "HeightCm": 167, "WeightKg": 82}
    ]


def bmi_d(data):
    x = PrettyTable()
    x.field_names =["BMI Category", "BMI Range (kg/m2)", "Health risk"]
    count = 0
    for person_detail in data:
        bmi = round(person_detail['WeightKg']/((person_detail['HeightCm']/100) ** 2),1)
        if bmi < 18.4:
            result = "Underweight"
            health_risk = 'Malnutrition risk'
        elif bmi >= 18.5 and bmi <= 24.9:
            result = "Normalweight"
            health_risk = 'Low risk'
        elif bmi >= 25 and bmi <= 29.9:
            result = "Overweigh"
            health_risk = 'Enhanced risk'
            count = count+1
        elif bmi >= 30 and bmi <= 34.9:
            result = "Moderately obese"
            health_risk = 'Medium risk'
        elif bmi >= 35 and bmi <= 39.9:
            result = "Severely obese"
            health_risk = 'High risk'
        else:
            result = "Very severely obese"
            health_risk = 'Very High risk'

        x.add_row([result,bmi,health_risk])
    
    return x,count


    
bmi_table =(bmi_d(data)[0]) 
print(bmi_table)
print(f"total no of overweight persons are: {bmi_d(data)[1]}")


