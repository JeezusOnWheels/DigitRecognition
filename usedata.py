#Read the mnist db into ideal_outputs and digits respectively
f = open("mnist_train.csv", "r")
ideal_output = []#[1,6,3,7,9,0,...]
digits = []#digits will be [[1,2,...,284],[1,2,...,284],[1,2,...,284]]
for line in f:
    ideal_output.append(int(line[0]))
    digit = []
    filtered = line.split(',')
    for item in filtered:
        digit.append(int(item)/255)
    digits.append(digit[1:])
