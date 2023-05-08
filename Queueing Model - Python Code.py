import numpy as np
import random 
import sys

#path = 'C:/Users/Dell-PC/Desktop/Outputfile.txt'
#sys.stdout = open(path, 'w')

def Sort_Future_event_list(List):
    for i in range(0,len(List)):
        for j in range(0,len(List)-i-1):
            if(List[j][1] > List[j+1][1]):
                value = List[j]
                List[j] = List[j+1]
                List[j+1] = value 
            
def Generate_interarrival():
    return random.expovariate(3)
      
def Generate_service_time():
    return random.expovariate(0.5)

def Add_to_List(Event):
    Customer.append(Event[0])
    Arrival.append(Event[1])
    

Server_state = 0

Future_event_list = []
Queue = []
Waiting_time = []
Response_time = []
Simulation_time = []
Number_Queue = []

Customer = []
Arrival = []
Departure = []


Clock = 0
Arrival_No = 0
Departure_No = 0



Number_in_queue = 0
Dropped_arrival = 0

Queue_capacity = 49

# Schedule the first arrival
Arrival_time = Clock + Generate_interarrival()
Arrival_No += 1
Event_list = ["Customer : " + str(Arrival_No), Arrival_time, "Arrival"]
Add_to_List(Event_list)

Future_event_list.append(Event_list)

print("***********************************************************************************************************************")
for i in range(100):
     print("For iteration : " + str(i))
     print("-----------------------------------------------------------------------------------------------------------------------")
     print("Future Event List :",Future_event_list)
     current_event = Future_event_list[0]
     print("Current Event : " , current_event)
     Customer_No = current_event[0]
     Clock = current_event[1]
     Simulation_time.append(Clock)
     print("Current Time :" , Clock)
     print("Current Customers in the Queue" ,Number_in_queue)
     Number_Queue.append(Number_in_queue)
     #print("Customers in the Queue" , Queue)
     if "Arrival" in current_event:
         Arrival_No += 1
         if Number_in_queue < Queue_capacity:
             #Number_in_queue += 1
             Arrival_time = Clock + Generate_interarrival()
             Event_list = ["Customer : " + str(Arrival_No), Arrival_time, "Arrival"]
             Add_to_List(Event_list)
             Future_event_list.append(Event_list)
             Sort_Future_event_list(Future_event_list)
             if Server_state == 0:
                 # Service
                 Server_state = 1
                 Future_event_list.remove(current_event)
                 Departure_time = Clock + Generate_service_time()
                 Response = Departure_time - (Departure_time - Clock)
                 Response_time.append(Response)
                 Event_list = [str(Customer_No), Departure_time, "Departure"]
                 Future_event_list.append(Event_list)
                 Sort_Future_event_list(Future_event_list)
             else:
                 Number_in_queue += 1
                 Queue.append(current_event)
                 Sort_Future_event_list(Queue)
                 Future_event_list.remove(current_event)
                 
         else:
             Dropped_arrival += 1
     if "Departure" in current_event:
         Current_clock = current_event[1]
         Departure.append(current_event[1])
         Future_event_list.remove(current_event)
         Departure_No += 1
         Server_state = 0
         if Number_in_queue != 0:
             # Service
             Server_state = 1
             Number_in_queue -= 1
             Event_queue = Queue[0]
             Queue_Customer_No = Event_queue[0]
             Waiting = Current_clock - Event_queue[1]
             Waiting_time.append(Waiting)
             Departure_time = Current_clock + Generate_service_time()
             Response = Departure_time - (Departure_time - Current_clock)
             Response_time.append(Response)
             Event_list = [str(Queue_Customer_No), Departure_time, "Departure"]
             Future_event_list.append(Event_list)
             Sort_Future_event_list(Future_event_list)
             Queue.remove(Event_queue)
         else:
             Server_state = 0
             
print("-----------------------------------------------------------------------------------------------------------------------")            
print("Final Future Event List : " ,Future_event_list)
print("Customers in the Queue" , Queue)


print("-----------------------------------------------------------------------------------------------------------------------")
print("Number of Arrivals : " , Arrival_No)
print("Number of Departure : " , Departure_No)
print("Number of Customers in the Queue" , Number_in_queue)
print("Number of Dropped arrivals : " , Dropped_arrival)

Sum_Weighting_time = 0
for i in range(len(Waiting_time)):
    Sum_Weighting_time += Waiting_time[i]
    
Sum_Response_time = 0
for i in range(len(Response_time)):
    Sum_Response_time += Response_time[i]
    
print("-----------------------------------------------------------------------------------------------------------------------")
print("Simulation has ended at ==> " + str(Clock))
print(" Average number of Waiting time ==> " + str(Sum_Weighting_time / Clock) )
print(" Average Response time ==> " + str(Sum_Response_time / Arrival_No) )
print(" Average number of Waiting Customers in the system ==> " + str((Number_in_queue / 3) + 0.5 ))
print("Blocking probability  ==> " , float(Dropped_arrival) / Arrival_No)

print("-----------------------------------------------------------------------------------------------------------------------")
print("Customers :")
print(Customer)
print("\n")
print("Arrivals : ")
print(Arrival)
print("\n")
print("Departures : ")
print(Departure)

# importing the required module 
import matplotlib.pyplot as plt 
  
# plotting the points  
plt.plot(Simulation_time ,Number_Queue , '-ok') 
    
# naming the x axis 
plt.xlabel('x - axis: Simulation Time') 
# naming the y axis 
plt.ylabel('y - axis: Number Queue') 
    
# giving a title to my graph 
plt.title('The Graph for the Simulation!') 
    
# function to show the plot 

plt.show()

#sys.stdout.close() 

                
             
             
         
    