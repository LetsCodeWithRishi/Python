"""Function definitions, defaults, return values, scope, and lambdas."""

TAX_RATE = 0.05


def total(price: float, quantity: int = 1) -> float:
    """Return a price including a module-level tax rate."""
    return price * quantity * (1 + TAX_RATE)


square = lambda value: value * value
print(f"Total: {total(10, 2):.2f}; square: {square(4)}")
