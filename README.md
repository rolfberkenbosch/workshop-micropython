# Workshop MicroPython

Voordat we aan de slag kunnen gaan met MicroPython moeten we eerst zorgen dat we kunnen inloggen op het bordje. Dit kan op verschillende manieren.

## MAC OS gebruikers

1. driver [downloaden](https://www.silabs.com/documents/public/software/Mac_OSX_VCP_Driver.zip) voor MAC OS
2. driver installeren, open de zip file, je ziet dan onderstaande files:
![uitgepakte driver bestand screenshot](images/image001.png)
3. Klik vervolgens op de SiLabsUSB....dmg
4. Klik vervolgens op "Agree"
5. Vervolgens verschijnt het onderstaande screenshot:
![uitgepakte driver bestand screenshot2](images/image002.png)
6. Klik vervolgens op de Silicon Labs VCP Driver.pkg
7. Druk constant op "Continue" tot het onderstaande screenshot:
![installatie mac driver gelukt](images/image002.png)
8. Nu moet de mac opnieuwe opgestart worden.
> **Note:** Het kan zijn dat er een beveiligingswaarschuwing komt, de driver moet u uitzonderen in "Security & Privacy".

9. Vervolgens kunt in de shell het volgende commando uitvoeren:

   screen /dev/tty.wchusbserial [vervolgens tab om automatisch te laten aanvullen] 115200

   Het commando ziet er ongeveer als volgt uit:

   screen /dev/tty.wchusbserial14610 115200
