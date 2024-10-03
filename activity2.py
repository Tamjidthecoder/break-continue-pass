x=int(input("ENTER A NUMBER : "))
if (x%20)==0:
    print("TWISt")
elif (x%15)==0:
    pass
elif (x%5)==0:
    print('fizz')
elif (x%3)==0:
    print("buzz")
else:
    print(x)