def odd_and_even(phrase: list[int]) -> list[int]:
  i: int = 0
  freshlist: list[int] = []
  for num in phrase:
    if i % 2 == 0 and phrase[i] % 2 != 0:
        freshlist.append(phrase[i])
    i += 1
  return freshlist


print(odd_and_even([2, 9, 4, 17, 9, 10, 15, 13, 14, 21]))
print(odd_and_even([1, 1, 1, 0, 1]))
  

