from collections import Counter
inventory = Counter()

loot = {"sword": 1, "bread": 3}
inventory.update(loot)
print(inventory)
# Counter({'bread': 3, 'sword': 1})

more_loot = {"sword": 1, "apple": 1}
inventory.update(more_loot)
print(inventory)
# Counter({'bread': 3, 'sword': 2, 'apple': 1})


print(len(inventory))
# 3

print(sum(inventory))
# 6




