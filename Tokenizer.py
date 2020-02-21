import string, re

puncList = ["।","”","“","’",'"','৷',"‘"]
for p in string.punctuation.lstrip():
    puncList.append(p)


def tokenizer(doc):
    # remove punctuation
    tokens = []
    for word in doc.split(" "):
        i =0
        # print(list(word))
        while i< len(word):

            if(word[i] in puncList):
                tokens.append(word[i])

            else:
                w = ""
                p = ""
                while i< len(word):
                    # print(word[i])
                    if word[i] in puncList:
                        p = word[i]
                        # tokens.append(word[i])
                        break
                    else:
                        w += word[i]
                        i+=1
                tokens.append(w)
                # print(tokens)
                if p!="":
                    tokens.append(p)

            i+=1



    # print(tokens)

    # bn_tok.append(tokens)
    return " ".join(tokens)
    # return "\n".join(tokens)

def col():
    bn = []
    with open("bn-en/GlobalVoices.bn-en.bn", 'r') as bnfile:
        for line in bnfile:
            bn.append(line.replace('\n', ''))

    # print(bn)
    bn_tok = []
    for i in range (len(bn)):
        bn_tok.append(tokenizer(bn[i]))
    # print(bn_tok)
    with open("train.tok.bn", 'w') as outfile:
        for i in range (len(bn_tok)):
            outfile.write(bn_tok[i] + '\n')

col()
# t = tokenizer("মির্জা ফখরুল বলেন, খালেদা জিয়ার মুক্তির দাবিতে আগামী শুক্রবার খালেদা জিয়ার রোগমুক্তি ও সুস্বাস্থ্য কামনায় দেশব্যাপী বাদ জুমা দোয়া মাহফিল এবং শনিবার বেলা দুইটায় রাজধানীতে নয়াপল্টনে বিএনপির কেন্দ্রীয় কার্যালয়ের সামনে সমাবেশ ও সারা দেশে জেলা সদরে বিক্ষোভ সমাবেশ করা হবে।")
# print(bn_tok)
# print(tokenizer("এবং সবশেষে তান্জানিয়া থেকে সান্দ্রা মুশি স্মরন করছেন তার ‘প্রথমবার ’ ।"))