quantity_size = input()

quantity_size = quantity_size.split(' ')
quantity = int(quantity_size[0])
size = int(quantity_size[1])

splits = []
while len(splits) < quantity-1:
    splits.append(int(input()))

sum = size
for split in range(len(splits)):
    sum = sum + (size - splits[split])

def calculate_square(i):
    return size * i
print(calculate_square(sum))



