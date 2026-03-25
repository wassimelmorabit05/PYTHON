class Plant:
    def __init__(self, name: str, height: int):
        self.name = name
        self.height = height

    def grow(self) -> None:
        self.height += 1

    def display(self) -> None:
        print(f"- {self.name}: {self.height}cm")


# 🌸 FloweringPlant
class FloweringPlant(Plant):
    def __init__(self, name: str, height: int, color: str):
        super().__init__(name, height)
        self.color = color

    def display(self) -> None:
        print(f"- {self.name}: {self.height}cm, {self.color} flowers (blooming)")


# 🏆 PrizeFlower
class PrizeFlower(FloweringPlant):
    def __init__(self, name: str, height: int, color: str, points: int):
        super().__init__(name, height, color)
        self.points = points

    def display(self) -> None:
        print(f"- {self.name}: {self.height}cm, {self.color} flowers, Prize points: {self.points}")


# 📊 Manager
class GardenManager:
    total_gardens = 0  # class variable

    class GardenStats:
        @staticmethod
        def total_growth(plants) -> int:
            return len(plants)

    def __init__(self, owner: str):
        self.owner = owner
        self.plants = []
        GardenManager.total_gardens += 1

    def add_plant(self, plant: Plant) -> None:
        self.plants.append(plant)
        print(f"Added {plant.name} to {self.owner}'s garden")

    def grow_all(self) -> None:
        print(f"\n{self.owner} is helping all plants grow...")
        for plant in self.plants:
            plant.grow()
            print(f"{plant.name} grew 1cm")

    def show_report(self) -> None:
        print(f"\n=== {self.owner}'s Garden Report ===")
        print("Plants in garden:")
        for plant in self.plants:
            plant.display()

        total = self.GardenStats.total_growth(self.plants)
        print(f"\nPlants added: {len(self.plants)}, Total growth: {total}cm")

    @classmethod
    def create_garden_network(cls):
        print(f"\nTotal gardens managed: {cls.total_gardens}")


def main():
    print("=== Garden Management System Demo ===\n")

    garden1 = GardenManager("Alice")
    garden2 = GardenManager("Bob")

    # Add plants
    garden1.add_plant(Plant("Oak Tree", 100))
    garden1.add_plant(FloweringPlant("Rose", 25, "red"))
    garden1.add_plant(PrizeFlower("Sunflower", 50, "yellow", 10))

    # Grow
    garden1.grow_all()

    # Report
    garden1.show_report()

    # Class method
    GardenManager.create_garden_network()


if __name__ == "__main__":
    main()