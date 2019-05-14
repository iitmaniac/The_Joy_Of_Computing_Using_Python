# -*- coding: utf-8 -*-
"""
Created on Tue May 14 14:36:28 2019

@author: Shrikant Tambe
"""
#Here we are finding the trimmed mean and plotting it with meadian on the graph.

surveydata = [10,89,220,56465,52,5,25,52,56321,51,43,45,56,5,4,4,8,46,545,54,51,545,245,51,54,565,665,61,58,85]  #Random given list.

from statistics import mean

newsurverydata = surveydata.copy() #Copying the above given sorted list for later purposes.
normalmean = mean(newsurverydata)

outliers = int(0.1*len(surveydata)) # Here we are finding the 10% count of the elements present in the above given list.
surveydata.sort() # We are sorting the above given list.

surveydata = surveydata[outliers:] #Trimming the 10% elements (floor value only) from the starting of the "original sorted list".
surveydata = surveydata[:len(surveydata)-outliers] #Trimming the 10% elements (floor value only) from the ending of the above given "modified" sorted list.


avg = mean(surveydata) #finding the 10% trimmed mean for the 'Survey Data List' using mean function from statistics library.
print("The 10% trimmed mean for the 'Survey Data List' using mean function from statistics library is",avg)
print()

from scipy import stats
print(newsurverydata)
print()
newavg = stats.trim_mean(newsurverydata, 0.1)  #finding the 10% trimmed mean for the 'New Survey Data List' using stats.trim_mean function from stats library
print("The 10% trimmed mean for the 'New Survey Data List' using stats.trim_mean function from stats library is",newavg)



import matplotlib.pyplot as plt
import statistics

yaxs = []                  #Creating empty list yaxis for the 'y-axis' with respect to given 'x-axis'.


# b-- means blue dashed line.
# b0 means blue dotted line.
# bs means blue square.
# b^ means blue triangle.
# you can replace 'b' with 'r' OR with 'g' in the above terminologies.
# 'r' means red and 'g' means green.

plt.xlabel("This is X-axis")
plt.ylabel("This is Y-axis")
plt.plot(surveydata,'b--')  #plotting the 'surveydata (blue dashed line ) on x-axis WITHOUT PLOTTING the y-axis'.Here 'y-axis' is assumed automatically by matplotlib, if not given explicitly.
for i in surveydata:
    yaxs.append(20)    
plt.plot(surveydata, yaxs, 'r--')                       #plotting the 'surveydata (red dashed line) on x-axis WITH PLOTTING the y-axis'.Here for plotting 'y-axis'we are taking 'y-axis' with any constant value. ex: here we are taking '20' as contant value for 'y-axis' in matplotlib.
plt.plot([avg],[yaxs],'ro')                             #plotting the 'trimmed average' or trimmed mean value (red dot) of the trimmed data list on x-axis WITH PLOTTING the y-axis'.Here for plotting 'y-axis'we are taking 'y-axis' with any constant value. ex: here we are taking '20' as contant value for 'y-axis' in matplotlib.
plt.plot([normalmean], [yaxs],'gs')                     #plotting the 'actual average' or original mean value (green square) of the original given data list on x-axis WITH PLOTTING the y-axis'.Here for plotting 'y-axis'we are taking 'y-axis' with any constant value. ex: here we are taking '20' as contant value for 'y-axis' in matplotlib.
plt.plot([statistics.median(surveydata)],[yaxs],'g^')   #plotting the 'median' value (green triangle) on x-axis WITH PLOTTING the y-axis'.Here for plotting 'y-axis'we are taking 'y-axis' with any constant value. ex: here we are taking '20' as contant value for 'y-axis' in matplotlib.


print()                                 #Please note that even this is the last line written in the program, but this will be displayed before (above) the (matplotlib) graph plotted on Console.
print("Thanks for using this service!") #Please note that even this is the last line written in the program, but this will be displayed before (above) the (matplotlib) graph plotted on Console.
