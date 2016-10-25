import re

class StringCalculator:

    def add(self, input_str):
        numbers     = self.__parse_numbers(input_str)
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
        str_numbers = self.__data(input_str)
        if str_numbers == '':
            return []

        pattern  = self.__split_pattern(input_str)
        str_list = re.split(pattern, str_numbers)

        numbers  = list(map(lambda x: int(x), str_list))

        return numbers


    def __split_pattern(self, input_str):
        delimiters = self.__delimiters(input_str)
        pattern    = '|'.join(map(re.escape, delimiters))

        return pattern


    def __delimiters(self, input_str):
        if input_str.startswith('//'):
            first_line = input_str.split('\n', 1)[0]
            pattern    = "\[(.+?)\]"
            delimiters = re.findall(pattern, first_line)
            if not delimiters:
                delimiters = [first_line[2]]
        else:
            delimiters = [',']
        delimiters.append('\n')

        return delimiters


    def __data(self, input_str):
        if input_str.startswith('//'):
            return input_str.split('\n', 1)[-1]
        else:
            return input_str
