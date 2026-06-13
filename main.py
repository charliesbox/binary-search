import math
import time
import random

def getstartedmanual():
  listmax = int(input("Maximum list number: "))
  searching = int(input("The number to find: "))
  thelist = [searching]
  sleepy_input = input("Sleeping time between searching cycles (0 as default): ")
  sleepy = float(sleepy_input) if sleepy_input.strip() != '' else 0.0
  if sleepy == ():
    sleepy = 0
  a = list(range(1, listmax + 1))
  med = a[len(a) // 2]
  steps = int(0)
  stepsexpected = math.ceil(math.log2(listmax))
  return sleepy, a, med, steps, stepsexpected, thelist, listmax

def getstartedauto():
  listmax = int(input("Maximum list number: "))
  sleepy_input = input("Sleeping time between searching cycles (0 as default): ")
  sleepy = float(sleepy_input) if sleepy_input.strip() != '' else 0.0
  if sleepy == ():
    sleepy = 0
  thelist = []
  for i in range(5):
    searching = int(random.randint(1, listmax))
    thelist.append(searching)
  a = list(range(1, listmax + 1))
  med = a[len(a) // 2]
  steps = int(0)
  stepsexpected = math.ceil(math.log2(listmax))
  return sleepy, a, med, steps, stepsexpected, thelist, listmax

def main(sleepy, a, med, steps, stepsexpected, thelist, listmax, mode):
  while len(thelist) > 0:
    print(thelist)
    letsgo =  thelist.pop(0)
    print("We're looking for", letsgo)
    print(" ".join([str(x) if x != med else f"[{x}]" for x in a]))
    print("")
    time.sleep(sleepy)

    if med == letsgo:
      print("Found!", med)
      print("Steps used:", steps)
      print("Steps expected according to log2(" + str(listmax) + "):", stepsexpected)
      print("")
      print("")
      if len(thelist) > 0:
        steps = 0
        a = list(range(1, listmax + 1))
      else:
        break
    if med != letsgo:
      while True:
        if letsgo > med:
          del a[:a.index(med) + 1]
          if len(a) == 0:
            print("There is no such element in the list. You're debil.")
            break
          med = a[len(a) // 2]
          print(" ".join([str(x) if x != med else f"[{x}]" for x in a]))
          print("")
          steps += 1
          time.sleep(sleepy)
        if letsgo < med:
          del a[a.index(med):]
          if len(a) == 0:
            print("There is no such element in the list. You're debil.")
            break
          med = a[len(a) // 2]
          print(" ".join([str(x) if x != med else f"[{x}]" for x in a]))
          print('')
          steps += 1
          time.sleep(sleepy)
        if med == letsgo:
          print("Found!", med)
          print("Steps used:", steps)
          print("Steps expected according to log2(" + str(listmax) + "):", stepsexpected)
          print("")
          print("")
          if len(thelist) > 0:
            steps = 0
            a = list(range(1, listmax + 1))
            break
          else:
            break
  print("Done searching!")
  print("One more time? Type nothing as 'Yes'. Type something as 'No'.")
  user_input = str(input())
  if user_input == '':
    if mode == 1:
      searchauto()
    if mode == 2:
      searchmanual()

def searchmanual():
  sleepy, a, med, steps, stepsexpected, thelist, listmax = getstartedmanual()
  main(sleepy, a, med, steps, stepsexpected, thelist, listmax, mode)
def searchauto():
  sleepy, a, med, steps, stepsexpected, thelist, listmax = getstartedauto()
  main(sleepy, a, med, steps, stepsexpected, thelist, listmax, mode)


mode = int(input("Hey there!! Wanna use an automatic binaric search or a manual one? Type 1 or 2 respectively: "))
if mode == 1:
  searchauto()
if mode == 2:
  searchmanual()