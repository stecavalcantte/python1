#!/usr/bin/env python3


class Plant:
    name: str
    height: float
    age: int
    growth_rate: float

    def grow(self) -> None:
        self.height += self.growth_rate

    def age_one_day(self) -> None:
        self.age += 1

    def show(self) -> None:
        print(f"{self.name}: {self.height:.1f}cm, {self.age} days old")


def main() -> None:
    print("=== Garden Plant Growth ===")

    rose = Plant()
    rose.name = "Rose"
    rose.height = 25.0
    rose.age = 30
    rose.growth_rate = 0.8

    start_height: float = rose.height
    rose.show()

    for day in range(1, 8):
        print(f"=== Day {day} ===")
        rose.grow()
        rose.age_one_day()
        rose.show()

    growth_total: float = round(rose.height - start_height, 1)
    print(f"Growth this week: {growth_total}cm")


if __name__ == "__main__":
    main()
