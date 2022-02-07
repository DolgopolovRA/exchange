import re
"""https://regex101.com/r/y3mIqm/1"""

data = re.compile(r'(?:^[\d\.:a-z]+)|(?:[^\s\[]{3,}.+(?=\]))|(?:[A-Z]{3,}(?= /))|(?:/\w+/\w+(?= ))|(?:\d+(?= \d+))|(?:\d+(?= "))')
with open('nginx_logs.txt', 'r', encoding='utf-8') as fr:
    with open('nginx_logs_parser.txt', 'w', encoding='utf-8') as wf:
        while True:
            lines = fr.readline()
            if not lines:
                break
            sp_data = data.findall(lines)
            wf.write(f'{sp_data}\n')
