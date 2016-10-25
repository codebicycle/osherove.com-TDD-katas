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
        delimiter   = self.__delimiter(input_str)
        str_numbers = self.__data(input_str)

        if str_numbers == '':
            return []

        escaped_delimiter    = re.escape(delimiter)
        delimiter_or_newline = "{}|\n".format(escaped_delimiter)
        str_list = re.split(delimiter_or_newline, str_numbers)

        numbers  = list(map(lambda x: int(x), str_list))

        return numbers


    def __delimiter(self, input_str):
        if input_str.startswith('//'):
            first_line = input_str.split('\n', 1)[0]
            pattern = "\[(.+?)\]"
            match = re.search(pattern, first_line)
            if match:
                delimiter = match.group(1)
            else:
                delimiter = first_line[2]
        else:
            delimiter = ','
      
        return delimiter


    def __data(self, input_str):
        if input_str.startswith('//'):
            return input_str.split('\n', 1)[-1]
        else:
            return input_str
