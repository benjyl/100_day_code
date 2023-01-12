class Fish:
    def __init__(self) -> None:
        self.num_eyes = 2

    def breath(self):
        print("inhale, exhale")


class Human(Fish):
    def __init__(self) -> None:
        super().__init__()
