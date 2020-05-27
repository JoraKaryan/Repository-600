
import math

#ex-1
class Circle:
    def __init__(self, radius, color):
        self.radius = radius
        self.color = color
        if not (isinstance(radius, float) or isinstance(radius, int)):                
            raise Exception("Please type an integer or a float number")

        if not isinstance(color, str):
            raise Exception("Please type a string")

    def area(self):
        return math.pi * (self.radius)**2

    def circumference(self):
        return 2 * math.pi * self.radius


    def __add__(self, x):
        ob = Circle(10, "red")
        ob1 = Circle(10, "brown")                               #################  2 shrani gumar  
        sum_of_circumference = self.circumference() + x.circumference()
        return sum_of_circumference

obj = Circle(10, "red")
obj1 = Circle(10.01, "yellow")
print (obj1.circumference())
print(obj.__add__(obj1))



#ex-2


class RomanNumber:
    def __init__(self, roman_number):
        self.number = roman_number

        if not isinstance(roman_number, str):
            raise Exception("Please type a string")
        
    def get_num(self):
        return self.number
    
    def set_num(self, num1):
        self.number = num1

    def convert_to_num(self):
        num_dict = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        result = 0
        for key,value in enumerate(self.number):
            if (key+1) == len(self.number) or num_dict[value] >= num_dict[self.number[key+1]]:
                result += num_dict[value]
            else:
                result -= num_dict[value]
        return result


    def convert_to_roman(self, num):
            val = [
                1000, 900, 500, 400,
                100, 90, 50, 40,
                10, 9, 5, 4,
                1
                ]
            syb = [
                "M", "CM", "D", "CD",
                "C", "XC", "L", "XL",
                "X", "IX", "V", "IV",
                "I"
                ]
            roman_num = ''
            i = 0
            
            while  num > 0:
                for _ in range(num // val[i]):
                    roman_num += syb[i]
                    num -= val[i]
                i += 1
            return roman_num

        
    def __mul__(self, x):
        a = RomanNumber("IV")
        b = RomanNumber("X")
        number = self.convert_to_num() * x.convert_to_num()
        return self.convert_to_roman(number)

    
    def __truediv__(self, x):
        a = RomanNumber("IV")
        b = RomanNumber("X")
        number = self.convert_to_num() // x.convert_to_num()
        return self.convert_to_roman(number)
    
obj1 = RomanNumber("X")
obj2 = RomanNumber("II")

print (obj1.convert_to_num())
print (obj1.__mul__(obj2))
print (obj1.__truediv__(obj2))


#ex-3

class Person:
    def __init__(self,name,last_name,age,gender,student,password): 
        self.name=name 
        self.last_name = last_name
        self.age = age
        self.gender = gender
        self.__password = password
        
        assert isinstance(student, bool), "Student attribute takes values True or False"                                    #assert ogtagorcel
        self.student = student

        assert isinstance(name, str), "Last_name attribute takes values String"
        self.name = name

        assert isinstance(last_name, str), "Last_name attribute takes values String"
        self.last_name = last_name

        assert isinstance(age, int), "Age attribute takes values Integer"
        self.age = age
        
        assert isinstance(gender, str), "Gender attribute takes values String"
        self.gender = gender

        assert isinstance(password, int), "Password attribute takes values Integer"
        self.__password = password

            
    def Greeting(self,second_person):
        return 'Welcome dear {}'.format(second_person.name)
    
    def Goodbye(self):
        print( "Bye everyone!" )
    
    def Favourite_num(self, num1):
        return 'My favorite number is {}'.format(num1)


    def Read_file(self, filename):
        try:
            open_file = open (f"{filename}.txt")
        except FileNotFoundError:
            return(" File is not exist ")

        return open_file.read()


man = Person ("Andres", "Iniesta", 35, "male", False, 505050)
print(man.Read_file("filename"))


#ex-4

class Polygon:
    def __init__(self, n_of_sides):
        self.n = n_of_sides
        self.sides = list()


    def input_sides(self, sides):
        self.sides = sides
        print(self.sides)
        if len(self.sides) != 4*self.n:
           raise Exception ("ERRoooooooooor")
        
    def disp_sides(self):
        for i in range(self.n):
            print("Side",i+1,"is",self.sides[i])
            
    def get_perimeter(self):
        return sum(self.sides)

class Quadrilateral(Polygon):
    def __init__(self):
        super().__init__(4)
        
class  Rectangle(Quadrilateral):
#     def __init__(self):
#         super().__init__()   
    def input_sides(self, s):
        super().input_sides(s*2)
    def get_area(self):
        return self.sides[0]*self.sides[1]
    
class  Square(Rectangle):
#     def __init__(self):
#         super().__init__()
    def input_sides(self,s):
        super().input_sides(s*2)

obj = Square()
obj.input_sides([5,5,5,5])
obj.get_perimeter()

print(obj.get_perimeter())
print(obj.disp_sides())





