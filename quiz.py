#Copyright Håkon Nysveen 2025
#Prøvde å kommentere så mye som mulig for å vise at jeg forstår den, kos deg!

import sqlite3 #importerer sqlite3 
import random 
import time


con = sqlite3.connect("quiz.db") #Kobler til databasen
cur = con.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS Quiz_Highscore(id INTEGER PRIMARY KEY AUTOINCREMENT, navn TEXT NOT NULL, poeng INTEGER NOT NULL)""")

# Når jeg bruker AUTOINCREMENT her så lages det en sqlite_sequence table som husker på hvilken id som er brukt sist


def krev_svar(prompt): #def er starten av en funksjon i py    #krev_svar er navnet på funksjonen som gjør så brukeren må skrive et svar, denne kan kalles hva som helst siden den er kun et navn
    while True:
        answer = input(prompt).strip()
        if answer !="": 
           return answer
        print ("Du må skrive noe før du kan gå videre!\n")


while True:  # hoved loop for hele quizzen

    poeng = 0 # Dette er starter poeng summen og det legges på 1 per riktig spørsmål

    navn = krev_svar("Hva heter du? ")

    if not all(c.isalpha() or c.isspace() for c in navn):
        # isalpha sjekker om det brukeren skriver er kun bokstaver og ikke tall
        print("Navn kan kun inneholde bokstaver.\n")
        continue
    elif any(len(del_navn) < 2 for del_navn in navn.split()):
         # dette gjør sånn at det må være 2 eller fler bokstaver i navnet brukeren skriver, den teller ikke med mellomrom. Du har lov til å legge til etternavn, men da må det også har mer en 2 bokstaver
        print("Navn må være minst 2 bokstaver langt.\n")
        continue


    questions = [
        "Hva er hovedstaden i Norge?",
        "Hva er 2 + 2?",
        "Hvem er presidenten i USA nå? (Fult navn)",
        "Hvor mange KM er en Mil",
        "Hva er 5 ganger 3"
    ]
        
    answers = [  # om vi plasserer svarene våre inni brackets så kan vi ha fler svar alternativer per spørsmål.
        ["Oslo"],
        ["4", "fire"] , #brukeren kan skrive både med et tall og bokstaver
        ["Donald Trump"],
        ["10", "ti"],
        ["15", "femten"]
    ]


    #Her er to ektra spørsmål som er multiple choice

    questions.append("Hvilket språk brukes mest til å endre på utsene til en nettside?\nA) Python  B) HTML  C) CSS")
    answers.append(["c", "css"])
                   
    questions.append("Hvor mange megabyte er det i en gigabyte\nA) 100  B) 1000  C) 10000")
    answers.append(["b", "1000"])


    quiz = list(zip(questions, answers)) #her kobler den sammen to lister
    random.shuffle(quiz) #Denne blander rekkefølgen i listen
    questions, answers = zip(*quiz) # *quiz utpakker quiz spørsmålene og zip putter de i en pakke.


    start_tid = time.time() #Her starter tidtakingen, time er python som jobber med tid.
        

    for i in range(len(questions)):   # denne koden går gjennom alle spørsmålene i quizzen
        user_answer = krev_svar("\n" + questions[i] + "\n").lower() # her så får du ikke lov til å svare blankt så da kommer krev_svar funksjonen inn.
        if user_answer in [a.lower() for a in answers[i]]:  # denne linjen sjekker om det brukeren skrev finnes blant svarene og gjør svaret til brukeren til små bokstaver
            print("\nRiktig!") 
            poeng += 1 # Om brukeren svarer riktig så legges det på ett poeng og vi sender en print til brukeren
        else:
            print("\nFeil!") 


    slutt_tid = time.time() #Stopper tidtaking
    brukt_tid = round(slutt_tid - start_tid, 2) #Regner ut hvor mye tid, 2 er 2 desimaler


    print("----------------------------------------------------------------\n")
    print(f"Gratulerer {navn}, Du fikk {poeng} av {len(questions)} poeng. \nDu brukte {brukt_tid} sekunder.\n")
    # Her printer den og tar navnet brukeren skrev + poenget brukeren fikk

    cur.execute(
        "INSERT INTO Quiz_Highscore (navn, poeng) VALUES (?, ?)",
        (navn, poeng)
    )
    con.commit()
    # Her tar den navn og poengsumm inn i databasen hvor ?, ? er placeholders til verdiene (VALUES)


    vis_highscore = krev_svar("\nVil du se highscoren? (Ja/Nei): ").lower() #lower gjør så brukeren kan svare : JA, Ja, jA eller ja, den gjør alle bokstaver små


    #-------------------------------------

    # Denne koden som er markert ut tar DEN beste poengsummen, jeg ville lage top 3 så det gjorde jeg under

    #if vis_highscore == "ja": 
#    cur.execute("""
#        SELECT navn, poeng
#        FROM Quiz_Highscore
#        ORDER BY poeng DESC
#        LIMIT 1 
#    """) 

        # På koden over så, SELECT henter navn og poeng FROM (fra) databasen
        # ORDER BY sorterer poengene i DESC (synkende rekkefølge), altså høyeste poeng først
        # LIMIT 1 gjør så kun en bruker/spiller kan poppe opp på highscoren som brukeren ser, det er personen som fikk best score.



#    beste = cur.fetchone()

#    if beste: 
#        print("\nBESTE QUIZ SPILLER!")
#        print(f"Navn: {beste[0]}")
#        print(f"Poeng: {beste[1]}\n")

    #-------------------------------------

    # Denne koden under vil vise top 3 beste svarene på quizzen.

    if vis_highscore == "ja":
        cur.execute("""
            SELECT navn, poeng
            FROM Quiz_Highscore
            ORDER BY poeng DESC
            LIMIT 3
    """)

        topp_3 = cur.fetchall() 
        # Fetchall returnerer en liste med rader fra databasen. 

        plass = 1 
        for spiller in topp_3: # Her ser den gjennom top spillere i top 3 som fetcher fra databasen også printer
            print(f"{plass}. {spiller[0]} - {spiller[1]} poeng")  # her skriver den ut plasseringen, spiller 0 er navn spiller 1 er poeng
            plass += 1 # På plass teksten så legger den til +1 hver gang, siden vi har LIMIT 3 over så kommer det kun 3 plasser


    ny_runde = krev_svar("\nHar du lyst til å ta quizzen på nytt? (Ja/Nei): ").lower()

    if ny_runde == "ja":
        print("\nLykke til!\n")
        continue
    else:
        print("\nTakk for at du spilte!")
        break


  #  break # går ur av while loopen (ikke i bruk nå)
