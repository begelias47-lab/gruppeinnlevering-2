#david.py - Erlings utfordringer (IS-118, gruppeinnlevering 2)
# Interaktiv historie: spilleren er Erling og tar tre beslutninger.
# Valgene lagres som poeng, og summen avgjør hvilket av tre utfall man får.
 
# INTRODUKSJON

print("=== ERLINGS UTFORDRING ===")
print()
print("Det har gått seks uker siden Erling samlet prosjektteamet")
print("som utvikler kommunens nye digitale medborgerportal.")
print("Teamet er i storming-fasen, og første prototype skal være")
print("klar om tre uker.")
print()
print("To konflikter har tatt plass:")
print("- Silje (UX/UI) og Elias (IT) er uenige om teknologi og design.")
print("- Hamdi (kultur) og Hallgeir (bruker) er uenige om folkemøter.")
print()
print("Du er Erling. Svar med A eller B ved hvert valg.")
print()

poeng = 0

#Beslutningspunkt 1 - Silje og Elias

print("--- BESLUTNING 1: Konflikten mellom Silje og Elias ---")
print("Diskusjonene blir stadig mer emosjonelle. Hva gjør du?")
print("A: Samle gruppen til en åpen diskusjon (plenum)")
print("B: Ta individuelle samtaler og be dem inngå et kompromiss")

# Presenterer valget til spilleren og lagrer det i variabelen valg1.
# Spør spilleren om valget. .strip() fjerner mellomrom og .upper() gjør
# svaret til store bokstaver, slik at "a" også blir "A" i if-testen under.
valg1 = input("Ditt valg (A/B): ").strip().upper()
 
if valg1 == "A":
    print("Silje og Elias forklarer synspunktene sine for hele gruppen.")
    print("Sammen finner dere en løsning som tar hensyn til både")
    print("brukeropplevelse, sikkerhet og kostnader. Tilliten styrkes,")
    print("men møtet tok mye tid.")
    poeng = poeng + 2
elif valg1 == "B":
    print("Du snakker med dem hver for seg og de inngår et kompromiss.")
    print("Arbeidet går videre, men ingen er helt fornøyde, og den")
    print("underliggende konflikten er ikke løst.")
    poeng = poeng + 1
else:
    # Ugyldig input: historien fortsetter, men Erling gjør ingenting.
    print("Erling nøler og gjør ingenting. Uenigheten mellom Silje")
    print("og Elias fortsetter å gnage i bakgrunnen.")
    valg1 = "ingen"
 
print()


 #Beslutningspunkt 2 - Hamdi og Hallgeir

print("--- BESLUTNING 2: Konflikten mellom Hamdi og Hallgeir ---")
print("Hamdi vil bruke kommunens plattform. Hallgeir vil ha et åpnere system.")
print("A: Ta initiativ til et felles møte for å avklare uenigheten")
print("B: Vente og la dem løse det selv")

# Samme som i beslutningspunkt 1: spilleren velger A eller B, og valget lagres i variabelen valg2.
 
valg2 = input("Ditt valg (A/B): ").strip().upper()
 
if valg2 == "A":
    print("Hamdi og Hallgeir blir enige om å bruke kommunens plattform,")
    print("men med flere muligheter for innspill fra innbyggerne.")
    print("Teamet får en tidlig suksess som styrker samarbeidet.")
    poeng = poeng + 2
elif valg2 == "B":
    print("Du avventer. Det sparer tid nå, men uenigheten er ikke løst")
    print("og kan blusse opp senere.")
    # B gir 0 poeng
else:
    print("Erling blir revet med av andre ting, og saken blir liggende.")
    print("Frustrasjonen mellom Hamdi og Hallgeir vokser.")
    valg2 = "ingen"
 
print()
# Valg A (felles møte) gir 2 poeng fordi teamet får en tidlig suksess som styrker samarbeidet.
# Valg B (avvente) gir 0 poeng fordi uenigheten ikke løses, og kan blusse opp senere.
# Ugyldig input behandles som ingen valg.
 

#Beslutningspunkt 3 - Teamets fremdrift/ Motivasjon i teamet

print("--- BESLUTNING 3: Motivasjonen i teamet ---")
print("Prototypen skal leveres om tre uker. Hva prioriterer du?")
print("A: Sette av tid til relasjonsbygging og tillit")
print("B: Prioritere fremdrift og leveranser")

# Samme utføring slik som i de to første beslutningspunktene.
 
valg3 = input("Ditt valg (A/B): ").strip().upper()
 
if valg3 == "A":
    print("Teamet bruker tid på å bli bedre kjent. Kommunikasjonen")
    print("og arbeidsmoralen blir bedre, selv om prototypen får")
    print("litt mindre utviklingstid.")
    poeng = poeng + 2
elif valg3 == "B":
    print("Teamet jobber hardt med prototypen, men de uløste")
    print("konfliktene blir liggende og tilliten svekkes.")
    # B gir 0 poeng
else:
    print("Erling kommer ikke med noen tydelig retning, og")
    print("teamet blir usikkert på hva som er viktigst.")
    valg3 = "ingen"
 
print()
# A prioriterer kommunikasjon og forbedret arbeidsmoral og gir 2 poeng.
# B prioriterer prototypen og gir 0 poeng, fordi konflikten blir liggende og tilliten svekkes.


 #Avslutning av spiller - utfall basert på poengsum, og valgene spilleren har gjort.


print("=== PROSJEKTETS UTFALL ===")
print(f"Dine valg: {valg1}, {valg2}, {valg3} (poeng: {poeng} av 6)")
print()
 
if poeng >= 5:
    # Utfall 1
    print("UTFALL 1: Tillit gjenopprettes")
    print("Konfliktene handler nå om saken, ikke personene. Prototypen")
    print("er klar i tide, og teamet går videre til norming-fasen")
    print("med tydeligere roller og økt tillit.")
elif poeng >= 3:
    # Utfall 2
    print("UTFALL 2: Delvis løst, men sårbare relasjoner")
    print("Prototypen blir levert, men løsningene bygger på kompromisser")
    print("ingen er helt fornøyde med. Konfliktene kan blusse opp igjen,")
    print("og teamet kan falle tilbake til storming-fasen.")
else:
    # Utfall 3
    print("UTFALL 3: Samholdet svekkes, prosjektet forsinkes")
    print("Konfliktene er ikke løst, og teamet opplever at Erling ikke")
    print("griper inn. Arbeidsmoralen faller, teamet blir værende i")
    print("storming-fasen, og prototypen blir forsinket.")
 
print()
print("Takk for at du spilte!")