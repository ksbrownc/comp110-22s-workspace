"""An example of for in syntax."""

# names: list[str] = ["Kayla", "Kaleb", "Kisha", "Donnie"]

# # Example of iterating through snames using a while loop.
# print("while output:")
# i: int = 0
# while i <len(names):
#     name: str = names[i]
#     print(name)
#     i += 1

# print("for in...output:")
# # The following for..in loop is the same as the while loop
# for name in names:
#         print(name)

# for x in [1, 2, 3]:
#     print(x)
print("while output:")
i: int = 0
ys: list[int] = [110, 120]
while i < len(ys):
  y: int = ys[i]
  print(y)
  i += 1

print("for in...output:")
ys: list[int] = [110, 120]
for y in ys:
  print(y)
