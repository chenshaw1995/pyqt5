def output(txt):
    with open('NumericRecords.txt', 'a+') as f:
        txt = txt + '\n'
        f.write(txt)