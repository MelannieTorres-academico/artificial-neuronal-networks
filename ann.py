import fileinput

def main():
    # example input
    file_input = fileinput.input()
    training_set = []

    d = int(file_input[0])
    m_size = int(file_input[1])
    n_size = int(file_input[2])


    for i in range(m_size):
        training_set.append(file_input[i+3])
        #separate in dimensions d

    for i in range(n_size):
        training_set.append(file_input[i+3+m_size])
        #separate in dimensions d



if __name__ == "__main__":
    main()
