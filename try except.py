#17 try and except (error handling)
# by GHOT AungWinnHtut

x=0;
try:
    if x==0:
        print("x is zero")
except:
    print("some error occure")
    

def oneover(i):
    return 1/i
# print ok but return no result why?
oneover(3)

def oneover(i):
    print(1/i) 
# print ok but return no result why?

oneover(3)

#try except

def oneover(i):
    print(1/i) 
# print ok but return no result why?

try:
    oneover(0)
except:
    print("some error")
    
def oneover(i):
    print(1/i) 
# print ok but return no result why?

try:
    oneover(0)
except ZeroDivisionError:
    print("cannot divided by Zero")
  
 
#exception
 
 
def oneover(i):
    print(1/i) 
# print ok but return no result why?

try:
    oneover(2)
    print(k)  # k is not define
except ZeroDivisionError:
    print("cannot divided by Zero")
    
except TypeError:
    print("Must use Integer")
    
except Exception as e:
    print('name error %s' ,e)
    print(e)
    
    
    
    
    
    
#done  at 260319 5:00pm
    
    
    
    







   
