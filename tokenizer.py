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
        print self.getchar()
        if self.getchar() in WHITESPACE_CHARS:
            print self.getchar()
            self.pos+=1;

    def next_tok(self):
        #self.skip_whitespace();
        j = 0;
        while j in xrange(len(self.rawtext)):
            print self.pos, self.row, self.col;
            print self.next();
            j+=1;

