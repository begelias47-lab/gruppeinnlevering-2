# IS-118 Gruppeoppgave 2 - Erlings utfordringer
#Forfatter: Elias Beg
#---------Varibeles that store the player's choices ------------
trust_score = 0  # points from choices, decides the ending 
choice_1 = ""    # Decision 1: "A" or "B"
choice_2 = ""    # Decision 2: "A" or "B"
choice_3 = ""    # Decision 3: "A" or "B"



#----------helper: asks A or B until the input is valid ----------
def ask(option_a,  option_b):
    print(" A)" + option_a)
    print(" B)" + option_b)
    while True:
        answer = input("Ditt valg (A/B): ").strip().upper()
        if answer == "A" or answer == "B":
            return answer
        print("ugyldig valg. Skriv Aller B.")



#--------introduction -----------
print("=" * 50)
print("ERLINGS UTFORDDRING")
print("=" * 50)
print("Du er Erling, prosjektleder for kommunens nye medborgerportal.")
print("Det er gått seks uker, og teamet er i storming-fasen.")
print("Silje (UX) og Elias (IT) er uenige om teknologi og design.")
print("Hamdi og Hallgeir er uenige om digitale folkemøter.")
print("Første prototype skal være klar om tre uker.")
input("\nTrykk Enter for å starte...")

# ---------- Decision 1: Silje vs Elias ----------
print("\n--- BESLUTNING 1: Silje og Elias ---")
print("Konflikten har gått fra sakskonflikt til personkonflikt.")
print("Hva gjør Erling?")
choice_1 = ask("Snakker med dem hver for seg og søker kompromiss",
               "Tar det opp i plenum og løser problemet sammen")

if choice_1 == "A":
    print("\nTemperaturen synker, og arbeidet går videre.")
    print("Men ingen er helt fornøyde, og konflikten ligger under overflaten.")
    trust_score = trust_score + 1
else:
    print("\nDiskusjonen blir tøff, men fokus flyttes fra personene til saken.")
    print("Teamet finner en løsning som ivaretar brukeropplevelse, sikkerhet og kost.")
    print("Det tar mer tid, men tilliten styrkes.")
    trust_score = trust_score + 2

# ---------- Decision 2: Hamdi vs Hallgeir ----------
print("\n--- BESLUTNING 2: Hamdi og Hallgeir ---")
print("Uenigheten om folkemøter vokser. Hamdi vil ha en kontrollert løsning,")
print("Hallgeir vil ha en åpen og dialogbasert løsning.")
print("Hva gjør Erling?")
choice_2 = ask("Kaller inn til et felles møte med problemløsning",
               "Avventer og håper de løser det selv")

if choice_2 == "A":
    print("\nBegge får forklare seg. De blir enige om å bruke kommunens plattform,")
    print("men med mer rom for innspill fra innbyggerne.")
    print("Teamet får en tidlig suksess.")
    trust_score = trust_score + 2
else:
    print("\nDu sparer tid på kort sikt, og de legger uenigheten til side.")
    print("Men konflikten er ikke løst, og frustrasjonen kan vokse senere.")
    trust_score = trust_score + 0

# ---------- Decision 3: Motivation ----------
print("\n--- BESLUTNING 3: Motivasjon i teamet ---")
# The text depends on an earlier choice, so the story feels connected
if choice_2 == "B":
    print("Spenningen mellom Hamdi og Hallgeir er fortsatt merkbar.")
else:
    print("Den tidlige suksessen har gitt teamet litt ny energi.")
print("Prototypen nærmer seg. Hva prioriterer Erling?")
choice_3 = ask("Setter av tid til relasjonsbygging og tillit",
               "Prioriterer fremdrift og leveranser")

if choice_3 == "A":
    print("\nKommunikasjonen og arbeidsmoralen blir bedre.")
    print("Du mister litt tid på prototypen, men teamet står sterkere sammen.")
    trust_score = trust_score + 2
else:
    print("\nDu får mer tid til utvikling, men uløste konflikter blir ikke tatt tak i.")
    print("Tilliten og arbeidsmoralen kan svekkes.")
    trust_score = trust_score + 0

# ---------- Summary of choices ----------
print("\n" + "=" * 50)
print("OPPSUMMERING AV DINE VALG")
print("Beslutning 1:", choice_1, "| Beslutning 2:", choice_2, "| Beslutning 3:", choice_3)
print("Tillitspoeng:", trust_score, "av 6")
print("=" * 50)

# ---------- Ending (3 possible outcomes) ----------
if trust_score >= 5:
    print("\nUTFALL 1: Tilliten gjenopprettes!")
    print("Konfliktene handler nå om saken, ikke personene.")
    print("Prototypen leveres i tide, og teamet går videre til norming-fasen.")
elif trust_score >= 3:
    print("\nUTFALL 2: Delvis løst, men sårbare relasjoner.")
    print("Prototypen blir levert, men flere er fortsatt misfornøyde.")
    print("Konfliktene kan blusse opp igjen, og teamet kan falle tilbake til storming.")
else:
    print("\nUTFALL 3: Prosjektet mister samhold og forsinkes.")
    print("Konfliktene er uløste og har eskalert.")
    print("Teamet blir stående fast i storming-fasen, og prototypen blir forsinket.")

print("\nTakk for at du spilte!")
