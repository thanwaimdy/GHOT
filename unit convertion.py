# unit convertion
# thanks sir AungWinnHtut
# 01042019 1:09pm


#Temperature

#T(℉) = T(℃) x 9/5 + 32
#T(℉) = T(℃) x 1.8 + 32 
# c = (f-32)/1.8

print("""\n
        ###################
        # UNIT CONVERTION #
        ###################
        """)
      


def f():
    fah = input("\nEnter Temperature in °F: ") 
    if fah == 'x':
        exit() 

    else:
        fahrenheit = int(fah)
        celsius = (fahrenheit-32)/1.8
        print("Temperature in °C = ", celsius)
    
def c():
    
    cel = input("\nEnter Temperature in °C: ") 
    if cel == 'x':
        exit() 

    else:
        celsius = int(cel)
        fahrenheit = (celsius*1.8)+32
        print("Temperature in °F = ", fahrenheit)

#Measure

#Miles = kilometer * 0.62137   
#Kilometer = Miles / 0.62137      

def mile():
    mile = input('\nEnter mile: ')
    if mile == 'x':
        exit()
    else:
        mile = int(mile)
        km = (mile / 0.62137)
        print('Kmeter= ' , km)

def km():
    km = input('\nEnter Km: ')
    if km == 'x':
        exit()
    else:
        km = int(km)
        mile = (km * 0.62137)
        print('mile = ' , mile)      
        



# meter to inch   
    
def m2in():
    meters = float(input("\nEnter height in meters:"))
    if km == 'x':
        exit()
    else:
        meters_in_ft = meters // .3048
        meters_in_in = meters_in_ft % 12
        print("The height is", meters_in_ft,"feet and",meters_in_in, "inches")

# power
# 1HP = 746 W
# 1KW = 1/0.746 HP
# 1KW = 1000 W

def hp():
    hosepower = input('\nEnter HosePower: ')
    if hosepower == 'x':
        exit()
    else:
        hosepower = float(hosepower)
        W = (hosepower * 746)
        print('Watt = ' , W , 'W' )
        


def kw():
    kw = input('\nEnter KW: ')
    if kw == 'x':
        exit()
    else:
        kw = float(kw)
        hp = (kw / 0.746)
        print('HosePower = ' , hp ,'HP' )      
"""        

while 1:
    
    operator = input('\nPlease Enter operator: ')
    
    if operator == 'f()':
        result = f()
    elif operator == 'c()':
        result = c()
    elif operator == 'mile()':
        result = mile()
    elif operator == 'km()':
        result = km()
    elif operator == 'm2in()':
        result = m2in()
    else:
        print("wrong operator ")

    print(result)
    
"""   
    
convertion = []
convert = ""
while convert != "shwe":
   print("""\nThe following things are 
what you can do whith this program.
       
       0 = Exit
       1 = fahrenheit
       2 = celsius
       3 = mile
       4 = kilometer
       5 = meter to inch
       6 = hosepower
       7 = kilowatt   	   	
   	   	 """)
   choice = input(" \n Choice : ")
   if choice == "0":
      print ("\n ***GOOD BYE***")
   elif choice == "1":
      print (f())
   elif choice == "2":
      print (c())   
   elif choice == "3":
      print (mile())
   elif choice == "4":
      print (km())
   elif choice == "5":
      print (m2in())
   elif choice == "6":
      print (hp())
   elif choice == "7":
      print (kw())
      
   else:
      print ("\n Hello can't you read English \n yout choice is : ")  , 
      "choice"
      
   
   	  








"""

f()        #fahrenheit
c()        #celsius
mile()     #mile
km()       #kilometer
m2in()     #meter to inch
hp()       #hosepower
kw()       #kilowatt
 
"""

"""
Temperature
f, c
Weight
kg, gm, lb, ounce, mg
Length
mile, km, m, cm, mm, inch, ft
Power
watts, hosepower, kw
Energy
calories, joles, kcal
Velocity
km/hr, miles/hr, m/s, ft/s
Area
sq km, sq miles, sq m, sq cm, sq mm, sq yards
Volume
litre, militre, cubic m, cub mm, cub cm, cub mm, cub ft


"""



