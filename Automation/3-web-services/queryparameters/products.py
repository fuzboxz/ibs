class Products():
    def __init__(self):
        self.products = []
        with open(file="products.csv", mode="r") as f:
            # skip header
            f.readline()
            while (line := f.readline()):
                line = line.replace("\n","").split(sep=';')
                if len(line) == 4:
                    self.products.append(Product(id=line[0], name=line[1], price=line[2], qty=line[3]))

    def findbyName(self, name):
        matches = []
        for item in self.products:
            if name in item.name:
                matches.append(item)
        return matches 

    def findbyPrice(self, price):
        matches =[]
        for item in self.products:
            if price == item.price:
                matches.append(item)
        return matches

    def findbyQty(self, qty):
        matches = []
        for item in self.products:
            if qty == item.qty:
                matches.append(item)
        return matches

class Product():
    def __init__(self, id, name, price, qty):
        self.id = id
        self.name = name
        self.price = price
        self.qty = qty


if __name__=="__main__":
    prod = Products()
    for product in prod.products:
        print(product.id, product.name, product.price, product.qty, sep=" - ")