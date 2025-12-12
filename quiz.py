#Copyright Håkon Nysveen 2025

def krev_svar(prompt): #def er starten av en funksjon i py    #krev_svar er navnet på funksjonen som gjør så brukeren må skrive et svar, denne kan kalles hva som helst siden den er kun et navn
    while True:
        answer = input(prompt).strip()
        if answer !="": 
           return answer
        print ("Du må skrive noe før du kan gå videre!")
 
while True:
    navn = krev_svar("Hva heter du?")

    questions = [
        "Hva er hovedstaden i Norge?",
        "Hva er 2 + 2?",
        "Hvem er presidenten i USA nå? (Fult navn)",
        "Hvor mange KM er en Mil",
        "Hva er 5 ganger 3"
    ]
    
    answers = [
        ["Oslo"],
        ["4", "fire"] ,
        ["Donald Trump"],
        ["10", "ti"],
        ["15", "femten"]
    ]
    
    poeng = 0
    
    for i in range(len(questions)):
        user_answer = krev_svar(questions[i] + " ").lower()
        if user_answer in [a.lower() for a in answers[i]]:
            print("Riktig!")
            poeng += 1
        else:
            print("Feil!")

    print(f"Gratulerer {navn}, Du fikk {poeng} av {len(questions)} poeng. \nTakk for at du tok quizzen!")