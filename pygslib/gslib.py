import pandas as pd

def read_to_pandas(filename, dtype=None):
    """
    Function that reads a gslib file to pandas
    """
    number_of_variables, column_names = read_header_info_(filename)
    number_of_lines_to_skip = number_of_variables + 2
    return pd.read_table(filename, skiprows=number_of_lines_to_skip, names=column_names, delim_whitespace=True, dtype=dtype)

def read_header_info_(filename):
    with open(filename, 'r') as gslib_file:
        gslib_file.readline()
        number_of_variables = int(gslib_file.readline().strip().split()[0])
        return number_of_variables, [gslib_file.readline().strip().split()[0] for line_number in range(number_of_variables)]
