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
	''' Main class for all animals.'''
	def __init__(self,anim_type, weight, voice):
		self.anim_type = anim_type
		self.voice = voice
		self.weight = weight

	def set_resource(self):
		pass
	def get_resource(self):
		pass
	def get_weight(self):
		return self.weight
	def voice(self):
		return self.voice

class Animals_with_resource(Animals):
	def __init__(self, anim_type, weight, res_name, resource_action_name, quantity, voice):
		self.res_name = res_name
		self.resource_action_name = resource_action_name
		self.quantity = quantity
		self.anim_type = anim_type
		self.voice = voice
		Animals.__init__(self, anim_type, weight, voice)
	def set_resource(self, value):
		if value > 0:
			self.quantity = self.quantity + value
		else :
			print('malo edy')
		return self.quantity
	def get_resource(self, value):
		if value < self.quantity :
			self.quantity = self.quantity - value
		else:
			self.quantity = 0
		return [self.res_name, self.resource_action_name, self.quantity]

class Milking(Animals_with_resource):
	def __init__(self,anim_type, quantity, name, weight ):
		self.anim_type = anim_type
		self.res_name = 'молоко'
		self.resource_action_name = 'доить'
		self.quantity = quantity
		self.name = name
		self.weight = weight
		Animals_with_resource.__init__(self, self.anim_type, self.weight, self.res_name, self.resource_action_name, self.quantity, self.voice)

class Birds(Animals):
	def __init__(self,anim_type, quantity, name, weight ):
		self.anim_type = anim_type
		self.res_name = 'яйца'
		self.resource_action_name = 'собирать'
		self.quantity = quantity
		self.name = name
		self.weight = weight
		Animals_with_resource.__init__(self, self.anim_type, self.weight, self.res_name, self.resource_action_name, self.quantity, self.voice)

class Cows(Milking):
	def __init__(self, name, quantity = 10, weight = 200):
		self.anim_type = 'cow'
		self.quantity = quantity
		self.name = name
		self.weight = weight
		self.voice = 'мууу'
		Milking.__init__(self, self.anim_type, self.quantity, self.name, self.weight)

class Goats(Milking):
	def __init__(self, name, quantity = 3, weight = 30):
		self.anim_type = 'goat'
		self.quantity = quantity
		self.name = name
		self.weight = weight
		self.voice = 'беее'
		Milking.__init__(self, self.anim_type, self.quantity, self.name, self.weight)

class Sheep(Animals_with_resource):
	def __init__(self, name, quantity = 2, weight = 20):
		self.anim_type = 'sheep'
		self.res_name = 'шерсть'
		self.resource_action_name = 'стричь'
		self.quantity = quantity
		self.name = name
		self.weight = weight
		Animals_with_resource.__init__(self, self.anim_type, self.weight, self.res_name, self.resource_action_name, self.quantity, self.voice)

class Hen(Birds):
	def __init__(self, name, quantity = 5, weight = 2):
		self.anim_type = 'hen'
		self.quantity = quantity
		self.name = name
		self.weight = weight
		self.voice = 'кудах'
		Birds.__init__(self, self.anim_type, self.quantity, self.name, self.weight)

class Ducks(Birds):
	def __init__(self, name, quantity = 3, weight = 3):
		self.anim_type = 'duck'
		self.quantity = quantity
		self.name = name
		self.weight = weight
		self.voice = 'гагага'
		Birds.__init__(self, self.anim_type, self.quantity, self.name, self.weight)

class Gooses(Birds):
	def __init__(self, name, quantity = 3, weight = 3):
		self.anim_type = 'goose'
		self.quantity = quantity
		self.name = name
		self.weight = weight
		self.voice = 'гугугу'
		Birds.__init__(self, self.anim_type, self.quantity, self.name, self.weight)

'''
cow1 = Cows('Буренка', 5)
cow2 = Cows('Рыжуха', 5)
goat1 = Goats('Рогатая',2)
sheep1 = Sheep('Козлрог')

print('Pet1 resource', cow1.res_name, 'Pet1 can get', cow1.resource_action_name,'Ресурса осталось', cow1.quantity)
print('goat1 resource', goat1.res_name, '== can get ==', goat1.resource_action_name,'Ресурса осталось', goat1.quantity)
print('Pet1 resorce', cow1.quantity, 'Pet1 говорит', cow1.voice)
print('Goat1 resource', goat1.quantity, 'Goat say', goat1.voice)
cow1.get_resource(2)
print('Pet1 resorce', cow1.quantity)
'''
#goose1 = Gooses('Bely')
#print('goose1 resource', goose1.res_name, 'Pet1 can get', goose1.resource_action_name,'Ресурса осталось', goose1.quantity)
# Создаю список со всеми животными:

pet_obj = []
i = 0
for one_pet in list_animals:
	if one_pet['anym_type'] == 'cow':
		pet_obj.append(Cows(one_pet[anym_name]))
	elif one_pet['anym_type'] == 'goat':
		pet_obj.append(Goats(one_pet[anym_name]))
	elif one_pet['anym_type'] == 'sheep':
		pet_obj.append(Sheep(one_pet[anym_name]))
	elif one_pet['anym_type'] == 'hen':
		pet_obj.append(Hen(one_pet[anym_name]))
#	elif one_pet['anym_type'] == 'goose':
#		pet_obj.append(Gooses(one_pet[anym_name]))
	elif one_pet['anym_type'] == 'duck':
		pet_obj.append(Ducks(one_pet[anym_name]))
	i = i + 1

print('Pets:', pet_obj)



