print('This application will help you achieve your desired result using all of the following: add, subtract, multiply, divide, exponent, and square root.')
expected_result=int(input("the result you want to achieve:"))
first_num=input("What do you want as your first number")
second_num=input("What do you want as your second number")
result=int(first_num)+int(second_num)
fix_first_num = 0
fix_second_num = 0
if result == expected_result:
  print("\n\nUsing Addition You have achieved your desired result")
else:
  print(f"\n\nUsing Addition You have not achieved your desired result as {first_num} - {second_num} = {result}")
  fix_first_num = int(expected_result)-int(second_num)
  fix_second_num = int(expected_result)-int(first_num)
  print(f"\nUsing Addition you can achieve your desired result by using either first num as {fix_first_num} or second number as {fix_second_num}")


result=int(first_num)-int(second_num)
fix_first_num = 0
fix_second_num = 0
if result == expected_result:
  print("\n\nUsing Subtraction You have achieved your desired result")
else:
  print("\n\nUsing Subtraction You have not achieved your desired result")
  fix_first_num = int(expected_result)+int(second_num)
  fix_second_num = int(expected_result)+int(first_num)
  print(f"\nUsing Subtraction you can achieve your desired result by using either first num as {fix_first_num} or second number as {fix_second_num}")

  
