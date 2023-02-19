import arithmetic_int, arithmetic_string

class Arithmetic:
    def __init__(self, a_type):
        self.methods = {}
        if a_type not in ['INT','STRING']:
            raise ValueError('Invalid arithmetic type)')
        if a_type == 'INT':
            arithmetic_int.ArithmeticInt(register=self._register)
        if a_type == 'STRING':
            arithmetic_string.ArithmeticString(register=self._register)
        for k,v in self.methods.items():
            setattr(self, k, v)

    def _register (self, _name, _method):
        self.methods[_name] = _method


def main():

    a_i = Arithmetic('INT')
    a_s = Arithmetic('STRING')
    for a in (a_i, a_s):
        res = a.add(3,40)
        print(res, f"type: {type(res)}")
        res = a.mul(7, 3)
        print(res, f"type: {type(res)}")

if __name__ == '__main__':
    main()