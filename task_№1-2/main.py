import pprint
cook_book = {}
with open('list_of_dishes.txt', encoding='utf-8') as f:
    last_key = ''
    for line in f:
        line = line.strip()
        if line.isdigit():
            continue
        elif line and '|' not in line:
            cook_book[line] = []
            last_key = line
        elif line and '|' in line:
            name, qt, msure = line.split(" | ")
            cook_book.get(last_key).append(dict(ingredient_name=name, quantity=int(qt), measure=msure))

    pprint.pprint(cook_book)
print()


def get_shop_list_by_dishes(dishes, person_count):
    quantity_ingredients = {}
    for dish in dishes:
        for ingredient in cook_book[dish]:
            dish_cook = ingredient['ingredient_name']
            quantity = int(ingredient['quantity']) * person_count
            measure = ingredient['measure']
            if dish_cook not in quantity_ingredients:
                quantity_ingredients[dish_cook] = {
                    "quantity": quantity,
                    "measure": measure
                }
            else:
                quantity_ingredients[dish_cook]['quantity'] += quantity
    return pprint.pprint(quantity_ingredients)


print(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))
