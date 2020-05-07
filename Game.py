from src.Player import Player


class Game:

    def __init__(self, player1: Player, player2: Player):
        self.player1 = player1
        self.player2 = player2

    def get_score(self) -> str:
        points_player1 = self.player1.get_points()
        points_player2 = self.player2.get_points()
        if points_player1 == points_player2:
            if points_player1 == 0:
                return "Love-All"
            elif points_player1 == 1:
                return "Fifteen-All"
            elif points_player1 == 2:
                return "Thirty-All"

            return "Deuce"

        else:
            if points_player1 == 0:
                if points_player2 == 1:
                    return "Love-Fifteen"
                elif points_player2 == 2:
                    return "Love-Thirty"
                elif points_player2 == 3:
                    return "Love-Forty"

                return "Win for player2"
            elif points_player2 == 0:
                if points_player1 == 1:
                    return "Fifteen-Love"
                elif points_player1 == 2:
                    return "Thirty-Love"
                elif points_player1 == 3:
                    return "Forty-Love"

                return "Win for player1"
            elif points_player1 == 1:
                if points_player2 == 2:
                    return "Fifteen-Thirty"
                elif points_player2 == 3:
                    return "Fifteen-Forty"

                return "Win for player2"
            elif points_player2 == 1:
                if points_player1 == 2:
                    return "Thirty-Fifteen"
                elif points_player1 == 3:
                    return "Forty-Fifteen"

                return "Win for player1"
            elif points_player1 == 2:
                if points_player2 == 3:
                    return "Thirty-Forty"

                return "Win for player2"
            elif points_player2 == 2:
                if points_player1 == 3:
                    return "Forty-Thirty"

                return "Win for player1"
            elif points_player1 >= 3 and points_player2 >= 3:
                if points_player1 > points_player2:
                    distance = points_player1 - points_player2
                    if distance == 1:
                        return "Advantage player1"

                    return "Win for player1"
                else:
                    distance = points_player2 - points_player1
                    if distance == 1:
                        return "Advantage player2"

                    return "Win for player2"

    def won_point(self, player: Player) -> None:
        if self.player1.is_equal(player):
            self.player1.add_point()
        else:
            self.player2.add_point()
