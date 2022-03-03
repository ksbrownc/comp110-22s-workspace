"""Demonstrate defining a module imported elsewhere."""


THE_ANSWER: int = 42


def main() -> None:
    print(powerful(2, 10))
    print("helpers.py run as a module")


def powerful(x: float, n:float) -> float:
    """Raise x to the power of n."""
    return x ** n




if __name__ == "__main__":
    main()  
# idiom for making a module able to run
# or have its global definitions imported
else: 
    # This is not idiomatic to have an else branch
    print(f"helpers.py wsas  imported: {__name__}")