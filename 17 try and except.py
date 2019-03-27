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
    
f = open('textt.py' ,'r')
print(f.read())  

# if file was not found , error occured
f = open ('textt.py','r')
print (f.read())

try:
    f = open ('textt.py','r')
    print (f.read())
except:
    f = open ('textt.py','r')
    print('file error')

#show exactly

try:
    f = open ('textt.py','r')
    print (f.read())
except FilenotFoundError as e:
    print('file not found %s' , e)

# with else function
try:
    f = open ('textt.py','r')
    print (f.read())
except FilenotFoundError as e:
    print('file not found %s' , e)

else:
    print(f.read())
    f.close()

#finally if or not error

finally:
    print("finally done")

#if file not found error will be show
#text.txt and text1.txt 
# error handling

# done! at 5:11pm 270319
# Thanks Sir AungWinnHtut



