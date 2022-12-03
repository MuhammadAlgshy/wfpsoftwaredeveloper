from getData import getData
from settings import *
import time
from scheduleTask import scheduleTask
def main():
 while True:
    try:
        print("Welcome to WFP Software Develop App ~ Muhammad Algshy \n |> Programes: \n \
          1- Test DB  \n \
          2- Test API \n \
          3- Test Schedule Function \n \
          3- Run API without Schedule \n \
          4- Exit!")

        # if I am using Python 10 I could use Match function to create the switch
        # Get user input
        programe= int(input("Please select one of the programes: "))
        # Run the programme
        if programe == 1:
          testDB()
        if programe == 2:
          getData("")
        if programe == 3:
          scheduleTask("")
        if programe == 4:
          print("Thank you for using our system! \n looking forward to see you soon! ^_^")
          exit()  
    except ValueError:
          print('Please select one of the programes')
          time.sleep(1)
    # Schedule the job to run every day at 6:00
   # 
    # For Testing you can try the 10 Sec 
    # schedule.every(10).seconds.do(getData)
    
    # Run the job continuously
    # while True:
    #     schedule.run_pending()
    #     time.sleep(1)

if __name__ == '__main__':
    main()





