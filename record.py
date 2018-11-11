def output(txt):
    with open('NumericRecords.txt', 'a+') as f:
        txt = txt + '\n'
        f.write(txt)

# def outputCSV(txt, fname):
#     with open(fname, 'a+') as f:
#         txt = txt + '\n'
#         f.write(txt)

import pickle

def save_pickle(fname, data):
    with open(f'{fname}.pickle', 'wb') as handle:
        pickle.dump(a, handle, protocol=pickle.HIGHEST_PROTOCOL)

    return f'{fname}.pickle'

def load_pickle(fname):
    if not os.path.isfile(f'{fname}.pickle'):
        return ""

    with open(f'{fname}.pickle', 'rb') as handle:
        b = pickle.load(handle)
    return b

def test_pickle():
    a = {'hello': 'world'}

    with open('filename.pickle', 'wb') as handle:
        pickle.dump(a, handle, protocol=pickle.HIGHEST_PROTOCOL)

    with open('filename.pickle', 'rb') as handle:
        b = pickle.load(handle)

    print(a == b)

if __name__ == '__main__':
    test_pickle()