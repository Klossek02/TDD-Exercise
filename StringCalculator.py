import re

class StringCalculator:
    def calculate(s: str): 
        if not s:
            return 0

        delimiters = [',', '\n']
        numbers_str = s

        # delimiter handling
        if s.startswith('//'):
            header, numbers_str = s.split('\n', 1)
            custom_delimiters = re.findall(r'\[(.*?)\]', header)
            if not custom_delimiters:  # if lack of brackets, use only one symbol 
                custom_delimiters = [header[2:]]
            delimiters.extend(custom_delimiters)

        # changing all delimiters to default (comma)
        for delimiter in delimiters[1:]:
            numbers_str = re.sub(re.escape(delimiter), delimiters[0], numbers_str)

        def parse_num(t: str):
            if t == "" or t.startswith('//'):
                return 0
            result = int(t)
            if result < 0: # limitation for negative number 
                raise Exception("negative numbers not allowed")
            if result >= 1000: # limitation for numbers more/equal than 1000
                return 0
            return result

        # retrun sum using above conditions
        return sum(map(parse_num, numbers_str.split(delimiters[0])))
