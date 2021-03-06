from time import time
from tqdm import tqdm
from json import dump

print('Welcome to \u001b[1;38;2;80,200,120mMingus\'\u001b[0m crappy Fuzz Buzz Generator.')

to = int(input('Generate to what? '))

start = time()
final = ['Fuzz Buzz' if i%15==0 else 'Buzz' if i%3==0 else 'Fuzz' if i%5==0 else str(i) for i in tqdm(range(int(to)))]
duration = time() - start
print(f'Done! Took {duration} seconds. Don\'t stop yet, we are still writing the results to a file.')
with open('final.json', 'w') as f: dump(final, f, indent=2)
print('Ok, now we\'re done.')