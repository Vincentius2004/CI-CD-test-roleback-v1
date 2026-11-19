"""Program diskon sederhana untuk demonstrasi CI/CD dan rollback."""


def final_price(price: float, discount_percent: float) -> float:
    """Return the price after a percentage discount."""
    if price < 0:
        raise ValueError("price cannot be negative")
    if not 0 <= discount_percent <= 100:
        raise ValueError("discount_percent must be between 0 and 100")

    return round(price * (1 - discount_percent / 100), 2)


if __name__ == "__main__":
    print(f"Harga setelah diskon: Rp{final_price(100_000, 10):,.2f}")
