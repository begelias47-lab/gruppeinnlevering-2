#dette er min endelige løsning, her kan man gå alle veier og velge alle løsninger som ligger illustret i del 
#av oppgaven, gjennom beslutningpunktene får brukeren som kjører dette i terminal vinduet, mulighet til å velge hvordan Erling skal håndtere situasjonene
#her kan brukeren velge forksjellige valg som fører til ulike konsekvenser og utfall


#print() får og få ut tekst i terminalen
print("Velkommen til den interaktive historien om Erling og hans vei som prosjekt leder")
print()
print("I denne historien skal du som bruker ta valg som påvirker teamet.")
print("Hvert valg kan føre til ulike konsekvenser og utfall.")

#Her legger jeg til beslutning 1 mellom silje og elias
#og gir brukeren alternativer til hva Erling kan gjøre 
print("\n----------------------------")
print("Beslutning 1: Silje og Elias")
print("------------------------------")

#Brukeren får situasjonen og de to forskjellige valgene man kan ta
print("Erling må finne ut hvordan han skal håndtere konflikten mellom Silje og Elias.")
print("\nHva bør Erling gjøre?")
print("A. Ha individuelle samtaler")
print("B. Holde en plenumsamtale")

#Input() lar brukeren av terminal vinduet velge mellom A og B
#Variabelen valg1 lagrer svaret brukeren velger
#strip() fjerner eventuelle mellomrom og upper() gjør bokstavene til store bokstaver
valg1 = input("Velg A eller B: ").strip().upper()

#while spør brukeren på nytt dersom det blir skrevet noe annet en A eller B
#så dersom det blir skrevet noe annet enn A og B kan brukeren velge på nytt
while valg1 != "A" and valg1 != "B":
    print("Ugyldig valg. Skriv A eller B.")
    valg1 = input("Velg A eller B: ").strip().upper()

 #if her sjekker om brukeren valgte alternativ A individuelle samtaler
if valg1 == "A":
    print("\nErling velger individuelle samtaler.")
    print("Velg hvilken konsekvens du vil se:")
    print("A. Økt personlig tilfredshet")
    print("B. Lavere arbeidseffektivitet")

 #konsekvens1 variabelen her lagrer svaret til brukeren
    konsekvens1 = input("Velg A eller B: ").strip().upper()

 #Ser om brukeren velger A eller B
    while konsekvens1 != "A" and konsekvens1 != "B":
        print("Ugyldig valg. Skriv A eller B.")
        konsekvens1 = input("Velg A eller B: ").strip().upper()
 
 #hvis bruker velger alternativ A viser den konsekvensen og så utfallet
 #ved å trykke enter
    if konsekvens1 == "A":
        print("\nKonsekvens: Den personlige tilfredsheten øker.")
        input("Trykk Enter for å se utfallet...")
        print("Relasjonene i teamet kan bli bedre.")

 #Brukeren får mulighet til å se hva som kunne ha skjedd dersom det andre
 #alternative ble valgt
        se_andre = input(
            "\nVil du se hva utfallet ville blitt med alternativ B? (ja/nei): "
        ).strip().lower()

 #Hvis brukeren svarer ja vises det alternative utfallet.
        if se_andre == "ja":
            print("\nAlternativ B:")
            print("Konsekvens: Arbeidseffektiviteten blir lavere.")
            print("Utfall: Teamets arbeid kan bli forsinket.")
 
 #Hvis brukeren svarer nei velger den og ikke se det andre utfallet og
 #gå videre i den interaktive historie     
        elif se_andre == "nei":
            print("Du valgte å ikke se det andre utfallet.")

 #Her brukes elif for og håndtere det andre konsekvensvalget
    elif konsekvens1 == "B":
        print("\nKonsekvens: Arbeidseffektiviteten blir lavere.")
        input("Trykk Enter for å se utfallet...")
        print("Prosjektet kan bli forsinket til avtalt tid.")

 #Gir brukeren mulighet til å se hva som hadde skjedd dersom de valgte 
 #alternativ A
        se_andre = input(
            "\nVil du se hva utfallet ville blitt med alternativ A? (ja/nei): "
        ).strip().lower()

        if se_andre == "ja":
            print("\nAlternativ A:")
            print("Konsekvens: Den personlige tilfredsheten øker.")
            print("Utfall: Relasjonene i teamet kan bli bedre.")
        elif se_andre == "nei":
            print("Du valgte å ikke se det andre utfallet.")

#Hvis brukeren valgte alternativ B i den første beslutningen
#vil Erling håndtere konflikten med alternativ B
elif valg1 == "B":
    print("\nErling velger en plenumsamtale.")

#Brukeren må trykke enter for at konsekvensen skal vises
    input("Trykk Enter for å se konsekvensen...")
    print("Teamet får mulighet til å snakke sammen.")   
    input("Trykk Enter for å se utfallet...")
    print("Konflikten kan bli lettere å håndtere.")

#her kan brukeren se hva utfallet hadde blitt med alternativ A
    se_andre = input(
        "\nVil du se hva utfallet ville blitt med alternativ A? (ja/nei): "
    ).strip().lower()


#Brukeren kan trykke enter for å gå til neste beslutning
input("\nTrykk Enter for å gå til beslutning 2...")

#Beslutning 2: Hamdi og Hallgeir
print("\n----------------------------")
print("BESLUTNING 2: HAMDI OG HALLGEIR")
print("----------------------------")

print("Hamdi og Hallgeir er uenige om digitale folkemøter.")

print("\nHva bør Erling gjøre?")
print("A. Ha individuelle samtaler")
print("B. Ha en plenumssamtale")

#Variabelen valg2 lagrer  hvordan Erling skal håndtere uenigheten
valg2=input("Velg A eller B: ").strip().upper()

 #Kontrollerer om brukeren velger et gyldig alternativ
while valg2 != "A" and valg2 != "B":
    print("Ugyldig valg. Skriv A eller B.")
    valg2=input("Velg A eller B: ").strip().upper()

 #Hvis brukeren velger A, velger Erling og ha individuelle samtaler.
if valg2=="A":
    print("\nErling velger å ha individuelle samtaler med Hamdi og Hallgeir.")

    input("Trykk Enter for å se konsekvensen...")
    print("Konflikten eskalerer mellom Hamdi og Hallgeir.")

    input("Trykk Enter for å se utfallet...")
    print("Utfall: Konflikten blir ikke løst.")

 #Brukeren får mulighet til å se utfallet til det andre alternative
    se_andre=input(
        "\nVil du se hva utfallet kunne blitt med en plenumssamtale? (ja/nei): "
    ).strip().lower()

    if se_andre=="ja":
        print("\nAlternativ B: Plenumssamtale")
        print()
        print("Konsekvens A: Samtalen blir løsningsorientert.")
        print("Utfall: Konflikt ikke løst.")
        print()
        print("\nKonsekvens B: Teamet samarbeider om problemløsning.")
        print("Utfall: Arbeidseffektiviteten øker.")

    elif se_andre=="nei":
        print("Du valgte å ikke se de andre utfallene.")

 #Brukeren får velge mellom to mulige retninger i historien.
elif valg2=="B":
    print("\nErling velger å ha en plenumssamtale.")
    print("Velg hvilket alternativ du vil se utfallet av:")
    print("A. Hamdi og Hallgeir har en løsningsorientert samtale.")
    print("B. Hamdi og Hallgeir samarbeider om å finne en løsning.")

 #Variabelen konsekvens2 lagrer hvilken retning brukeren vil gå
    konsekvens2=input("Velg A eller B: ").strip().upper()

 #gjentar om brukeren vil skrive A eller B 
    while konsekvens2 != "A" and konsekvens2 != "B":
        print("Ugyldig valg. Skriv A eller B.")
        konsekvens2 = input("Velg A eller B: ").strip().upper()

 #Alternativ A fører til utfallet svekket løsningsevne
    if konsekvens2 == "A":
        input("\nTrykk Enter for å se utfallet...")
        print("Utfall: Teamets løsningsevne blir svekket, men kan alikavel forsette")

        se_andre = input(
            "\nVil du se hva utfallet ville blitt med alternativ B? (ja/nei): "
        ).strip().lower()

        if se_andre=="ja":
            print("\nAlternativ B: Hamdi og Hallgeir samarbeider om å finne en løsning")
            print("Utfall: Arbeidseffektiviteten øker i teamet.")

        elif se_andre=="nei":
            print("Du valgte å ikke se det andre utfallet.")

 #Alternativ B fører til at arbeidseffektiviten øker
    elif konsekvens2=="B":
        input("\nTrykk Enter for å se utfallet...")
        print("Utfall: Arbeidseffektiviteten øker.")

 #Brukeren kan velge å se utfallet av alternativ A
        se_andre=input(
            "\nVil du se hva utfallet ville blitt med alternativ A? (ja/nei): "
        ).strip().lower()

        if se_andre=="ja":
            print("\nAlternativ A: Hamdi og Hallgeir har en løsningsorientert samtale. ")
            print("Utfall: Teamets løsningsevne blir svekket.")

        elif se_andre=="nei":
            print("Du valgte å ikke se det andre utfallet.")


input("\nTrykk Enter for å gå til beslutning 3...")

#Beslutning 3
print("\n----------------------------")
print("Beslutning 3: Motivasjon")
print("----------------------------")

print("Erling må bestemme hvordan teamet skal jobbe videre.")

print("\nHva bør Erling prioritere?")
print("A. Bygge tillit i teamet")
print("B. Prioritere arbeidseffektivitet")

# Variabelen valg3 lagrer hva Erling skal gjøre
valg3=input("Velg A eller B: ").strip().upper()

while valg3 != "A" and valg3 != "B":
    print("Ugyldig valg. Skriv A eller B.")
    valg3 = input("Velg A eller B: ").strip().upper()

if valg3=="A":
    print("\nErling velger å bygge tillit i teamet.")

    input("Trykk Enter for å se konsekvensen...")
    print("Det tar mye tid og ressurser.")

    input("Trykk Enter for å se utfallet...")
    print("Arbeidsmiljøet blir bedre.")

    se_andre=input(
        "\nVil du se hva utfallet ville blitt med alternativ B? (ja/nei): "
    ).strip().lower()

    if se_andre=="ja":
        print("\nAlternativ B: Prioritere arbeidseffektivitet")
        print("Konsekvens: Arbeidsmoralen kan bli lavere.")
        print("Utfall: Arbeidsmiljøet blir svekket.")

    elif se_andre=="nei":
        print("Du valgte å ikke se det andre utfallet.")

    else:
        print("Du skrev ikke ja eller nei.")

elif valg3=="B":
    print("\nErling velger å prioritere arbeidseffektivitet.")

    input("Trykk Enter for å se konsekvensen...")
    print("Konsekvens: Arbeidsmoralen kan bli lavere.")

    input("Trykk Enter for å se utfallet...")
    print("Arbeidsmiljøet blir svekket.")

    se_andre=input(
        "\nVil du se hva utfallet ville blitt med alternativ A? (ja/nei): "
    ).strip().lower()

    if se_andre=="ja":
        print("\nAlternativ A: Bygge tillit i teamet")
        print("Konsekvens: Det krever mye tid og ressurser.")
        print("Utfall: Arbeidsmiljøet blir bedre.")

    elif se_andre=="nei":
        print("Du valgte å ikke se det andre utfallet.")

else:
    print("Du skrev ikke ja eller nei.")


#Skriver ut en overskrift før oppsumeringen starter
print("\nOppsumering av dine valg.")

#viser hvilken beslutning oppsumeringer handler om
print("\n----------------------------")
print("Beslutning 1 – Silje og Elias")
print("----------------------------")

#sjekker om brukeren valgte individuelle samtaler
if valg1=="A":
    print("Du valgte individuelle samtaler.")

 #sjekker hvilken konsekvens brukeren valgte 
    if konsekvens1=="A":
        print("Du valgte konsekvensen: Økt personlig tilfredshet.")
        print("Utfall: Forbedret arbeidsmoral.")

 #Hvis konsekvens A ikke ble valgt sjekker elif om konsekvens B ble valgt
    elif konsekvens1=="B":
        print("Du valgte konsekvensen: Lavere effektivitet.")
        print("Utfall: Konflikten ble ikke løst.")

#hvis valg1 ikke er A sjekker den om brukeren valgte B
elif valg1=="B":
    print("Du valgte plenumsamtale.")
    print("Du valgte konsekvensen: Lavere effektivitet.")
    print("Utfall: Åpen kommunikasjon.")

print("\nBESLUTNING 2 – Hamdi og Hallgeir")

if valg2=="A":
    print("Du valgte individuelle samtaler.")
    print("Du fikk konsekvensen: Konflikteskalering.")
    print("Utfall: Konflikten ble ikke løst.")

#hvis brukeren valgt B viser programmet plenumsamtale
elif valg2=="B":
    print("Du valgte plenumsamtale.")

#Sjekker om brukeren valgte konsekvens A
    if konsekvens2=="A":
        print("Du valgte konsekvensen: Løsningsorientert samtale.")
        print("Utfall: Svekket løsningsevne.")

#Hvis ikke konsekvens A ble valgt, sjekker den konsekvens B
    elif konsekvens2=="B":
        print("Du valgte konsekvensen: Problemløsning.")
        print("Utfall: Økt arbeidseffektivitet.")


#Oppsumering av beslutning 3
print("\nBESLUTNING 3 – BEVARE MOTIVASJONEN")

if valg3=="A":
    print("Du valgte å bygge tillit.")
    print("Du fikk konsekvensen: Ressurskrevende.")
    print("Utfall: Forbedret arbeidsmiljø.")

elif valg3=="B":
    print("Du valgte å øke effektiviteten.")
    print("Du fikk konsekvensen: Lavere arbeidsmoral.")
    print("Utfall: Svekket arbeidsmiljø.")

input("\nTrykk Enter for å se hvordan historien ender...")

#sjekker om valgene førte til positiv slutt
if (
    valg1=="B"
    and valg2=="B"
    and konsekvens2=="B"
    and valg3=="A"
):
    #skriver ut resultatet dersom det matcher med brukerens valg
    print("\nPositivt slutt – Teamet finner sammen!")
    print("Erling bidro til åpen kommunikasjon og gode løsninger.")
    print("Arbeidseffektiviteten økte, og arbeidsmiljøet ble forbedret.")

elif (
    (valg2=="A" or (valg2 =="B" and konsekvens2=="A"))
    and valg3=="B"
):
    print("\nNegativ slutt - konfliktene påvirker teamet negativt")
    print("Konfliktene ble ikke håndtert på en god måte.")
    print("Arbeidsmoralen og arbeidsmiljøet ble svekket.")

else:
    print("\nBlandet slutt noe gikk bra men ikke alt!")
    print("Noen av valgene bidro positivt til teamet, mens andre valg skapte utfordringer.")
    print("Teamet har fortsatt ting og jobbe med for å få ett bedre arbeidsmiljø.")


#pause før de andre alternativene
input("\nTrykk Enter for å se hva som kunne skjedd hvis du valgte annerledes...")

print("\nHva om du hadde valgt annerledes?")

#Beslutning 1
print("\nBeslutning 1, Silje og Elias")

if valg1=="A":
    print("Du valgte individuelle samtaler.")
    print("Hvis Erling hadde valgt plenumsamtale, ville utfallet ha vært åpen kommunikasjon.")
else:
    print("Du valgte plenumsamtale.")
    print("Hvis du hadde valgt individuelle samtaler, kunne konsekvensen av det ha vært økt personlig tilfredshet eller lavere effektivitet.")


print("\nBeslutning 2, Hamdi og Hallgeir")

if valg2=="A":
    print("Du valgte individuelle samtaler.")
    print("Hvis du hadde valgt plenumsamtale, kunne konsekvensen blitt løsningsorientert samtale eller problemløsning.")

elif valg2=="B":
    print("Du valgte plenumsamtale.")

    if konsekvens2=="A":
        print("Du valgte konsekvensen: Løsningsorientert samtale.")
        print("Utfallet av det ble svekket løsningsevne.")
        print("Hvis du i stedet hadde valgt problemløsning, kunne arbeidseffektiviteten økt.")

    elif konsekvens2=="B":
        print("Du valgte konsekvensen: problemløsning.")
        print("Utfallet ble økt arbeidseffektivitet.")
        print("Hvis du i stedet hadde valgt løsningsorientert samtale kunne løsningsevnen blitt svekket.")

print("\nBesltuning 3, bevare motivasjonen i teamet.")

if valg3=="A":
    print("Du valgte å bygge tillit.")
    print("Hvis du hadde valgt å øke effektiviteten kunne arbeidsmoralen blitt lavere og arbeidsmiljøet blit dårligere.")

elif valg3=="B":
    print("Du valgte å øke effektiviteten.")
    print("Hvis du hadde valgt å bygge tillit kunne arbeidsmiljøet blitt bedre, men det hadde krevd mer tid og ressurser.")

print()
print("Den interaktive Historien er ferdig og du er i mål!")
print("Takk for at du spilte gjennom historien.")