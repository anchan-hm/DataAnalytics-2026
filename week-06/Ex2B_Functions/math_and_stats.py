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

# Experimenting with a subset of integers 1-100
sample_sum = sum(vals_sample) #sum of 75 numbers
sample_avg = statistics.mean(vals_sample) #average of 75 numbers
sample_median = statistics.median(vals_sample) #median of 75 numbers

#displaying outputs for vals_sample as sample_
print("_Experimenting with a subset of integers 1-100:")
print(f"Sum of 75 sample values from 1 to 100: {sample_sum}")
print(f"Average of 75 sample values: {sample_avg}")
print(f"Median of 75 sample values: {sample_median}")
print('\n') #line break

# Experimenting with a SUPERSET of 200 numbers, integers 1-100
choices_avg = statistics.mean(vals_choice) #average of 200 values
choices_median = statistics.median(vals_choice) #median of 200 values
choice_mode = statistics.mode(vals_choice) #mode of 200 values
choices_stdev = statistics.stdev(vals_choice) # standard deviation
choices_variance = statistics.variance(vals_choice) #variance

#displaying output for vals_choice as choice
print("_Experimenting with a superset of 200 values, integer 1-100:")
print(f"Average of 200 values: {choices_avg}")
print(f"Median of 200 values: {choices_median}")
print(f"Mode of 200 values: {choice_mode}")
print(f"Standard deviation of 200 values: {choices_stdev}")
print(f"Variance of 200 values: {choices_variance}")
print('\n') #line break

# Modeling a random circle
area = pi*(radius**2) #area formula for a circle
area_r_up = math.ceil(area) #rounding up
area_r_down = math.floor(area) #rounding down

#displaying output for are of a circle
print("_Modeling a random circle:")
print(f"Radius = {radius}, area = {area_r_up} (rounded up to the nearest integer)")
print(f"Radius = {radius}, area = {area_r_down} (rounded down to the nearest integer)")

# Final outputs
# _Experimenting with a subset of integers 1-100:
# Sum of 75 sample values from 1 to 100: 3854
# Average of 75 sample values: 51.38666666666666
# Median of 75 sample values: 53


# _Experimenting with a superset of 200 values, integer 1-100:
# Average of 200 values: 46.45
# Median of 200 values: 43.5
# Mode of 200 values: 70
# Standard deviation of 200 values: 27.78050182064815
# Variance of 200 values: 771.7562814070352


# _Modeling a random circle:
# Radius = 3, area = 29 (rounded up to the nearest integer)
# Radius = 3, area = 28 (rounded down to the nearest integer)