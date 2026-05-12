#importing 3 modules
import random
import math
import statistics

#creating variables
vals_1_100 = range(1, 100) # 1-99
vals_sample = random.sample(vals_1_100, 75) #selecting 75 random numbers (no repeats)
vals_choice = random.choices(vals_1_100, k=200) # 200 numbers (repeats)
radius = random.randint(3, 10) #random radius (3-10)
pi = math.pi #value of pi