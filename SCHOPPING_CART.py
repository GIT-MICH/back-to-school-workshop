class Product:
    counter_id = 0

    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.__class__.counter_id += 1
        self.id = self.counter_id

    def __str__(self):
        return f"\t {self.id}) {self.name} - {self.price} zł \n"


class ShoppingCart:
    def __init__(self):
        self.products = {}
        self.quantities = {}

    def __str__(self):
        return "PRODUCTS:{}, QUANTITY: {}".format([name for name in self.products.values()], self.quantities)

    def add_product(self, product):
        q = self.quantities.get(product.id, 0)
        q += 1
        self.products[product.id] = product
        self.quantities[product.id] = q

    def remove_product(self, product):
        if product.id in self.products:
            del self.products[product.id]
            del self.quantities[product.id]

    def change_product_quantity(self, product, new_quantity):
        if int(new_quantity) < 0:
            raise ValueError("Negative quantity not supported")
        if product.id in self.products:
            if int(new_quantity) > 0:
                self.quantities[product.id] = new_quantity
            else:
                self.remove_product(product)

    def get_receipt(self):
        total = 0.0
        res = ""
        for p_id in self.products:
            p = self.products[p_id]
            q = self.quantities[p_id]
            t = p.price * q
            total += t
            res += f"{p.name} - amount: {q}, price: {p.price:.2f}zł, total: {t:.2f}zł\n"
        res += f"\nTotal: {total:.2f} zł\n"
        return res

    def get_bonus(self, bonus):
        total = 0.0
        res = ""
        for p_id in self.products:
            p = self.products[p_id]
            q = self.quantities[p_id]
            t = p.price * q
            total += t
            res += f"{p.name} - amount: {q}, price: {p.price:.2f}zł, total: {t:.2f} zł\n"
        total = total - (total * bonus/100)
        res += f"\nTotal with {bonus}% bonus: {total:.2f} zł\n"
        return res


if __name__ == "__main__":
    bread = Product('Bread', 2.70)
    ham = Product('Ham', 8.40)
    cheese = Product('Cheese', 4.40)
    chive = Product('Chive', 1.50)
    pepper = Product('Pepper', 2.35)
    cart = ShoppingCart()
    cart.add_product(bread)
    cart.add_product(bread)
    cart.add_product(bread)
    cart.add_product(pepper)
    cart.add_product(chive)
    cart.add_product(cheese)
    cart.remove_product(bread)
    cart.change_product_quantity(pepper, 2)
    print(cart.get_receipt())
    print(cart.get_bonus(50))
