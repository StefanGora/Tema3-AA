import itertools
import fileinput

#takes the input and splits it
#builds a string matrix with every variable from input
def string_matrix(input_line, matrix):
    index = 0
    ant = 0
#index for the begining of a claus 
    for i in input_line:
        index += 1
        if str(i) == str(")"):
#splits after or
            substring = input_line[ant + 1 :index - 1]
            buffer = substring.split("V")
#splits after and
            matrix.append(buffer)
            ant = index + 1
    return matrix

#takes the string matrix and builds the claus matrix
def build_matrix(ch_matrix, nr_matrix):
    line_index = 0
    for line in ch_matrix:
        for string in line:
            if string[0] != "~":
                column_index = int(string)
#takes the positiv variable and assigns it to a column index 
                nr_matrix[line_index][column_index-1] = 1
            else:
                column_index = int(string[1:])
#takes the negative variable and assigns it to a column index 
                nr_matrix[line_index][column_index-1] = -1
        line_index += 1

#finds the biggest claus from input
def big_chungus(matrix, mini):
    for i in matrix:
        if len(i) > mini:
            mini = len(i)
            big_claus = i
    return big_claus

#checking for a vild interpretation
def check (interpretation, matrix):
    for line in matrix:
        claus = 0
        for index in range(0, len(line), 1):
            if interpretation[index] == 0 and line[index] == -1:
                claus = 1
                break
            elif interpretation[index] == 1 and line[index] == 1:
                claus = 1
                break
        if claus == 0:
            return 0
    return 1

def main():
    n_var = 0
    lines = 0
    columns = 0
    mini = -1
    str_matrix = []
    claus_matrix = [[]] 

#reading the input from stdin
    for f_line in fileinput.input():
        pass

    str_matrix = string_matrix(f_line, str_matrix)
    lines = len(str_matrix)
    columns = len(big_chungus(str_matrix, mini))
    n_var = columns

#build a matrix full of zeros like my hopes for this homework
    claus_matrix = [[0 for i in range(0, columns)] for i in range(0, lines)]

#fills the matrix with 1 and -1 after given conditions
    build_matrix(str_matrix,claus_matrix)

#list of lists with all the possible interpretation    
    table = list(itertools.product([0, 1], repeat=n_var))

#loop for checking every possible interpretation 
    for i in range(0, len(table)):
        if check(table[i], claus_matrix) != 0:
            print(1)
            return
    print(0)
    
    return 
    
if __name__ == "__main__":
    main()