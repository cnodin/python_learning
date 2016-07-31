motorcycles=['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles[0] = 'ducati'
#print ['ducati','yamaha','suzuki']
print(motorcycles)
motorcycles.append('honda')
print(motorcycles)
motorcycles.insert(0, 'ducati')
print(motorcycles)
del motorcycles[0]
print(motorcycles)

#pop
poped_motorcycle = motorcycles.pop()
print(motorcycles)
print(poped_motorcycle)

#delete by value
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)

motorcycles.remove('ducati')
print(motorcycles)
