from datetime import date

def calcBirthYear(dobYear):
    today = date.today().year
    return today - int(dobYear)

def calcAreaRectangle(length, width):
    area = length * width 
    return area

def calcAreaCircle(radious):
    area = 3.14 * radious * radious 
    return area

def calcAreaCube(side):
    area = 6 * side * side 
    return area
def calcTemperature(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius

def calcMinAndSec(seconds):
    minutes = seconds // 60
    remainingSeconds = seconds % 60 
    return f"Minutes:{minutes} Seconds: {remainingSeconds}"

def calcPercentage(totalMarks, obtainedMarks):
    percentage = (obtainedMarks / totalMarks) * 100
    return percentage

dobYear = input("Enter your birth year: ")
print(calcBirthYear(dobYear))

length = 10
width = 20
print("Area of rectangle:", calcAreaRectangle(10, 20))

radius = int(input("Enter radius: ")) 
print("Area of circle:", calcAreaCircle(radius))

side = int(input("Enter side: "))
print("Area of cube:", calcAreaCube(side)) 


fahrenheit = int(input("Enter temperature in Fahrenheit: "))  
print("Celsius:", calcTemperature(fahrenheit))  

result = calcMinAndSec(int(input("Enter seconds: ")))
print(result) #16 40

totalMarks = 100
obtainedMarks = 80
print("Percentage:", calcPercentage(totalMarks, obtainedMarks))
