from emora_stdm import DialogueFlow, KnowledgeBase, Macro
from enum import Enum, auto
import random
from nltk.corpus import wordnet as wn


class State(Enum):
    START = auto()
    U0 = auto()
    S0ERR = auto()
    S1 = auto()
    U1 = auto()
    S1ERR = auto()
    S2 = auto()
    U2 = auto()
    S2ERR = auto()
    S3 = auto()
    U3 = auto()
    S3ERR = auto()
    S4 = auto()
    U4 = auto()
    S4ERR = auto()
    S5 = auto()


class RANDFOOD(Macro):
    def run(self, ngrams, vars, args):
        if 'cuisine' in vars:
            cuisineOnt = "ont" + vars['cuisine']
            listOfFoods = ontology['ontology'][cuisineOnt]
            vars['dish'] = random.choice(listOfFoods)

        return "I don't know about that particular food. My favorite food from that cuisine is " + vars[
            'dish'] + ". Do you know of " + \
               "any history behind " + vars['dish'] + "?"


class RANDCUISINE(Macro):
    def run(self, ngrams, vars, args):
        listofcuisines = ["american", "italian", "chinese", "mexican", "korean"]
        vars['cuisine'] = random.choice(listofcuisines)
        return "I am not sure if that is a country. My favorite cuisine is " + vars['cuisine'] + ". Do you have any " + \
               vars['cuisine'] + " food that you like in particular?"


class CHECK(Macro):
    def run(self, ngrams, vars, args):
        keyword = historyKeyWords.get(vars['dish'])
        fact = history.get(vars['dish'])
        if 'history' in vars:
            user = vars['history'].split()
            for w in keyword:
                for x in user:
                    if w == x:
                        return "I was just about to say that! Just like this, many dishes have their own unique history. How do you think the history of a country can affect their cuisines?"
            return "Let me tell you about " + vars[
                'dish'] + ". " + fact + ". Just like this, many dishes have their own unique history. How do you think the history of a country can affect their cuisines?"


class INFLUENCE(Macro):
    def run(self, ngrams, vars, args):
        listOfReasons = ["lifestyle", "weather", "immigration", "colonization", "geography", 'cultivation',
                         'agriculture', 'economy', 'disease', 'religion']
        similarity = 0.0
        influence_synset = []
        randomReason = random.choice(listOfReasons)
        if 'influence' in vars:
            influencesplit = vars['influence'].split()
            for variable in influencesplit:
                influence_synset.append(wn.synsets(variable, 'n'))
            for reason in listOfReasons:
                var2_synset = wn.synsets(reason, 'n')
                for influencesynset in influence_synset:
                    for influenceinnersynset in influencesynset:
                        for var2synset in var2_synset:
                            if influenceinnersynset.wup_similarity(var2synset) > similarity:
                                similarity = influenceinnersynset.wup_similarity(var2synset)
        if similarity > 0.85:
            return 'Yeah, that was one of the factors that I was thinking of too! One especially cool example of how food evolved that I know of is that pizza used to have no tomato sauce until the 17th century when tomatoes were introduced from South America.  There are many instances like this where foods evolve throughout history, which I think is really cool. Going back to ' + \
                   vars['dish'] + ', what do you like about it?'
        else:
            return randomReason + ' was one of the factors that I was thinking of. One especially cool example of how food evolved that I know of is that pizza used to have no tomato sauce until the 17th century when tomatoes were introduced from South America.  There are many instances like this where foods evolve throughout history, which I think is really cool. Going back to ' + \
                   vars['dish'] + ', what do you like about it?'


class REASON(Macro):
    def run(self, ngrams, vars, args):
        listOfPossibleReasons = ["aroma", "accessibility", "comfort", "health", "history", 'ingredients', 'price']
        similarity = 0.0
        reason_synset = []
        flavors = ['sweet', 'spicy', 'savory', 'sour', 'bitter', 'salty']
        foodFlavor = ""
        for flavor in flavors:
            listOfFoods = ontology['ontology'][flavor]
            if vars['dish'] in listOfFoods:
                foodFlavor = flavor
                break
        if 'reason' in vars:
            reasonsplit = vars['reason'].split()

            for flavor in flavors:
                for reason in reasonsplit:
                    if flavor == reason:
                        newFood = []
                        while len(newFood) <= 3:
                            newFood.append(ontology['ontology'][flavor].pop())
                        simFoods = ''
                        for food in newFood:
                            simFoods += food + ", "
                        simFoods = simFoods[:-2]
                        return tastePref[
                                   flavor] + ' Here are some foods that have similar flavor profiles: ' + simFoods + '. What other cuisines would you like to learn about?'

            for variable in reasonsplit:
                reason_synset.append(wn.synsets(variable, 'n'))
            for possibleReason in listOfPossibleReasons:
                var2_synset = wn.synsets(possibleReason, 'n')
                for reasonsynset in reason_synset:
                    for reasoninnersynset in reasonsynset:
                        for var2synset in var2_synset:
                            if reasoninnersynset.wup_similarity(var2synset) > similarity:
                                similarity = reasoninnersynset.wup_similarity(var2synset)

        if similarity > 0.85:
            return 'Yeah, that is a great reason to like this food. I personally like it because it tastes ' + foodFlavor + '. What other cuisines would you like to learn about?'
        else:
            return 'I see, the ' + foodFlavor + ' taste is one of the reasons that I like this food.' + '. What other cuisines would you like to learn about?'


class DISHES(Macro):
    def run(self, ngram, vars, args):
        ont = 'ont' + vars['cuisine']
        return ont


tastePref = {
    'sweet': 'Yeah, I get that. I am not a huge fan of sweet food because sugar makes my parts sticky.',
    'spicy': 'I prefer foods that are not too spicy because my processor cannot take too much heat.',
    'savory': 'I love savory food! A nice savory taste always hits the spot.',
    'sour': 'Sour food is not bad, I agree.',
    'bitter': 'I love bitter foods, they really hit the spot.',
    'salty': 'Salty foods are delicious!'
}

history = {
    'hamburger': 'The idea to put meat in between buns came into popularity during the Industrial Revolution to be able to feed factory workers while they were standing.',
    'fried chicken': 'Fried chicken was brought to the United States by Scottish immigrants in the 19th century.',
    'barbecue': 'Barbecue originated by a type of smoked meat by natives of Carribeans.',
    'deep dish pizza': 'Deep dish pizza was invented by Italian immigrants in Chicago during the 19th century.',
    'hot dog': 'The hot dog was invented by a food vendor in 1869 in Brooklyn, New York.',
    'mac and cheese': 'Mac and cheese was popularized by Thomas Jefferson.',
    'apple pie': 'Apple pie is actually originally from England.',
    'grits': 'Grits were originally eaten by Native Americans in the southern parts of the United States.',
    'bagel': 'Bagels are a variety of bread brought from Eastern Europe by Jewish immigrants.',
    'bread pudding': 'Original bread pudding was from england; American variants are usually sweet and served as dessert.',
    'panini': 'Although originated in Italy during the 19th century, it became widely popular in the United States.',
    'pizza': 'Pizza became popular during the 17th century by peasants in Naples.',
    'pasta': 'Records of pasta exists since the Etruscans.',
    'polenta': 'Corn was introduced to polenta only since the 16th century.',
    'gelato': 'Gelato is thought to have been created by an alchemist in the 17th century.',
    'risotto': 'Risotto was introduced by the Arabs during the Middle Ages.',
    'tiramisu': 'A relatively recent dish, tiramisu was invented in the 1980s.',
    'minestrone': 'Minestrone was a poor mans soup with its origin going back as far as the 1st century.',
    'gnocchi': 'Potato was introduced to gnocchi only since the 19th century.',
    'ravioli': 'The earliest documentation of the ravioli recipe is from the 14th century.',
    'dumpling': 'Dumplings are one of the most traditional chinese cuisine, having a history of more than 1,800 years.',
    'sweet and sour pork': 'It originated from Guangdong region.',
    'fried rice': 'It is believed that this originates from General Yang Su of the Sui Dynasty.',
    'mongolian beef': 'Mongolian beef is a Chinese American dish adapted from the beef component of Mongolian barbecue.',
    'peking duck': 'The origin of the Peking Duck dates back to the Ming Dynasty, about 600 years ago.',
    'kung pao chicken': 'The dish is believed to be named after Ding Baozhen (1820–1886), a late Qing Dynasty official and governor of Sichuan Province.',
    'spring roll': 'Spring rolls are usually eaten during the Spring Festival in mainland China.',
    'dandan noodle': 'The name refers to a type of carrying pole (dan dan) that was used by walking street vendors who sold the dish to passerby.',
    'sesame chicken': 'Sesame chicken is a Americanized Chinese dish that is similar to General Tsos chicken but the taste of the Chinese-based chicken is sweet rather than spicy.',
    'mapo tofu': 'The origin of mapo tofu can be traced to 1862 during the Qing Dynasty (1644-1911) and to a couple surnamed Chen, who ran Chen Xingsheng Restaurant, a small eatery near Wanfu Bridge in north Chengdu.',
    'taco': 'The exact origin of tacos is unknown; it is thought that the existence of tacos predates the arrival of the Spanish in Mexico.',
    'fried avocado': 'Avocados were regarded by the Aztecs to be a delicacy and an aphrodisiac.',
    'nachos': 'There is a special nachos event called the International Nacho Festival, held every October in Piedras Negras.',
    'quesadilla': 'Literally meaning “little cheesy thing,” quesadillas originated in northern and central Mexico in the 16th century.',
    'enchilada': 'Enchiladas were mentioned in the first Mexican cookbook, El cocinero mexicano ("The Mexican Chef"), published in 1831.',
    'fajita': 'The word “fajita” didn’t even appear in print until 1975.',
    'caldo de queso': 'Caldo de queso is a simple mexican soup with gummy and chewable texture; it comes from north Mexico.',
    'carnita': 'Carnitas, literally meaing "small meats", originated from Michoachan.',
    'gorditas zacatecanas': 'This variety of gorditas comes from Zacatecas, hence the name.',
    'pozole': 'Pozole is typically served on New Years Eve to celebrate the new year. Pozole is frequently served as a celebratory dish throughout Mexico and in Mexican communities outside Mexico.',
    'kimchi': 'Kimchi is a Korean staple, is served with almost every single meal, and was made by ancient Koreans.',
    'bulgogi': 'Bulgogi originated during the goguryeo era (37 BCE-668 CE); it was on a skewer at this time.',
    'japchae': 'Japchae originally started off as a dish that did not have any meat; only fairly recently was meat added',
    'bibimbap': 'Historically, people ate this food on the eve of the lunar new year, putting all leftover side dishes into one and mixing it up.',
    'ddukbokki': 'At first, this dish was not made spicy; it was around 1950 that this dish first became spicy.',
    'samgyeopsal': 'This is a common dish at Korean BBQ; it is often eaten wrapped in lettuce or perilla leaves. It became popular in the 1960s when the price of soju dropped.',
    'jjajangmyeon': 'This dish originated based on a Chinese dish; however, recent iterations differ quite a bit.',
    'kimbap': 'Origin is controversial; some believe it to be influenced by Japanese nori and others think that it came from Korean ssam.',
    'doenjang jjigae': 'Doenjang jjigae is one of the most historic foods of Korea and it originated before the Three Kingdoms era.',
    'bingsoo': 'Bingsoo originated during the Joseon dynasty (1392-1910).'
}
historyKeyWords = {'hamburger': ['industrial', 'revolution', 'factory', 'workers'],
                   'fried chicken': ['scottish', '19th century'],
                   'barbecue': ['caribbean', 'natives'],
                   'deep dish pizza': ['italian immigrants', 'chicago', '19th century', 'italian'],
                   'hot dog': ['brooklyn', 'new york', 'food vendor', '1869', 'vendor'],
                   'mac and cheese': ['thomas jefferson'],
                   'apple pie': ['england'],
                   'grits': ['native americans', 'south'],
                   'bagel': ['eastern', 'europe', 'jewish immigrants', 'jewish'],
                   'bread pudding': ['england', 'sweet', 'dessert'],
                   'panini': ['italy', '19th century'],
                   'pizza': ['17th century', 'peasants', 'naples'],
                   'pasta': ['etruscans'],
                   'polenta': ['corn', '16th century'],
                   'gelato': ['alchemist', '17th century'],
                   'risotto': ['arabs', 'middle ages'],
                   'tiramisu': ['recent', '1980s'],
                   'minestrone': ['poor', '1st century'],
                   'gnocchi': ['19th century', 'potato'],
                   'ravioli': ['14th century'],
                   'dumpling': ['1800 years', 'traditional'],
                   'sweet and sour pork': ['guangdong'],
                   'fried rice': ['yang su', 'sui dynasty', 'general'],
                   'mongolian beef': ['chinese american', 'mongolian barbecue'],
                   'peking duck': ['ming dynasty', '600 years ago'],
                   'kung pao chicken': ['ding baozhen', 'qing dynasty', 'sichuan'],
                   'spring roll': ['spring festival'],
                   'dandan noodle': ['carrying pole', 'pole', 'street vendors', 'street vendor', 'vendor'],
                   'sesame chicken': ['americanized', 'general tso'],
                   'mapo tofu': ['1862', 'qing dynasty', 'chen', 'chen xingsheng', 'wanfu', 'chengdu'],
                   'taco': ['spanish'],
                   'fried avocado': ['azetcs', 'delicacy', 'aphrodisiac'],
                   'nachos': ['international nacho festival', 'october', 'piedras negras'],
                   'quesadilla': ['north', 'northern', 'central', '16th century'],
                   'enchilada': ['1831', 'El cocinero mexicano', 'the mexican chef', 'cookbook'],
                   'fajita': ['1975', 'print'],
                   'caldo de queso': ['north mexico', 'north'],
                   'carnita': ['michoachan'],
                   'gorditas zacatecanas': ['zacatecas'],
                   'pozole': ['new years eve', 'new year', 'celebratory', 'celebration'],
                   'kimchi': ['ancient', 'staple'],
                   'bulgogi': ['goguryeo', '37 BCE', '668 CE', 'skewer'],
                   'japchae': ['no meat', 'recently'],
                   'bibimbap': ['lunar new year', 'eve', 'leftover', 'side dish', 'side dishes', 'mix'],
                   'ddukbokki': ['not spicy', '1950'],
                   'samgyeopsal': ['1960s', '1960', 'soju'],
                   'jjajangmyeon': ['chinese'],
                   'kimbap': ['controversial', 'nori', 'ssam'],
                   'doenjang jjigae': ['historic', 'three kingdoms era'],
                   'bingsoo': ['joseon dynasty', '1392', '1910']
                   }

ontology = {
    "ontology": {
        "ontCuisines": [
            "american", "italian", "chinese", "mexican", "korean"
        ],
        "ontkorean": [
            "kimchi", "bulgogi", "japchae", "bibimbap", "ddukbokki", "samgyeopsal", "jjajangmyeon", "kimbap",
            "doenjang jjigae", "bingsoo"
        ],
        "ontitalian": [
            "panini", "pizza", "pasta", "polenta", "gelato", "risotto", "tiramisu", "minestrone", "gnocchi", "ravioli"
        ],
        "ontchinese": [
            "dumpling", "sweet and sour pork", "fried rice", "mongolian beef", "peking duck", "kung pao chicken",
            "spring roll", "dan dan noodle", "sesame chicken", "mapo tofu"
        ],
        "ontmexican": [
            "taco", "fried avocado", "nachos", "quesadilla", "enchilada", "fajita", "caldo de queso", "carnita",
            "gordita", "pozole"
        ],
        "ontamerican": [
            "grits", "hamburger", "fried chicken", "barbecue", "deep-dish pizza", "hot dog", "mac and cheese",
            "apple pie", "bagel", "bread pudding"
        ],
        "spicy": [
            "enchilada", "carnita", "gorditas zacatecana", "pozole", "kimchi", "bibimbap", "ddukbokki"
        ],
        "sweet": [
            "barbecue", "apple pie", "bread pudding", "tiramisu", "sweet and sour pork", "mongolian beef",
            "peking duck", "sesame chicken", "bulgogi", "japchae", "ddukbokki", "jjajangmyeon", "bingsoo", "gelato"
        ],
        "salty": [
            "hamburger", "fried chicken", "barbecue", "deep-dish pizza", "hot dog", "mac and cheese", "bagels",
            "panini", "pizza", "minestrone", "ravioli", "dumplings", "fried rice", "mogolian beef", "kungpao chicken",
            "spring roll", "dandan noodles", "mapo tofu", "tacos", "fried avocado", "nachos", "quesadilla", "fajitas",
            "soy bean paste soup"
        ],
        "savory": [
            "hamburger", "fried chicken", "barbecue", "deep-dish pizza", "hot dog", "mac and cheese", "grits", "bagel",
            "panini", "pizza", "pasta", "polenta", "risotto", "minestrone", "gnocchi", "ravioli", "mongolian beef",
            "peking duck", "kung pao chicken", "dan dan noodle", "mapo tofu", "taco", "fried avocado", "nacho",
            "quesadilla", "enchilada", "fajita", "gordita", "pozole", "kmchi", "bulgogi", "japchae", "bibimbap",
            "ddukbokki", "samgyeopsal", "jjajangmyeon", "kimbap", "doenjang jjigae"
        ],
        "sour": [
            "gelato", "sweet and sour pork", "caldo de queso", "kimchi"
        ]
    }
}

knowledge = KnowledgeBase()
knowledge.load_json(ontology)
df = DialogueFlow(State.START, initial_speaker=DialogueFlow.Speaker.SYSTEM, kb=knowledge,
                  macros={"RANDCUISINE": RANDCUISINE(), "CHECK": CHECK(), "INFLUENCE": INFLUENCE(), "REASON": REASON(),
                          'DISHES': DISHES(), 'RANDFOOD': RANDFOOD()})

# S0
df.add_system_transition(State.START, State.U0, '"What kind of cuisine do you like?"')
df.add_user_transition(State.U0, State.S1, '$cuisine=[#ONT(ontCuisines)]')
df.set_error_successor(State.U0, State.S0ERR)
df.add_system_transition(State.S0ERR, State.U1, '#RANDCUISINE')

# S1
df.add_system_transition(State.S1, State.U1,
                         '[! I think $cuisine food is quite tasty as "well." Do you have any $cuisine food that you "like?"]')
df.add_user_transition(State.U1, State.S2, '[$dish=#ONT(#DISHES)]')
df.set_error_successor(State.U1, State.S1ERR)
df.add_system_transition(State.S1ERR, State.U2,
                         '#RANDFOOD')

# S2
df.add_system_transition(State.S2, State.U2,
                         '[!Oh yeah, I have heard of $dish "before." Do you know any history behind the "food?"]')
df.add_user_transition(State.U2, State.S3, '$history=[/.*/]')
df.set_error_successor(State.U2, State.S2ERR)
df.add_system_transition(State.S2ERR, State.U3,
                         '#CHECK')

# S3
df.add_system_transition(State.S3, State.U3, "#CHECK")
df.add_user_transition(State.U3, State.S4, '[$influence=[/.*/]]')

# S4
df.add_system_transition(State.S4, State.U4, "#INFLUENCE")
df.add_user_transition(State.U4, State.S5, '[$reason=[/.*/]]')

# S5
df.add_system_transition(State.S5, State.U0, '#REASON')

if __name__ == "__main__":
    df.precache_transitions()
    df.run(debugging=False)