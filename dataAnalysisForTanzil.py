from nltk.tokenize import RegexpTokenizer

def merge_into_words(text):
    text = text.replace("\n","")
    t = text.split(" ")
    # print(t)
    # print(t[len(t)-1])
    words =[]
    i = 0
    while i<len(t):
        if i+1 < len(t) and t[i+1] == '্':
            if i+2 < len(t):
                if i+3 < len(t) and t[i+3] == '্':
                    if i+4 < len(t):
                        if i+5 < len(t) and t[i+5] == '্':
                            if i+6 < len(t):
                                wrrr= t[i]+t[i+1]+t[i+2]+t[i+3]+t[i+4]+t[i+5]+t[i+6]
                                words.append(wrrr)
                                i+=6
                            else:
                                i+=1
                        else:
                            wrr = t[i]+t[i+1]+t[i+2]+t[i+3]+t[i+4]
                            # print(wrr)
                            words.append(wrr)
                            i+=4
                    else:
                        i+=1
                else:
                    w = t[i]+t[i+1]+t[i+2]
                    # print(w)
                    words.append(w)
                    # print(i)
                    i+=2

            else:
                print(t[i]+t[i+1])
                i+=1
        else:
            # print(i)
            words.append(t[i])
        i+=1

    sen = " ".join(words)
    # print(sen)
    return sen


unique_words_en = set()
def split_into_words_en(text):
    tokenizer = RegexpTokenizer(r'\w+')
    t = tokenizer.tokenize(text)
    # print(t)
    # print(type(t))
    for w in t:
        # print(w.lower())
        unique_words_en.add(w.lower())
    # print(unique_words_en)
    # print(len(unique_words_en))
    return len(t)

unique_words_bn = set()
def split_into_words(text):
    word_tokenizer = RegexpTokenizer(r"[\u0980-\u09FF']+")
    t= word_tokenizer.tokenize(text)
    # print(t)
    for w in t:
        unique_words_bn.add(w)
    # print(unique_words_bn)
    # print("unique_bn: ",len(unique_words_bn))
    return len(t)

def totalWords(bn,en):
    total_bn = 0
    total_en = 0
    for i in range(len(bn)):
        b= split_into_words(bn[i])
        e = split_into_words_en(en[i])
        total_bn+=b
        total_en+=e
    print("total_en",total_en)
    print("total_bn", total_bn)
    print("average word_en",total_en/len(en))
    print("average word_bn", total_bn / len(bn))
    print("lex en:",total_en/len(unique_words_en))
    print("lex bn:", total_bn/len(unique_words_bn))

def uniqueWords(bn,en):
    for i in range(len(bn)):
        split_into_words(bn[i])
        split_into_words_en(en[i])
    print("unique words of en :",len(unique_words_en))
    print("unique words of bn :", len(unique_words_bn))


def dataLen():
    bn = []
    with open("bn-en/Tanzil.bn-en.bn", 'r') as bnfile:
        for line in bnfile:
            # bn.append(line.replace('\n',''))
            bn_line = merge_into_words(line)
            bn.append(bn_line)
            # print(line)
    print("len of Bn",len(bn))
    # print(bn[4])
    en = []
    with open("bn-en/Tanzil.bn-en.en", 'r') as enfile:
        for line in enfile:
            # en.append(line.replace('\n',''))
            en_line = merge_into_words(line)
            en.append(en_line)
            # print(line)
    print("len of En",len(en))

    # print(split_into_words(bn[16]))
    # print(split_into_words_en(en[6]))

    totalWords(bn,en)
    uniqueWords(bn,en)


dataLen()