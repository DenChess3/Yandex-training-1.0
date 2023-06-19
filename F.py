from sys import stdin


buyers = dict()
for line in stdin:
    name, product, number = line.split()
    number = int(number)
    if name not in buyers:
        buyers[name] = {product: number}
    else:
        buyers[name][product] = buyers[name].get(product, 0) + number

for buyer, products in sorted(buyers.items(), key=lambda x: x[0]):
    print(buyer, ':', sep='')
    for good, count in sorted(products.items(), key=lambda x: x[0]):
        print(good, count)
