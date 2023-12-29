# property.csv is a data set of property values from 2007 - 2019. The data contain sales prices for houses and units with 1, 2, 3, 4, and 5 bedrooms.
# The data are: date of sale; price in dollars; property type (unit or house); number of bedrooms
# Don't forget to install pandas in replit! :)
import pandas as pd
# Load property.csv into a data frame.
pd.options.display.float_format = '{:,.2f}'.format
prop = pd.read_csv("property.csv")
# How many rows and columns are there in the data set?
print('2: How many rows and columns are there in the data set?')
print(f'Number of rows: {prop.shape[0]}')
print(f'Number of columns: {prop.shape[1]}')
print('')
# Calculate and show summary statistics (mean, median, max, etc.) for the price column.
# https://www.w3schools.com/python/pandas/ref_df_describe.asp
print('3: Calculate and show summary statistics (mean, median, max, etc.) for the price column.')
print(prop['price'].describe())
print('')
# Remove the variables V1 and V2 from the data set. Show the head() of your data set to confirm this.
print('4: Remove the variables V1 and V2 from the data set. Show the head() of your data set to confirm this.')
np = prop.drop('V1', axis='columns').drop('V2', axis='columns')
print(np.head())
print('')
# A. Are there any NA values in the data set?
print('5: NA Values')
check = np.isna().values.any()
if check:
    print(f'{check}: There are na values in the dataframe')
else:
    print(f'{check} there are no na values in the dataframe')
# B. If any NA values are in the price column, replace it with the mean price.
# https://www.w3schools.com/python/pandas/ref_df_fillna.asp
meanprice = round(np['price'].mean())
np['price'].fillna(meanprice, inplace=True)
print(np.head())
# C. If any NA values are in any of the other columns, remove the entire row from the data set.
np.dropna(inplace=True)
# D. Show that there are no more NA values in the data set.
check = np.isnull().values.any()
if check:
    print(f'{check}: There are na values in the dataframe')
else:
    print(f'{check} there are no na values in the dataframe after changes been made')
print('')
# Rename the saledate column to date. Show the head() of your data set to confirm this.
print('6: Rename the saledate column to date. Show the head() of your data set to confirm this.')
np.rename(columns={'saledate': 'date'}, inplace=True)
print(np.head())
print('')
# Calculate and show the mean price of house properties and unit properties.
print('7: Calculate and show the mean price of house properties and unit properties.')
meanprice = round(np.groupby('type')['price'].mean())
print(f'Mean price of house properties: ${meanprice[0]}')
print(f'Mean price of unit properties: ${meanprice[1]}')
print('')
# Calculate the total income (i.e., total amount of money made by selling) for each of the bedroom types. Show the output from highest to lowest total income.
print('8: Calculate the total income (i.e., total amount of money made by selling) for each of the bedroom types. Show the output from highest to lowest total income.')
rooms = np.groupby('bedrooms')['price'].sum()
rooms.sort_values(inplace=True, ascending=False)
print(rooms.head())
print('')
# Which property and bedroom type COMBINATION results in the highest income? Show the property type and number of bedrooms in your output. You don’t need to show the income.
# (I did it using this, there might be other ways.)
print('9: Which property and bedroom type COMBINATION results in the highest income? Show the property type and number of bedrooms in your output. You don’t need to show the income.')
roomtype = round(np.groupby(['type', 'bedrooms'])['price'].mean())
roomtype = roomtype.idxmax()
print(f'Property type: {roomtype[0]}')
print(f'Number of bedrooms: {roomtype[1]}')
print('')
# Create a new column year which is the year from the sales date. Show the head() of your data to confirm this.
# https://www.geeksforgeeks.org/python-pandas-to_datetime/
print('10: Create a new column year which is the year from the sales date. Show the head() of your data to confirm this.')
np['date'] = pd.to_datetime(np['date'], format='%d/%m/%Y')
np['year'] = pd.to_datetime(np['date'], format='%d/%m/%Y').dt.year
print(np.head())
print('')
# Find and show the years (and that year’s income) having a total income of more than $12,500,000 from selling properties.
print('11: Find and show the years (and that year’s income) having a total income of more than $12,500,000 from selling properties.')
groupincome = np.groupby('year')['price'].sum()
groupincome = groupincome.loc[groupincome > 12500000]
print(groupincome)
print('')
# How many houses have been sold after 2015 for a price higher than $800,000?
print('12: How many houses have been sold after 2015 for a price higher than $800,000?')
housesold = np[(np['type'] == 'house') & (np['year'] > 2015) & (np['price'] > 800000)]
print(housesold.shape[0])
print('')
# Find the number of UNIT sales per year for the year range 2015 to 2019. Show the year and number of sales for that year. Show the output from lowest to highest sales.
print('13: Find the number of UNIT sales per year for the year range 2015 to 2019. Show the year and number of sales for that year. Show the output from lowest to highest sales.')
units = np[(np['year'] >= 2015) & (np['year'] <= 2019) & (np['type'] == 'unit')].groupby('year')['type'].count()
units = units.sort_values(ascending=True)
print(units)
