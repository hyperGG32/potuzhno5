
"""
🚗 TASK 7 — Group Car Colors by Brand
Topic: list of tuples → dict of lists

Cars: [("BMW","black"), ("Audi","red"), ("BMW","white"), ("Audi","blue")]
Build a dictionary where key is the brand and value is a list of colors for that brand.

"""
# Starter:
cars = [("BMW","black"), ("Audi","red"), ("BMW","white"), ("Audi","blue")]
# TODO: build brand -> list_of_colors dict and print it
cars_dict = {}
for Tuple in cars:
    if cars_dict.get(Tuple[0]) == None:
        cars_dict[Tuple[0]] = []
        cars_dict[Tuple[0]].append(Tuple[1])
    else:
        cars_dict[Tuple[0]].append(Tuple[1])
print(cars_dict)