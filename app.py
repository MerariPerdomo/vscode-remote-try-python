#-----------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See LICENSE in the project root for license information.
#-----------------------------------------------------------------------------------------

import random

def jugar_piedra_papel_tijera():
    elementos = ["rock", "paper", "scissor"]
    continuar = True
    puntos = 0

    while continuar:
        eleccion_usuario = input("Choose rock, paper or scissor: ").lower()

        if eleccion_usuario not in elementos:
            print("Esa opción no está disponible.")
            continue

        eleccion_computadora = random.choice(elementos)

        print("The computer choose:", eleccion_computadora)

        if eleccion_usuario == eleccion_computadora:
            print("Es un empate!")
            puntos += 0.5
        elif (eleccion_usuario == "rock" and eleccion_computadora == "scissor") or \
             (eleccion_usuario == "paper" and eleccion_computadora == "rock") or \
             (eleccion_usuario == "scissor" and eleccion_computadora == "paper"):
            print("¡Ganaste!")
            puntos += 1
        else:
            print("Perdiste.")
            puntos += 0

        print("Tu puntuación actual:", puntos)

        respuesta = input("¿Quieres seguir jugando? (s/n): ").lower()
        if respuesta != "s":
            continuar = False

    print("Puntuación total:", puntos)

jugar_piedra_papel_tijera()

from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return app.send_static_file("index.html")
