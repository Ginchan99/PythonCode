import pandas as pd
#Create series
obj=pd.Series([1,"Tushti",3,"Prateek"])
print("obj",obj)
obj2=pd.Series([1,"Tushti",3,"Prateek"],index=['a','b','c','d'])
print("obj2",obj2)
#dictionary into series
marks = {'rohit':100,'tushti':102,'prateek':103,'meenakshi':104}
marksDF = pd.Series(marks)
print("marksDF",marksDF)
#reducing the value of rohit by 1
marksDF['rohit'] = marksDF['rohit'] - 1
print("marksDF",marksDF)


marksDF[marksDF<=100] = 102
print("marksDF",marksDF)
#finding whether value is in list or not
#'tushti' in marksDF
marksDF = marksDF/10
print("marksDF",marksDF)
marksDF = marksDF**2
print("marksDF",marksDF)
#add new student
marksDF['newstd'] = 82
print("marksDF",marksDF)

#Delete new student
marksDF = marksDF.drop('newstd')
print("marksDF",marksDF)