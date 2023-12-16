for i in range(151):
    print (i)

print([i for i in range(5,1005,5)])

for multiples in range(1,101):
    if multiples % 5 == 0:
        print('Coding')
    if multiples % 10 == 0:
        print('Coding Dojo')
    if multiples % 5 != 0 and multiples % 10 != 0:
        print(multiples)

sumOfOdd = 0
for Odd in range(500001):
    if Odd % 2!=0:
        sumOfOdd += Odd
print(sumOfOdd)

for fours in range(2018,-1,-4):
    print(fours)

lowNum = int(input(2))
highNum = int(input(9))
mult = int(input(3))

for flexibleCounter in range(lowNum,highNum + 1):
    if flexibleCounter % mult == 0:
        print(flexibleCounter)