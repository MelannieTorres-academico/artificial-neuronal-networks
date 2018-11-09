import fileinput


def main():
    file_input = fileinput.input()
    training_set = []
    test_set = []

    d = int(file_input[0])
    m_size = int(file_input[1])
    n_size = int(file_input[2])

    for i in range(m_size):
        training_set.append(file_input[i+3].replace(" ", "").replace("\t", "").replace("\n", "").split(','))
        # separate in dimensions d

    for i in range(n_size):
        test_set.append(file_input[i+3+m_size].replace(" ", "").replace("\t", "").replace("\n", "").split(','))
        # separate in dimensions d

    print(d)
    print(m_size)
    print(n_size)
    print(training_set)
    print(test_set)


if __name__ == "__main__":
    main()
