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

class Birds(Animals_with_resource):
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
		self.voice = 'бубубу'
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



# Создаю список всех животных:

pet_obj = []
i = 0
for one_pet in list_animals:
	if one_pet['anym_type'] == 'cow':
		pet_obj.append(Cows(one_pet['anym_name']))
	elif one_pet['anym_type'] == 'goat':
		pet_obj.append(Goats(one_pet['anym_name']))
	elif one_pet['anym_type'] == 'sheep':
		pet_obj.append(Sheep(one_pet['anym_name']))
	elif one_pet['anym_type'] == 'chicken':
		pet_obj.append(Hen(one_pet['anym_name']))
	elif one_pet['anym_type'] == 'goose':
		pet_obj.append(Gooses(one_pet['anym_name']))
	elif one_pet['anym_type'] == 'duck':
		pet_obj.append(Ducks(one_pet['anym_name']))
	i = i + 1
sum_weight = 0
for one_pet in pet_obj:
	print('Pet name:', one_pet.name, 'pet type:', one_pet.anim_type, 'pet voice:', one_pet.voice)
	sum_weight = sum_weight + int(one_pet.weight)
print('Total weight:', sum_weight)

i = 0
while i < len(pet_obj):
	print('====Берем животное номер',i,'====')
	print('     Это животное типа:', pet_obj[i].anim_type,' его зовут:', pet_obj[i].name, 'у него есть ', pet_obj[i].quantity, 'ресурса', pet_obj[i].res_name)
	print('     Будем',pet_obj[i].resource_action_name,' ',pet_obj[i].res_name,' у животного')
	pet_obj[i].get_resource(2)
	print('     У животного',pet_obj[i].anim_type,' ', pet_obj[i].name, 'осталось ', pet_obj[i].quantity, 'ресурса', pet_obj[i].res_name)
	print('     Покормим животное')
	pet_obj[i].set_resource(8)
	print('     У животного',pet_obj[i].anim_type,' ', pet_obj[i].name, 'осталось ', pet_obj[i].quantity, 'ресурса', pet_obj[i].res_name)
	print('====Животное обработано====')
	i = i + 1

