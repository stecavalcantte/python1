#!/usr/bin/env python3


class Plant:
    def __init__(self, name: str, height: float, age: int,
                 growth_rate: float) -> None:
        self.name = name
        self._height = 0.0
        self._age = 0
        self.growth_rate = growth_rate
        self.set_height(height)
        self.set_age(age)

    def set_height(self, height: float) -> None:
        if height < 0:
            print(f"{self.name}: Error, height can't be negative")
            print("Height update rejected")
            return
        self._height = height

    def get_height(self) -> float:
        return self._height

    def set_age(self, age: int) -> None:
        if age < 0:
            print(f"{self.name}: Error, age can't be negative")
            print("Age update rejected")
            return
        self._age = age

    def get_age(self) -> int:
        return self._age

    def grow(self) -> None:
        self.set_height(self._height + self.growth_rate)

    def age_one_day(self) -> None:
        self.set_age(self._age + 1)

    def show(self) -> None:
        print(f"{self.name}: {self._height:.1f}cm, {self._age} days old")


def main() -> None:
    print("=== Garden Security System ===")

    rose = Plant("Rose", 15.0, 10, 0.8)
    print(f"Plant created: {rose.name}: "
          f"{rose.get_height():.1f}cm, {rose.get_age()} days old")
    print()

    rose.set_height(25)
    print(f"Height updated: {rose.get_height():.0f}cm")
    rose.set_age(30)
    print(f"Age updated: {rose.get_age()} days")
    print()

    rose.set_height(-10)
    rose.set_age(-5)
    print()

    print(f"Current state: {rose.name}: "
          f"{rose.get_height():.1f}cm, {rose.get_age()} days old")


if __name__ == "__main__":
    main()
