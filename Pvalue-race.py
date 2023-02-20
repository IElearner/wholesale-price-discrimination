#calculate the mean of discount and p value between each two races under No-info condition
import numpy as np
import pandas as pd
from scipy import stats
data1 = pd.read_excel(r'C:\Users\mac\Desktop\homework data\Analysis of the race\calculate p value.xlsx')
Asian = data1['Asian'].tolist()            #turn the column into a list
Asian = [a for a in Asian if a == a]      #remove the nan figure
Black = data1['Black'].tolist()
Black = [b for b in Black if b == b]
White = data1['White'].tolist()
White = [c for c in White if c == c]
discount_asian = np.mean(Asian)
discount_black = np.mean(Black)
discount_white = np.mean(White)
t1,p_Asian_White = stats.ttest_ind(Asian,White)
t2,p_Black_White = stats.ttest_ind(Black,White)
t3,p_Asian_Black = stats.ttest_ind(Asian,Black)
print(f"the p value of AW,BW,AB under no-info are:{p_Asian_White,p_Black_White,p_Asian_Black}")
print(f"the average discount of Asian,Black,White under no-info are:{discount_asian,discount_black,discount_white}")

##calculate the mean of discount and p value under the market information comparing with no information
data2 = pd.read_excel(r'C:\Users\mac\Desktop\homework data\Analysis of the information\Market-info comparison.xlsx')
All_no = data2['All-No'].tolist()        #turn the column into a list
All_no = [x for x in All_no if x == x]   #remove the nan figure
Asian_market = data2['Asian-Market'].tolist()
Asian_market = [a for a in Asian_market if a == a]
Black_market = data2['Black-Market'].tolist()
Black_market = [b for b in Black_market if b == b]
White_market = data2['White-Market'].tolist()
White_market = [c for c in White_market if c == c]
All_market = data2['All-Market'].tolist()
All_market = [d for d in All_market if d == d]
discount_all_no = np.mean(All_no)
discount_asian_market = np.mean(Asian_market)
discount_black_market = np.mean(Black_market)
discount_white_market = np.mean(White_market)
discount_all_market = np.mean(All_market)
t4,p_Asian_no_market = stats.ttest_ind(Asian,Asian_market)
t5,p_Black_no_market = stats.ttest_ind(Black,Black_market)
t6,p_White_no_market= stats.ttest_ind(White,White_market)
t7,p_All_no_market= stats.ttest_ind(All_no,All_market)
print(f"the average discount of All data under no-info are:{discount_all_no}")
print(f"the average discount of Asian,Black,White,All data under market-info are:{discount_asian_market,discount_black_market,discount_white_market,discount_all_market}")
print(f"the p value(no-market) of Asian,Black,White,All data are:{p_Asian_no_market,p_Black_no_market,p_White_no_market,p_All_no_market}")
##calculate the mean of discount and p value under the social information comparing with no information
data3= pd.read_excel(r'C:\Users\mac\Desktop\homework data\Analysis of the information\Social-info comparison.xlsx')
Asian_social = data3['Asian-Social'].tolist()
Asian_social = [a for a in Asian_social if a == a]
Black_social = data3['Black-Social'].tolist()
Black_social = [b for b in Black_social if b == b]
White_social = data3['White-Social'].tolist()
White_social = [c for c in White_social if c == c]
All_social = data3['All-Social'].tolist()
All_social = [d for d in All_social if d == d]
discount_asian_social = np.mean(Asian_social)
discount_black_social = np.mean(Black_social)
discount_white_social = np.mean(White_social)
discount_all_social = np.mean(All_social)
t8,p_Asian_no_social = stats.ttest_ind(Asian,Asian_social)
t9,p_Black_no_social = stats.ttest_ind(Black,Black_social)
t10,p_White_no_social= stats.ttest_ind(White,White_social)
t11,p_All_no_social = stats.ttest_ind(All_no,All_social)
print(f"the average discount of Asian,Black,White,All under social-info are:{discount_asian_social,discount_black_social,discount_white_social,discount_all_social}")
print(f"the p value(no-social) of Asian,Black,White,All data are:{p_Asian_no_social,p_Black_no_social,p_White_no_social,p_All_no_social}")