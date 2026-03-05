class overload:
    def __init__(self,var):
        self.var=var
    def __gt__(self, other):
        if(self.var > other.var):
            return "obj1 is greater than obj2"
        else:
            return "obj1 is lesser than obj2"
    def __it__(self, other):
        if (self.var < other.var):
            return "obj1 is lesser than obj2"
        else:
            return "obj1 is greater than obj2"
        
obj1 = overload(10)
obj2 = overload(20)
print("passed values :", obj1.var, obj2.var)
print(obj1 > obj2)
obj3 = overload(50)
obj4 = overload(50)
print("passed values :", obj3.var, obj4.var)
print(obj3 < obj4)