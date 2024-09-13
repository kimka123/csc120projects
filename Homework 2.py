#!/usr/bin/env python
# coding: utf-8

# In[5]:


#1st question

celsius = int(input("Enter the Temperature in Celsius :\n"))

fahrenheit = (1.8 * celsius) + 32

print("Temperature in Fahrenheit :", fahrenheit)


# In[7]:


#2nd a)

zork = 0

print('Before', zork)

for thing in [9, 41, 12, 3, 74, 15] :
    
    zork = zork +thing 
   
    print(zork, thing)
    
    print('After', zork)


# In[8]:


#2nd b)

count=0

sum=0

print('Before',count,sum)

for value in [9, 41, 12, 3, 74, 15] :
    count=count+1
    sum=sum+value
    print(count, sum,value)
    print('After', count,sum,sum / count)


# In[12]:


#3rd

x= int(input("Enter the first number :\n"))
y=int(input("Enter the second number :\n"))
sum= x**3 +y**3

print("result :", sum)


# In[15]:


#4th

P= int(input("Enter the principal amount :\n"))
R=int(input("Enter the rate of interest :\n"))
T=int(input("Enter the period :\n"))

SI= (P*R*T)/100

print("Simple interest :", SI)


# In[25]:


#5th

radius = int(input("The radius of the circle? : "))
pi=3.14
area = pi * radius ** 2
    
print('Area of the circle:',area)


# In[26]:


#6th

days = int(input("Enter the number of days: "))

hours = days * 24
minutes = hours * 60
seconds = minutes * 60

print(f"{days} days is equal to:")
print(f"{hours} hours")
print(f"{minutes} minutes")
print(f"{seconds} seconds")


# In[30]:


#7th

hourly_wage = input('Please enter your hourly wage: ')

print("Hourly wage: ")
print('hourly wage:')
print("Hours worked: ")
print('hours_worked')

hours_worked = input("How many hours did you work this week? ")



# In[5]:


#8th

width = 17
height = 12.0

expressions = [
    ("width//2", width//2),
    ("width/2.0", width/2.0),
    ("height/3", height/3),
    ("1+2**5", 1+2**5) ]
    

print("Results:")
for expr, result in expressions:
    print(f"{expr:10} = {result:<10} (Type: {type(result).__name__})")


# In[3]:


#9th

weight = int(input("Enter your weight in kilograms: "))

height = int(input("Enter your height in meters: "))

bmi = weight/(height**2)

print("your body mass index is:", bmi)


# In[4]:


#10th

name = input("Please enter your name: ")
print(f"Welcome to Python programming {name}.")

