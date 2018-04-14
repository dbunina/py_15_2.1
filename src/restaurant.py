# cook_book = {
#   'яичница': [
#     {'ingridient_name': 'яйца', 'quantity': 2, 'measure': 'шт.'},
#     {'ingridient_name': 'помидоры', 'quantity': 100, 'measure': 'гр.'}
#     ],
#   'стейк': [
#     {'ingridient_name': 'говядина', 'quantity': 300, 'measure': 'гр.'},
#     {'ingridient_name': 'специи', 'quantity': 5, 'measure': 'гр.'},
#     {'ingridient_name': 'масло', 'quantity': 10, 'measure': 'мл.'}
#     ],
#   'салат': [
#     {'ingridient_name': 'помидоры', 'quantity': 100, 'measure': 'гр.'},
#     {'ingridient_name': 'огурцы', 'quantity': 100, 'measure': 'гр.'},
#     {'ingridient_name': 'масло', 'quantity': 100, 'measure': 'мл.'},
#     {'ingridient_name': 'лук', 'quantity': 1, 'measure': 'шт.'}
#     ]
#   }
#
# order_list = {
#     'яичница': 3,
#     'стейк': 4,
#     'салат': 5
# }

cook_book = dict()
order_list = dict()

def read_order_list():
    with open('order.txt') as f:
        for raw_line in f:
            print('Title:', raw_line.strip())
            print('Quantity:', f.readline().strip())
            ingredient_line = f.readline().strip()
            while ingredient_line != '':
                print('Ingredient:',ingredient_line)
                ingredient_line = f.readline().strip()
            print('End\n')

def get_shop_list_by_dishes():
  shop_list = {}
  for dish in order_list.keys():
    for ingridient in cook_book[dish]:
      new_shop_list_item = dict(ingridient)

      new_shop_list_item['quantity'] *= order_list[dish]
      if new_shop_list_item['ingridient_name'] not in shop_list:
        shop_list[new_shop_list_item['ingridient_name']] = new_shop_list_item
      else:
        shop_list[new_shop_list_item['ingridient_name']]['quantity'] += \
            new_shop_list_item['quantity']
  return shop_list

def print_shop_list(shop_list):
  for shop_list_item in shop_list.values():
    print('{} {} {}'.format(shop_list_item['ingridient_name'], shop_list_item['quantity'],
                            shop_list_item['measure']))

def create_shop_list():
  read_order_list()
  shop_list = get_shop_list_by_dishes()
  print_shop_list(shop_list)

create_shop_list()
