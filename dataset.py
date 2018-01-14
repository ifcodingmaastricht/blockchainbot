f = open('dataset.txt', 'r')
dataset = f.readlines()
dataset = [float(i) for i in dataset]
for i in dataset:
    print(i)
