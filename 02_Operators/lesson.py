"""The most common Python operators in one focused script."""

left, right = 10, 3
print(f"arithmetic: +={left + right}, /={left / right}, //={left // right}, **={left ** right}")
print(f"comparison/logical: {left > right and right > 0}")
items = ["a", "b", "c"]
same_items = items
print(f"membership: {'a' in items}; identity: {items is same_items}")
print(f"bitwise AND: {6 & 3}")
