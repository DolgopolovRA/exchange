import re

class Date:
    def __init__(self, date_str):
        self.date = date_str
        self.str_to_int(date_str)

    @classmethod
    def str_to_int(cls, date):
        da = re.findall(r'(?:[^.]+)-(?:.+)-(?:.+)', date)
        for i in da:
            print(i)
        # for el in date.split('-'):
        #     if el.isdigit():
        #         print(int(el))

    @staticmethod
    def valid_date():
        pass


dt = Date('-1.2-2e-2321')
# dt.str_to_int()
