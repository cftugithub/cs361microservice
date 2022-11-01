import csv
import time
from dataclasses import dataclass
from collections import defaultdict


@dataclass
class Applicant:
    name: str
    email: str
    profession: str
    resume: str
    cover_letter: str


def update_applicants(applicants, type_applicants):
    print("updating applicants...")
    with open('applicants.csv') as f:
        csv_reader = csv.DictReader(f)
        for row in csv_reader:
            new_applicant = Applicant(
                row['Name'],
                row['Email'],
                row['Profession'],
                row['Resume'],
                row['Cover Letter']
            )

            if new_applicant not in applicants:
                applicants.append(new_applicant)

            if new_applicant not in type_applicants[row['Profession']]:
                type_applicants[row['Profession']].append(new_applicant)


def retrieve_applicants(applicants, num_applicants, type_applicants=None, profession_type=None):
    num_applicants = int(num_applicants)

    if profession_type is not None:
        return type_applicants[profession_type][:num_applicants]

    else:
        return applicants[:num_applicants]


def get_request(applicants, type_applicants):
    with open('request.txt', 'r') as f:
        data = f.read()

    if "get" in data:
        print("found a request")
        args = data.split(' ')
        num = args[1]
        if len(args) == 3:
            profession_type = args[2]
            print(f"getting {num} {profession_type}s")
            return retrieve_applicants(applicants, num, type_applicants, profession_type)
        else:
            print(f"getting {num} applicants")
            return retrieve_applicants(applicants, num)


def clear_request():
    print("clearing request.txt")
    with open('request.txt', 'r+') as f:
        # erase data in request.txt
        f.truncate(0)


def write_output(applicants_list):
    with open('output.csv', 'w', newline='') as f:
        field_names = ['name', 'email', 'profession', 'resume', 'cover_letter']
        writer = csv.DictWriter(f, field_names)

        writer.writeheader()

        for applicant in applicants_list:
            writer.writerow({
                'name': applicant.name,
                'email': applicant.email,
                'profession': applicant.profession,
                'resume': applicant.resume,
                'cover_letter': applicant.cover_letter
            })


def run():
    print("starting microservice...")
    applicants = []
    type_applicants = defaultdict(list)

    update_applicants(applicants, type_applicants)

    while True:
        time.sleep(10)
        update_applicants(applicants, type_applicants)
        results = get_request(applicants, type_applicants)
        if results:
            write_output(results)
            clear_request()


if __name__ == "__main__":
    run()
