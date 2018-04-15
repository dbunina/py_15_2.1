# Поскольку количество человек уже указано в исходных данных, код немного переделан
#

cook_book = dict()
order_list = dict()

def read_order_list():
    with open('order.txt') as f:
        for raw_line in f:
            title = raw_line.strip()
            quantity = f.readline().strip()
            order_list[title] = int(quantity)

            ingredient_line = f.readline()

            while ingredient_line.strip() != '':
                record = dict()
                items = list(map(str.strip, ingredient_line.split('|')))
                record['ingredient_name'] = items[0]
                record['quantity'] = int(items[1])
                record['measure'] = items[2]

                if title in cook_book:
                    cook_book[title].append(record)
                else:
                    cook_book[title] = [record]

                ingredient_line = f.readline()

def get_shop_list_by_dishes():
    shop_list = {}
    for dish in order_list.keys():
        for ingridient in cook_book[dish]:
            new_shop_list_item = dict(ingridient)
            new_shop_list_item['quantity'] *= order_list[dish]
            if new_shop_list_item['ingredient_name'] not in shop_list:
                shop_list[new_shop_list_item['ingredient_name']] = new_shop_list_item
            else:
                shop_list[new_shop_list_item['ingredient_name']]['quantity'] += \
                    new_shop_list_item['quantity']
    return shop_list

def print_shop_list(shop_list):
    for shop_list_item in shop_list.values():
        print('{} {} {}'.format(shop_list_item['ingredient_name'], shop_list_item['quantity'],
                            shop_list_item['measure']))

def create_shop_list():
    read_order_list()
    shop_list = get_shop_list_by_dishes()
    print_shop_list(shop_list)

create_shop_list()
