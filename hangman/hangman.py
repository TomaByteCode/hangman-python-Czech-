

# Hangman
import random
from hangman2 import stages

# Uvítání a pravidla hry
print("Vítejte ve hře hádání slov . Vašim ůkolem je uhodnout správné písmeno.")

# Generování  náhodného slova
words = [
    "strom", "auto", "dům", "kniha", "pes", "kočka", "telefon", "papír", "klíč", "pero", 
    "zahrada", "město", "vesnice", "počítač", "strom", "slunce", "měsíc", "hvězda", "mrak", "déšť", 
    "snadný", "těžký", "rychlý", "pomalu", "vysoký", "nízký", "červený", "modrý", "zelený", "bílý", 
    "stůl", "židle", "okno", "dveře", "podlaha", "střecha", "lampa", "postel", "skříň", "koberec", 
    "hora", "řeka", "les", "pole", "louka", "pláž", "moře", "jezero", "rybník", "potok", 
    "jídlo", "pití", "polévka", "chleba", "sýr", "vejce", "mléko", "voda", "kafe", "čaj", 
    "letadlo", "vlak", "loď", "tramvaj", "autobus", "kolo", "motorka", "helikoptéra", "vlak", "vozík", 
    "baterie", "telefon", "nabíječka", "sluchátka", "televize", "monitor", "klávesnice", "myš", "kamera", "reproduktor", 
    "knoflík", "zip", "rukáv", "kalhoty", "tričko", "kabát", "čepice", "boty", "ponožky", "šála", 
    "jablko", "banán", "pomeranč", "hruška", "meloun", "jahoda", "třešeň", "broskev", "meruňka", "citron"
]
random.word = words[random.randint(0 , len(words)-1]

# Generování podtržítek
hidden_word =[]
for one_letter in  random.word:
    hidden_word.append("_")

# Životy
lives = 6
print(stages[lives])

# vypsání slova s podtržítky v normální podobě
printedWord = ""
for one_letter in hidden_word:
    printedWord += one_letter
print(printedWord)


while "_" in hidden_word:
    guess = input("Zadejte hádané písmeno\n").lower()
    for index in range(0 , len(random.word)):
        if guess == random.word[index]:
            hidden_word[index] = guess

    # kontrola životů
    if guess not in random.word:
        lives -= 1
        print(stages[lives])
    print(f"Počet vašich životů je {lives}")
    if lives == 0:
        print("Prohráli jste!!!")
        break

# vypsání slova s podtržítky v normální podobě
    printedWord = ""
    for one_letter in hidden_word:
        printedWord += one_letter
    print(printedWord) 

# kontrola vítěztví
    if "_" not in hidden_word:
        print("Vyhráli jste!!!")




