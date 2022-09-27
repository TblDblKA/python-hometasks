import json
from keyword import iskeyword


class Parser:
    def __init__(self, mapping):
        self._mapping = mapping
        for key, value in mapping.items():
            if not isinstance(value, dict):
                if isinstance(key, str) and iskeyword(key):
                    key = key + '_'
                if key == 'price':
                    key = '_' + key
                setattr(self, key, value)
            else:
                setattr(self, key, Parser(value))

    def __repr__(self):
        return json.dumps(self._mapping, indent=4, ensure_ascii=False)


class ColorizeMixin:
    def __repr__(self):
        print(f"\033[1;{self.repr_color_code};40m")


class Advert(ColorizeMixin, Parser):
    repr_color_code = 31

    def __init__(self, mapping):
        self._price = None
        if 'title' not in mapping.keys():
            raise Exception('There is no field named "title"')
        super().__init__(mapping)

    @property
    def price(self):
        if self._price is None:
            return 0
        elif self._price < 0:
            raise Exception(ValueError, 'must be >= 0')
        else:
            return self._price

    @price.setter
    def price(self, value):
        self._price = value

    @price.deleter
    def price(self):
        del self._price

    def __repr__(self):
        super(Advert, self).__repr__()
        return f'{self.title} | {self.price} ₽'


if __name__ == '__main__':
    lesson_str = """{
        "title": "Вельш-корги",
        "class": "dogs",
        "price": 1000,
        "location": {
            "address": "город Москва, Лесная, 7",
            "metro_stations": ["Белорусская", "Тверская"],
            "p": {
                "a": "b",
                "class": "a"
            }
        }
    }"""
    lesson = json.loads(lesson_str)
    lesson_ad = Advert(lesson)
    print(lesson_ad.price)
