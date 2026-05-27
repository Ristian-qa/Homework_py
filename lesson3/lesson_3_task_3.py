from address import Address
from mailing import Mailing

from_address = Address("101000", "Москва", "Тверская", "15", "42")
to_address = Address("394000", "Воронеж", "Ленинский проспект", "7", "123")

mailing = Mailing(to_address, from_address, 250.75, "RX123456789RU")

print(
    f"Отправление {mailing.track} из {mailing.from_address.index}, "
    f"{mailing.from_address.city}, {mailing.from_address.street}, "
    f"{mailing.from_address.home} - {mailing.from_address.number} "
    f"в {mailing.to_address.index}, {mailing.to_address.city}, "
    f"{mailing.to_address.street}, {mailing.to_address.home} "
    f"-{mailing.to_address.number}. Стоимость {mailing.cost} рублей.")
