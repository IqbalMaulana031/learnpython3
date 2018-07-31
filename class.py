AlreadyExistError = Exception("Already exists")


class DB:
    """DB store list of objects"""

    def __init__(self):
        self.storage = []
        self._name = "db_storage"
        self.__password = "secretpassword"
        self.___triple = 3

    def save(self, obj):
        if obj not in self.storage:
            self.storage.append(obj)
        else:
            raise AlreadyExistError

    def __repr__(self):
        return "DB(with {} objects)".format(len(self.storage))

    def __str__(self):
        return self.__repr__()

    def find(self, filter_func):
        return filter(filter_func, self.storage)


def create_filter(query):
    def wrapper(item):
        return query in item.name

    return wrapper


class Contact:
    """Contact class define person contact"""

    db = DB()

    @classmethod
    def find(cls, query):
        return list(cls.db.find(create_filter(query)))

    def __init__(self, name: str, phone_number: str = "+62"):
        self.name = name
        self.phone_number = phone_number

    def save(self):
        self.db.save(self)

    def __str__(self):
        return "<{} {}>".format(self.name, self.phone_number)

    def __repr__(self):
        return "Contact({} {})".format(self.name, self.phone_number)


budi = Contact("budi")
budi.save()
try:
    budi.save()
except Exception as e:
    print(e)

yoga = Contact("yoga")
yoga.save()

andi = Contact("andi")
andi.save()

print(Contact.find("a"))
