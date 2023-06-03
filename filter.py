# this script reads a txt file, then splits the data and filters out the transport spending
# https://www.ocr2edit.com

sum = 0

with open("./sample.txt", "r") as file:
    data = file.read()
    data = data.split("\n")

    for i in data:
        i = i.split(" ")

        for j in i:
            if j == "BUS/MRT":
                sum += float(i[-1])
            else:
                pass

    print(sum)
