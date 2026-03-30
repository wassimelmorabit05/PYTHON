class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age

    def grow(self) -> None:
        self.height += 0.8  # كل نهار كتزاد 0.8cm

    def age_up(self) -> None:
        self.age += 1  # كل نهار كيزيد يوم

    def show(self) -> None:
        print(f"{self.name}: {round(self.height, 1)}cm, {self.age} days old")


def main() -> None:
    plant = Plant("Rose", 25.0, 30)

    print("=== Garden Plant Growth ===")

    start_height = plant.height

    for day in range(1, 8):
        print(f"=== Day {day} ===")
        plant.grow()
        plant.age_up()
        plant.show()

    total_growth = round(plant.height - start_height, 1)
    print(f"Growth this week: {total_growth}cm")


if __name__ == "__main__":
    main()