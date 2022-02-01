import argparse

parser = argparse.ArgumentParser(description='Dict for users and hobby')
parser.add_argument('users_dir', type=str, help='Input dif for users')
parser.add_argument('hobby_dir', type=str, help='Input dif for hobby')
parser.add_argument('dict_users_dir', type=str, help='Input dir for the output file')
args = parser.parse_args()

with open(fr'{args.users_dir}\users.csv', 'r', encoding='utf-8') as usr:
    users = tuple(line.replace(',', ' ').rstrip('\n') for line in usr if line.isspace() is False)

with open(fr'{args.hobby_dir}\hobby.csv', 'r', encoding='utf-8') as hob:
    hobby = tuple(line.rstrip('\n') for line in hob if line.isspace() is False)

if len(users) >= len(hobby):
    dict_users = {us: hobby[users.index(us)] if users.index(us) < len(hobby) else None for us in users}
    with open(fr'{args.dict_users_dir}\dict_users.csv', 'w', encoding='utf-8') as dict_usr:
        dict_usr.write(str(dict_users))
else:
    exit(1)
