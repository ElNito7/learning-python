
count = 0
sum = 0
max = None
min = None 
while True :
    n = input('Please enter a number: ')
    if n == 'done' :
        break
    try :
        num = float(n)
    except :
        print('I said enter a number you idiot')
        continue
    sum = sum + num 
    count = count + 1
    av = sum/count
    if max is None : 
        max = num
        min = num
    if max < num :
        max = num
    if min > num :
        min = num
print(sum, count, av, min, max)
