from address import Address
from mailing import Mailing

# Создаем адрес отправителя
from_address = Address(
    "123456",
    "Москва",
    "Тверская улица",
    "15",
    "78"
)

# Создаем адрес получателя
to_address = Address(
    "654321",
    "Санкт-Петербург",
    "Невский проспект",
    "25",
    "42"
)

# Создаем экземпляр класса Mailing
mailing = Mailing(
    to_address=to_address,
    from_address=from_address,
    cost=350.50,
    track="TRK123456789"
)

# Распечатываем информацию об отправлении
print(f"Отправление {mailing.track} из {mailing.from_address.index}, "
      f"{mailing.from_address.city}, {mailing.from_address.street}, "
      f"{mailing.from_address.house} - {mailing.from_address.apartment} в "
      f"{mailing.to_address.index}, {mailing.to_address.city}, "
      f"{mailing.to_address.street}, {mailing.to_address.house} - "
      f"{mailing.to_address.apartment}. Стоимость {mailing.cost} рублей.")