"""Lists are ordered, mutable collections."""

scores = [85, 90, 78]
scores.append(92)
scores.sort()
matrix = [[1, 2], [3, 4]]
print(f"scores={scores}; top two={scores[-2:]}; matrix item={matrix[1][0]}")
