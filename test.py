from tokenizer import Tokenizer;

code = "54.345 var  \na=5; andf=5\n\n\n\n 1 ";
tok = Tokenizer(code);

def doit(code):
    tok.next_tok();

if __name__ == '__main__':
    doit(code);
