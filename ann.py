import fileinput
from random import random

def initialize_weights(num_weights):
    weights = []
    for i in range(1, num_weights):
        weights.push(random() * 0.01)
    return weights


def ann(d, l_rate, x_train_set, y_train_set):
    weights = initialize_weights(d + 1)
    error = 1
    num_iterations = 0
    while (error > 0 and num_iterations < 1000):
        for x in x_train_set:




def main():
    file_input = fileinput.input()
    x_training_set = []
    y_training_set = []
    test_set = []

    d = int(file_input[0])
    m_size = int(file_input[1])
    n_size = int(file_input[2])

    for i in range(m_size):
        training_set_str = file_input[i + 3].replace(" ", "").replace("\t", "").replace("\n", "").split(',')
        training_set_float = [float(x) for x in training_set_str]
        x_training_row = training_set_float[0:d-1].append(1)
        x_training_set.append(x_training_row)
        y_training_set.append(training_set_float[d])
        # separate in dimensions d

    for i in range(n_size):
        test_set_str = file_input[i + 3].replace(" ", "").replace("\t", "").replace("\n", "").split(',')
        test_set.append([float(x) for x in test_set_str])
        # separate in dimensions d


if __name__ == "__main__":
    main()
