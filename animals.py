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
	def __init__(self,anim_type, name, voice, hungry, legs = 4, weight = 1 ):
		self.anim_type = anim_type
		self.name = name
		self.voice = voice
		self.hungry = hungry
		self.legs = legs
		self.weight = weight
		self.classname = ''

	def feed(self):
		self.hungry = False
		return self.hungry

class Animals_with_resource(Animals):
	def __init__(self,resource_name,resource_action_name,quantity):
		self.resource_name = resourse_name
		self.resource_action_name = resource_action_name
		self.quantity = quantity
	def get_resource(self, value = 1):
		if value < self.quantity :
			self.quantity = self.quantity - value
		return [self.resource_name, resource_action_name, value]

class Cows(Animals_with_resource):
	def __init__(self):
		self.voice = 'мууу'
		Animals_with_resource.__init__(self)
	def voice(self):
		return self.voice
	
	
class Goats(Animals_with_resource):
	def __init__(self):
		self.voice = 'беее'
		Animals_with_resource.__init__(self)
	def voice(self):
		return self.voice
	




# Создаю список со всеми животными:
pet_obj = []
i = 0
for one_pet in list_animals:
	i = i + 1
	pet_obj.append(Animals(one_pet['anym_type'], one_pet['anym_name'],'',True))
#	print(one_pet)
#	print('Type: ',one_pet['anym_type'], 'Name: ',one_pet['anym_name'])
'''
	if one_pet['anym_type'] == 'goat':
		pet_obj.append(Animals('goat', one_pet['anym_name'],'',True))
	elif one_pet['anym_type'] == 'hen':
		pet_obj.append(Animals('hen', one_pet['anym_name'],'',True))
	else: 
'''
	
	#print(pet_obj[i].name,' ',pet_obj[i].weight)

# Вывожу список со всеми животными:
for other_pet in pet_obj:
	#принт для отладки:
	#print(type(other_pet))
	print('Тип: ', other_pet.anim_type,' Имя: ', other_pet.name,' Вес: ',other_pet.weight, ' Голодное: ', other_pet.hungry, ' Голос: ',other_pet.voice)

print("Животное по имени ", pet_obj[0].name," голодное?", pet_obj[0].hungry)
pet_obj[0].feed
print("Животное по имени ", pet_obj[0].name," голодное?", pet_obj[0].hungry)



'''

	
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
'''



