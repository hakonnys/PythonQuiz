#Copyright Håkon Nysveen 2025

def get_nonempty_input(prompt):
    while True:
        answer = input(prompt).strip()
        if answer !="": 
           return answer
        print ("Du må skrive noe før du kan gå videre!")
 
while True:
    navn = get_nonempty_input("Hva heter du?")

    questions = [
        "Hva er hovedstaden i Norge?",
        "Hva er 2 + 2?",
        "Hvem er presidenten i USA nå? (Fult navn)",
        "Hvor mange KM er en Mil",
        "Hva er 5 ganger 3"
    ]
    
    answers = [
        "Oslo",
        "4",
        "Donald Trump",
        "10",
        "15"
    ]
    
    poeng = 0
    
    for i in range(len(questions)):
        user_answer = get_nonempty_input(questions[i] + " ").lower()
        if user_answer == answers[i].strip().lower():
            print("Riktig!")
            poeng += 1
        else:
            print("Feil!")

    print(f"Gratulerer, \n{navn} Du fikk {poeng} av {len(questions)} poeng.")