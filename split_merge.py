# this script reads 2 pdf files, then splits the pdf and merges the pdf

# CONSTANTS
FILEPATH_1 = "C:/Users/Username/Desktop/split_merge1.pdf"
FILEPATH_2 = "C:/Users/Username/Desktop/split_merge2.pdf"
OUTPUT_FILEPATH = "C:/Users/Username/Desktop/split_merge3.pdf"
FILE_1_PAGE = 2

from pypdf import PdfReader, PdfWriter

reader1 = PdfReader(FILEPATH_1)
reader2 = PdfReader(FILEPATH_2)
number_of_pages_file1 = len(reader1.pages)
number_of_pages_file2 = len(reader2.pages)

merger = PdfWriter()

file1 = open(FILEPATH_1, "rb")
file2 = open(FILEPATH_2, "rb")

merger.append(fileobj=file1, pages=(0, FILE_1_PAGE))
merger.append(fileobj=file2, pages=(0, number_of_pages_file2 - 1))
merger.append(fileobj=file1, pages=(FILE_1_PAGE, number_of_pages_file1))
merger.append(fileobj=file2, pages=(number_of_pages_file2 - 1, number_of_pages_file2))

output = open(OUTPUT_FILEPATH, "wb")
merger.write(output)

merger.close()
output.close()
