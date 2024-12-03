import json


#current_dir = pathlib


respuestas_completas = [{'pregunta': 'FILA1-1', 'respuestas': ['+', '-', '']}, {'pregunta': 'FILA1-2', 'respuestas': ['', '+', '-']}, {'pregunta': 'FILA1-3', 'respuestas': ['-', '', '+']}, {'pregunta': 'FILA1-4', 'respuestas': ['+', '', '-']}, {'pregunta': 'FILA1-5', 'respuestas': ['+', '-', '']}, {'pregunta': 'FILA1-6', 'respuestas': ['+', '-', '']}, {'pregunta': 'FILA1-7', 'respuestas': ['-', '', '+']}, {'pregunta': 'FILA1-8', 'respuestas': ['+', '', '-']}, {'pregunta': 'FILA1-9', 'respuestas': ['+', '', '-']}, {'pregunta': 'FILA1-10', 'respuestas': ['+', '', '-']}, {'pregunta': 'FILA1-11', 'respuestas': ['-', '', '+']}, {'pregunta': 'FILA1-12', 'respuestas': ['+', '-', '']}, {'pregunta': 'FILA1-13', 'respuestas': ['+', '', '-']}, {'pregunta': 'FILA1-14', 'respuestas': ['+', '-', '']},{'pregunta': 'FILA1-1', 'respuestas': ['+', '-', '']}, {'pregunta': 'FILA1-2', 'respuestas': ['', '+', '-']}, {'pregunta': 'FILA1-3', 'respuestas': ['-', '', '+']}, {'pregunta': 'FILA1-4', 'respuestas': ['+', '', '-']}, {'pregunta': 'FILA1-5', 'respuestas': ['+', '-', '']}, {'pregunta': 'FILA1-6', 'respuestas': ['+', '-', '']}, {'pregunta': 'FILA1-7', 'respuestas': ['-', '', '+']}, {'pregunta': 'FILA1-8', 'respuestas': ['+', '', '-']}, {'pregunta': 'FILA1-9', 'respuestas': ['+', '', '-']}, {'pregunta': 'FILA1-10', 'respuestas': ['+', '', '-']}, {'pregunta': 'FILA1-11', 'respuestas': ['-', '', '+']}, {'pregunta': 'FILA1-12', 'respuestas': ['+', '-', '']}, {'pregunta': 'FILA1-13', 'respuestas': ['+', '', '-']}, {'pregunta': 'FILA1-14', 'respuestas': ['+', '-', '']},{'pregunta': 'FILA1-1', 'respuestas': ['+', '-', '']}, {'pregunta': 'FILA1-2', 'respuestas': ['', '+', '-']}, {'pregunta': 'FILA1-3', 'respuestas': ['-', '', '+']}, {'pregunta': 'FILA1-4', 'respuestas': ['+', '', '-']}, {'pregunta': 'FILA1-5', 'respuestas': ['+', '-', '']}, {'pregunta': 'FILA1-6', 'respuestas': ['+', '-', '']}, {'pregunta': 'FILA1-7', 'respuestas': ['-', '', '+']}, {'pregunta': 'FILA1-8', 'respuestas': ['+', '', '-']}, {'pregunta': 'FILA1-9', 'respuestas': ['+', '', '-']}, {'pregunta': 'FILA1-10', 'respuestas': ['+', '', '-']}, {'pregunta': 'FILA1-11', 'respuestas': ['-', '', '+']}, {'pregunta': 'FILA1-12', 'respuestas': ['+', '-', '']}, {'pregunta': 'FILA1-13', 'respuestas': ['+', '', '-']}, {'pregunta': 'FILA1-14', 'respuestas': ['+', '-', '']},{'pregunta': 'FILA1-1', 'respuestas': ['+', '-', '']}, {'pregunta': 'FILA1-2', 'respuestas': ['', '+', '-']}, {'pregunta': 'FILA1-3', 'respuestas': ['-', '', '+']}, {'pregunta': 'FILA1-4', 'respuestas': ['+', '', '-']}, {'pregunta': 'FILA1-5', 'respuestas': ['+', '-', '']}, {'pregunta': 'FILA1-6', 'respuestas': ['+', '-', '']}, {'pregunta': 'FILA1-7', 'respuestas': ['-', '', '+']}, {'pregunta': 'FILA1-8', 'respuestas': ['+', '', '-']}, {'pregunta': 'FILA1-9', 'respuestas': ['+', '', '-']}, {'pregunta': 'FILA1-10', 'respuestas': ['+', '', '-']}, {'pregunta': 'FILA1-11', 'respuestas': ['-', '', '+']}, {'pregunta': 'FILA1-12', 'respuestas': ['+', '-', '']}, {'pregunta': 'FILA1-13', 'respuestas': ['+', '', '-']}, {'pregunta': 'FILA1-14', 'respuestas': ['+', '-', '']},{'pregunta': 'FILA1-1', 'respuestas': ['+', '-', '']}, {'pregunta': 'FILA1-2', 'respuestas': ['', '+', '-']}, {'pregunta': 'FILA1-3', 'respuestas': ['-', '', '+']}, {'pregunta': 'FILA1-4', 'respuestas': ['+', '', '-']}, {'pregunta': 'FILA1-5', 'respuestas': ['+', '-', '']}, {'pregunta': 'FILA1-6', 'respuestas': ['+', '-', '']}, {'pregunta': 'FILA1-7', 'respuestas': ['-', '', '+']}, {'pregunta': 'FILA1-8', 'respuestas': ['+', '', '-']}, {'pregunta': 'FILA1-9', 'respuestas': ['+', '', '-']}, {'pregunta': 'FILA1-10', 'respuestas': ['+', '', '-']}, {'pregunta': 'FILA1-11', 'respuestas': ['-', '', '+']}, {'pregunta': 'FILA1-12', 'respuestas': ['+', '-', '']}, {'pregunta': 'FILA1-13', 'respuestas': ['+', '', '-']}, {'pregunta': 'FILA1-14', 'respuestas': ['+', '-', '']},{'pregunta': 'FILA1-1', 'respuestas': ['+', '-', '']}, {'pregunta': 'FILA1-2', 'respuestas': ['', '+', '-']}, {'pregunta': 'FILA1-3', 'respuestas': ['-', '', '+']}, {'pregunta': 'FILA1-4', 'respuestas': ['+', '', '-']}, {'pregunta': 'FILA1-5', 'respuestas': ['+', '-', '']}, {'pregunta': 'FILA1-6', 'respuestas': ['+', '-', '']}, {'pregunta': 'FILA1-7', 'respuestas': ['-', '', '+']}, {'pregunta': 'FILA1-8', 'respuestas': ['+', '', '-']}, {'pregunta': 'FILA1-9', 'respuestas': ['+', '', '-']}, {'pregunta': 'FILA1-10', 'respuestas': ['+', '', '-']}, {'pregunta': 'FILA1-11', 'respuestas': ['-', '', '+']}, {'pregunta': 'FILA1-12', 'respuestas': ['+', '-', '']}, {'pregunta': 'FILA1-13', 'respuestas': ['+', '', '-']}, {'pregunta': 'FILA1-14', 'respuestas': ['+', '-', '']},{'pregunta': 'FILA1-1', 'respuestas': ['+', '-', '']}, {'pregunta': 'FILA1-2', 'respuestas': ['', '+', '-']}, {'pregunta': 'FILA1-3', 'respuestas': ['-', '', '+']}, {'pregunta': 'FILA1-4', 'respuestas': ['+', '', '-']}, {'pregunta': 'FILA1-5', 'respuestas': ['+', '-', '']}, {'pregunta': 'FILA1-6', 'respuestas': ['+', '-', '']}, {'pregunta': 'FILA1-7', 'respuestas': ['-', '', '+']}, {'pregunta': 'FILA1-8', 'respuestas': ['+', '', '-']}, {'pregunta': 'FILA1-9', 'respuestas': ['+', '', '-']}, {'pregunta': 'FILA1-10', 'respuestas': ['+', '', '-']}, {'pregunta': 'FILA1-11', 'respuestas': ['-', '', '+']}, {'pregunta': 'FILA1-12', 'respuestas': ['+', '-', '']}, {'pregunta': 'FILA1-13', 'respuestas': ['+', '', '-']}, {'pregunta': 'FILA1-14', 'respuestas': ['+', '-', '']},{'pregunta': 'FILA1-1', 'respuestas': ['+', '-', '']}, {'pregunta': 'FILA1-2', 'respuestas': ['', '+', '-']}, {'pregunta': 'FILA1-3', 'respuestas': ['-', '', '+']}, {'pregunta': 'FILA1-4', 'respuestas': ['+', '', '-']}, {'pregunta': 'FILA1-5', 'respuestas': ['+', '-', '']}, {'pregunta': 'FILA1-6', 'respuestas': ['+', '-', '']}, {'pregunta': 'FILA1-7', 'respuestas': ['-', '', '+']}, {'pregunta': 'FILA1-8', 'respuestas': ['+', '', '-']}, {'pregunta': 'FILA1-9', 'respuestas': ['+', '', '-']}, {'pregunta': 'FILA1-10', 'respuestas': ['+', '', '-']}, {'pregunta': 'FILA1-11', 'respuestas': ['-', '', '+']}, {'pregunta': 'FILA1-12', 'respuestas': ['+', '-', '']}, {'pregunta': 'FILA1-13', 'respuestas': ['+', '', '-']}, {'pregunta': 'FILA1-14', 'respuestas': ['+', '-', '']},{'pregunta': 'FILA1-1', 'respuestas': ['+', '-', '']}, {'pregunta': 'FILA1-2', 'respuestas': ['', '+', '-']}, {'pregunta': 'FILA1-3', 'respuestas': ['-', '', '+']}, {'pregunta': 'FILA1-4', 'respuestas': ['+', '', '-']}, {'pregunta': 'FILA1-5', 'respuestas': ['+', '-', '']}, {'pregunta': 'FILA1-6', 'respuestas': ['+', '-', '']}, {'pregunta': 'FILA1-7', 'respuestas': ['-', '', '+']}, {'pregunta': 'FILA1-8', 'respuestas': ['+', '', '-']}, {'pregunta': 'FILA1-9', 'respuestas': ['+', '', '-']}, {'pregunta': 'FILA1-10', 'respuestas': ['+', '', '-']}, {'pregunta': 'FILA1-11', 'respuestas': ['-', '', '+']}, {'pregunta': 'FILA1-12', 'respuestas': ['+', '-', '']}, {'pregunta': 'FILA1-13', 'respuestas': ['+', '', '-']}, {'pregunta': 'FILA1-14', 'respuestas': ['+', '-', '']},{'pregunta': 'FILA1-1', 'respuestas': ['+', '-', '']}, {'pregunta': 'FILA1-2', 'respuestas': ['', '+', '-']}, {'pregunta': 'FILA1-3', 'respuestas': ['-', '', '+']}, {'pregunta': 'FILA1-4', 'respuestas': ['+', '', '-']}, {'pregunta': 'FILA1-5', 'respuestas': ['+', '-', '']}, {'pregunta': 'FILA1-6', 'respuestas': ['+', '-', '']}, {'pregunta': 'FILA1-7', 'respuestas': ['-', '', '+']}, {'pregunta': 'FILA1-8', 'respuestas': ['+', '', '-']}, {'pregunta': 'FILA1-9', 'respuestas': ['+', '', '-']}, {'pregunta': 'FILA1-10', 'respuestas': ['+', '', '-']}, {'pregunta': 'FILA1-11', 'respuestas': ['-', '', '+']}, {'pregunta': 'FILA1-12', 'respuestas': ['+', '-', '']}, {'pregunta': 'FILA1-13', 'respuestas': ['+', '', '-']}, {'pregunta': 'FILA1-14', 'respuestas': ['+', '-', '']},{'pregunta': 'FILA1-1', 'respuestas': ['+', '-', '']}, {'pregunta': 'FILA1-2', 'respuestas': ['', '+', '-']}, {'pregunta': 'FILA1-3', 'respuestas': ['-', '', '+']}, {'pregunta': 'FILA1-4', 'respuestas': ['+', '', '-']}, {'pregunta': 'FILA1-5', 'respuestas': ['+', '-', '']}, {'pregunta': 'FILA1-6', 'respuestas': ['+', '-', '']}, {'pregunta': 'FILA1-7', 'respuestas': ['-', '', '+']}, {'pregunta': 'FILA1-8', 'respuestas': ['+', '', '-']}, {'pregunta': 'FILA1-9', 'respuestas': ['+', '', '-']}, {'pregunta': 'FILA1-10', 'respuestas': ['+', '', '-']}, {'pregunta': 'FILA1-11', 'respuestas': ['-', '', '+']}, {'pregunta': 'FILA1-12', 'respuestas': ['+', '-', '']}, {'pregunta': 'FILA1-13', 'respuestas': ['+', '', '-']}, {'pregunta': 'FILA1-14', 'respuestas': ['+', '-', '']},{'pregunta': 'FILA1-1', 'respuestas': ['+', '-', '']}, {'pregunta': 'FILA1-2', 'respuestas': ['', '+', '-']}, {'pregunta': 'FILA1-3', 'respuestas': ['-', '', '+']}, {'pregunta': 'FILA1-4', 'respuestas': ['+', '', '-']}, {'pregunta': 'FILA1-5', 'respuestas': ['+', '-', '']}, {'pregunta': 'FILA1-6', 'respuestas': ['+', '-', '']}, {'pregunta': 'FILA1-7', 'respuestas': ['-', '', '+']}, {'pregunta': 'FILA1-8', 'respuestas': ['+', '', '-']}, {'pregunta': 'FILA1-9', 'respuestas': ['+', '', '-']}, {'pregunta': 'FILA1-10', 'respuestas': ['+', '', '-']}, {'pregunta': 'FILA1-11', 'respuestas': ['-', '', '+']}, {'pregunta': 'FILA1-12', 'respuestas': ['+', '-', '']}, {'pregunta': 'FILA1-13', 'respuestas': ['+', '', '-']}, {'pregunta': 'FILA1-14', 'respuestas': ['+', '-', '']},]



def print_respuestas_completas():
    print('file connected:', respuestas_completas)

def appendRespuestas(respuestas_completas):
    all_respuestas = []

    for i, respuesta in enumerate(respuestas_completas): 
        all_respuestas.extend(respuesta["respuestas"])

    print('printing inside func:', all_respuestas)
    return all_respuestas


#test validation kuder test
def kuder_validator():
    validators_paths = ['json/puntajes/VERIFICATION.JSON', 'json/puntajes/AL0.JSON', 'json/puntajes/MC1.JSON', 'json/puntajes/CL2.JSON', 'json/puntajes/CT3.JSON', 'json/puntajes/PR4.JSON', 'json/puntajes/AR5.JSON', 'json/puntajes/LT6.JSON', 'json/puntajes/MS7.JSON', 'json/puntajes/SS8.JSON', 'json/puntajes/OF9.JSON']

    answers = appendRespuestas(respuestas_completas)
    print('answers :', answers)
    test_values = []

    # Abrir y cargar archivo JSON
    def cargar_test(path):
        with open(path, 'r', encoding='utf-8') as file:
            return json.load(file)

    for path in validators_paths:
  
        points = 0

        verification = cargar_test(path)

        for question in verification:
            #get the question number
            question_index = question["pregunta"] - 1

            #check if the answer matches
            if question_index < len(answers) and answers[question_index] == question["respuesta"] or (answers[question_index] != "" and question["respuesta"] == "*"):
                points += 1
                print(f"Match: {question['respuesta']} for question {question['pregunta']}")

        # Split by '/' to isolate the last part
        filename = path.split('/')[-1]

        # Split by '.' to remove the file extension
        identifier = filename.split('.')[0]

        test_values.append({identifier:points})

    return test_values   

#appendRespuestas(respuestas_completas)

print(kuder_validator())