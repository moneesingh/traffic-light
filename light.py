import time
from queue import Queue, Empty

#colors = {"GREEN":"green", "YELLOW":"yellow", "RED":"red"}

#ASCII color codes
class color:
    YELLOW = '\033[93m'
    RED = '\033[91m'
    GREEN = '\033[92m'

class Light:
    shape = """\

        , - ~ ~ ~ - ,
     , ' ###########  ,
   ,   ##############   ,
  ,   ################   ,
 ,   ##################   ,
 , #####################  ,
 ,  ###################   ,
  ,  ##################  ,
   ,  ################ ,
     , ############# ,'
       ' - _ _ _ , '


                """

    def __init__(self, red_time, yellow_time, green_time):
        self.red_time = red_time
        self.yellow_time = yellow_time
        self.green_time = green_time

    def display(self, in_q, sentinel):
        while True:
            print(f"{color.RED}{self.shape}")
            time.sleep(self.red_time)

            print(f"{color.GREEN}{self.shape}")
            time.sleep(self.green_time)

            print(f"{color.YELLOW}{self.shape}")
            time.sleep(self.yellow_time)

            try:
                #Using non-blocking get with 1 ms
                data = in_q.get(False) 
            except Empty:
                data = None
                continue
            # Check for termination
            if data is sentinel:
                print("Exiting Traffic Light Simulator")
                return


    def __str__(self):   
        print("Light's Iniitial color ", self.initial_color)  
        print("Light's Current color ", self.current_color) 
        print("Light's Next color ", self.next_color)        
        return f"Red:{self.red_time}, Yellow:{self.yellow_time}, Green:{self.green_time}"    
