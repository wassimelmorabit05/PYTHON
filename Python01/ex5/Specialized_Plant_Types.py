class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name
        self._height = height
        self._age = age

    def grow(self) -> None:
        self._height += 1

    def age_up(self) -> None:
        self._age += 1

    def show(self) -> None:
        print(f"{self.name}: {self._height}cm, {self._age} days old")


# 🌸 Flower
class Flower(Plant):
    def __init__(self, name: str, height: float, age: int, color: str) -> None:
        super().__init__(name, height, age)
        self.color = color
        self.bloomed = False

    def bloom(self) -> None:
        self.bloomed = True

    def show(self) -> None:
        super().show()
        print(f"Color: {self.color}")
        if self.bloomed:
            print(f"{self.name} is blooming beautifully!")
        else:
            print(f"{self.name} has not bloomed yet")


# 🌳 Tree
class Tree(Plant):
    def __init__(self, name: str, height: float, age: int, trunk_diameter: float) -> None:
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self) -> None:
        print(f"Tree {self.name} now produces a shade of {self._height}cm long and {self.trunk_diameter}cm wide.")

    def show(self) -> None:
        super().show()
        print(f"Trunk diameter: {self.trunk_diameter}cm")


# 🥕 Vegetable
class Vegetable(Plant):
    def __init__(self, name: str, height: float, age: int, harvest_season: str) -> None:
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = 0

    def grow(self) -> None:
        super().grow()
        self.nutritional_value += 1

    def age_up(self) -> None:
        super().age_up()
        self.nutritional_value += 1

    def show(self) -> None:
        super().show()
        print(f"Harvest season: {self.harvest_season}")
        print(f"Nutritional value: {self.nutritional_value}")


def main() -> None:
    print("=== Garden Plant Types ===")

    # Flower
    flower = Flower("Rose", 15.0, 10, "red")
    print("\n=== Flower ===")
    flower.show()

    print("\n[asking the rose to bloom]")
    flower.bloom()
    flower.show()

    # Tree
    tree = Tree("Oak", 200.0, 365, 5.0)
    print("\n=== Tree ===")
    tree.show()

    print("\n[asking the oak to produce shade]")
    tree.produce_shade()

    # Vegetable
    veg = Vegetable("Tomato", 5.0, 10, "April")
    print("\n=== Vegetable ===")
    veg.show()

    print("\n[make tomato grow and age for 20 days]")
    for _ in range(20):
        veg.grow()
        veg.age_up()
    veg.show()


if __name__ == "__main__":
    main()