class circle:
    
    def __init__(self,r):
        self.r = r
    
    def getr(self,r):
        self.r = r
        
    def geta(self):
        self.a = 3.143*self.r*self.r
        return self.a
        
    def printa(self):
        print(str(self.geta()))
    
c1 = circle(3)
c1.printa()