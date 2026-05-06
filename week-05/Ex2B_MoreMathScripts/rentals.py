# tour vans
# importing lirbary
import math

# how many people
tourists = 38

# van information
capacity_per = 15
price_per_day = 250

# how many vans are needed (rounded)
vans_needed = math.ceil(tourists/capacity_per)

# total cost
total_cost = vans_needed*price_per_day

# price per person
per_person = total_cost/tourists

# displaying results
print(f"Vans needed: {vans_needed}")
print(f"Total rental cost: ${total_cost}")
print(f"Cost per person: ${per_person:.2f}")
# Vans needed: 3
# Total rental cost: $750
# Cost per person: $19.74
# there was leftover money because we had to round up to make sure the costs were doable