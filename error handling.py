'''
raj = int(input("enter a age: "))

try:
    num1 = 5
    num2 = "10"
    print(num1 + num2)

except SyntaxError:
    print("there is some syntax error in this code")
except TypeError:
    print("Wrong data type")
except:
    print("unknown error")
else:
    print("code has run successfully")
finally:
    print("program ended")

    
try:
    num = ["one","two","three","four","five"]
    print(num[5])
       
except SyntaxError:
    print("there is some syntax error in this code")
except TypeError:
    print("Wrong data type")
except:
    print("unknown error")
else:
    print("code has run successfully")
finally:
    print("program ended")    
'''

nums = ["10", "20", "abc", "40"]
for n in nums:
 try:
     print(int(n))
 except ValueError:
    print("Skipping invalid value:", n)







    
