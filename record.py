import pickle
import os

def output(app, id1, id2, idx):
    
    app.graph.add_edge(id1, id2, idx)
    txt = '%s %s %s' % (id1, id2, idx)
    # with open('NumericRecords.txt', 'a+') as f:
    #     txt = txt + '\n'
    #     f.write(txt)
    print(txt)

# def pop_message_box(title,message):
#     QMessageBox.about(self, "compare result", message)
# def outputCSV(txt, fname):
#     with open(fname, 'a+') as f:
#         txt = txt + '\n'
#         f.write(txt)

def save_pickle(fname, data):
    with open(fname, 'w+b') as handle:
        pickle.dump(data, handle)

    return True

def load_pickle(fname):
    # if not os.path.isfile(fname):
    #     raise ValueError

    with open(fname, 'r+b') as handle:
        b = pickle.load(handle)
    return b

def test_pickle():
    a = {'hello': 'world'}

    with open('filename.pickle', 'w+b') as f:
        pickle.dump(a, f)

    with open('filename.pickle', 'rb') as f:
        b = pickle.load(f)

    print(a == b)

if __name__ == '__main__':
    test_pickle()