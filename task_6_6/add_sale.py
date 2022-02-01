import argparse

parser = argparse.ArgumentParser(description='Script for recording the price')
parser.add_argument('price', type=str, help='Input the price')
args = parser.parse_args()

with open('bakery.csv', 'a', encoding='utf-8') as f:
    f.write(f'{args.price}\n'.zfill(10))
