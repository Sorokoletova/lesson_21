from classes import Store, Shop, Request

if __name__ == '__main__':
    my_store = Store()
    my_shop = Shop()
    my_store.add('медведь', 10)
    my_store.add('слон', 25)
    my_store.add('тигр', 10)
    my_store.add('лев', 10)
    my_store.add('лягушка', 25)
    my_store.add('собака', 20)

    my_shop.add('медведь', 1)
    my_shop.add('слон', 1)
    my_shop.add('лев', 3)

    print(f"Товары на складе:\n {my_store.get_items()}")
    print(f"Товары в магазине:\n {my_shop.get_items()}")

    user_answer = input(
        "Введите текст в формате:<действие> <количество> <наименование товара> из <место откуда> в <место куда>, "
        "Например Доставить 3 медведь из склад в магазин\n")

    data = Request(user_answer)
    result_request = my_store.remove(data.product, data.amount)
    if result_request:
        print("Нужное количество есть на складе")
        print(f"Курьер забрал {data.amount} {data.product} со склад")
        print(f"Курьер везет {data.amount} {data.product} в магазин")
        result = my_shop.add(data.product, data.amount)

        if not result:
            my_store.add(data.product, data.amount)
        else:
            print(f"Курьер доставил {data.amount} {data.product} в магазин")
    items_store = my_store.get_items()
    items_shop = my_shop.get_items()
    print("Товары на складе:")
    for k, v in items_store.items():
        print(k, v)
    print("Товары в магазине:")
    for k, v in items_shop.items():
        print(k, v)
