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
RE_HEX_NUMBER = re.compile(r'^0[xX][0-9a-fA-F]+');
RE_OCT_NUMBER = re.compile(r'^0[0-7]+');
#RE_DEC_NUMBER = re.compile(r'^\d*\.?\d*(?:e-?\d*(?:\d\.?|\.?\d)\d*)?$');
RE_DEC_NUMBER = re.compile('[-+]?\d*\.\d+|[-+]?\d+');

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
        hexa = re.match(RE_HEX_NUMBER,num);
        octa = re.match(RE_OCT_NUMBER,num);
        deci = re.match(RE_DEC_NUMBER,num);

        if hexa:
            return int(hexa.group(0)[2:], 16);
        elif octa:
            return int(octa.group(0)[1:], 8);
        elif deci:
            return float(deci.group(0));

    def read_num(self, f):
        tok = "";
        ch = self.getchar()
        while ch and f(ch):
            tok += self.next();
            ch = self.getchar();
        valid = self.parse_js_number(tok);
        if valid != valid:
            print "syntex error"
        else:
            return valid;

    def next_tok(self):
        self.skip_whitespace();
        self.start_tok();
        ch = self.getchar();
        if self.is_digit(ch):
           f = self.checkdigit;
           return self.read_num(f);
        return self._pos;

"""     j = 0;
        while j in xrange(len(self.rawtext)):
            print self.pos, self.row, self.col;
            print self.next();
            j+=1;
"""
