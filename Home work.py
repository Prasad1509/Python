#!/usr/bin/env python
# coding: utf-8

# In[5]:


#create afunction name as fun() that should display "Hello from BSc(IT)"
def fun():
    return " Hello from BSc(IT)"
fun()


# In[6]:


# write a program to check number is even or odd
def check_number(num):
    if num % 2 ==0:
        print("Even")
    else:
        print("Odd")
check_number(10)        


# In[7]:


#write a program contains one function named as Add() which accept two number
def Add():
    a=int(input("Enter the number:"))
    b=int(input("Enter the number:"))
    return a+b
result=Add()
print("Sum:",result)


# In[11]:


#write a program display 10 to 1 on screen 
for i in range(10,0,-1):
    print(i)


# In[12]:


#write a program which accept number from user and check number positive negative or zero
def check_number():
        num=float(input("Enter the number:"))
        
        if num >0:
            print("Positive")
            
        elif num<0:
            print("Negative")
        else:
            print("Zero")
check_number()            
            
    


# In[1]:


##write a program which accept number from user and print thst number of "*" on screen

num=int(input("Enter the number:"))
print("*"*num)


# In[2]:


#write a program which accept number from user and check number positive negative or zero
   
num=float(input("Enter the number:"))
    
    if num >0:
        print("Positive")
        
    elif num<0:
        print("Negative")
    else:
        print("Zero")


# In[9]:


#write a program to disdplay first 10 even number on screen 
for i in range(2,21,2):
    print(i)


# In[ ]:





# In[10]:


#write a program which contain one function that accept one number from the user and returns true if number is divisible by b5  otherwise return gfalse
def is_divisible_by_5(num):
    return num % 5 == 0
num=int(input("Enter the number:"))
if is_divisible_by_5(num):
    print("The number is divisible by 5")
else:
        print("The number is not divisible by 5")


# In[13]:


#write a program  which accept name from user and display length of its name
name=input("Enter the name: ")
print("lenght of your name is: ")
len(name)


# In[6]:


#create a calculator  to perform basic operation
num1=float(input("Enter the number:"))
num2=float(input("Enter the number:"))
operation=input("Enter the operation(+,-,*,/):")
if operation =='+':
        print(num1+num2)
elif operation =='-':
        print(num1-num2)
elif operation =='*':
        print(num1*num2)
elif operation =='/':
        print(num1/num2 if num2 != 0 else "Error:Division by zero")
else:
        print("Invalid operation")
        



   


# In[17]:


#fibinacci series
num=int(input("Enter the number:"))
a,b=0,1
for i in range(num):
    print(a)
    a,b=b,a+b


# In[4]:


#prime number
num=int(input("Enter the number:"))
if num > 1:
    for i in range(2,num):
        if num % i==0:
            print(f"{num} is not a prime number")
            break
        else:
            print(f"{num} is  a prime numberr")
else:
    print(f"{num} is not aprime numbe")


# In[29]:


#palindrome unmber
num=int(input("Enter the number:"))
original_num=num
reverse_num=0

while num>0:
    digit=num%10
    reverse_num=reverse_num*10+digit
    num=num//10
if original_num==reverse_num:
      print(f"{original_num} is not a palindrome number")
else:
      print(f"{original_num} is not a palindrome number")
    



# In[3]:


#Armstrong number
num=int(input("Enter the number:"))
sum=0
temp=num

while temp > 0:
    digit=temp%10
    sum+=digit**3
    temp//=10
if num == sum:
    print(f"{num} is an Armstrong numbe")
else:
    print(f"{num} is not an Armstrong numbe")



# In[ ]:





# In[ ]:




