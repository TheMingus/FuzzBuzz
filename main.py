from time import time
from tqdm import tqdm
from json import dump
from csv import writer

# - - $$$ - - #
# Main Menu
print('Welcome to \u001b[1;38;2;80,200,120mMingus\'\u001b[0m very, very crappy Fuzz Buzz Generator. Please select an option to continue:')
print('\u001b[1;94m[0]\u001b[0m Fast, but will fill up your ram I think.')
print('\u001b[1;94m[1]\u001b[0m Slower, doesn\'t fill ram as much I think.\n')
opt = 0
while opt not in ['0','1']:
  opt = input('> \u001b[91m')
  print('\u001b[0m')

to = input('Generate to what? ')
  
if opt == '0':
  start = time()
  final = ['Fuzz Buzz' if i%15==0 else 'Buzz' if i%3==0 else 'Fuzz' if i%5==0 else str(i) for i in tqdm(range(int(to)))]
  duration = time() - start
  print(f'Done! Took {duration} seconds. Don\'t stop yet, we are still writing the results to a file.')
  with open('final.json', 'w') as f: dump(final, f, indent=2)
  print('Ok, now we\'re done.')
if opt == '1':
  start = time()
  for i in tqdm(range(int(to))):
    if i%15==0:
      item = 'Fuzz Buzz'
    elif i%3==0:
      item = 'Buzz'
    elif i%5==0:
      item = 'Fuzz'
    else:
      item = str(i)
    print(item)
    with open('final.csv','a') as fd:
      write(fd)
  duration = time() - start
  print(duration)
