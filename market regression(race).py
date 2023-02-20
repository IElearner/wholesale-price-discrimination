#analyse the market-info impact on quoted price  based on different races
#no-info-0,market-info-1
#consider the listed price factor
import pandas as pd
import statsmodels.api as sm
#different races choose different forms
#1.Market-Asian-regression 2.Market-Black-regression 3.Market-White-regression
file = r'C:\Users\mac\Desktop\homework data\Analysis of the information\Market-White-regression.xlsx'
data = pd.read_excel(file)
data.columns = ['discount', 'info','listed_price']
x = sm.add_constant(data.iloc[:,1:])
y = data['discount']
model = sm.OLS(y, x)
result = model.fit()
print(result.summary())