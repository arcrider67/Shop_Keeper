#pragma once

#include <string>
#include <vector>
using std::string;

class shop_keeper
{
	float bank;
	std::vector<good> inventory;


public:
	int sell_to();
	int buy_from();
	int give_money(float amount);
	int take_money(float amount);
	void add_item(float min, float max);


};


struct good
{
	string name = "item";
	float min_price;
	float current;
	float max_price;
};