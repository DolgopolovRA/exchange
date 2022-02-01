import argparse

parser = argparse.ArgumentParser(description='Script for show the price')
parser.add_argument('start', type=int, nargs='?', default=0, help='Input the start position')
parser.add_argument('end', type=int, nargs='?', default=0, help='Input the end position')
args = parser.parse_args()

if args.start <= 0 and args.end <= 0:
    with open('bakery.csv', 'r', encoding='utf-8') as rf:
        prices = list(lines for lines in rf)
    print(*prices, sep='')
elif args.start > 0 and args.end <= 0:
    with open('bakery.csv', 'r', encoding='utf-8') as rf:
        rf.seek((args.start - 1) * 11)
        print(*rf.readlines(), sep='')
elif args.start > 0 and args.end > 0:
    with open('bakery.csv', 'r', encoding='utf-8') as rf:
        rf.seek((args.start - 1) * 11)
        while rf.tell() <= ((args.end - 1) * 11):
            print(*rf.readline(), sep='', end='')
