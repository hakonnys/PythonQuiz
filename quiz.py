#Copyright Håkon Nysveen 2025

import sqlite3 #importerer sqlite3 

con = sqlite3.connect("quiz.db")
cur = con.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS Quiz_Highscore(id INTEGER PRIMARY KEY AUTOINCREMENT, navn TEXT NOT NULL, poeng INTEGER NOT NULL)""")

# Når jeg bruker AUTOINCREMENT her så lages det en sqlite_sequence table som husker på hvilken id som er brukt sist


def krev_svar(prompt): #def er starten av en funksjon i py    #krev_svar er navnet på funksjonen som gjør så brukeren må skrive et svar, denne kan kalles hva som helst siden den er kun et navn
    while True:
        answer = input(prompt).strip()
        if answer !="": 
           return answer
        print ("Du må skrive noe før du kan gå videre!")


 
while True:
    navn = krev_svar("Hva heter du? ")

    if not navn.isalpha(): # isalpha sjekker om det brukeren skriver er kun bokstaver og ikke tall
        print("Navn kan kun inneholde bokstaver.\n")
    elif len(navn) < 2: # dette gjør sånn at det må være 2 eller fler bokstaver i navnet brukeren skriver
        print("Navn må være minst 2 bokstaver langt.\n")
    else:
        break # break her gjør så man kan ikke komme videre uten å skrive et gyldig navn


questions = [
    "\nHva er hovedstaden i Norge?",
    "Hva er 2 + 2?",
    "Hvem er presidenten i USA nå? (Fult navn)",
    "Hvor mange KM er en Mil",
    "Hva er 5 ganger 3"
]
    
answers = [
    ["Oslo"],
    ["4", "fire"] , #brukeren kan skrive både med et tall og bokstaver
    ["Donald Trump"],
    ["10", "ti"],
    ["15", "femten"]
]
    
poeng = 0
    
for i in range(len(questions)):
    user_answer = krev_svar(questions[i] + " ").lower()
    if user_answer in [a.lower() for a in answers[i]]:
        print("\nRiktig!\n") 
        poeng += 1
    else:
        print("\nFeil!\n")
        
print("----------------------------------------------------------------\n")
print(f"Gratulerer {navn}, Du fikk {poeng} av {len(questions)} poeng. \nTakk for at du tok quizzen!")

cur.execute(
    "INSERT INTO Quiz_Highscore (navn, poeng) VALUES (?, ?)",
    (navn, poeng)
)
con.commit()

  #  break # går ur av while loopen