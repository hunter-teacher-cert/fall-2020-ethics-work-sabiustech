
import random

# table with randomly populated cells
def matrix(rows, cols):
  table = [[random.randint(0,1) for x in range(cols)] for y in range(rows)]
  return table


# prints the table created in matrix()
def printTable(table):
  party = 1
  for x in table:
    print('P{}:'.format( str(party)), x)
    party += 1


#show results
def results(table):
  results = []
  P = 1
  for x in table:
    outcome = {0:0,1:0}
    for y in x:
      if y == 0:
        outcome[0]+= 1
      else:
        outcome[1]+= 1

    printOutcome = 'P{} outcome: {}'.format(P,outcome)
    results.append(printOutcome)
    P += 1
  return outcome



def outPut(table):
  p1 = 0
  p0 = 0
  for x in table:
      if (x + x) > len(table[0]):
          p1 += 1
      p0 += x + x
  print(f'Number of p1 {p1:.2f}.')
  print(f'Number of p0 {p0:.2f}.')

  return [p1,p0]



# run program
rows = int(random.randrange(1,10))
cols = int(random.randrange(1,10))

print('\nThe Table:\n')

table = matrix(rows,cols)

printTable(table)
results = results(table)

print('\nThe Final Results:')

for x in results:
  print(x)
print('\nNumbers for P1 and P0:')

outPut(table)
