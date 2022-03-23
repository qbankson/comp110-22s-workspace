"""An example of for in."""

names: list[str] = ["Kris", "Kaki", "E", "Marc"]

#Example of iterating through names in a while loop
i: int = 0
while i < len(names):
    name: str = names[i]
    print(name)
    i += 1


#Example of for...in loop is the same as the while loop
print("for...in items")
for name in names:
    print(name)

ys: list[int] = [110, 120]
for y in ys:
  print(y)

i: int = 0
ys: list[int] = [110, 120]
while i < len(ys):
  y: int = ys[i]
  print(y)
  i += 1
