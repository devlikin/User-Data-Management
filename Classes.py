class Dictionary:
    list = []

    def __init__(self):
        for x in range(100):
            self.list.append([])

    def get(self, key):
        index = key.__hash__() % 100

        bucket = self.list[index]

        for x in bucket:
            if x[0] == key:
                return x[1]

        return None

    def set(self, key, value):
        index = key.__hash__() % 100

        bucket = self.list[index]

        for x in bucket:
            if x[0] == key:
                x[1] = value
                return

        bucket.append([key, value])


dictionary = Dictionary()

dictionary.set('ala', 'bala')
print(dictionary.get('ala'))

dictionary.set(302, 'alex')
dictionary.set(18, 'silviu')
dictionary.set(2, 'raadu')
dictionary.set(118, 'ceva')

print(dictionary.list)

print(dictionary.get(302))
print(dictionary.get(18))

print(dictionary.get(2))

dictionary.set(18, 'whatever')

print(dictionary.get(18))

print(dictionary.get(2))
