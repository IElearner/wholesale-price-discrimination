#analyse if social information helps to decline the price discrmination towards the White
import pandas as pd
import statsmodels.api as sm
#choose the form first
#1.social-info-Asian and White(Asian-0,White-1) 2.social-info-Black and White(Black-0,White-1)
file = r'C:\Users\mac\Desktop\homework data\Analysis of the information\social-info-Black and White.xlsx'
data = pd.read_excel(file)
data.columns = ['Discount', 'Race','Listed_price']
x = sm.add_constant(data.iloc[:,1:])
y = data['Discount']
model = sm.OLS(y, x)
result = model.fit()
print(result.summary())