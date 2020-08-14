class Employee:
    level = 5
    __interests = ''

    def __init__(self, name, email):
        self.name = name
        self.email = email

    def get_name(self):
        return self.name

    def get_email(self):
        return self.email

    def set_level(self, level=5):
        self.level = level

    def get_level(self):
        return self.level

    def set_interests(self, interests):
        self.__interests = interests

    def get_interests(self):
        return self.__interests


james = Employee('James', 'james@example.com')

james.set_interests('Computer Science')
print(james.get_interests())
