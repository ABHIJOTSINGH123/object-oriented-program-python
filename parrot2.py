class parrot:
    def __init__(self, name, age, ):
        self.name = name
        self.age = age
    def sing(self,song):
        return"{}sings{}".format(self.name,song)
    def dance(self):
        return "{}is dancing".format(self.name)
blu=parrot("Blu",10)
print(blu.sing("'happy"))

print(blu.dance())
   