#!/usr/bin/env python3
import os


def python_file_writer():
    try:
        file_writer = open("output.txt", "w")
        input_text = input("Enter text to write to the input file: ")
        file_writer.write(input_text + "\n")
        print("Output written successfully")

    except Exception as e:
        print(e)
    finally:
        file_writer.close()


def python_file_appender():
    try:
        file_writer = open("output.txt", "a")
        input_text = input("Enter additional data to append: ")
        file_writer.write(input_text + "\n")
        print("Data appended successfully")
    except Exception as e:
        print(e)
    finally:
        file_writer.close()


def python_file_reader(filename):
    try:
        file_reader = open(filename, 'r')
        file_name = os.path.basename(filename)
        reader_text = file_reader.readlines()
        print(f"Final contents of file:{file_name}")
        for line in reader_text:
            print(line)

    except FileNotFoundError:
        print(f"Error:The file {file_reader}  was not found")

    finally:
        file_reader.close()


python_file_writer()
python_file_appender()
python_file_reader("output.txt")
