class shape(object):
    def __init__(self, nam=None, ol=None, bc=None):
        self.name = nam
        self.outline = ol
        self.background = bc
    @property
    def Name(self):
        return self.name
    @Name.setter
    def Name(self,nam):
        self.name = nam
    @property
    def Outline(self):
        return self.outline
    @Outline.setter
    def Outline(self,ol):
        self.outline = ol
    @property
    def BackgroundColor(self):
        return self.background
    @BackgroundColor.setter
    def BackgroundColor(self,bc):
        return self.background
    def __str__(self):
        return f"Name:{self.Name}, Outline:{self.Outline}, BackgroundColor:{self.BackgroundColor}"
    

class square(shape):
    def __init__(self, nam, ol, bc, sl):
        super().__init__(nam, ol, bc)
        self.length = sl
    @property
    def Length(self):
        return self.length
    @Length.setter
    def Length(self,sl):
        self.length = sl
    def __str__(self):
        return f"{super().__str__()},length:{self.Length},area ={self.area()}"
    def area(self):
        return self.Length ** 2

class rectangle(square):
    def __init__(self, nam, ol, bc, ln, wd):
        super().__init__(nam, ol, bc, ln)
        self.width = wd
    @property
    def Width(self):
        return self.width
    @Width.setter
    def Width(self,wd):
        self.width = wd
    def __str__(self):
        return f"{super().__str__()}, width:{self.Width},area = {self.area()}"
    def area(self):
        return self.Length * self.Width
class Circle(shape):
    def __init__(self,nam,ol,bc,r):
        super().__init__( nam,ol,bc)
        self.radius = r
    @property
    def Radius(self):
        return self.radius
    @Radius.setter
    def Radius(self,r):
        self.radius = r
    def area(self):
        return (3.14 *(self.Radius**2))
    def __str__(self):
        return f"{super().__str__()},Radius:{self.Radius},area={self.area()}"
class Ellipse(shape):
    def __init__(self, nam, ol, bc,hr,vr):
        super().__init__(nam, ol, bc)
        self.horizontal_radius = hr
        self.vertical_radius = vr
    @property 
    def Hr(self):
        return self.horizontal_radius
    @Hr.setter
    def Hr(self,hr):
        self.horizontal_radius = hr
    @property
    def Vr(self):
        return self.vertical_radius
    @Vr.setter
    def Vr(self,vr):
        self.vertical_radius = vr
    def area(self):
        return ((3.14)*(self.Hr)*(self.Vr))
    def __str__(self):
        return f'{super().__str__()},horizontal radius:{self.Hr},vettical radius:{self.Vr},area={self.area()}'
class Traingle(shape):
    def __init__(self, nam, ol, bc,s1,s2,s3):
        super().__init__(nam, ol, bc)
        
        self.side1 = s1
        self.side2 = s2
        self.side3 = s3
    @property
    def Side1(self):
        return self.side1
    @Side1.setter
    def Side1(self,s1):
        self.side1 = s1
    @property
    def Side2(self):
        return self.side2
    @Side2.setter
    def Side2(self,s2):
        self.side2 = s2
    @property
    def Side3(self):
        return self.side3
    @Side3.setter
    def Side3(self,s3):
        self.side3 = s3
    def is_valid(self):
        if self.Side1 + self.Side2 > self.Side3 and self.Side1 + self.Side3 > self.Side2 and self.Side3 + self.Side2 > self.Side1:
            return True
        else:
            return False
    def __str__(self):
        return f'{super().__str__()},side-1={self.Side1},side-2={self.Side2},side-3={self.Side3},{self.area()}'
    def area(self):
        if self.is_valid():
            if self.Side1 == self.Side2 == self.Side3 :
                return (f'area of Equilateral traingle:{((3**0.5)/(4))*self.Side1**2}')
            elif  self.Side1 == self.Side2 or self.Side1 == self.Side3 or self.Side2 == self.Side3:
                # a = samesides and b = differentside and  Area = 1/2[a^2-b^2/2]*b
                
                if self.Side1 == self.Side2:
                    return (f'area of Isoscles Traingle:{(((self.Side2**2)-((self.Side3**2)/4))**0.5)*self.Side3/2}')
                elif self.Side1 == self.Side3:
                    return (f'area of Isoscles Traingle:{(((self.Side1**2)-((self.Side2**2)/4))**0.5)*self.Side2/2}')
                else:
                   return (f'area of Isoscles Traingle:{(((self.Side2**2)-((self.Side1**2)/4))**0.5)*self.Side1/2}')
            else:
                p = (self.Side1 + self.Side2 + self.Side3)/2
                return(f'area of scalene traiangle {((p *(p-self.Side1))*(p-self.Side2)*(p-self.Side3))*0.5}')
        else:
            return 'invalid Triangle'
class Canvas:
    def __init__(self,name=None,ol=None,bc=None):
        self.name = shape(name)
        self.ol = shape(ol)
        self.bc = shape(bc)
    def area(self):
        pass
    def show():
        a=[]
        a.append(rectangle('rectangle', True, 'blue', 3, 4))
        a.append(square('square', False, 'golden', 5))
        a.append(Ellipse('Ellipse',True,'yellow',12,15))
        a.append(square('square', False, 'red', 15))
        a.append(rectangle('rectangle', True, 'blue', 3, 4))
        a.append(Circle('circle',True,'Blue',23))
        a.append(square('square', False, 'golden', 5))
        a.append(Traingle('Traingle',True,'Purple',12,12,23))
        p=1        
        for i in range(len(a)):
            
            print(f'{a[i]} at position {p}')
            p=p+5
        



def main():
    
    Canvas.show()


main()
