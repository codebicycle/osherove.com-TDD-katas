import re

class StringCalculator:

    def add(self, input):
        numbers     = self.__parse_numbers(input)
        total       = 0
        negatives   = []
        for num in numbers:
            if num < 0:
                negatives.append(str(num))
            elif num > 1000:
                continue
            else:
                total += num

        if negatives:
            message = 'negatives not allowed ' + ' '.join(negatives)
            raise ValueError(message)

        return total


    def __parse_numbers(self, input_str):
        delimiters  = self.__delimiters(input_str)
        str_numbers = self.__data(input_str)

        if str_numbers == '':
            return []

        pattern = '|'.join(map(re.escape, delimiters))
        delimiter_or_newline = pattern + "|\n"
        str_list = re.split(delimiter_or_newline, str_numbers)

        numbers  = list(map(lambda x: int(x), str_list))

        return numbers


    def __delimiters(self, input_str):
        if input_str.startswith('//'):
            first_line = input_str.split('\n', 1)[0]
            pattern = "\[(.+?)\]"
            delimiters = re.findall(pattern, first_line)
            if not delimiters:
                delimiters = [first_line[2]]
        else:
            delimiters = [',']
        return delimiters


    def __data(self, input_str):
        if input_str.startswith('//'):
            return input_str.split('\n', 1)[-1]
        else:
            return input_str
