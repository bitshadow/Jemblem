from tokenizer import Tokenizer;

code = " 1000 int a; not true'hell world!' 03432:w a .345 var  \na=5; andf=5\n\n\n\n 1 ";
tok = Tokenizer(code);

def doit(code):
    print tok.next_tok();
    print tok.next_tok();
    print tok.next_tok();
    print tok.next_tok();

if __name__ == '__main__':
    doit(code);
