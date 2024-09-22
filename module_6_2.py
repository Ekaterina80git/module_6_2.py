class Vehicle:
    __COLOR_VARIANTS = ["blue",'red','green','black','white']# список цветов

    def __init__(self,owner,__model,__engine_power,__color):
          self.owner = str(owner) # владелец
          self.__model = str(__model)# модель
          self.__engine_power = int(__engine_power)  #мощность двигателя (не можем изменять)
          self.__color = str(__color)  # цвет ( не можем изменять)
    def get_model(self):
        return f'Модель:{self.__model}'
    def get_horsepower(self):
        return f'Мощность двигателя:{self.__engine_power}'
    def get_color(self):
        return f'Цвет:{self.__color}'
    def print_info(self):
        print(self.get_model())
        print(self.get_horsepower())
        print(self.get_color())
        print(f"Владелец:{self.owner}")
    def set_color(self,new_color:str):
        if new_color.lower() in (color.lower() for color in self.__COLOR_VARIANTS):
            self.__color = new_color
        else:
            print(f'Нельзя сменить цвет на {new_color}')



class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5 # только 5 пассажиров


vehicle1 = Sedan("Katerina",'BMV',110,'red')

# изночальные свойства
vehicle1.print_info()

# меняем свойства вызывая методы
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = "Den"
# проверяем что изменилось

vehicle1.print_info()