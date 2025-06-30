# pylint: disable=import-outside-toplevel
# pylint: disable=line-too-long
# flake8: noqa
import os
import pandas as pd
import zipfile
"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""

def generate_csv(ruta, target):
    texts = []
    # Recorrer todos los archivos en la carpeta
    for file_name in os.listdir(ruta):
            file_path = os.path.join(ruta, file_name)
            
            with open(file_path, "r", encoding="utf-8") as file:
                content = file.read()
                texts.append(content)
            
    df = pd.DataFrame([[text, target] for text in texts], columns=["phrase", "target"])
    return df


import zipfile

def pregunta_01():
    # Descomprimir ZIP
    with zipfile.ZipFile("files/input.zip", "r") as zip_ref:
        zip_ref.extractall("files/")

    targets = ["negative", "neutral", "positive"]
    csvs_train = []

    for target in targets:
        csvs_train.append(generate_csv("files/input/train/" + target, target))

    train_csv = pd.concat(csvs_train, ignore_index=True)

    csvs_test = []
    for target in targets:
        csvs_test.append(generate_csv("files/input/test/" + target, target))

    test_csv = pd.concat(csvs_test, ignore_index=True)

    os.makedirs("files/output", exist_ok=True)
    train_csv.to_csv("files/output/train_dataset.csv", index=False, encoding="utf-8")
    test_csv.to_csv("files/output/test_dataset.csv", index=False, encoding="utf-8")

    print("CSV guardados correctamente.")


   
         


pregunta_01()
