import random

word_list = ['mouse', 'cat', 'dog', 'came', 'house']

rando_world = random.choice(word_list)
world_showed = []
for letter in rando_world:
    world_showed.append("_")

choisen_world = input('guess a letter: ').lower()

print(f'hint the solution is {rando_world}')
print(world_showed)

for pos in range(len(rando_world)):
    if rando_world[pos] == choisen_world:
        world_showed[pos]=choisen_world

print(world_showed)
