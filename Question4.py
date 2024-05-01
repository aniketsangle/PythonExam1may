import pandas as pd
import numpy as np

pd.set_option('display.max_rows',500)
pd.set_option('display.max_columns',500)
pd.set_option('display.width',1000)
df =pd.read_excel(r"C:\Users\anike\OneDrive\Desktop\movies_metadata.xlsx")
# print(df)






# SubSques1) write a python program to get the details of the columns title and genres of the dataframe

# print(df.info())
print(df.get('title', 'genres'))






# Subquest2) display the first 10 rows of the dataframe
# print(df.head(10))









# SubQues4) To sort movies on runtime in descending
# print(df.sort_values('runtime', ascending=False))



# Subques5)
print(df.get('title', 'runtime'))


