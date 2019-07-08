from market import person
from market import make_deal

def main():
    
    keeper = person("seller", 500, 1000, 25, 100)
    customer = person("buyer",500, 200, 0, 75)
    print(keeper.offer)
    print(customer.offer)

    for day in range(0,100):
        current_price = keeper.offer
        deal_made = make_deal(keeper, customer)
 
        print(str(keeper.offer) + ":" +str(customer.offer) + " - "+str(deal_made))

        keeper.adjust_price(deal_made)
        customer.adjust_price(deal_made)




main()