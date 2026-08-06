class Nigiri:
    category = "にぎり"
    top = "ねた"
    base = "しゃり"

    def show_attributes(self):
        print("top: {}, base: {}, category: {}".format(self.top, self. base, self.category))

class katsuo(Nigiri):
    top = "かつお"
    topping = "生姜とねぎ"
    price = 100

    def show_attributes(self):
        super().show_attributes()
        print("price: {}円".format(self.price))
        print("topping: {}".format(self.topping))
k1 = katsuo()
k1.show_attributes()
