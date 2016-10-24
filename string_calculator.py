import re

class StringCalculator:

    def add(self, input):
        numbers     = self.__parse_numbers(input)
        total       = 0
        negatives   = []
        for num in numbers:
            if num < 0:
                negatives.append(str(num))
            else:
                total += num

        if negatives:
            message = 'negatives not allowed ' + ' '.join(negatives)
            raise ValueError(message)

        return total


    def __parse_numbers(self, input):
        delimiter, string_numbers = self.__delimiter_data(input)

        if string_numbers == '':
            return []

        pattern  = "[{}\n]".format(delimiter)
        str_list = re.split(pattern, string_numbers)

        numbers  = list(map(lambda x: int(x), str_list))

        return numbers


    def __delimiter_data(self, input):
        if input.startswith('//'):
            first_line, string_numbers = input.split('\n', 1)
            delimiter = first_line[2]
        else:
            string_numbers  = input
            delimiter       = ','

        return delimiter, string_numbers
