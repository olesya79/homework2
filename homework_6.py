# создаём класс "Легковые автомобили"
class PassengerCar:
    # прописываем свойства класса
    def __init__(self, stamp, model, year, speed):
        self.stamp = stamp # марка
        self.model = model # модель
        self.year = year   # год выпуска
        self.speed = speed # скорость

# наследуем класс "Автомобили"
class Car(PassengerCar):
    pass

# создаём объект класса "Легковые автомобили"
car1 = Car('Мерседес', 'Е500', 2000, 100)
print(car1.stamp)
print(car1.model)
print(car1.year)
print(car1.speed)
