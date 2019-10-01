#by eyob muktar
#works only for the years between 1900&2100
#after that the leap years of eth & greg calender wont sync
import sys

DAYDIFFERENCE=2810 #manually calculated day difference b/n eth & gregorian calender
DAYSINAYEAR=365
MONTHS=[31,28,31,30,31,30,31,31,30,31,30,31] #no of days in gregorian calender months



day = int(input('Enter the day: '))
month = int(input('Enter the month: '))
year = int(input('Enter the year: '))

def leapyears(): 
    if (month>1):#add current year if february has passed
        leapyears=year//4
    else: #leave the current year if february hasnt passed
        leapyears=(year-1)//4
    return leapyears

        
def daysInLastYear():
    daysInLastYear=0
    for i in range(month-1):
        daysInLastYear+=MONTHS[i]
    return (daysInLastYear+day)


totalDays = ((year-1)*365)+leapyears()+daysInLastYear()
ethTotalDays = totalDays-DAYDIFFERENCE
ethLeapYears = ethTotalDays//(4*365)
ethTotalDays -= ethLeapYears
ethYear = (ethTotalDays//365)+1    
ethDaysOfYear = ethTotalDays%365
flag = True#to use for the leap year


if(ethYear%4==0):#in case of leap years
    if(ethDaysOfYear==0):
        ethYear-=1
        ethDay=6
        ethMonth=13
        flag=False
   ## else:
        ##ethDaysOfYear-=1
if(flag):
    if(ethDaysOfYear%30==0):
        if(ethDaysOfYear==0):
            ethDay=5
            ethMonth=13
            ethYear-=1
        else:
            ethMonth=(ethDaysOfYear//30)
            ethDay=30       
    else:
        ethMonth=(ethDaysOfYear//30)+1
        ethDay=ethDaysOfYear%30


print(ethDay,"/",ethMonth,"/",ethYear," EC")    









