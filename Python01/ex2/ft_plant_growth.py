class Plant:
    def __init__(self, name: str, height: int, age: int):
        self.name = name
        self.height = height
        self.age = age

    def grow(self) -> None:
        self.height += 1

    def age_up(self) -> None:
        self.age += 1

    def get_info(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.age} days old")


def main():
    plant = Plant("Rose", 25, 30)

    print("=== Day 1 ===")
    plant.get_info()

    initial_height = plant.height

    for _ in range(7):
        plant.grow()
        plant.age_up()

    print("=== Day 7 ===")
    plant.get_info()

    growth = plant.height - initial_height
    print(f"Growth this week: +{growth}cm")


if __name__ == "__main__":
    main()