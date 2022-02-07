import re


def email_parse(email=input('Введите e-mail: ')):
    out_dict = {}
    try:
        data = re.compile(r'(^[^@ ]+|\w+\.\w+)')
        sp_data = data.findall(email)
        if len(sp_data) < 2:
            raise ValueError()
        else:
            out_dict.setdefault('username', sp_data[0])
            out_dict.setdefault('domain', sp_data[1])
            return out_dict
    except ValueError:
        print(f'wrong email: {email}')


print(email_parse())
