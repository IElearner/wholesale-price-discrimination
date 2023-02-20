import pandas as pd
import statsmodels.api as sm
#regress without the interaction with races
file = r'C:\Users\mac\Desktop\homework data\Analysis of the race\Multiple variables regression.xlsx'
data = pd.read_excel(file)
data.columns = ['Discount', 'GoodSupplierYears','TransactionLevel','No_ofTransaction','ResponseRate','No_ofReviews','Listed_Price'
    ,'Dummy1','Dummy2']
x = sm.add_constant(data.iloc[:,1:7])
y = data['Discount']
model = sm.OLS(y, x)
result = model.fit()
print(result.summary())
