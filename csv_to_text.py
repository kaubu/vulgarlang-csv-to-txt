import csv

# adj. adjective 
# adv. adverb 
# art. article 
# conj. conjunction 
# det. determiner 
# interj. interjection 
# n. noun 
# num. numeral 
# prep. preposition 
# pron. pronoun 
# v. verb

adjectives = []
adverbs = []
articles = []
conjunctions = []
determiners = []
interjections = []
nouns = []
numerals = []
prepositions = []
pronouns = []
verbs = []

### PATTERN
## Key words:
# DEFINITION
# WORD
# PRONUNCIATION
PATTERN = "DEFINITION – WORD – PRONUNCIATION"
###

with open(
f"./input/{input('Input file name: input/')}",
"r",
encoding="utf8",
newline="") as csvfile:
    reader = csv.reader(csvfile, quotechar="|")

    for i, row in enumerate(reader):
        if i == 0: # This has [Lang],Pronunciation,Part, of, speech,English
            continue

        # ['a', '/ä/', 'prep.', 'after']
        # ['ä', '/æ/', 'adj.', 'thin (slender); slim']

        # Modular pattern replacing
        new_entry = PATTERN.replace("DEFINITION", row[3])
        new_entry = new_entry.replace("WORD", row[0])
        new_entry = new_entry.replace("PRONUNCIATION", row[1])

        if row[2] == "adj.": adjectives.append(new_entry)
        elif row[2] == "adv.": adverbs.append(new_entry)
        elif row[2] == "art.": articles.append(new_entry)
        elif row[2] == "conj.": conjunctions.append(new_entry)
        elif row[2] == "det.": determiners.append(new_entry)
        elif row[2] == "interj.": interjections.append(new_entry)
        elif row[2] == "n.": nouns.append(new_entry)
        elif row[2] == "num.": numerals.append(new_entry)
        elif row[2] == "prep.": prepositions.append(new_entry)
        elif row[2] == "pron.": pronouns.append(new_entry)
        elif row[2] == "v.": verbs.append(new_entry)

with open(
f"./output/{input('Output file name: output/')}",
"w",
encoding="utf8") as f:
    
    f.write("[Adjectives]\n")
    for entry in adjectives: f.write(f"{entry}\n")

    f.write("\n\n[Adverbs]\n")
    for entry in adverbs: f.write(f"{entry}\n")

    f.write("\n\n[Articles]\n")
    for entry in articles: f.write(f"{entry}\n")

    f.write("\n\n[Conjunctions]\n")
    for entry in conjunctions: f.write(f"{entry}\n")

    f.write("\n\n[Determiners]\n")
    for entry in determiners: f.write(f"{entry}\n")

    f.write("\n\n[Interjections]\n")
    for entry in interjections: f.write(f"{entry}\n")

    f.write("\n\n[Nouns]\n")
    for entry in nouns: f.write(f"{entry}\n")

    f.write("\n\n[Numerals]\n")
    for entry in numerals: f.write(f"{entry}\n")

    f.write("\n\n[Prepositions]\n")
    for entry in prepositions: f.write(f"{entry}\n")

    f.write("\n\n[Pronouns]\n")
    for entry in pronouns: f.write(f"{entry}\n")

    f.write("\n\n[Adjectives]\n")
    for entry in adjectives: f.write(f"{entry}\n")

    f.write("\n\n[Verbs]\n")
    for entry in verbs: f.write(f"{entry}\n")