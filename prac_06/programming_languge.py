class ProgrammingLanguage:
    def __init__(self, name="", typing="", reflection="", year="",):
        self.typing = typing.title()
        self.name = name.title()
        self.reflection = reflection
        self.year = year

    def __str__(self):
        return f"{self.name}, {self.typing} Typing, Reflection={self.reflection}, {self.year}"

    def is_dynamic(self):
        if self.typing == "Dynamic":
            return True
        if self.typing == "Static":
            return False


