for i in range(1, 101):
  if i%15==0:
    print(i,"fizzBuzz")
  elif i%3 ==0:
    print(i,"Fizz")
  elif i%5==0:
    print(i,"Buzz")
  elif i%i==0:
    print(i,"error")
  
