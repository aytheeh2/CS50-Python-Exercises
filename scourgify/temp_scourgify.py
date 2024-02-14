import csv
import sys
from tabulate import tabulate
if len(sys.argv) ==3:
    if sys.argv[1].endswith(".csv") and sys.argv[2].endswith(".csv"):
        try:
            with open("before.csv") as file:
                reader = csv.DictReader(file)
                names =[]
                las_name =""
                fir_name=""
                for row in reader:
                    with open(sys.argv[2],"a") as file2:
                        # print(sys.argv[2])
                        las_name,fir_name = row["name"].split(",")
                        # print(las_name,fir_name)
                        file2.write(f"\"{fir_name.lstrip().rstrip()} {las_name.lstrip().rstrip()}\", {row['house']}\n")
                        # writer = csv.writer(file2)
                        # writer.writerow(f"{fir_name} {las_name} {row['house']}\n")
                        # """ {str(names[0]).rstrip().lstrip()}")"""

                    # print(names[0],end=" ")

                # print(first_name,second_name)
                # print(tabulate(r,headers="keys",tablefmt="grid"))
                # with open(sys.argv[2],"w") as file2:
                #     s= csv.DictWriter(file2,"")
        except FileNotFoundError:
            sys.exit("File does not exist")
elif len(sys.argv) <3:
    sys.exit("Too few command-line arguments")

elif len(sys.argv) >3:
    sys.exit("Too many command-line arguments")

