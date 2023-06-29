import pandas as pd
df = pd.read_csv("customer_booking.csv", encoding="ISO-8859-1")
print(df.head())
print(df.info)
print(df["flight_day"].unique())
mapping = {
    "Mon": 1,
    "Tue": 2,
    "Wed": 3,
    "Thu": 4,
    "Fri": 5,
    "Sat": 6,
    "Sun": 7,
}

df["flight_day"] = df["flight_day"].map(mapping)
print(df["flight_day"].unique())
print(df.describe())