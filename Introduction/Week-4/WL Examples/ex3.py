numberOfYears = 0
balance = eval(input('Enter initial deposit: '))

while balance < 1000000:
    balance += 0.04 * balance
    numberOfYears += 1

print('In', numberOfYears, 'years you will be a millionaire')