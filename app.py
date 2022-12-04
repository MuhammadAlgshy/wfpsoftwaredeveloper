from getData import getData, select_Cfii_calcualtion
from settings import *
import time
from scheduleTask import scheduleTask
import datetime

def main():
 while True:
    try:
        print("Welcome to WFP Software Develop App ~ Muhammad Algshy \n |> Programes: \n \
          1- Test DB  \n \
          2- Test API \n \
          3- Test Schedule Function \n \
          4- Run API without Schedule \n \
          5- Select Data \n \
          0- Exit!")

        # if I am using Python 10 I could use Match function to create the switch
        # Get user input
        programe= int(input("Please select one of the programes: "))
        # Run the programme
        if programe == 1:
          connectionDB("Test")
        if programe == 2:
          getData("")
        if programe == 3:
          scheduleTask("")
        if programe == 4:
          print("1 -> Use defualt(ISO3 = AFG, Start date = 2022-12-01, End date = 2022-12-02 ) \n2 -> Enter your own data")
          scenario= int(input("Scenario: "))
          if scenario ==1:
               getData("production")
          elif scenario==2:
            Iso3_entry = input('Enter ISO3: ')
            start_date_entry = input('Enter a start date in YYYY-MM-DD format: ')
            year, month, day = map(int, start_date_entry.split('-'))
            start_date = datetime.date(year, month, day)
            end_date_entry = input('Enter a end date in YYYY-MM-DD format: ')
            year, month, day = map(int, end_date_entry.split('-'))
            end_date = datetime.date(year, month, day)
            print("ISO3 => "+Iso3_entry+"\nStart Date =>" + str(start_date) +"\nEnd Date =>" + str(end_date))
            getData("production", Iso3_entry, start_date, end_date )
        if programe == 5:
          select_Cfii_calcualtion()
        if programe == 0:
          print("Thank you for using our system! \n looking forward to see you soon! ^_^")
          exit()  
    except ValueError:
          print('Please select one of the programes')
          time.sleep(1)

if __name__ == '__main__':
    main()





