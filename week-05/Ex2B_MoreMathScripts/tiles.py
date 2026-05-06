# tiling a room
# importing library
import math

# room dimensions example in feet
length = 14
width = 12

# tiles needed (each 1x1 ft)
tiles_needed = length*width

# tile per box
per_box = 12

# what is needed to complete a box
boxes_needed = tiles_needed/per_box

# rounding
boxes_needed = math.ceil(boxes_needed)

# 10% more tiles (backups)
extra_tiles = tiles_needed*0.10

# tiles needed including extras
total_with_extras = tiles_needed+extra_tiles

# total boxes + extras (rounded)
total_boxes = math.ceil(total_with_extras/per_box)

# displaying results
print(f"Boxes needed: {boxes_needed}")
print(f"Total with extra 10%: {total_boxes}")
# Boxes needed: 14
# Total with extra 10%: 16