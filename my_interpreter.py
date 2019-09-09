class Interpreter:
    def __init__(self, text: str):
        self.pos = 0
        self.text = text

    def parseNumber(self):
        number_text = ''
        while self.pos < len(self.text) and self.text[self.pos].isdigit():
            number_text += self.text[self.pos]
            self.pos += 1
        return int(number_text)

    def parseOp(self):
        if self.pos >= len(self.text):
            return None
        if self.text[self.pos] in ('+', '-'):
            self.pos += 1
            return self.text[self.pos - 1]
        raise Exception('wrong operation')

    def expr(self):
        result = self.parseNumber()
        while True:
            op = self.parseOp()
            if op is None:
                break
            term = self.parseNumber()
            if op == '+':
                result += term
            else:
                result -= term
        return result


def main():
    while True:
        try:
            text = input('calc>')
        except EOFError:
            break
        if not text:
            continue
        interpreter = Interpreter(text)
        result = interpreter.expr()
        print(result)


if __name__ == '__main__':
    main()
