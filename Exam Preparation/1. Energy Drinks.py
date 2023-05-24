from collections import deque
max_caffeine = 300
milligrams  = [int(x) for x in input().split(", ")]
drinks = deque([int(x) for x in input().split(", ")])
caffeine_drunk = 0

while milligrams and drinks:
    test_milligrams = milligrams[-1]
    test_drink = drinks[0]
    if ((test_milligrams * test_drink) + caffeine_drunk) > max_caffeine:
        milligrams.pop()
        drinks.append(drinks.popleft())
        caffeine_drunk -= 30
        if caffeine_drunk < 0:
            caffeine_drunk = 0
    else:
        milli = milligrams.pop()
        drink = drinks.popleft()
        result = milli * drink
        caffeine_drunk += result
if drinks:
    print(f"Drinks left: {', '.join([str(x) for x in drinks])}")
else:
    print("At least Stamat wasn't exceeding the maximum caffeine.")
print(f"Stamat is going to sleep with {caffeine_drunk} mg caffeine.")
