# Written by siembra1978
from math import *
from random import randint
from fractions import Fraction
from dotenv import load_dotenv
import os

import wolframalpha

load_dotenv()
app_id = os.getenv('API_KEY')
print('API key initialized from .env')
client = wolframalpha.Client(app_id)


class wolframCalc:

    def __init__(self):
        print("Initialized Wolfram")

    def answer(question):
        query = client.query(question)
        print("query processed")
        output = next(query.results).text
        print("query results released")
        return output


def calculate(calculation):
    answer = eval(calculation, {"sqrt": sqrt,
                                "pow": pow,
                                "sin": sin,
                                "cos": cos,
                                "tan": tan,
                                "pi": pi,
                                "π": pi,
                                "log": log,
                                "rand": randint,
                                "frac": Fraction 
                                })

    print(type(answer))

    if isinstance(answer, float):
        print("Answer is a decimal.")
        return answer
        # return Fraction(answer).limit_denominator()
    else:
        print("Answer is an integer.")
        return answer
