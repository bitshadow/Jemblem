def atoh(a):
    ret = {};
    i=0;
    for i in range(len(a)):
        ret[a[i]] = True;
    return ret;

def chars(s):
    return list(s);

WHITESPACE_CHARS = atoh(chars(" \n\r\t"));

class Tokenizer:
    def __init__(self, text):
        self.rawtext = text;
        self.pos = 0;
        self.row = 0;
        self.col = 0;
        self.tokpos=0;
        self.tokrow=0;
        self.tokcol=0;

    def getchar(self):
        return self.rawtext[self.pos];

    def next(self):
        ch = self.getchar();
        self.pos += 1;
        if ch == '\n':
            self.row += 1;
            self.col = 0;
        else:
            self.col+=1;
        return ch;

    def skip_whitespace(self):
        while self.getchar() in WHITESPACE_CHARS:
            self.next();

    def start_tok(self):
        self.tokpos=self.pos;
        self.tokrow=self.row;
        self.tokcol=self.col;

    def is_digit(self, ch):
        i = ord(ch);
        if i >= 48 and i<=57:
            return True;
        return False;

    def is_in_alphabet(self, ch):
        i = ord(ch);
        return (i >= 65 and i <= 90) or (i >= 97 and i <= 122)

    def is_alphanumeric(self, ch):
        return self.is_digit(ch) or self.is_in_alphabet(ch);

    def checkdigit(self, ch):
        return self.is_alphanumeric(ch) or ch=='.'  or ch=='-';

    def read_num(self, checkdig):
        tok = ""
        while checkdig(self.getchar()):
            tok += self.next();
        return tok;

    def next_tok(self):
        self.skip_whitespace();
        self.start_tok();
        ch = self.getchar();
        if self.is_digit(ch):
           print self.read_num(self.checkdigit);

"""     j = 0;
        while j in xrange(len(self.rawtext)):
            print self.pos, self.row, self.col;
            print self.next();
            j+=1;
"""
