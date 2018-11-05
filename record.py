def output(txt):
    with open('NumericRecords.txt', 'a+') as f:
        txt = txt + '\n'
        f.write(txt)

def outputCSV(txt, fname):
    with open(fname, 'a+') as f:
        txt = txt + '\n'
        f.write(txt)