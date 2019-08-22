class student:
    count=+1
    def __init__(self):
        student.count = student.count + 1
    
    def setname(self, name):
        #pass
        self.name = name
        
    def getname(self):
        return self.name
        
    def printname(self):
        print(self.name)
        
        
    def setage(self, age):
        #pass
        self.age = age
        
    def getage(self):
        return self.age
        
    def printage(self):
        print(self.age)   
        
        
    def setmajor(self, major):
        #pass
        self.major = major
     
    def getmajor(self):
        return self.major
        
    def printmajor(self):
        print(self.major)
        
    def setfather_name(self, father_name):
        #pass
        self.father_name = father_name
     
    def getfather_name (self):
        return self.father_name
        
    def printfather_name (self):
        print(self. father_name)  
    
  
koko = student()
koko.setname("koko")
print(koko.name)
koko.setage("28")
print(koko.age)
koko.setmajor("English")
print(koko.major)
koko.setfather_name("U Myo Gyi")
print(koko.father_name)
print(koko.count)

mgmg = student()
mgmg.setname("mgmg")
print(mgmg.name)
mgmg.setage("35")
print(mgmg.age)
mgmg.setmajor("Computer")
print(mgmg.major)
mgmg.setfather_name("U Han Htoo")
print(mgmg.father_name)
print(mgmg.count)

agag = student()
agag.setname("agag")
print(agag.name)
agag.setage("48")
print(agag.age)
agag.setmajor("Electrical")
print(agag.major)
agag.setfather_name("U Tet Toe")
print(agag.father_name)
print(agag.count)





    