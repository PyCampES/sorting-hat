import csv
import random
import typer
import json

HOUSES = ["GRYFFINDOR", "SLYTHERIN", "HUFFLEPUFF", "RAVECLAW"]

FINAL_DISTRIBUTION = {}

with open("./sorting_hat.csv", "r") as csvfile:
    reader = csv.reader(csvfile, delimiter=",")
    for row in reader:
        name_size = len(row[0])
        house_id = name_size % len(HOUSES)
        house = HOUSES[house_id]
        FINAL_DISTRIBUTION[row[0]] = house


def main():
    person_name = typer.prompt("Cual es tu nombre/What's your name?")
    print(f"Hola/Hello {person_name}")

    with open('form.json') as f:
        questions = json.load(f)
        for q in questions:
            print(q['question'])
        
            

if __name__ == "__main__":
    typer.run(main)
