#kush

import random
import time

print("\nWelcome to Kush's dice-rolling program! Press ctrl + c at any time to exit!")
time.sleep(2)

try:
    while True:
        print("\nRolling your die...")
        time.sleep(1)
        a = random.randint(1,6)
        print("\nYour number is",a)
        time.sleep(1)

except KeyboardInterrupt:
    pass
