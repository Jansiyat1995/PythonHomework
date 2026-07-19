from smartphone import Smartphone

catalog = [
         Smartphone("iPhone", "16", "+79994445566"),
         Smartphone("Samsung", "S25", "+79991112233"),
         Smartphone("Xiaomi", "15", "+79511472563"),
         Smartphone("Lenovo", "305", "+79511475743"),
         Smartphone("Poco", "promax", "+79884572563")
         ]

for smartphone in catalog:

    print(smartphone.brand, smartphone.model, smartphone.number)
