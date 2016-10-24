import re

class StringCalculator:

    def add(self, input):
        if input.startswith('//'):
            first_line, string_numbers = input.split('\n', 1)
            delimiter = first_line[2]
        else:
            string_numbers  = input
            delimiter       = ','

        if string_numbers == '':
            return 0

        pattern = "[{}\n]".format(delimiter)
        numbers_list = re.split(pattern, string_numbers)
        sum = 0
        negatives = []
        while len(numbers_list) > 0:
            current_nr = int(numbers_list.pop(0))
            if current_nr < 0:
                negatives.append(str(current_nr))
                continue

            sum += current_nr

        if negatives:
            message = 'negatives not allowed ' + ' '.join(negatives)
            raise ValueError(message)

        return sum
