# HOW TO ACCESS CLASS PROPERTIES
from surveys import *

for survey in surveys.values():
    print("title: ",survey.title)
    print("instructions: ",survey.instructions)
    for question in survey.questions:
        print("allow text: ", question.allow_text)
        print(question.question)
        for choice in question.choices:
            print("choice: ",choice)
    print('\r\n')