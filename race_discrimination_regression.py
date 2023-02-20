#analyse if there is a siginificant difference on price discount between Asian and White (or Asian and Black or Black and White)
import pandas as pd
import statsmodels.api as sm
#choose the form first
#1.No-info-Asian and White(Asian-0,White-1) 2.No-info-Asian and Black(Asian-0,Black-1) 3.No-info-White and Black(White-0,Black-1)
file = r'C:\Users\mac\Desktop\homework data\Analysis of the race\No-info-Asian and White.xlsx'
data = pd.read_excel(file)
data.columns = ['Discount', 'Race','Listed price']
x = sm.add_constant(data.iloc[:,1:])
y = data['Discount']
model = sm.OLS(y, x)
result = model.fit()
print(result.summary())