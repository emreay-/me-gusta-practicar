import os
from typing import List, Dict, Optional

from openai import OpenAI

class AIBackend:
    def __init__(self, api_key: Optional[str] = None) -> None:
        self.client = OpenAI(api_key=api_key or os.environ['OPENAI_API_KEY'])

    def ask(self, question: str) -> str:
        try:
            chat_completion = self.client.chat.completions.create(
                messages=[
                    {
                        "role": "user",
                        "content": question,
                    }
                ],
                model="gpt-3.5-turbo",
            )
            return chat_completion.choices[0].message.content
        except Exception as e:
            print(f"An error occurred: {e}")
            return None

def get_question(verb, index):
    return """
I want to create a json structure for Spanish verbs as below:

{
    "id": 0,
    "name": "abandonar",
    "EN": "to abandon",
    "is_regular": true,
    "is_reflexive": false,
    "conjugation": {
        "indicativo": {
            "present": ["abandono", "abandonas", "abandona", "abandonamos", "abandonáis", "abandonan"],
            "preterite": ["abandoné", "abandonaste", "abandonó", "abandonamos", "abandonasteis", "abandonaron"],
            "imperfect": ["abandonaba", "abandonabas", "abandonaba", "abandonábamos", "abandonabais", "abandonaban"],
            "future": ["abandonaré", "abandonarás", "abandonará", "abandonaremos", "abandonaréis", "abandonarán"],
            "conditional": ["abandonaría", "abandonarías", "abandonaría", "abandonaríamos", "abandonaríais", "abandonarían"]
        },
        "subjuntivo": {
            "present": ["abandone", "abandones", "abandone", "abandonemos", "abandonéis", "abandonen"],
            "imperfect": ["abandonara", "abandonaras", "abandonara", "abandonáramos", "abandonarais", "abandonaran"],
            "future": ["abandonare", "abandonares", "abandonare", "abandonáremos", "abandonareis", "abandonaren"]
        },
        "imperativo": {
            "affirmative": ["-", "abandona", "abandone", "abandonemos", "abandonad", "abandonen"],
            "negative": ["-", "no abandones", "no abandone", "no abandonemos", "no abandonéis", "no abandonen"]
        }
    }
}

It is important to check that the verb is regular or not as if it is in reflexive form.

Please curate this structure for verb """ + verb + " with id being " + str(index)

verbs = [
    "abandonar",
    "abrir",
    "acabar",
    "aceptar",
    "acompañar",
    "admitir",
    "alcanzar",
    "almorzar",
    "amar",
    "analizar",
    "anunciar",
    "apagar",
    "aparecer",
    "aplicar",
    "apoyar",
    "aprender",
    "arreglar",
    "asegurar",
    "asistir",
    "aumentar",
    "avanzar",
    "ayudar",
    "añadir",
    "bailar",
    "bajar",
    "buscar",
    "caer",
    "calcular",
    "cambiar",
    "caminar",
    "cantar",
    "celebrar",
    "cenar",
    "cerrar",
    "cocinar",
    "comenzar",
    "comer",
    "compartir",
    "comprar",
    "comprender",
    "comunicar",
    "concluir",
    "conectar",
    "confirmar",
    "conocer",
    "conseguir",
    "conservar",
    "considerar",
    "construir",
    "consultar",
    "contar",
    "contestar",
    "controlar",
    "convertir",
    "correr",
    "cortar",
    "crear",
    "crecer",
    "creer",
    "cumplir",
    "dar",
    "deber",
    "decidir",
    "decir",
    "defender",
    "dejar",
    "demostrar",
    "descansar",
    "descubrir",
    "desear",
    "dibujar",
    "dirigir",
    "discutir",
    "diseñar",
    "dormir",
    "elegir",
    "empezar",
    "encontrar",
    "enseñar",
    "entender",
    "entrar",
    "enviar",
    "escapar",
    "escribir",
    "escuchar",
    "esperar",
    "establecer",
    "estar",
    "estudiar",
    "existir",
    "explicar",
    "expresar",
    "formar",
    "funcionar",
    "ganar",
    "gastar",
    "guardar",
    "gustar",
    "hablar",
    "hacer",
    "importar",
    "incluir",
    "insistir",
    "intentar",
    "interesar",
    "investigar",
    "ir",
    "jugar",
    "lanzar",
    "lavar",
    "leer",
    "levantar",
    "llamar",
    "llegar",
    "llevar",
    "lograr",
    "manifestar",
    "mantener",
    "medir",
    "mejorar",
    "mirar",
    "morir",
    "mover",
    "nacer",
    "necesitar",
    "notar",
    "observar",
    "obtener",
    "ocurrir",
    "ofrecer",
    "olvidar",
    "oír",
    "pagar",
    "parar",
    "parecer",
    "participar",
    "partir",
    "pasar",
    "pedir",
    "pensar",
    "perder",
    "permitir",
    "pintar",
    "poder",
    "poner",
    "practicar",
    "preguntar",
    "preocupar",
    "preparar",
    "presentar",
    "prever",
    "producir",
    "proponer",
    "quedar",
    "querer",
    "realizar",
    "rechazar",
    "recibir",
    "recoger",
    "reconocer",
    "recordar",
    "reducir",
    "remar",
    "repetir",
    "representar",
    "resolver",
    "responder",
    "resultar",
    "retirar",
    "romper",
    "saber",
    "sacar",
    "salir",
    "seguir",
    "sentar",
    "sentir",
    "ser",
    "servir",
    "señalar",
    "sorprender",
    "subir",
    "sufrir",
    "sugerir",
    "suponer",
    "tener",
    "terminar",
    "tocar",
    "tomar",
    "trabajar",
    "traer",
    "tratar",
    "usar",
    "utilizar",
    "vender",
    "venir",
    "ver",
    "viajar",
    "visitar",
    "vivir",
    "volar",
    "volver",
    "votar",
]

path = "C:\\Users\\mremr\\personal-dev\\me-gusta-practicar\\src\\assets\\chatgpt.json"

# for i, verb in enumerate(verbs):
#     try:
#         print(f"{i}/{len(verbs)}: {verb}")
#         answer = ask_chatgpt(get_question(verb, i))
#         print(answer)

#         append_to_file(path, answer)
#     except Exception as e:
#         print(f"Error occured for verb {verb}: {e}")
