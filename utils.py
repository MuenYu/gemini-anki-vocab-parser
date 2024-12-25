import csv


def read_lines_from_txt(filepath):
    """
    read a text file and output lines in array
    :param filepath: file path
    :return: lines array
    """

    try:
        with open(filepath, 'r') as file:
            lines = [line.strip() for line in file]  # strip removes trailing newline
            return lines
    except FileNotFoundError:
        print(f"Error: File not found at path: {filepath}")
        exit(1)
    except Exception as e:
        print(f"Unexpected Error: {e}")
        exit(1)


def read_line_from_txt(filepath):
    """
    Read a text file and output the content as one line
    :param filepath: file path
    :return: the string
    """
    try:
        with open(filepath, 'r') as file:
            return file.read()
    except FileNotFoundError:
        print(f"Error: File not found at path: {filepath}")
        exit(1)
    except Exception as e:
        print(f"Unexpected Error: {e}")
        exit(1)


def export_csv(header, data, dst):
    try:
        if not data:
            print("Warning: No data to export.")
            return

        with open(dst, 'w', newline='', encoding='utf-8') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=header)
            writer.writerows(data)
    except Exception as e:
        print(f"Unexpected error: {e}")
        exit(1)
