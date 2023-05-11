class MyDict(dict):

    def get(self,key):
        val = super().get(key)
        if val is None:
            return 0
        else:
            return val
d = {'a':4,'b':5}

dict_1 = MyDict(d)
print(dict_1.get('c'))
