print('This program displays famous movies')
responses = ['1', '2', '3']
current_response = '-1'

while current_response not in responses:
    current_response = input('Enter 1, 2, or 3: ')
    if current_response == '1':
        print('Dark Knight')
    elif current_response == '2':
        print('Ferris Bueller\'s Day Off')
    elif current_response == '3':
        print('The Incredibles')

print('Program Exiting')