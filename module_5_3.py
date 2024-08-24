class House ():
	def __init__ (self, name, number_of_floors):
		self.name = name
		self.number_of_floors = number_of_floors
		
	def go_to (self, new_floor):
		if new_floor < 1 or new_floor > self.number_of_floors:
			print ('Такого этажа не существует')
		else:
			for int in range (1, new_floor+1):
				print (int)
				
	def __len__ (self):
		return self.number_of_floors
		
	def __str__ (self):
		return f'Название: {self.name}, кол-во этажей: {self.number_of_floors}'
	
	def __eq__(self, other):
		if isinstance (other, House) == True:
			return self.number_of_floors == other.number_of_floors
		else:
			print ('нельзя сравнить')
	
	def __lt__(self, other):
		if isinstance (other, House) == True:
			return self.number_of_floors < other.number_of_floors
		else:
			print ('нельзя сравнить')
	
	def __le__(self, other):
		if isinstance (other, House) == True:
			return self.number_of_floors <= other.number_of_floors
		else:
			print ('нельзя сравнить')
	
	def __gt__(self, other):
		if isinstance (other, House) == True:
			return self.number_of_floors > other.number_of_floors
		else:
			print ('нельзя сравнить')
			
	def __ge__(self, other):
		if isinstance (other, House) == True:
			return self.number_of_floors >= other.number_of_floors
		else:
			print ('нельзя сравнить')
			
	def __ne__(self, other):
		if isinstance (other, House) == True:
			return self.number_of_floors != other.number_of_floors
		else:
			print ('нельзя сравнить')

	def __add__(self, value):
		self.number_of_floors = self.number_of_floors + value
		return self
		
	def __iadd__(self, value):
		self.number_of_floors += value
		return self
		
	def __iadd__(self, value):
		self.number_of_floors = value + self.number_of_floors
		return self					

h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

print ('Исходные данные:')
print(h1)
print(h2)

print ()
print ('Сравнение:')
#__eq__
print('Дом ЖК Эльбрус равен дому ЖК Акация: ', h1 == h2)

# __lt__
print('Дом ЖК Эльбрус меньше домa ЖК Акация: ', h1 < h2)

 #__le__
print('Дом ЖК Эльбрус меньше либо равен дому ЖК Акация: ', h1 <= h2) 

# __gt__
print('Дом ЖК Эльбрус больше дома ЖК Акация: ', h1 > h2) 

# __ge__
print('Дом ЖК Эльбрус больше либо равен дому ЖК Акация: ', h1 >= h2) 

# __ne__
print('Дом ЖК Эльбрус не равен дому ЖК Акация: ', h1 != h2) 

print ()
print ('Сложение:')
# __add__
h1.__add__(10)
print (h1)
print ('Дом ЖК Эльбрус равен дому ЖК Акация: ', h1 == h2)

# __iadd__
h1.__add__(10)
print (h1)

# __radd__
h2.__add__(10)
print (h2)
		
