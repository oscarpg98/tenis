class Player:

    def __init__(self, name: str):
        self.name = name
        self.points = 0

    def get_name(self) -> str:
        return self.name

    def get_points(self) -> int:
        return self.points

    def is_equal(self, player) -> bool:
        return self.name == player.name

    def add_point(self) -> None:
        self.points = self.points + 1
