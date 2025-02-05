def sort(width, height, length, mass):
    # Basic input validation
    for value in (width, height, length, mass):
        if not isinstance(value, (int, float)) or value < 0:
            raise ValueError("All dimensions and mass must be non-negative numbers.")

    volume = width * height * length
    bulky = (volume >= 1000000) or (width >= 150) or (height >= 150) or (length >= 150)
    heavy = mass >= 20

    if bulky and heavy:
        return "REJECTED"
    elif bulky or heavy:
        return "SPECIAL"
    else:
        return "STANDARD"


if __name__ == "__main__":
    # Simple demo run
    print("Demo run (50, 50, 50, 10):", sort(50, 50, 50, 10))
