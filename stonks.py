def display_menu():
    """ prints a menu of options
    """  
    print()
    print('(0) Input a new list of prices')
    print('(1) Print the current prices')
    print('(2) Find the latest price')
    print('(3) Find the average price')
    print('(4) Find the min price and its day')
    print('(5) Find the max single-day change and its day')
    print('(6) Test a threshold')
    print('(7) Your investment plan')
    print('(8) Quit')

def get_new_prices():
    """ gets a new list of prices from the user and returns it
    """

    new_price_list = eval(input('Enter a new list of prices: '))
    return new_price_list

def print_prices(prices):
    """ prints the current list of prices
        input: prices is a list of 1 or more numbers.
    """

    if len(prices) == 0:
        print('No prices have been entered.')
        return
    
    print('Day Price')
    print('--- -----')
    for i in range(len(prices)):
        print('%3d' % i, end='')
        print('%6.2f' % prices[i])

def latest_price(prices):
    """ returns the latest (i.e., last) price in a list of prices.
        input: prices is a list of 1 or more numbers.
    """

    return prices[-1]


def avg_price(vals):
    """
    takes list of values and returns the avg
    """

def min_day(vals):
    """
    returns the index of the smallest val
    """

def max_change_day(prices):
    """
    Returns the day of the max single-day 
    change in price
    """

def any_above(prices,threshold):
    """
    Determines of there are any prices 
    above the threshold
    """

def find_tts(vals):
    """
    Calculates the ideal time to sell by 
    returning the buy day, the sell day, and the profit
    """

def tts():
    """ the main user-interaction loop
    """

    prices = []

    while True:
        display_menu()
        choice = int(input('Enter your choice: '))
        print()

        if choice == 0:
            prices = get_new_prices()

        elif choice == 8:
            break

        elif choice < 8 and len(prices) == 0:
            print('You must enter some prices first.')

        elif choice == 1:
            print_prices(prices)

        elif choice == 2:
            latest = latest_price(prices)
            print('The latest price is', latest)

        '''
        elif choice == 3:
            print('The average price is',avg_price(prices))

        elif choice == 4:
            m = min_day(prices)
            print('The min price is', prices[m], 'on day', m)

        elif choice == 5:
            d = max_change_day(prices)
            print('The max single-day change occurs on day', d)
            print('when the price goes from', prices[d-1], 'to', prices[d])

        elif choice == 6:
            threshold = int(input('Enter the threshold: '))
            if any_above(prices, threshold):
                print('There is at least one price above', threshold)
            else:
                print('There are no prices above', threshold)

        elif choice == 7:
            vals = find_tts(prices)
            print('Buy on day', vals[0], 'at price', prices[vals[0]])
            print('Sell on day', vals[1], 'at price', prices[vals[1]])
            print('Total Profit:', vals[2])
        
        else:
            print('Invalid choice. Please try again.')
        '''

    print('Program exited.')

tts()