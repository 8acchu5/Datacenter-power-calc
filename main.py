#This program is used to calculate the Overall power usage and safety of a Datacenter. 
#The user will provide the electrical service voltage and available amperage. 
#They will then provide the number of circuits and their details along with the devices using the circuits. 
#The program will then calculate the wattage available per circuit and the current usage per circuit and in aggregate.


#A function to calculate power from provided voltage and amperage.
def power_calculate(volts, amps):
  power = volts * amps
  return power  

#A Function to check if current wattage use is within 80% of max wattage.
def safety_check(current_watts, max_watts):
  Percent80 = max_watts * 0.8
  if current_watts <= Percent80:
    return True
  else:
    return False  

#Initializing the variables 
Serv_Volts = 0
Serv_Amps = 0
Cir_Count = 0 
Cir_Volts = 0 
Cir_Amps = 0 
Cir_Dev_Count = 0
Cir_Dev_Volts = 0
Cir_Dev_Amps = 0
Current_Cir_Dev_Volts = 0
Current_Cir_Dev_Amps = 0
Current_Cir_Dev_Watts = 0
Max_Serv_Watts = 0 
Current_Serv_Watts = 0 
Max_Cir_Watts = 0  
Current_Cir_Count = 0
Current_Dev_Count = 0 
Output_List = []
Serv_80percent_list = []

# Input electrical service details from user.
# This also checks for safety and validity of the inputs.
while True:
  try:
    Temp_Serv_Volts = int(input("PLease Enter Your Datacenters Electrical Service Voltage in Whole Numbers: "))
    if 0 >= Temp_Serv_Volts:
      print("This is not a Positive Voltage Value. This is not supported")
    else:
      Serv_Volts = Temp_Serv_Volts 
      break
  except ValueError:
    print("Please Follow Directions")  
while True:
  try:
    Temp_Serv_Amps = int(input("Please Enter Your Datacenters Electrical Service Amps in Whole Numbers: "))
    if 0 >= Temp_Serv_Amps:
      print("This is not a Positive Amperage Value. This is not supported")
    else:
      Serv_Amps = Temp_Serv_Amps 
      break
  except ValueError:
      print("Please Follow Directions")
Max_Serv_Watts = power_calculate(Serv_Volts, Serv_Amps)
#print(Max_Serv_Watts)

# Input Circuit Count from user.
# This also checks for safety and validity of the inputs.
while True:
  try:
    Temp_Cir_Count = int(input("Please Enter Your Datacenters Electrical Circuit Count: "))
    if 0 >= Temp_Cir_Count:
      print("This is not a Positive Circuit Count. This is not supported")
    else:
      Cir_Count = Temp_Cir_Count 
      break
  except ValueError:
    print("Please Follow Directions")
# print(Serv_Volts,' ',Serv_Amps, ' ', Cir_Count)

#  Loops until Current Circuit = Circuit Count
while Cir_Count > Current_Cir_Count:
  Current_Cir_Count += 1 
  #print("Current Circuit Count: ", Current_Cir_Count)

# Loop inputs circuit volts from user.
# This also checks for safety and validity of the inputs.
  #Resets varialbe between circuits
                                                                                  
  while True:
    try:
      Temp_Volts = int(input(F'{"Please Enter Circuit "}{Current_Cir_Count}{"s Voltage"}: '))
        #print("circut ", Current_Cir_Count, "s voltage")
#    Tests If Circuit Volts are greater than Service Volts
      if Temp_Volts > Serv_Volts:
        print("Danger this is a Voltage Higher than the Main Service Voltage. This is not Supported")
      elif Temp_Volts <= 0:
        print("This is not a Positive Voltage Value. This is not supported")    
      else:
        Cir_Volts = Temp_Volts 
        break
    except ValueError:
      print("Please Follow Directions")
    #print("passed loop")

# Loop inputs circuit amps from user.
# This also checks for safety and validity of the inputs.
  while True:
    try:
      Temp_Amps = int(input(F'{"Please Enter Circuit "}{Current_Cir_Count}{"s Amperage"}: '))
#      Input Circuit Amps from user 
#      If Circuit Amps are greater than Service Amps
      if Temp_Amps > Serv_Amps:
        print("Danger this is a higher amperage than the main service amperage. This is not supported")
      elif Temp_Amps <= 0:
        print("This is not a Positive Amperage Value. This is not supported")
      else:
        Cir_Amps = Temp_Amps 
        break
    except ValueError:
      print("Please Follow Directions")

# Calls function to calculate the circuits max wattage.
  Max_Cir_Watts = power_calculate(Cir_Volts, Cir_Amps)
  #print(Max_Cir_Watts)

# Input Device Count from user 
# This also checks for safety and validity of the inputs.
  while True:
    try:
      Temp_Dev_Count = int(input(F'{"Please Enter How Many Devices Use Circuit "}{Current_Cir_Count}: '))
      if Temp_Dev_Count <= 0:
        print("This is not a Positive Device Count. This is not supported") 
      else:
        Cir_Dev_Count = Temp_Dev_Count
        break
    except ValueError:
      print("Please Follow Directions")

#  Loops until current device = device count 
  while Cir_Dev_Count > Current_Dev_Count:
    Current_Dev_Count += 1

# Input Device Volts from user 
# This also checks for safety and validity of the inputs.
    while True:
      try:
        Temp_Dev_Volts = int(input(F'{"Please Enter Device "}{Current_Dev_Count}{"s Voltage"}: '))
        if Temp_Dev_Volts != Cir_Volts:
          print("Danger this is not the same voltage as the circuit. This is not supported")
        else:
          Current_Cir_Dev_Volts = Temp_Dev_Volts
          #print(Current_Cir_Dev_Volts)
          break
      except ValueError:
        print("Please Follow Directions")

# Input Device Amps from user
# This also checks for safety and validity of the inputs.
    while True:
      try:
        Temp_Dev_Amps = int(input(F'{"Please Enter Device "}{Current_Dev_Count}{"s Amperage"}: '))
        if Temp_Dev_Amps > Cir_Amps:
          print("Danger this is a higher amperage than the circuit. This is not supported")
        elif Temp_Dev_Amps <= 0:
          print("This is not a Positive Amperage Value. This is not supported")
        else:
          Current_Cir_Dev_Amps = Temp_Dev_Amps
          #print(Current_Cir_Dev_Amps)
          break
      except ValueError:
        print("Please Follow Directions")

# Calls function to calculate current power usage of all devices on the current circuit.
    Current_Cir_Dev_Watts += power_calculate(Current_Cir_Dev_Volts, Current_Cir_Dev_Amps)
    #print(Current_Cir_Dev_Watts)
        #print(Current_Cir_Dev_Watts)

# Adds calculated data to output storage for the current circuit. 
  Output_List.append(Current_Cir_Count)
  Output_List.append(Max_Cir_Watts)
  Output_List.append(Current_Cir_Dev_Watts)
  
# Calls function to check if the current circuit power usage is within 80% of max.
  Safe = safety_check(Current_Cir_Dev_Watts, Max_Cir_Watts)
  if Safe == False:
    Output_List.append("Utilization is over 80%")
  else:
    Output_List.append("Utilization is safetly within 80% of the maximum")

# Updates service usage total for the current circuit.
  Current_Serv_Watts += Current_Cir_Dev_Watts
  #print(Current_Serv_Watts)

# Reset device counter and wattage for next circuit    
  Current_Dev_Count = 0
  Current_Cir_Dev_Watts = 0
  
#Calls function to calculate the safety of the service 
Serv_safe = safety_check(Current_Serv_Watts, Max_Serv_Watts)
if Serv_safe == False:
  Serv_80percent_list.append("Service Utilization is over 80%.")  
else:
  Serv_80percent_list.append("Service Utilization is safetly within 80% of the maximum")

 
#print(Output_List)
#print(Serv_80percent_list)
#print(Current_Serv_Watts)

# Outputs the results
print("Currently Your Datacenter is using ", (Current_Serv_Watts), "Watts out of ", (Max_Serv_Watts), " Watts Avalable")
print(Serv_80percent_list[0])
for x in range(Cir_Count):
  if x == 0:
    y = x
  print("For Circuit ", Output_List[y+0], "The Max Watts are ", Output_List[y+1], " and   the Current Watts are ", Output_List[y+2], ". The ", Output_List[y+3])
  y += 4