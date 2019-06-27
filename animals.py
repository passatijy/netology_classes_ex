'''
Вы приехали помогать на ферму Дядюшки Джо и видите вокруг себя множество разных животных:

attributes:
	types
		voice
	names
	weight

interfaces:
	all
		feed
	cow, goat
		milk
	sheep
		cut
	chicken, duck, goose
		egg


гусей "Серый" и "Белый"
корову "Маньку"
овец "Барашек" и "Кудрявый"
кур "Ко-Ко" и "Кукареку"
коз "Рога" и "Копыта"
и утку "Кряква"
Со всеми животными вам необходимо как-то взаимодействовать:

кормить
корову и коз доить
овец стричь
собирать яйца у кур, утки и гусей
различать по голосам(коровы мычат, утки крякают и т.д.)
Задача №1
Нужно реализовать классы животных, не забывая использовать наследование, 
определить общие методы взаимодействия с животными и дополнить их в дочерних классах, если потребуется.

Задача №2
Для каждого животного из списка должен существовать экземпляр класса. Каждое животное требуется накормить и подоить/постричь/собрать яйца, если надо.

Задача №3
У каждого животного должно быть определено имя(self.name) и вес(self.weight).

Необходимо посчитать общий вес всех животных(экземпляров класса);
Вывести название самого тяжелого животного.
'''

list_animals = [ 
	{'anym_type':'goose','anym_name':'Серый'},  
	{'anym_type':'goose','anym_name':'Белый'},
	{'anym_type':'cow','anym_name':'Манька'}, 
	{'anym_type':'sheep','anym_name':'Барашек'},
	{'anym_type':'sheep','anym_name':'Кудрявый'},
	{'anym_type':'chicken','anym_name':'Ко-Ко'},
	{'anym_type':'goat','anym_name':'Рога'},
	{'anym_type':'goat','anym_name':'Копыта'},
	{'anym_type':'duck','anym_name':'Кряква'},
	]


class Animals:
	def __init__(self, name, legs = 4, weight = 1, voice, hungry)
	self.name = ''
	self.voice = ''
	hungry = True
	classname = ''

	def feed(self):
		self.hungry = False


class Milking(Animals):
	milk = 5
	resourse_name = 'молоко'
	def get_milk(self, value = 1):
		if value < self.milk :
			self.milk = self.milk - value
		return [self.milk, value]

class Cows(Milking):
	classname = 'cow'
	voice = 'муууу'
	
class Goats(Milking):
	classname = 'goat'
	voice = 'беее'
	
class Sheep(Animals):
	classname = 'sheep'
	pass

class Birds(Animals):
	eggs = 5
	resource_name = 'яйцо'
	def get_egg(self, value):
		if value < self.eggs :
			self.eggs = self.eggs - value
		return self.eggs, value

class Hen(Birds):
	classname = 'hen'
	pass

class Ducks(Birds):
	classname = 'duck'
	voice = 'крякря'

class Gooses(Birds):
	classname = 'goose'
	pass


anim1 = Cows()

print('Животное 1: ', anim1.classname, '  Оно может давать ', anim1.resource_name, 'было ', anim1.get_milk(3)[0], ' осталось ', anim1.get_milk(5)[1])

