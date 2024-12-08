import colorama

print("Атрибуты и методы модуля colorama:")
print(colorama.dir(colorama))
#ключевая информация
print("\nИнформация о классе Fore:")
print(colorama.dir(Fore))
print("\nИнформация о классе Back:")
print(colorama.dir(Back))
print("\nИнформация о классе Style:")
print(colorama.dir(Style))
# Документация модуля
print("\nДокументация модуля colorama:")
help(colorama)
