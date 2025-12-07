memory = 1.44   # Мб
pages = 100
lines = 50
symbols = 25
weight = 4      # б

volume = pages * lines * symbols * weight
books = int(memory * 1024 ** 2 / volume)
print("Количество книг, помещающихся на дискету:", books)
