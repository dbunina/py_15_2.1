

def load_cookbook():
    cook_book = dict()
    with open('order.txt', encoding='cp1251') as f:
        for raw_line in f:
            title = raw_line.strip().lower()
            next(f)  # skip quantity
            ingredient_line = f.readline()

            while ingredient_line.strip():
                ingredient_record = create_ingredient_record(ingredient_line)
                add_record_to_cookbook(cook_book, title, ingredient_record)

                ingredient_line = f.readline()
    return cook_book


def create_ingredient_record(ingredient_line):
    record = dict()
    items = list(map(str.strip, ingredient_line.split('|')))
    record['ingredient_name'] = items[0]
    record['quantity'] = int(items[1])
    record['measure'] = items[2]
    return record


def add_record_to_cookbook(cook_book, title, ingredient_record):
    if title in cook_book:
        cook_book[title].append(ingredient_record)
    else:
        cook_book[title] = [ingredient_record]


def get_shop_list_by_dishes(cook_book, dishes, person_count):
    shop_list = {}
    for dish in dishes:
        for ingredient in cook_book[dish]:
            new_shop_list_item = dict(ingredient)
            new_shop_list_item['quantity'] *= person_count
            if new_shop_list_item['ingredient_name'] not in shop_list:
                shop_list[new_shop_list_item['ingredient_name']] = new_shop_list_item
            else:
                shop_list[new_shop_list_item['ingredient_name']]['quantity'] += \
                    new_shop_list_item['quantity']
    return shop_list


def print_shop_list(shop_list):
    for shop_list_item in shop_list.values():
        print('{} {} {}'.format(
            shop_list_item['ingredient_name'], shop_list_item['quantity'], shop_list_item['measure'])
        )


def create_shop_list():
    person_count = int(input('Введите количество человек: '))
    dishes = input('Введите блюда в расчете на одного человека (через запятую): ') \
        .lower().split(', ')
    cook_book = load_cookbook()
    shop_list = get_shop_list_by_dishes(cook_book, dishes, person_count)
    print_shop_list(shop_list)

create_shop_list()
