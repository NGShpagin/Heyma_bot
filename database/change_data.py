from collections import defaultdict
import json


class Database:
    def __init__(self):
        self.path_items = 'database/data/items.json'
        self.path_cart = 'database/data/cart.json'
        self.path_anketa = 'database/data/anketa.json'

    def add_item(self, category: str, item_id: str, name: str, status: str, count: str):
        with open(self.path_items, 'r') as file:
            items = json.load(file)
        items[category].append({"item_id": item_id, "name": name, "status": status, "count": count})
        with open(self.path_items, 'w') as file:
            json.dump(items, file, indent=4, ensure_ascii=False)

    def get_item(self, item_index, category, path):
        with open(path, 'r') as file:
            items = json.load(file)
        status = 'Ok'
        if item_index == 0:
            status = 'Left_side'
        elif item_index == len(items[0][category]) - 1:
            status = 'Right_side'
        return status, items[0][category][item_index]

    def put_in_cart(self, item_id, category, user_id):
        with open(self.path_items, 'r') as file_items:
            items = json.load(file_items)
        print(item_id)
        for item in items[0][category]:
            for value in item.values():
                if value == item_id:
                    my_item = item
                    if int(my_item["amount"]) > 0:
                        with open(self.path_cart, 'r') as file_cart:
                            cart = json.load(file_cart)
                        print(user_id)
                        if len(cart) > 0:
                            if str(user_id) in cart[0]:
                                cart[0][str(user_id)].append(my_item)
                            else:
                                cart[0][user_id] = [my_item]
                        else:
                            cart.append({user_id: [my_item]})
                        with open(self.path_cart, 'w') as file_cart:
                            json.dump(cart, file_cart, indent=4, ensure_ascii=False)
                        return 'Позиция добавлена'
                    else:
                        return 'Нет в наличии'

    def search_items_by_name(self, name):
        with open(self.path_items, 'r') as file_items:
            items = json.load(file_items)
        for value in items[0].values():
            for item in value:
                if item['name'] == name:
                    result = item
                    return result
                else:
                    return 0

    def get_my_cart(self, user_id):
        with open(self.path_cart, 'r') as file_cart:
            my_cart = json.load(file_cart)
        if str(user_id) in my_cart[0]:
            return my_cart[0][str(user_id)]
        else:
            return False

    def remove_pos(self, user_id, item_id):
        with open(self.path_cart, 'r') as file_cart:
            my_cart = json.load(file_cart)
        for i in my_cart[0][str(user_id)]:
            print(item_id)
            for v in i.values():
                if v == item_id:
                    my_cart[0][str(user_id)].remove(i)
                    print(v)
        with open(self.path_cart, 'w') as file_cart:
            json.dump(my_cart, file_cart, indent=4, ensure_ascii=False)

    def save_anketa(self, user_id, data):
        with open(self.path_anketa, 'r') as file_1:
            anketas = json.load(file_1)
        my_anketa = {user_id: [dict((number, item) for number, item in enumerate(data, start=1))]}
        anketas.append(my_anketa)
        with open(self.path_anketa, 'w') as file_2:
            json.dump(anketas, file_2, indent=2, ensure_ascii=False)

