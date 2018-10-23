# Workshop MicroPython

Voordat we aan de slag kunnen gaan met MicroPython moeten we eerst zorgen dat we kunnen inloggen op het bordje. Dit kan op verschillende manieren.

## MAC OS gebruikers

1. driver [downloaden](https://www.silabs.com/documents/public/software/Mac_OSX_VCP_Driver.zip) voor MAC OS
2. driver installeren, open de zip file, je ziet dan onderstaande files:
![uitgepakte driver bestand screenshot](images/image001.png)
3. Klik vervolgens op de SiLabsUSB....dmg
4. Klik vervolgens op **"Agree"**
5. Vervolgens verschijnt het onderstaande screenshot:
![uitgepakte driver bestand screenshot2](images/image002.png)
6. Klik vervolgens op de Silicon Labs VCP Driver.pkg
7. Druk constant op **"Continue"** tot het onderstaande screenshot:
![installatie mac driver gelukt](images/image002.png)
8. Nu moet de mac opnieuwe opgestart worden.
> **Note:** Het kan zijn dat er een beveiligingswaarschuwing komt, de driver moet u uitzonderen in **"Security & Privacy"**.

9. Vervolgens kunt in de shell het volgende commando uitvoeren:

   screen /dev/tty.wchusbserial [vervolgens tab om automatisch te laten aanvullen] 115200

   Het commando ziet er ongeveer als volgt uit:

   screen /dev/tty.wchusbserial14610 115200

 10. Je ziet in het scherm **>>>** staan. Dit betekend dat je verbinding hebt met het bordje.

## Windows gebruikers

## Webrpl

Het is ook mogelijk om zonder driver het bordje te benaderen. Dit kan middels webrpl. Hiervoor moeten onderstaande stappen worden ondernomen.

 1. Download de [master.zip](https://github.com/micropython/webrepl/archive/master.zip) bestand.
 2. Pak vervolgens het zip bestand uit
 3. Open vervolgens het bestand webrepl.html in IE/Chrome/Firefox
 4. Maak vervolgens verbinding met Wifi naar MicroPython-[cijfersletters op gele briefje]
 5. De wifi code is **micropythoN**
 6. Na verbinding kun je vervolgens op de **Connect** knop klikken in de webpagina.
 7. Er wordt vervolgens gevraagd naar een wachtwoord, type hier in **ieni**
 8. Je ziet nu **>>>** dit betekend dat je verbinding hebt met het bordje

# Workshop 0 leren programmeren

Als we het over programmeren hebben, hebben we het eingelijk over het programmeren van algoritmes.

> "Een algoritme is een eindige reeks instructies die vanuit een gegeven begintoestand naar een beoogd doel leiden". Bron: wikipedia

Een computer programma is eigenlijk 1 groot algoritme, maar dan omgezet in een computerprogramma.

## python libraries
Python libraries zijn stukjes code/programma's die we kunnen aanroepen binnen onze eigen programma. Dit bespaard een hoop code, en zorgt tevens voor het succes van Python omdat veel libraries gedeeld worden waardoor iedereen elkaar helpt.

We kunnen Python libraries importeren met het commando import.

  import machine
  (nu importeren wij alle wat in de library machine staat, niet wenselijk)

  from machine import Pin
  (nu importeren wij alleen de module/class Pin van de machine library)

## Commando print


# Workshop 1 een ledje laten branden

1. zorg dat de kabeljes aangesloten is volgens het onderstaande voorbeeld

2. Type vervolgens na >>> de volgende regel in:

  from machine import Pin
  > Hiermee zorgen we dat de Pin module geladen wordt waardoor wij de pin kunnen aansturen van het bordje

  led = Pin(14, Pin.OUT)
  > Hiermee definieren wij **led** welke is aangesloten is op pin nummer 14, en dat het bordje stroom op het pinnetje moet gaan zetten.

  led.on()
  > Nu zeggen we tegen het bordje dat hij er stroom op het pinnetje moet gaan zetten.

  led.off()
  > Nu Zeggen we tegen het bordje dat hij de stroom er vanaf moet gaan halen.



# Workshop 2 een zwaailichtje maken

# Workshop 3 knopje met ledje
led = Pin(14, Pin.OUT)
   button = machine.Pin(12, machine.Pin.IN, machine.Pin.PULL_UP)
while True:
  if button.value():
    led.on()
  else:
    led.off()

# Workshop 4 een stoplichtje maken
