with open('users.csv', 'r', encoding='utf-8') as usr:
    users = usr.read().replace(',', ' ').rstrip('\n').split('\n')

with open('hobby.csv', 'r', encoding='utf-8') as hob:
    hobby = hob.read().rstrip('\n').split('\n')

if len(users) >= len(hobby):
    dict_users = {us: hobby[users.index(us)] if users.index(us) < len(hobby) else None for us in users}
    with open('dict_users.csv', 'w', encoding='utf-8') as dict_usr:
        dict_usr.write(str(dict_users))
else:
    exit(1)
