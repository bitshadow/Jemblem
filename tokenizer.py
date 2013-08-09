import re;

def atoh(a):
    ret = {};
    i=0;
    for i in range(len(a)):
        ret[a[i]] = True;
    return ret;

def chars(s):
    return list(s);

WHITESPACE_CHARS = atoh(chars(" \n\r\t"));
RE_HEX_NUMBER = re.compile(r'^0[xX][0-9a-fA-F]+$');
RE_OCT_NUMBER = re.compile(r'^0[0-7]+$');
RE_DEC_NUMBER = re.compile(r'[-+]?\d*\.\d+|[-+]?\d+$');

class Tokenizer:
    def __init__(self, text):
        self._rawtext = text;
        self._pos = 0;
        self._row = 0;
        self._col = 0;
        self._tokpos=0;
        self._tokrow=0;
        self._tokcol=0;

    def getchar(self):
        return self._rawtext[self._pos];

    def next(self):
        ch = self.getchar();
        self._pos += 1;
        if ch == '\n':
            self._row += 1;
            self._col = 0;
        else:
            self._col+=1;
        return ch;

    def skip_whitespace(self):
        while self.getchar() in WHITESPACE_CHARS:
            self.next();

    def start_tok(self):
        self._tokpos=self._pos;
        self._tokrow=self._row;
        self._tokcol=self._col;

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

    def parse_js_number(self,num):
        hexa = re.search(RE_HEX_NUMBER,num);
        octa = re.search(RE_OCT_NUMBER,num);
        deci = re.search(RE_DEC_NUMBER,num);

        if hexa:
            return int(hexa.group(0)[2:], 16);
        elif octa:
            return int(octa.group(0)[1:], 8);
        elif deci:
            return int(deci.group(0));

    def read_num(self, func):
        tok = "";
        ch = self.getchar()
        while ch and func(ch):
            tok += self.next();
            ch = self.getchar();
        valid = self.parse_js_number(tok);
        if valid == None:
            print "syntex error"
        else:
            return valid;

    def read_escape_char():
        ch = self.next();
        d = {
            "n":"\n",
            "r":"\r",
            "t":"\t",
            "b":"\b",
            "v":"\v",
            "f":"\f",
            "0":"\0"
            #TODO \x and \u
        }
        if ch in d:
            return d[ch];
        return ch;

    def read_string(self):
        quote = self.next(); tok = "";
        while True:
            ch = self.next();
            if ch == "\\":
                ch = self.read_escape_char();
            elif ch == quote:
                break;
            tok += ch;
        return tok;

    def next_tok(self):
        self.skip_whitespace();
        self.start_tok();
        ch = self.getchar();
        if self.is_digit(ch):
           func = self.checkdigit;
           return self.read_num(func);
        if ch == '"' or ch == "'":
           print self.read_string();

        return self._pos;

"""     j = 0;
        while j in xrange(len(self.rawtext)):
            print self.pos, self.row, self.col;
            print self.next();
            j+=1;
"""
