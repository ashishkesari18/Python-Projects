from art import logo
def add(n1,n2):
  return n1+n2
def subtract(n1,n2):
  return n1-n2
def multiply(n1,n2):
  return n1*n2
def divide(n1,n2):
  return n1/n2
def calculator():
  print(logo)
  operations = {"+":add,"-":subtract,"*":multiply,"/":divide}
  num1=float(input("please enter your 1st number"))
  is_continue = True
  while is_continue:
    for symbol in operations:
      print(symbol)
    choice = input("Please select the operations from above")
    num2=float(input("please enter your  next number"))
    calculate_operation = operations[choice]
    answer = calculate_operation(num1,num2)
    print(answer)
    if input(f"Type y to continue with {answer} or n to stop ").lower() =="y":
      num1 = answer
    else:
      is_continue = False
      calculator()
calculator()