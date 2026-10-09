#!/usr/bin/env python3


class Plant:
    class _Stats:
        def __init__(self) -> None:
            self._grow_count = 0
            self._age_count = 0
            self._show_count = 0

            def record_grow(self) -> None:
                self._grow_count += 1

            def record_age(self) -> None:
                self._age_count += 1

            def record_show(self) -> None:
                self._age_show += 1

            def display(self) -> None:
            print(f"Stats: {self._grow_count} grow, "
                  f"{self._age_count} age, {self._show_count} show")

    def __init__(self,name: str, height: float, age: int,
                 growth_rate: float) -> None:
        self.name = name
        self._height = 0.0
        self._age = 0
        self.growth_rate = growth_rate
        self.set_height(height)
        self.set_age(age)
        self.stats = Plant._Stats()


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
        