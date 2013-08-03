from tokenizer import Tokenizer;

code = "var \na;";
tok = Tokenizer(code);

def doit(code):
    tok.next_tok();

if __name__ == '__main__':
    doit(code);
