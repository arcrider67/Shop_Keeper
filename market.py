


class person:
    bank = 0
    income = 0
    offer = 0
    max = 0 
    min = 0 #minimum price to accept 
    per_type = "seller"

    def __init__(self,per_type, bank_in, max, min, price):
        self.bank = bank_in
        self.max = max
        self.min = min
        self.per_type = per_type

        if min == 0:
            #if min = 0 then person is a customer for this good
            self.offer = price*.8
        else:
            self.offer = price*1.8

    def money_trans(self, reciever, amount):
        self.bank = self.bank - amount
        reciever.bank += amount

    def adjust_price(self, sale_made):
        if self.per_type == "seller":
            if sale_made:
                self.offer = self.offer + 5
            else:
                self.offer = self.offer - 5
        else:
            if not sale_made:
                self.offer = self.offer + 5

        

def make_deal(keeper, customer):

    if abs(keeper.offer - customer.offer) <= 1.5:
        customer.offer = (keeper.offer + customer.offer)/2
        keeper.offer = customer.offer
        return(1)
    elif keeper.offer < customer.offer:
        customer.offer = keeper.offer
        return(1)
    else:
        return(0)