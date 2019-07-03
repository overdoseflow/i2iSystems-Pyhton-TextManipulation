import csv
def read_csv(v_object):

    reader = csv.reader(v_object)

    for row in reader:

        print(",".join(row))

if __name__ == "__main__":

    csv_path = "C:\\Users\\7307\\Downloads\\random_python_information.csv"

    with open(csv_path, "r") as v_read:

        read_csv(v_read)