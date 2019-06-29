#include <iostream>
#include "shop_keeper.h"
using namespace std;


int main() {
	cout << "hello welcome to my shop" << endl;
	//for a set of days
	//perform transactions
		
	shop_keeper keeper;
	keeper.add_item(2, 5);

	shop_keeper customer;
	customer.add_item(0, 3);

	return 0;
}

