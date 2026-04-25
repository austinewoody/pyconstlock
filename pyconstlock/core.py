class Const:
    def __setattr__(self, name, value):
        if name in self.__dict__:
            raise TypeError(f"Cannot reassign constant '{name}'")

        if not name.isupper():
            raise ValueError("Constant names must be uppercase")

        self.__dict__[name] = value

    def __delattr__(self, name):
        raise TypeError(f"Cannot delete constant '{name}'")

    def __repr__(self):
        return f"<Const {self.__dict__}>"