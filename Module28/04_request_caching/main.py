class LRUCache:
    def __init__(self, capacity: int) -> None:
        self.capacity = capacity
        self.cache_dict = {}

    @property
    def cache(self) -> None:
        return next(iter(self.cache_dict))  # возвращаем самый старый элемент

    @cache.setter
    def cache(self, new_elem: str) -> None:
        if len(self.cache_dict) >= self.capacity:
            self.cache_dict.pop(self.cache)  # удаляем самый старый элемент
        self.cache_dict[new_elem[0]] = new_elem[1]  # добавляем новый элемент

    def print_cache(self) -> None:
        print("LRU Cache:")
        for key, value in self.cache_dict.items():
            print(f"{key} : {value}")

    def get(self, key: str) -> str:
        val = self.cache_dict.pop(key) # обновляем порядок использования элемента
        self.cache_dict[key] = val  # обновляем порядок использования элемента
        return self.cache_dict.get(key)

# Создаем экземпляр класса LRU Cache с capacity = 3
cache = LRUCache(3)

# Добавляем элементы в кэш
cache.cache = ("key1", "value1")
cache.cache = ("key2", "value2")
cache.cache = ("key3", "value3")

# # Выводим текущий кэш
cache.print_cache()  # key1 : value1, key2 : value2, key3 : value3

# Получаем значение по ключу
print(cache.get("key2"))  # value2
# print(cache.get()) # value2

# Добавляем новый элемент, превышающий лимит capacity
cache.cache = ("key4", "value4")

# Выводим обновленный кэш
cache.print_cache()  # key2 : value2, key3 : value3, key4 : value4