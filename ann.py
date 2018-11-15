import fileinput
from random import random
# import matplotlib.pyplot as plt

def initialize_weights(num_weights):
    weights = []
    for i in range(0, num_weights):
        weights.append(random())
    return weights


def ann_training(d, l_rate, x_train_set, y_train_set, x_test_set):
    weights = initialize_weights(d + 1)
    error = 1
    num_iterations = 0
    while (error > 0 and num_iterations < 1000):
        error = 0
        num_iterations = num_iterations+1
        for key in range(0, len(x_train_set)):
            acum = 0
            for i in range(0, len(x_train_set[key])):
                acum += x_train_set[key][i] * weights[i]
            if(acum >= 0):
                y_hat = 1
            else:
                y_hat = 0

            y_difference = y_train_set[key] - y_hat
            if (y_difference != 0):
                error += 1

            for j in range(0, len(weights)):
                delta_w = (y_train_set[key]-y_hat) * l_rate * x_train_set[key][j]
                weights[j] += delta_w

    if (error != 0):
        print("no solution found")
        return []
    else:
        result = []
        for key in range(0, len(x_test_set)):
            acum = 0
            for i in range(0, len(x_test_set[key])):
                acum += x_test_set[key][i] * weights[i]
            if acum >= 0:
                y_hat = 1
            else:
                y_hat = 0
            print(y_hat)
            result.append(y_hat)
        return result


def main():
    file_input = fileinput.input()
    x_training_set = []
    y_training_set = []
    x_test_set = []
    l_rate = 0.01

    d = int(file_input[0])
    m_size = int(file_input[1])
    n_size = int(file_input[2])

    for i in range(m_size):
        training_set_str = file_input[i + 3].replace(" ", "").replace("\t", "").replace("\n", "").split(',')
        training_set_float = [float(x) for x in training_set_str]
        x_training_row = training_set_float[0:d]
        x_training_row.append(1.0)

        x_training_set.append(x_training_row)
        y_training_set.append(training_set_float[d])

    for i in range(n_size):
        test_set_str = file_input[i + m_size +3].replace(" ", "").replace("\t", "").replace("\n", "").split(',')
        test_set_float = [float(x) for x in test_set_str]
        x_test_row = test_set_float[0:d]
        x_test_row.append(1.0)
        x_test_set.append(x_test_row)

    x_training_set_col_1 = [item[0] for item in x_training_set]
    x_training_set_col_2 = [item[1] for item in x_training_set]

    x_test_set_col_1 = [item[0] for item in x_test_set]
    x_test_set_col_2 = [item[1] for item in x_test_set]

    y_test_set = ann_training(d, l_rate, x_training_set, y_training_set, x_test_set)

    # plotting code:
    # plt.figure(1)
    # for i in range(0, len(x_training_set_col_1)):
    #     if y_training_set[i] == 0:
    #         plt.scatter(x_training_set_col_1[i], x_training_set_col_2[i], c='r')
    #     else:
    #         plt.scatter(x_training_set_col_1[i], x_training_set_col_2[i], c='b')
    # plt.title('Train Dataset')
    #
    # plt.figure(2)
    # for i in range(0, len(x_test_set_col_1)):
    #     if y_test_set[i] == 0:
    #         plt.scatter(x_test_set_col_1[i], x_test_set_col_2[i], c='r')
    #     else:
    #         plt.scatter(x_test_set_col_1[i], x_test_set_col_2[i], c='b')
    # plt.title('Test Dataset')
    # plt.show()



if __name__ == "__main__":
    main()
