def greater_than_0(input_str):
    while True:
        x = input(f'Enter the {input_str}')
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

loan_amount = greater_than_0('loan amount in dollars: ')

loan_duration = greater_than_0('loan duration in years: ')
loan_duration_months = loan_duration * 12

apr = greater_than_0('APR: ')

while apr < 0 :
    print('Enter a number of at least 0')
    apr = greater_than_0('APR: ')

monthly_interest_rate = apr / 12 / 100

print(f'Your loan amount is ${loan_amount}')
print(f'Your loan duration is {loan_duration_months} months')
print(f'Your APR is {apr}%')

numerator = loan_amount * monthly_interest_rate
denominator = (1 - ((1 + monthly_interest_rate) ** (-loan_duration_months)))

try:
    monthly_payment = numerator / denominator
except ZeroDivisionError:
    monthly_payment = loan_amount / loan_duration_months

monthly_payment = round(monthly_payment, 2)

print(f'Your monthly payment is ${monthly_payment}')
