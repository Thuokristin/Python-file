def modify_and_write_file(input_filename, output_filename):
    """
    Reads a file, modifies each line, and writes the modified content to a new file.

    Args:
        input_filename (str): The name of the file to read.
        output_filename (str): The name of the file to write to.
    """
    try:
        with open(input_filename, 'r') as infile:
            try:
                with open(output_filename, 'w') as outfile:
                    for line in infile:
                        # Let's do a simple modification: add a timestamp to each line
                        import datetime
                        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                        modified_line = f"[{timestamp}] {line.strip()}\n"
                        outfile.write(modified_line)
                print(f"Successfully read '{input_filename}', modified it, and wrote to '{output_filename}'.")
            except IOError as e:
                print(f"Error writing to file '{output_filename}': {e}")
    except FileNotFoundError:
        print(f"Error: Input file '{input_filename}' not found.")
    except PermissionError:
        print(f"Error: Permission denied to read '{input_filename}'.")
    except IOError as e:
        print(f"Error reading file '{input_filename}': {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    input_file = input("Enter the name of the input file: ")
    output_file = input("Enter the name of the output file: ")
    modify_and_write_file(input_file, output_file)