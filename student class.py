class student:
    grade=10
    name="Karanveer singh cheema"
    def introduction(self):
        print("i am student")
    def details(self):
        print(f"my name is {self.name} and i am in grade {self.grade}")
ob=student()

ob.introduction()

ob.details()