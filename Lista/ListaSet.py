conjunto = set()
print(type(conjunto))

lista = ["Andre", "David", "Cebolinha", "Andre"]
print(lista)

conjunto2 = set(lista)
print(conjunto2)

conjunto3 = {"Cebolinha", "Magali", "Monica", "Cascao", "Cebolinha"}
print(conjunto3)

conjunto3.add("Franjinha")
print(conjunto3)

conjunto1 = {"Mega Drive", "Super Nintendo", "Playstation"}
conjunto2 = {"Playstation", "Nintendo 64", "Sega Saturn", "Dreamcast"}

print(f"O primeiro set contem {conjunto1}")
print(f"O segundo set contem {conjunto2}")

conjunto1.difference_update(conjunto2)
print(f"O primeiro contem {conjunto1}")

# Usar o Discart ao inves de Remove

