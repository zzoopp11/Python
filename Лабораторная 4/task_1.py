import json


FILENAME = "input.json"


def task() -> float:

    with open(FILENAME, 'r') as f:
        data = json.load(f)

    list_of_products = [x["score"] * x["weight"] for x in data]
    sum_of_products = sum(list_of_products)

    return round(sum_of_products, 3)


if __name__ == '__main__':
    print(task())
