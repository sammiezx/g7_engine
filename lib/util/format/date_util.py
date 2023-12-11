import nepali_datetime
import pandas as pd

# students = pd.read_csv("/home/samir/Desktop/rudraAnalytics/NEEM/data/factored/students.csv")

def convert_to_bs(x):
    try:
        x = x.split('-')
        x = [int(y) for y in x]
        return nepali_datetime.date(x[0], x[1], x[2]).to_datetime_date()
    
    except:
        return None

# students['admission_date_bs'] = pd.to_datetime(students['admission_date'][0:5].apply(convert_to_bs))