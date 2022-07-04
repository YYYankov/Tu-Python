import json


class GSM:
    def __init__(self, quantity, price, y_dev, brand, model):
        self.quantity = quantity
        self.price = price
        self.y_dev = y_dev
        self.brand = brand
        self.model = model


def sort_gsm(gsm_li):
    return sorted(gsm_li, key=lambda gsm: gsm.quantity)


def to_json(gsm_li):
    for gsm in gsm_li:
        if gsm.brand == "Samsung":
            json_file = "brand_S.json"
            with open(json_file, 'a') as file:
                json_data = json.dumps(
                    {"quantity": gsm.quantity, "price": gsm.price, "year": gsm.y_dev, "brand": gsm.brand,
                     "model": gsm.model})
                file.write(json_data)
        if gsm.brand == "Apple":
            json_file = "brand_A.json"
            with open( json_file, 'a') as file:
                json_data = json.dumps(
                    {"quantity": gsm.quantity, "price": gsm.price, "year": gsm.y_dev, "brand": gsm.brand,
                     "model": gsm.model})
                file.write(json_data)


my_gsms = [GSM(12, 500, 2018, "Samsung", "1"), GSM(18, 600, 2019, "Apple", "1"), GSM(4, 689, 2020, "Samsung", "2")]
to_json(sort_gsm(my_gsms))