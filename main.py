import random


class TreasureMap:
    def __init__(self):
        self.coordinates_x = random.randint(0, 9)
        self.coordinates_y = random.randint(0, 9)

    def distance(self, x, y):
        distance = abs(x - self.coordinates_x) + abs(y - self.coordinates_y)
        if distance == 0:
            return "Вы нашли сокровище!"
        elif distance < 3:
            return "Очень близко к сокровищу!"
        elif distance < 6:
            return "Близко к сокровищу!"
        elif distance < 10:
            return "Далеко от сокровища!"
        else:
            return "Очень далеко от сокровища!"


class Player:
    def __init__(self):
        self.count = 0

    def coordinates(self):
        while True:
            try:
                coordinates = input("Введите координаты в формате X,Y: ").strip().split(",")
                x2 = int(coordinates[0])
                y2 = ord(coordinates[1].upper()) - ord('A')
                if x2 < 0 or x2 > 9 or y2 < 0 or y2 > 9:
                    raise ValueError("Координаты выходят за границы поля! Попробуйте еще раз.")
                return x2, y2
            except ValueError as e:
                print(e)


class Game:
    def __init__(self):
        self.map = TreasureMap()
        self.player = Player()

    def start(self):
        print(f"Добро пожаловать в игру «Поиск сокровища»!\n"
              f"На игровом поле размером 10x10 спрятано сокровище. \n "
              f"Ваша задача — найти его за минимальное количество попыток. \n"
              f"Координаты вводятся в формате «x, y», где x — горизонтальная координата 0 до 9, y — вертикальная координата от A до J.\n"
              f"Удачи!")

        while True:
            x, y = self.player.coordinates()
            self.player.count += 1

            if self.coordinates_x = x2 and self.coordinates_y= y2:
                print("Поздравляем! Вы нашли сокровище за", self.player.count, "попыток!")
                break
            else:
                distance = self.map.distance(x, y)
                print(distance)


if __name__ == "__main__":
    game = Game()
    game.start()
