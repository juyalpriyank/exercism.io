def is_armstrong(number=int):
    power = int(len(str(number)))
    sum = 0
    for digit in str(number):
        try:
            sum += int(digit) ** power
        except ValueError:
            raise Exception('The number should be an integer')
    if sum == int(number):
        return True
    return False
