#analysis of the country impact on price discimination  SA-0,US-1

import pandas as pd
import statsmodels.api as sm
#different conditions choose different forms
#1.All-info-country 2.No-info-country 3.Both-onfo-country 4.Market-info-country 5.Social-info_country
file = r'C:\Users\mac\Desktop\homework data\Analysis of the country\All-info-country.xlsx'
data = pd.read_excel(file)
data.columns = ['discount', 'country']
x = sm.add_constant(data.iloc[:,1:])
y = data['discount']
model = sm.OLS(y, x)
result = model.fit()
print(result.summary())