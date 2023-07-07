from dataclasses import dataclass
from decimal import Decimal


@dataclass
class Item:
    name: str
    price: Decimal
    quantity: int


def print_aligned_row(row: list[str | int | Decimal], space: int = 12) -> None:
    row_items = "".join((f"{row_item:>{space}}" for row_item in row))
    print(row_items)


def main():
    # Create a shopping cart
    items = [
        Item("Apple", Decimal("1.50"), 10),
        Item("Banana", Decimal("2.00"), 2),
        Item("Pizza", Decimal("11.90"), 5),
    ]

    total = sum(item.price * item.quantity for item in items)

    # Print the cart
    headers = ["Item", "Price", "Qty", "Total"]
    print("Shopping Cart:")
    print_aligned_row(headers)
    for item in items:
        total_price = item.price * item.quantity
        print_aligned_row(
            [item.name, "$", item.price, item.quantity, "$", total_price], space=8
        )
    print("=" * 40)
    print(f"Total: ${total}")


if __name__ == "__main__":
    main()
