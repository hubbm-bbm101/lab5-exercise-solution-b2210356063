endpoint = int(input("enter a number: "))
sumEven = 0
sumOdd = 0
length = 0
for number in range (1, endpoint + 1):
    if number%2!=0:
        sumOdd += number
    else:
        sumEven += number
        length += 1
average = sumEven / length
print("sum of odd numbers:", sumOdd, "\naverage of even numbers:", average)