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
    person_name = typer.prompt("¿Cuál es tu nombre?")
    print(f"Hola/Hello {person_name}")

    result = []
    with open('form.json') as f:
        questions = json.load(f)
        for q in questions:
            answers = '\n'.join(f"{idx+1}) {i['answer']}" for idx, i in enumerate(q['options']))
            text = f"{q['question']} \n\n{answers}\n"
            result.append(typer.prompt(text))
        print(result)

if __name__ == "__main__":
    typer.run(main)
