def validate(input_str):
    while True:
        x = input(f'Enter the {input_str}')
        if ('nan' in x.lower()) or ('inf' in x.lower()):
            print('Do not use NaN or Inf')
            continue
        try:
            x = float(x)
            if x <= 0 and input_str != 'APR: ':
                print('Enter a number greater than 0')
            elif input_str == 'APR: ' and x < 0:
                print('Enter a number of at least 0')
            else:
                return x
        except ValueError:
            print('Enter a number')

def execute_calc():
    loan_amount = validate('loan amount in dollars: ')

    loan_duration = validate('loan duration in years: ')
    loan_duration_months = loan_duration * 12

    apr = validate('APR: ')

    while apr < 0 :
        print('Enter a number of at least 0')
        apr = validate('APR: ')

    monthly_interest_rate = apr / 12 / 100

    print()
    print(f'-> Your loan amount is ${round(loan_amount, 2)}')
    print(f'-> Your loan duration is {round(loan_duration_months)} months')
    print(f'-> Your APR is {round(apr, 2)}%')

    numerator = loan_amount * monthly_interest_rate
    denominator = (1 - ((1 + monthly_interest_rate) ** (-loan_duration_months)))

    try:
        monthly_payment = numerator / denominator
    except ZeroDivisionError:
        monthly_payment = loan_amount / loan_duration_months

    monthly_payment = round(monthly_payment, 2)

    print(f'-> Your monthly payment is ${monthly_payment}')
    print()

while True:
    execute_calc()
    reply = input('Would you like to use the calculator again? (y/n) ')
    while reply.lower() not in ['y', 'n']:
        print('Invalid input.')
        reply = input('Would you like to use the calculator again? (y/n) ')
    if reply.lower() == 'y':
        print()
        continue
    else:
        print('Stopping program')
        break
