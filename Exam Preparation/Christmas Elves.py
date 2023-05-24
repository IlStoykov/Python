# 1.	Christmas Elves
from collections import deque

energy = deque([int(x) for x in input().split()])
box = [int(x) for x in input().split()]
elvs_enery = 0
toys_prepared = 0
counter = 0

while energy and box:
    while energy and energy[0] < 5:
        energy.popleft()
    if not energy:
        break

    elf = energy.popleft()
    gift = box.pop()
    counter += 1
    toys_craft = 1
    energy_spent = gift
    energy_increase = 1

    if counter % 3 == 0:
        toys_craft = 2
        energy_spent *= 2

    if counter % 5 == 0:
        toys_craft = 0
        energy_increase = 0

    if energy_spent <= elf:
        toys_prepared += toys_craft
        elvs_enery += energy_spent
        energy.append(elf - energy_spent + 1)
    else:
        box.append(gift)
        energy.append(elf * 2)


    # if counter % 15 == 0 and elf >= 2 * gift:
    #     elvs_enery += 2 * gift
    #     energy.append(elf - (2 * gift))
    #
    # elif counter % 5 == 0 and elf >= gift:
    #     elvs_enery += gift
    #     energy.append(elf - gift)
    #
    # elif counter % 3 == 0 and elf >= 2 * gift:
    #     toys_prepared += 2
    #     elvs_enery += 2 * gift
    #     energy.append(elf - (2 * gift) + 1)
    #
    # elif elf >= gift and counter % 3 != 0:
    #     toys_prepared += 1
    #     elvs_enery += gift
    #     energy.append(elf - gift + 1)
    #
    # else:
    #     box.append(gift)
    #     energy.append(elf * 2)

print(toys_prepared)
print(elvs_enery)
print(energy)
print(box)
