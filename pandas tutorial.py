import pandas as pd 
"""mydic={"title":["python", "php", "data science"],
       "company":["google", "pinteres", "apple"],
        "location":["usa", "germany", "france"]
       }
table=pd.DataFrame(mydic)
print(table.loc[[0,2]])                #loc for dataframes is used to get a row or more(if more , use a list of indexes!!the result is a Dataframe), it returns a pandas Series
"""
"""
mylist=[1,3,7]
table=pd.Series(mylist, index=['x','y','z'])       #series is like a 1 column table
print(table)
print(table['x'])             #to access a special element using its index
"""
"""
mydic={"day1":450 , "day2":300, "day3":800}        #the keys become the labels
table=pd.Series(mydic, index=["day1", "day2"])      #to access multiple elements   , index
print(table)
"""
"""
mydic={"numbers":[39,45,67], "ages":[83,45,78]}      #0 1 2 3 indexing
table=pd.DataFrame(mydic)
print(table)
"""
#to load files into a dataframe
#table=pd.read_csv("C:\\Users\\Vivo\\Desktop\\data(1).csv")
 #print(table)                                                      this inly prints the first 5 rows and the last 5 rows
#print(table.to_string())                                           use to_string() to print the whole dataframe


#print(pd.options.display.max_rows)                                  to get the max number of rows, you can change the max number : pd.options.display.max_rows= x


# JSON = Python Dictionary
# JSON objects have the same format as Python dictionaries.
table=pd.read_csv("C:\\Users\\Vivo\\Desktop\\data(1).csv")
#print(table.head(10))                                               head only returns the headers and number of rows, default=5
#                                                                     there is also tail method to view the last rows + headers
#   .info() -->  returns more information about the data frame

""""
dropna() method :  it returns a new dataframe and removes all the rows with empty cells(NULL values), does not modify the original DF
if u want to change the original , use dropna(inplace=True)

fillna() method:    it replaces the null value with a value given     df.fillna(130, inplace=True)  -->this replaces all the null values of the data frame
to only replace the null values of 1 column :    df.fillna({"calories"}: x , inplace=True )
you can replace the empty cells with  1-mean  2-median  3-mode  
x=df["calories"].mean()/ .median()/ .mode()

"""

#    df['Date'] = pd.to_datetime(df['Date'], format='mixed')      df.dropna(subset=['Date'], inplace = True)
#    df.loc[7, 'Duration'] = 45
""""
for x in df.index:
  if df.loc[x, "Duration"] > 120:
    df.loc[x, "Duration"] = 120   /         df.drop(x, inplace = True) 

"""
#  df.duplicated() -->   this returns a boolean value for each row 
#  to remove duplicated :   df.drop_duplicates(inplace=True)