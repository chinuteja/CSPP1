'''
Author: teja
date : 6/8/2018
'''

def paying_debt_off_inayear(balance_unpaid, annual_interest_rate, monthly_payment_rate):
    '''this code is used to calculate remaining balance'''
    balance_copy = balance_unpaid

    i = 1
    while i <= 12:
        montly_interest_rate = annual_interest_rate / 12.0
        minimum_monthly_payment = monthly_payment_rate*balance_copy
        monthly_unpaid_balance = balance_copy - minimum_monthly_payment
        balance_copy = monthly_unpaid_balance + (montly_interest_rate * monthly_unpaid_balance)
        i += 1
    return "Remaining balance: "+str(round(balance_copy, 2))
def main():
    '''main function'''
    data = input()
    data = data.split(' ')
    data = list(map(float, data))
    print(paying_debt_off_inayear(data[0], data[1], data[2]))

if __name__ == "__main__":
    main()
    