def read_file(file_name):
    """ Reads in a file and returns the entire contents of the file as a string. """
    with open(file_name, 'r') as file:
        file_contents = file.read()
    return file_contents

def read_file_into_list(file_name):
    """ Reads in a file and stores each line as an element in a list. """
    with open(file_name, 'r') as file:
        file_lines = file.readlines()
    return file_lines

def write_first_line_to_file(file_contents, output_filename):
    """ Writes the first line of a string to a file. """
    first_line = file_contents.split('\n')[0]
    with open(output_filename, 'w') as output_file:
        output_file.write(first_line)

def read_even_numbered_lines(file_name):
    """ Reads in the even numbered lines of a file and returns them as a list. """
    with open(file_name, 'r') as file:
        file_lines = file.readlines()
    even_lines = [line.strip() for i, line in enumerate(file_lines) if i % 2 == 1]
    return even_lines

def read_file_in_reverse(file_name):
    """ Reads a file and returns a list of the lines in reverse order. """
    with open(file_name, 'r') as file:
        file_lines = file.readlines()
    reversed_lines = file_lines[::-1]
    return reversed_lines

def main():
    file_contents = read_file("sampletext.txt")
    print(file_contents)

    file_lines = read_file_into_list("sampletext.txt")
    print(file_lines)

    write_first_line_to_file(file_contents, "output.txt")

    even_lines = read_even_numbered_lines("sampletext.txt")
    print(even_lines)

    reversed_lines = read_file_in_reverse("sampletext.txt")
    print(reversed_lines)

if __name__ == "__main__":
    main()
