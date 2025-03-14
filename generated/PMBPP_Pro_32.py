def validate_list(numbers):
    def is_valid(number):
        digit_count = {}
        for digit in str(number):
            if digit not in digit_count:
                digit_count[digit] = 0
            digit_count[digit] += 1
        
        for digit, count in digit_count.items():
            if count > int(digit):
                return False
        return True

    return [is_valid(number) for number in numbers]
