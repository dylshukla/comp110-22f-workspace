"""Examples of the tuple and range sequences."""

# An example of a tuple without tupue aliasing.
goat: tuple[str, int] = ("MJ", 23)

# TUPLES are sequences, so theyre 0-indexed
print(goat[0])
print(goat[1])

# sequences have lengths
print(len(goat))

#sequences ar eiterable in for..in loops
#meaning you can loop over them with for...in
for item in goat:
    print(item)


# cannot reassign, append, pop, etc. a tuple

# we can "invent" our own type with a type alias
Player = tuple[str, int]

# once weve aliased a type, we can create variables of that type
unc_poy: Player = ("Bacot", 5)

# in a strange world, where jersey number changes
unc_poy = (unc_poy[0], unc_poy[1] + 1)

# a range is another common swequence type
zero_to_nine: range = range(0, 10, 1)

# We can access items of the range
print(zero_to_nine[0])
print(zero_to_nine[9])


for i in zero_to_nine:
    print(i)

# we can have different steps for more control
odds_to_99: range = range(1, 100, 2)
for i in odds_to_99:
    print(i)


names: list[str] = ["kris", "alyssa", "michael", "lebron"]
for i in range(len(names)):
    print(f"{i}. {names[i]}")


for i in range(0, len(names), 2):
    print(f"{i}. {names[i]}")

print(odds_to_99.stop)