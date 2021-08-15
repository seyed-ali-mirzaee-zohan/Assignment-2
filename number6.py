n=int(input("Please enter your desired number : "))
list_of_number=[]
def Fibonacci(n):
    if n<0:
        print("incorrect input")
    if n==0:
        return 0
    if n==1:
        return 1
    if n>1:
        return Fibonacci(n-1)+Fibonacci(n-2)
for i in range(n):
    if i==0:
        list_of_number.append(0)
    if i==1:
        list_of_number.append(1)
    if i>1:
        list_of_number.append(list_of_number[i-1]+list_of_number[i-2])
print(list_of_number,", The total value is equal to : ",Fibonacci(n))