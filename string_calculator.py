import re

class StringCalculator:

    def add(self, string_numbers):
        if string_numbers == '':
            return 0

        pattern = "[,\n]"
        numbers_list = re.split(pattern, string_numbers)
        sum = 0
        while len(numbers_list) > 0:
            sum += int(numbers_list.pop(0))
        return sum
