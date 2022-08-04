#multiple inheritance
class parent1:
    def assign_string_one(self,str1):
        self.str1=str1

    def show_string_one(self):
        return self.str1


class Parent2:
    def assign_string_two(self,str2):
        self.str2=str2

    def show_string_two(self):
        return self.str2

class Child(parent1,Parent2):
    def assign_string_three(self,str3):
        self.str3=str3

    def show_string_three(self):
        return self.str3

my_child=Child()
my_child.assign_string_one("I am string of parent 1 class")
my_child.show_string_one()

my_child.assign_string_two("I am string of parent 2 class")
my_child.show_string_two()

my_child.assign_string_three("I am string of child class")
my_child.show_string_three()