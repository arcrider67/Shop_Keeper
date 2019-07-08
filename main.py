from market import person
from market import make_deal
import random
import copy

def main():
    keeper_list = []
    for i in range(0,1):
        keeper = person("seller", 500, 1000, 25, 100)
        keeper_list.append(keeper)

    cus_list = []
    for i in range(0,1):
        customer = person("buyer",500, 200, 0, 75)
        cus_list.append(customer)


    print(keeper.offer)
    print(customer.offer)


    print("starting test")
    #simulates 100 days of buying and selling
    for day in range(0,100):

        customer, index = choose_person(cus_list)

        current_price = keeper.offer
        deal_made = make_deal(keeper, customer)

        print(str(keeper.offer) + ":" +str(customer.offer) + " - "+str(deal_made))

        keeper.adjust_price(deal_made)
        update_per(cus_list, index, deal_made)
def calc_day(keeper_list, cus_list):
    keeper_list_loc = copy.deepcopy(keeper_list)
    cus_list_loc = copy.deepcopy(cus_list)
    
    for keeper in keeper_list_loc:
        customer = choose_person(cus_list_loc)


def update_per(per_list, index, sale_made):
    for i, item in enumerate(per_list):
        if index == i:
            item.adjust_price(sale_made)
        else:
            item.adjust_price(False)



def choose_person(per_list):
    max = len(per_list)
    index = random.randint(0,max-1)
    return(per_list[index], index)


main()