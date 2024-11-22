import threading
from time import sleep


class Knight(threading.Thread):
    def __init__(self, name:str, power:int, enemy_nun: int = 100):
        threading.Thread.__init__(self)
        self.name = name
        self.power = power
        self.enemy_nun = enemy_nun

    def run(self):
        print(f'{self.name}, на нас напали!')
        day = 0
        while self.enemy_nun > 0:
            sleep(1)
            day += 1
            self.enemy_nun -= self.power
            print(f'{self.name} сражается {day} дней(дня),',
                  f'осталось {self.enemy_nun} войнов.')
        print(f'{self.name} одержал победу спустя {day} дней(дня)!')


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)



first_knight.start()
second_knight.start()
first_knight.join()
second_knight.join()
print('Все битвы закончились!')
