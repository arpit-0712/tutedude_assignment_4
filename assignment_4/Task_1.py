#!/usr/bin/env python3
def python_file_reader(filename):
    file_reader = None  # Initialize file_reader to None
    try:
        file_reader = open(filename, 'r')
        lines = file_reader.readlines()
        line_number = 1
        print("Reading file content:")
        for line in lines:
            print("Line no", line_number, ":", line)
            line_number += 1

    except FileNotFoundError:
        print(f"Error:The file {filename}  was not found")

    finally:
        file_reader.close()


python_file_reader("sample.txt")
