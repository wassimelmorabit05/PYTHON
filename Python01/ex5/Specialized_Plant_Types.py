class Plant:
    def __init__(self, name: str, height: int, age: int):
        self.name = name
        self.height = height
        self.age = age

    def display(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.age} days")


# 🌸 Flower
class Flower(Plant):
    def __init__(self, name: str, height: int, age: int, color: str):
        super().__init__(name, height, age)
        self.color = color

    def bloom(self) -> None:
        print(f"{self.name} is blooming beautifully!")

    def display(self) -> None:
        print(f"{self.name} (Flower): {self.height}cm, {self.age} days, {self.color} color")


# 🌳 Tree
class Tree(Plant):
    def __init__(self, name: str, height: int, age: int, trunk_diameter: int):
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self) -> None:
        shade = self.trunk_diameter * 1.5
        print(f"{self.name} provides {shade} square meters of shade")

    def display(self) -> None:
        print(f"{self.name} (Tree): {self.height}cm, {self.age} days, {self.trunk_diameter}cm diameter")


# 🥕 Vegetable
class Vegetable(Plant):
    def __init__(self, name: str, height: int, age: int, harvest_season: str, nutritional_value: str):
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

    def display(self) -> None:
        print(f"{self.name} (Vegetable): {self.height}cm, {self.age} days, {self.harvest_season} harvest")

    def show_nutrition(self) -> None:
        print(f"{self.name} is rich in {self.nutritional_value}")


def main():
    print("=== Garden Plant Types ===\n")

    # Flower
    rose = Flower("Rose", 25, 30, "red")
    tulip = Flower("Tulip", 20, 25, "yellow")

    # Tree
    oak = Tree("Oak", 500, 1825, 50)
    pine = Tree("Pine", 400, 1500, 40)

    # Vegetable
    tomato = Vegetable("Tomato", 80, 90, "summer", "vitamin C")
    carrot = Vegetable("Carrot", 30, 70, "winter", "vitamin A")

    # Display
    rose.display()
    rose.bloom()

    print()

    oak.display()
    oak.produce_shade()

    print()

    tomato.display()
    tomato.show_nutrition()


if __name__ == "__main__":
    main()