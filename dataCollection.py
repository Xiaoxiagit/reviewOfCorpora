def dataCollect():
    bn = []
    with open("train.bn", 'r') as bnfile:
        for line in bnfile:
            bn.append(line.replace('\n',''))
            # print(line)

    # print(bn[4])
    en = []
    with open("train.en", 'r') as enfile:
        for line in enfile:
            en.append(line.replace('\n',''))
            # print(line)

    # print(en[4])
    with open("bilingual.txt",'w') as outfile:
        for i in range(len(bn)):
            outfile.write(bn[i] + '\n')
            outfile.write(en[i] + '\n')
    # he = ('একমাত ্ র'.replace(' ',''))
    # print(he)
    # print(list('একমাত ্ র'.replace(' ','')))

dataCollect()
