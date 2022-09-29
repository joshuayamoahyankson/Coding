import csv
# Indexes of some of the columns
# in the dentists.csv file.
COMPANY_NAME_INDEX = 0
NUM_EMPS_INDEX = 3
NUM_PATIENTS_INDEX = 4

def main():
    with open("dentists.csv", "rt") as filename:
        reader = csv.reader(filename)
        
        next(reader)

        for i in reader:
            company = i[COMPANY_NAME_INDEX ]
            num_employees = int(i[NUM_EMPS_INDEX ])
            num_patients = int(i[NUM_PATIENTS_INDEX])

            calculations = num_patients / num_employees
        
        if calculations > 0:
            number = company
    print(f"{number} has {calculations:.1f}"
            " patients per employee")


if __name__ == "__main__":
    main()
