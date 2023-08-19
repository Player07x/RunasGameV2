class Fore:
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    RESET = '\033[39m'


class Back:
    BLACK = '\033[40m'
    RED = '\033[41m'
    GREEN = '\033[42m'
    YELLOW = '\033[43m'
    BLUE = '\033[44m'
    MAGENTA = '\033[45m'
    CYAN = '\033[46m'
    WHITE = '\033[47m'
    RESET = '\033[49m'


class Style:
    BRIGHT = '\033[1m'
    DIM = '\033[2m'
    NORMAL = '\033[22m'
    RESET_ALL = '\033[0m'


class Line:
    """Apagar a linha anterior. Não funciona no executar do Python"""
    def __init__(self):
        self.LINE_UP = "\033[1A"
        self.LINE_CLEAR = "\x1b[2K"

    def clearLine(self):
        print(self.LINE_UP, end=self.LINE_CLEAR)

    def clearLines(self, lines: int):
        for c in range(0, lines):
            self.clearLine()
