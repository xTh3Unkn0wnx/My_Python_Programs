import pandas as pd
pd.options.display.float_format = '{:,.2f}'.format
df = pd.read_csv('Car_sales.csv')
df.drop(['Width', 'Length', 'Power_perf_factor', 'Curb_weight', 'Wheelbase'], inplace=True, axis=1)
df['year'] = pd.to_datetime(df['Latest_Launch'], format='%m/%d/%Y').dt.year
df['month'] = pd.to_datetime(df['Latest_Launch'], format='%m/%d/%Y').dt.month
df.rename(columns={'Sales_in_thousands': 'Sales', 'Price_in_thousands': 'Price', '__year_resale_value': 'Resale_Value'}, inplace=True)
df['Sales'] = (df["Sales"] * 1000)
df['Price'] = (df['Price'] * 1000)
df['Resale_Value'] = (df['Resale_Value'] * 1000)
meanp = round(df['Price'].mean(),0)
meanre = df['Resale_Value'].mean()
df['Price'].fillna(meanp, inplace=True)
df['Resale_Value'].fillna(meanre, inplace=True)
df.dropna(inplace=True)
# Q1: How does the popularity of different car models impact the sales performance in the automotive industry in the least 3 years?
print("Question 1: How does the popularity of different car models impact the sales performance in the automotive industry in the last 3 years?")
popular = df[df['year'] >= 2010].groupby('Manufacturer')['Sales'].mean().sort_values(ascending=False)
print("printing popular")
print(popular)
# Q2: What is the monthly sales trend vechile types in the last 2008-2012?
print("\nQuestion 2: What is the monthly sales trend of vehicle types in 2008-2012?")
trend = df[(df['year'] >= 2008)].groupby(['Vehicle_type', 'month' ])['Sales'].sum()
print("Printing trends")
print("Cars top five months")
print(trend['Car'].sort_values(ascending=False).head(5))
print("Passenger top five months")
print(trend['Passenger'].sort_values(ascending=False).head(5))
# Q3: What was the sales growth of Toyota models over the last 2008-2012?
print("\nQuestion 3: What was the sales growth of Toyota models over the last 2008-2012?")
print("Toyota!!!")
Toyota = df[(df['Manufacturer'] == 'Toyota')].groupby(['year', 'Model'])['Sales'].sum()
print(Toyota.sort_values(ascending=False))
# Q4: Do cars with higher horsepower tend to sell for higher prices?
print("\nQuestion 4: Do cars with higher horsepower tend to sell for higher prices?")
horsepower = df.groupby('Manufacturer')[['Horsepower', 'Sales']].mean()
correlation = horsepower['Horsepower'].corr(horsepower['Sales'])
print(horsepower.head())
print(f"The correlation between horsepower and a car's popularity is {correlation:.4f}")
# Q5: What is the average sale price of cars in the dataset?
print("\nQuestion 5: What is the dataset's average sale price of cars?")
averagesale = df['Price'].mean()
print(f"The average sale price of cars in the data set is ${averagesale:,.2f}")
# Q6: Do the top five manufactuers also produce the top 5 fuel efficent cars?
print("\nQuestion 6: Do the top five manufacturers also produce the top 5 fuel-efficient cars?")
top5 = df.groupby('Manufacturer')['Sales'].sum().sort_values(ascending=False)
fuelEff = df.groupby('Manufacturer')['Fuel_efficiency'].mean().sort_values(ascending=False)
association = top5.corr(fuelEff)
print(top5.head())
print(fuelEff.head())
print(f"Correlation between popularity and fuel efficiency is {association:.4f}")