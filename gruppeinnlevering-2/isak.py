poeng = 0
#Koden min bruker poeng til å måle resultat til prosjektets konklusjon
#introduksjon
print("-- Erling og storming-fasen --")

print("\nErling er prosjektleder for kommunens nye medborgerportal.")
print("Prosjektet har et budkjett på 8 millioner kroner og skal vare i 15 måneder.")
print("Gruppen har jobbet i 6 uker, og den første prototypen skal være klar om 3 uker.")
print("Gruppen er nå i storming-fasen, og det har oppstått konflikter som Erling må")
print("håndtere før de går ut over projektet.")

input("\nTrykk enter for å starte..")
#input brukes til å ta imot svar fra brukeren. 
#Beslutningspukt 1

print("\n-- Beslutningspunkt 1: Silje og Elias --")
#(\n) betyr new line og det lager en linje mellomrom fra forrige linje til linjen med (\n)

print("Silje er en ekstern UX/UI-designer som er opptatt av brukervennlighet og visuelt design.")
print("Hun har kommet i konflikt med Elias, som er IT-rådgiver i kommunens IT-avdeling og legger")
print("stor vekt på teknisk sikkerhet og kostnadskontroll.")
print("Silje mener at løsningen Elias foreslår, vil begrense brukeropplevelsen")
print("og gjøre det vanskeligere å utvikle nye løsninger.")
print("Elias mener på sin side at Siljes forslag er lite realistisk,")
print("og kan føre til sikkerhetsutfordringer og vil bli for dyrt å gjennomføre.")

print("\na) Erling skal snakke med Silje og Elias hver for seg")
print("b) Samle gruppen til en plenumsamtale")

valg1 = input("Hva gjør Erling nå? (a/b): ").strip().lower()
#(.strip().lower()) strip fjerner mellomrom før og etter input, og lower gjør alle bokstavene små.
    
if valg1 == "a":
    print("\na) Erling snakker med Silje og Elias hver for seg")
    print("a) Få den ene parten til å gi etter for den andres forslag.")
    print("b) Erling skal gjennomføre individuelle samtaler og få partene til å inngå et kompromiss")

    valg1b = input("Hva prøver Erling å oppnå? (a/b): ").strip().lower()
    

    if valg1b == "a":
        print("\nKonflikten roes ned på kort sikt, men den ga etter er fortsatt misførnøyd. Uenigheten kan fortsatt oppstå igjen.")
        poeng += 0 

    elif valg1b == "b":
        print("Projektet kommer videre, men ingen er helt fornøyde.")
        poeng += 1


    else:
        print("\nErling får ikke til å bestemme seg, og derfor fortsetter konfklikten.")
        poeng += 0

elif valg1 == "b":
    print("Erling samler gruppen til en diskusjon hvor Silje og Elias må forklare sine synspunkter.")
    print("De finner en løsning som ivaretar begges ønsker.")
    print("Konflikten går tilbake til å handle om saken og tilliten i gruppen styrkes.")
    poeng += 2

else:
    print("\nErling får ikke til å bestemme seg, og derfor fortsetter konfklikten.")
    poeng += 0


input("\nTrykk enter for å fortsette..")


#beslutnings punkt 2

print("\n-- Beslutningspunkt 2: Hamdi og Hallgeir --")
print("Hamdi ønsker å bruke kommunens eksisterende plattform for å ha bedre kontroll over digitale folkemøter.")
print("Hallgeir ønsker en mer åpen løsning der innbyggerne kan delta aktivt og komme med egne innspill.")
print("Hallgeir og Hamid er uenige om hvordan innbyggerne skal kunne delta i folkemøter,")
print("og Erling merker at uenigheten vokser.")

print("\na) Samle Hamdi og Hallgeir til et felles møte")
print("b) Bare vente og la dem løse uenigheten selv")

valg2 = input("Hva gjør Erling nå? (a/b): ").strip().lower()

if valg2 == "a":
    print("\nErling samler Hamdi og Hallgeir til et møte hvor begge får forklare sine synspunkter.")
    print("De blir enige med å bruke kommunens eksisterende plattform, men med større mulighter")
    print("for innbyggere til å komme med innspill.")
    print("Konflikten løses, og det styrker gruppens sammarbeid.")
    poeng += 2

elif valg2 == "b":
    print("\nErling lar Hamdi og Hallgeir forsøke å løse uenigheten selv.")
    print("Dette sparer tid, men uenigheten blir ikke løst.")
    print("Hamdi og Hallgeir velger å legger uenigheten til side foreløpig, for å fokosere på prototypen.")
    poeng += 0

else:
    print("Erling får ikke til å bestemme seg, og derfor fortsetter uenigheten.") 
    poeng += 0

input("\nTrykk enter for å fortsette..")

#beslutnings punkt 3

print("\n-- Beslutningspunkt 3: Motivasjon i teamet --")
print("Erling må bestemme om han skal prioitere relasjonene i gruppen eller fremdriften mot prototypen.")

print("\na) Prioritere relasjonsbygging")
print("b) Fremdriften mot prototypen")

valg3 = input("Hva gjør Erling? (a/b): ").strip().lower()

if valg3 == "a":
    print("\nErling setter av tid til samtaler som skal styrke tilliten mellom medlemene. Gruppen for bedre kommunikasjon")
    print("og arbeidsmoral, som, gjør samarbeide mer effektivt.")
    poeng += 2

elif valg3 == "b":
    print("\nErling velger å prioritere arbeidet med prototypen fremfor relasjonsbygging.")
    print("Tilliten og arbeidsmoralen svekkes dersom konfliktene vedvarer, noe som kan føre til lavere produktivitet.")
    poeng += 0 

else:
    print("Erling får ikke til å bestemme seg, og motivasjon i teamet synker.") 
    poeng += 0

input("\nTrykk enter for å se resultatet..")

#avslutning
print("Resultat")

if poeng >= 5:
#(>=) dette tegnet sier betyr om poengsummen enten er større eller lik som poengsummen(5), så skal følgene kode printes.

    print("Utfall 1 - Tilitt gjenopprettes, og gruppen går videre til norming.")
    print("\nErling tok tak tidlig og hadde åpen kommunikasjon med teamet.")
    print("Konflikten mellom Silje og Elias handler nå om saken, ikke personene,")
    print("og Hamdi og Hallgeir har funnet en felles løsning. prototypen blir ferdig, og teamet går fra storming til norming.")

elif poeng >= 3:
    print("Utfall 2 - Koflikten blir delvis løst, men relasjonene er sårbare")
    print("\nNoen konflikter er løst, men løsningene bygger på kompromisser.")
    print("Tilitten er svekket, og gruppen kan falle tilbake til storming.")

else:
    print("Utfall 3 - Prosjektet mister samhold og forsinkes")
    print("\nKonfliktene er ikke løst, og Erling griper ikke inn.")
    print("Gruppen står fast i storming-fasen, og prototypen blir forsinket.")

print(f"\nErling fikk {poeng} av 6 mulige poeng.")
#(f) f-stringen forklarer at variabler kan plasseres inn i teksten.

