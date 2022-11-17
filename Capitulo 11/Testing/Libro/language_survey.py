from survey import AnonymousSurvey

# Define una pregunta y hace una encuesta
question = "What language did you first learn to speak?"
my_survey = AnonymousSurvey(question)

#Muestra la pregunta y guarda las respuestas a la pregunta
my_survey.show_question()
print("Enter 'q' at anytime to quit.\n")
while True:
    response = input("Language: ")
    if response == 'q':
        print("---ENCUESTA FINALIZADA---")
        break
    my_survey.store_response(response.title())
    
# Muestra los resultados de la encuesta
print("\nThank you to everyone who participated in the survey!")
my_survey.show_results()