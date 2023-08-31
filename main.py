#This is the traffic light driver
from threading import Thread
from queue import Queue
import signal
from time import sleep

from light import Light

q = Queue()
_sentinel = object()

#Validate light times. Valid options are 1-10s for all the lights
def light_times_valid(red, yellow, green):
    valid = True
    if red not in range (1,10):
        print("Valid values for red light are 1-10seconds")
        valid = False
    if green not in range (1,10):
        print("Valid values for red light are 1-10seconds")
        valid = False 
    if yellow not in range (1,10):
        print("Valid values for red light are 1-10seconds")
        valid = False      
    return valid

def sigint_handler(sig, frame):
    #print('In signal handler..You pressed Ctrl+C!,')
    #Indicate to the thread to stop traffic light
    q.put(_sentinel)
    return    


def main():

    print(f"\033[96m This is traffic light application.")
    
    while True:
        red_time = int(input("Enter how long in seconds(valid value are 1-10), red stays? "))
        yellow_time = int(input("Enter how long in seconds(valid value are 1-10), yellow stays? "))
        green_time = int(input("Enter how long in seconds(valid value are 1-10), green stays? "))
        if (not light_times_valid(red_time, yellow_time, green_time,)):
            print("Light times are not valid. Try again")
        else:
            break 

    light = Light(red_time, yellow_time, green_time)
 
    t = Thread(target=light.display, args =(q, _sentinel, ))

    print(f"\033[92m At any point press ctrl+c to exit traffic light application")
    #Sleep for a few seconds for user to read console message before light rendering
    sleep(3)
    signal.signal(signal.SIGINT, sigint_handler)
    t.start()
    t.join()

if __name__ == "__main__":
    main()