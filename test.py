# put your python code here
def t(s, tag='h1'):
    return f'<{tag}>{s}</{tag}>'


st = input()
print(t(st))
print(t(st, tag='div'))
