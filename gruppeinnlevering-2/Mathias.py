import time
#Tillit og Fremdrift er lagt in som gjeldende poengsystem - Brukes for å måle prosjektets fremdrift
tillit = 0
fremdrift = 0

print("Prosjektleder Erling sitter i saksa. Han har fått flere potensielle konflikter han må løse. Lille Erling føler at verden er imot han. Kan du hjelpe han?")
#svar = input brukes for å ta imot brukerens svar
svar = input("Vil du hjelpe Erling? (ja/nei): ") 
if svar == "ja":
    print("Du er en god venn! :)")
    #timesleep brukes for å lage pause i spillet. 
    time.sleep(3)
#if/elif/else brukes for å lage en if-setning som tar imot svar fra brukeren.
elif svar == "nei":
    print("Stakkars Erling! Da må han klare seg selv :'(.")
else:
    print("Ugyldig svar! Du må skrive ja eller nei.")
#svar == "ja" brukes for å sjekke om brukeren har skrevet ja. Hvis ja, fortsetter spillet.
if svar == "ja":
    #print ligger i en if-setning for å skrive ut tekst til brukeren. print() brukes for å lage en tom linje mellom tekstene.
    print()
    print("Plutselig hører du en merkelig lyd fra møterommet...")
    print("Du kjenner spenningen stige. Følelsene er i full sving!")
    #Symboler som musikknoter er limt inn for å lage en mer dramatisk effekt.* er for å lage en effekt som viser at musikken starter.
    print("🎵 *CUE BOSS MUSIC* 🎵")
    print("Å NEI! EN KONFLIKT HAR DUKKET OPP!")
    print()
   
    time.sleep(5)
    
    print("--- Konflikt mellom SILJE OG ELIAS ---")
    #--- brukes for å lage en visuell effekt som viser at konflikten starter.
    print("Silje og Elias krangler om medborgerportalen.")
    print("Silje vil ha et brukervennlig design, mens Elias er bekymret for sikkerheten og budsjettet.")
    print("Det som startet som en faglig uenighet, har nå blitt personlig. Emosjonene har tatt overhånd, og begge parter trekker inn andre i konflikten sin.")
    print("Erling skjønner at han må gjøre noe før hele prosjektgruppen blir påvirket.")
    print("Konfliktens intensitet begynner å stige...")
    
    time.sleep(8)
    
    print("Hva vil du gjøre?")
    print("1. Snakke med Silje og Elias hver for seg.")
    print("2. Samle gruppen til en åpen diskusjon.")

    valg1 = input("Velg 1 eller 2: ")
    if valg1 == "1":
        #valg1 == "1" brukes for å sjekke om brukeren har skrevet 1. Hvis ja, fortsetter spillet.
        print("Erling bestemmer seg for å snakke med Silje og Elias hver for seg.")
        print("Men hvordan skal han få dem til å bli enige? Erling må velge en strategi:O")

        time.sleep(2)

        print("1. Ettergivenhet – en av partene må gi etter.")
        print("2. Kompromiss – begge parter må gi litt etter.")

        strategi1 = input("Velg 1 eller 2: ")
        #velg 1 eller 2 brukes for å sjekke om brukeren har skrevet 1 eller 2. Hvis ja, fortsetter spillet.

        if strategi1 == "1":
            tillit -= 2
            fremdrift += 1
            #poengsystemet i bruk for å måle prosjektets fremdrift. Tillit og fremdrift brukes for å måle prosjektets fremdrift.
            
            time.sleep(3)
            
            print("Du har valgt at Silje må velge å gi etter.")
            print("Konflikten dempes når Erling velger å prioritere Elias sitt forslag.")
            print("Silje føler seg ikke hørt, og understreker at dette er en feil. ")
            print("Dette skal dere betale for!>:( - sier hun.")

        elif strategi1 == "2":
            tillit -= 1
            fremdrift += 1

            time.sleep(3)
            
            print("Silje og Elias inngår et kompromiss.")
            print("Begge må gi avkall på noen av ønskene sine. Begge føler at Erling er litt redd for å skuffe.")
            print("Prosjektet går videre, men konflikten er ikke helt løst. og Erling har mistet litt respekt.")

        else:
            print("Ugyldig valg!")

    elif valg1 == "2":
        tillit += 2

        time.sleep(3)

        print("Erling samler gruppen til en åpen plenumssamtale.")
        print("Silje og Elias får forklare sine synspunkter.")
        print("Gjennom problemløsning finner de en felles løsning.")
        print("Tilliten styrkes, og begge blir enig om å skape en løsning som vil revolusjonere medborgerportalen.")
        print("Denne gangen var en åpen samtale akkurat det gruppen trengte. Men vil samme strategi fungere neste gang?")
    else:
        print("Ugyldig valg!")
        #merkes ugyldig valg hvis brukeren skriver noe annet enn 1 eller 2.
    print()
    
    time.sleep(3)

    print("Erling trekker pusten dypt.")
    print("Endelig litt fred og ro på kontoret...")

    time.sleep(4)

    print("Men vent litt...")
    
    time.sleep(2)
    
    print("Hører du det?")
    
    time.sleep(3)

    print("NEI. IKKE IGJEN.")
    print("🎵 *BOSS MUSIC INTENSIFIES* 🎵")

    time.sleep(3)

    print()
    print("--- KONFLIKT 2: HAMDI VS. HALLGEIR ---")
    print("Hamdi fra kulturavdelingen og Hallgeir, innbyggerrepresentanten, har havnet i en faglig uenighet.")
    print("Konfliktskye Erling trenger deg igjen. Hva skal han gjøre nå da?")
    print("Hamdi mener kommunen må ha kontroll over innholdet i medborgerportalen.")
    print("Hallgeir mener innbyggerne må få diskutere fritt og komme med egne innspill.")

    time.sleep(6)

    print("Begge har gode argumenter, men de klarer ikke å bli enige.")
    print("Erling stirrer nervøst ned i kaffekoppen sin.")
    
    time.sleep(2)
    
    print()
    print("Hvordan skal Erling håndtere uenigheten mellom Hamdi og Hallgeir?")
    print("1. Snakke med Hamdi og Hallgeir hver for seg.")
    print("2. Samle Hamdi og Hallgeir til en plenumssamtale.")

    valg2 = input("Velg 1 eller 2: ")
    #Nytt valg, derfor valg2. 

    time.sleep(3)

    if valg2 == "1":
        tillit -= 2
        fremdrift -= 1

        time.sleep(3)
        
        print("Erling velger individuelle samtaler.")
        print("Han bestemmer seg for å bruke ad hoc-løsninger.")
        print("Planen er enkel: Ta problemene når de dukker opp. Analyse? Hvem har tid til sånt?")

        time.sleep(3)

        print("Erling snakker først med Hamdi, og deretter med Hallgeir.")
        print("Han lover begge at han skal se på saken.")

        time.sleep(3)

        print("Men Erling har egentlig ingen plan...")
        print("Han har bare utsatt problemet.")

        time.sleep(4)

        print("PLUTSELIG begynner Hamdi og Hallgeir å krangle igjen! Denne gangen med mer følelse.")
        print("Begge mener Erling har gitt dem rett.")
        print("Konflikten eskalerer, og Erling angrer på at han ikke tok seg tid til å analysere situasjonen.")

        time.sleep(2)

        print("Erling stirrer tomt ut i luften. Han har allerede valgt denne strategien. Det er forseint nå.")
    if valg1 == "1" and strategi1 == "1" and valg2 == "1":
        #and brukes for å sjekke om flere betingelser er sanne samtidig. Hvis ja, printes en melding.
        print()
        
        time.sleep(3)
        
        print("GRATULERER! DU HAR NÅ KLART Å GJØRE BEGGE KONFLIKTENE VERRE!")
        print("Silje planlegger hevn, Hamdi og Hallgeir krangler fortsatt, og Erling har begynt å oppdatere CV-en sin.")

        time.sleep(3)

        print("Erling ser mistenksomt på deg...")
        print("Du er sikker på at du er her for å HJELPE meg?")

    elif valg2 == "2":
        
        time.sleep(3)
        
        print("Erling bestemmer seg for å samle Hamdi og Hallgeir til en plenumssamtale.")
        print("Begge får forklare sitt syn på hvordan medborgerportalen skal fungere.")

        time.sleep(2)

        print("Men nå må Erling velge hvordan han skal lede samtalen...")
        time.sleep(3)

        print("1. Ta seg ekstra tid til problemløsning og finne en felles løsning.")
        print("2. La flertallet bestemme, slik at arbeidet kan komme i gang igjen.")

        strategi2 = input("Velg 1 eller 2: ")

        if strategi2 == "1":
            tillit += 2
            
            time.sleep(3)
            
            print("Erling bestemmer seg for å bruke litt ekstra tid på konflikten.")
            print("Hamdi og Hallgeir får diskutere ideene sine grundig.")

            time.sleep(3)

            print("Og utrolig nok... DET FUNGERER!")
            print("De finner en løsning som ivaretar både kommunens behov for kontroll og innbyggernes ønske om åpen dialog.")
            print("Denne gangen gjorde litt ekstra tid susen. Samarbeidet styrkes!")
            if valg1 == "2":
                print()
                
                time.sleep(4)
                
                print("🏆 WOW! DU ER JO EN KONFLIKTHÅNDTERINGSLEGENDE!")
                #pokal-emoji limt inn for å lage en visuell effekt som viser at brukeren har valgt den beste løsningen sålangt.
                print("Du har valgt den beste løsningen i begge konfliktene!")
                print("Erling vurderer seriøst å ansette deg som personlig rådgiver.")

                time.sleep(3)

                print("To plenumssamtaler, to suksesser! Du begynner kanskje å tro at du har knekt konfliktkoden?")

        elif strategi2 == "2":
            tillit -= 1
            fremdrift += 1
            
            time.sleep(3)
            
            print("Erling ser på klokken. Prosjektet må jo komme videre!")
            print("Han bestemmer seg for å la flertallet avgjøre saken.")

            time.sleep(3)

            print("Avstemningen er over. Endelig kan arbeidet fortsette!")
            print("Men det viser seg raskt at ideene ikke fungerer særlig godt sammen.")
            print("Gruppens evne til å finne gode løsninger svekkes, og flere føler at innspillene deres ikke ble tatt på alvor.")

            time.sleep(2)

            print("Erling sukker. Han vant avstemningen, men kanskje tapte han diskusjonen?")
            print("Hvordan kan jeg virkelig ha medborgerportalen på den kommunale nettsiden, og folkemøtene på Leos lekeland🤔")

        else:
            print("Ugyldig valg! Du må skrive 1 eller 2.")
    
    print()
    
    time.sleep(5)

    print("Erling synker ned i kontorstolen sin.")
    print("To konflikter senere er han fortsatt prosjektleder. På mirakuløst vis.")

    time.sleep(3)

    print("Men det er fortsatt én utfordring igjen...")
    
    time.sleep(4)

    print("🎵 *FINAL BOSS MUSIC* 🎵")
    print()
    print("--- EPISODE 3: KAMPEN OM MOTIVASJONEN ---")

    time.sleep(3)

    print("Prosjektgruppen begynner å merke presset.")
    print("Den første prototypen skal leveres om bare tre uker.")
    print("Noen er slitne etter konfliktene, mens andre er utålmodige etter å komme videre.")

    time.sleep(4)

    print("Erling vet at han må gjøre noe for å bevare motivasjonen.")
    print("Men hva skal han prioritere?")
    time.sleep(3)

    print()
    print("DET SISTE VALGET!")
    print("1. Relasjonsbygging – styrke tilliten og samarbeidet i gruppen.")
    print("2. Effektivitet og fremdrift – prioritere arbeidet med prototypen.")

    valg3 = input("Velg 1 eller 2: ")

    if valg3 == "1":
        tillit += 2
        fremdrift -= 1
        
        time.sleep(3)
        
        print("Erling bestemmer seg for å investere tid i relasjonsbygging.")
        print("Gruppen setter av tid til samtaler og aktiviteter som styrker tilliten.")

        time.sleep(3)

        print("Kommunikasjonen blir bedre, og arbeidsmoralen stiger.")
        print("Men klokken tikker... Prototypen bygger dessverre ikke seg selv!")

    elif valg3 == "2":
        tillit -= 1
        fremdrift += 2

        time.sleep(3)

        print("Erling bestemmer seg for å prioritere effektivitet og fremdrift.")
        print("Alle får beskjed om å konsentrere seg om prototypen.")

        time.sleep(3)

        print("Tastaturene gløder! Utviklingsarbeidet skyter fart!")
        print("Men eventuelle uløste konflikter forsvinner ikke bare fordi folk jobber raskere...")

    else:
        print("Ugyldig valg! Du må skrive 1 eller 2.")
    
    print()
    
    time.sleep(3)

    print("FINAL BOSS MUSIC FADES OUT...")
    print()
    print("Tre uker senere...")

    time.sleep(4)

    print()
    print("--- RESULTATET AV DINE BESLUTNINGER ---")
    print("Tillit:", tillit)
    print("Fremdrift:", fremdrift)

    time.sleep(3)

    if tillit >= 3 and fremdrift >= 0:
        print()
        print("--- SLUTT 1: ERLING HAR REDDET PROSJEKTET! ---")
        print("Tillit og kommunikasjon er gjenopprettet i gruppen.")
        print("Konfliktene er håndtert på en måte som styrker samarbeidet.")

        time.sleep(3)

        print("PROTOTYPEN LEVERES I TIDE!")
        print("Gruppen beveger seg fra storming til norming.")
        print("Erling kan endelig senke skuldrene. Kanskje prosjektledelse ikke var så dumt likevel?")

        time.sleep(3)

        print("Du har reddet prosjektet! Dette har du greie på! Elon Musk approves👍")
    elif tillit <= -3 or fremdrift <= -2:
        print()
        print("--- SLUTT 3: PROSJEKTET ER I FARE! ---")
        print("Konfliktene har svekket samarbeidet og arbeidsmoralen.")
        print("Erling har forsøkt å holde prosjektet i gang, men problemene har hopet seg opp.")

        time.sleep(3)

        print("PROTOTYPEN ER FORSINKET!")
        print("Gruppen sitter fortsatt fast i storming-fasen.")
        print("Erling stirrer på prosjektplanen. Hvordan kunne tre uker forsvinne så fort?")

        time.sleep(4)

        print("Du burde kanskje revurdere din deltakelse i prosjekledelse! Mission Failed!")
    else:
        print()
        print("--- SLUTT 2: PROSJEKTET OVERLEVER... SÅ VIDT! ---")
        print("Noen konflikter er løst, men ikke alle er helt fornøyde.")
        print("Gruppen klarer å fortsette arbeidet, men tilliten er fortsatt sårbar.")

        time.sleep(3)

        print("Prototypen kan bli ferdig, men samarbeidet er fortsatt ustabilt.")
        print("Gruppen risikerer å falle tilbake til storming.")
        print("Erling tar en lang slurk kaffe. Han trenger ferie.")

        time.sleep(4)

        print("Du gjorde ditt beste! Det kunne vært bedre!")
        print("men likevell, Bra spilt!😊")