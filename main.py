import datetime

class OnlineSalesRegisterCollector:

    def __init__(self):
        self.__name_items = []      # список с перечнем товаров в чеке
        self.__number_items = 0     # переменная с количеством товаров в чеке
        # словарь, где перечислены товары магазина и их стоимость;
        self.__item_price = {'чипсы': 50, 'кола': 100, 'печенье': 45, 'молоко': 55, 'кефир': 70} 
        # словарь, где записана налоговая ставка на товары. Она составляет 10% или 20% от стоимости.
        self.__tax_rate = {'чипсы': 20, 'кола': 20, 'печенье': 20, 'молоко': 10, 'кефир': 10}

    # допиши код здесь
    @property
    def name_items(self):
        return self.__name_items

    @property
    def number_items(self):
        return self.__number_items

    def add_item_to_cheque(self, name):
        len_name = len(name)
        if len_name == 0 or len_name > 40:
            raise ValueError('Нельзя добавить товар, если в его названии нет символов или их больше 40')

        if name not in self.__item_price:
            raise NameError('Позиция отсутствует в товарном справочнике')

        self.__name_items.append(name)
        self.__number_items += 1

    def delete_item_from_check(self, name):
        if name not in self.__name_items:
            raise NameError('Позиция отсутствует в чеке')
        self.__name_items.remove(name)
        self.__number_items -= 1

    def check_amount(self):
        total = []
        for item in self.__name_items:
            total.append(self.__item_price.get(item))
        amount = sum(total)
        if self.__number_items > 10:
            amount *= 0.9
        return amount

    def twenty_percent_tax_calculation(self):
        twenty_percent_tax = []
        for item in self.__name_items:
            if self.__tax_rate.get(item) == 20:
                twenty_percent_tax.append(item)
        total = []
        for item in twenty_percent_tax:
            total.append(self.__item_price.get(item))
        tax = sum(total) * 0.2
        if self.__number_items > 10:
            tax *= 0.9
        return tax

    def ten_percent_tax_calculation(self):
        ten_percent_tax = []
        for item in self.__name_items:
            if self.__tax_rate.get(item) == 20:
                ten_percent_tax.append(item)
        total = []
        for item in ten_percent_tax:
            total.append(self.__item_price.get(item))
        tax = sum(total) * 0.1
        if self.__number_items > 10:
            tax *= 0.9
        return tax

    def total_tax(self):
        return self.twenty_percent_tax_calculation() + self.ten_percent_tax_calculation()

    @staticmethod
    def get_telephone_number(telephone_number):
        if type(telephone_number) == int:
            if telephone_number // 10_000_000_000 != 0:
                raise ValueError('Необходимо ввести 10 цифр после "+7"')
            return f'+7{telephone_number}'
        elif type(telephone_number) == str:
            try:
                number_int = int(telephone_number)
            except ValueError:
                raise ValueError('Необходимо ввести цифры')
            if len(telephone_number) > 10:
                raise ValueError('Необходимо ввести 10 цифр после "+7"')
            return '+7' + telephone_number
                
        raise ValueError('Необходимо ввести цифры')

 