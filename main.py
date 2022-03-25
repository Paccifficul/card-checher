"""Check the correctness of the entered bank card number"""


def check(card_num):
    """Check using Luhn's algorithm; Counting control sum"""

    payment_system = 'Your payment system is '
    modified_card_num = ''
    control_sum = 0

    try:

        if card_num[0] == '4':  # Checking first number to prove that payment system is Visa
            payment_system += 'Visa'
        elif card_num[0] == '5':  # Checking first number to prove that payment system is MasterCard
            payment_system += 'MasterCard'
        elif card_num[0] == '2':  # Checking first number to prove that payment system is MIR
            payment_system += 'MIR'
        else:
            payment_system = 'I can not recognize your payment system'

        for elem in range(len(card_num)):  # Checking digits except the last one
            if elem % 2 == 0:
                i = int(card_num[elem]) * 2
                if i > 9:
                    i -= 9
                modified_card_num += str(i)
            else:
                modified_card_num += card_num[elem]

        for digit in modified_card_num:  # Counting sum of digits
            control_sum += int(digit)

        print(payment_system + '.')  # Output card's payment system

        if control_sum % 10 == 0:  # Check correctness
            print('You have entered correct number.')
        else:
            print('You have entered incorrect number.')
    except ValueError:
        print('Wait.. You have entered letter(s).')


def main():
    card_number = input('Enter your card number\n>> ').replace(' ', '')
    check(card_number)


if __name__ == '__main__':
    main()
