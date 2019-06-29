#include "shop_keeper.h"


void shop_keeper::add_item(float min, float max) {
	good item;
	item.max_price = max;
	item.min_price = min;
	inventory.push_back(item);

}

int shop_keeper::sell_to() {
	//transfer funds
	//remove item from inventory 
	//give item to customer 
	return 0;
}

int shop_keeper::buy_from() {

	return 0;
}

int shop_keeper::give_money(float amount) {

	return 0;
}

int shop_keeper::take_money(float amount) {

	return 0;
}