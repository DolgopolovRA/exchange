import argparse

parser = argparse.ArgumentParser(description='Script for write the price on position')
parser.add_argument('start', type=int, help='Input the position')
parser.add_argument('price', type=str, help='Input the price')
args = parser.parse_args()


with open('bakery.csv', 'r+', encoding='utf-8') as rf:
    rf.seek((args.start - 1) * 11)
    rf.write(f'{args.price}\n'.zfill(10))
