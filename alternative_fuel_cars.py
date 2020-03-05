from emora_stdm import KnowledgeBase, DialogueFlow, Macro
from enum import Enum
from nltk.corpus import wordnet as wn
import random

class State(Enum):
    START = 0
    PROMPT = 1
    ELEC = 2
    HYB = 3
    HYDROGEN = 4
    NOTFUELERROR = 5
    ELECCOMPLAINT = 6
    HYBCOMPLAINT = 7
    ELECTECH = 8
    HYBTECH = 9
    ELECPROS = 10
    HYBPROS = 11
    ELECOPTIONS = 12
    HYBOPTIONS = 13
    ELECIMPORTANT = 14
    HYBIMPORTANT = 15
    ELECCOMP = 16
    HYBCOMP = 17
    ELECBRAND = 18
    HYBBRAND = 19
    ELECLIKEBRANDQUESTION = 20
    HYBLIKEBRANDQUESTION = 21
    ELECBRANDERROR = 22
    HYBBRANDERROR = 23
    ELECLIKEBRANDANSWER = 24
    HYBLIKEBRANDANSWER = 25
    DONOTLIKE = 26
    WHYNOT = 27
    REASONWHYNOT = 28
    REASONWHYNOT2 = 29
    MODELGET = 30
    POSSIBLELIKE = 31
    CHECKINGGIB = 32
    MODEL = 34
    WANT = 35
    WANTANSWER = 36
    WANTERROR = 37
    BETTER = 38
    ENVIRONMENTGET = 39
    LEARNMORE = 40
    YES = 41
    NO = 42
    WHICH = 43
    OTHERWAYS = 44
    MOREINFO = 45
    YESHELP = 46
    NOHELP = 47
    CARCHOICE = 48
    YESCARCHOICE = 49
    NOCARCHOICE = 50
    ELECPROSERROR = 51
    HYBOPTIONSERROR = 52
    HYBIMPORTANTERROR = 53
    ELECIMPORTANTERROR = 54
    CHECKINGGIBERROR = 55
    WANTERROR0 = 56
    BETTERERROR = 57
    YESNOERROR = 58
    ENVIRONMENT = 59
    END = 60
    ELECOPTIONSA = 61
    HYBOPTIONSA = 62
    MOREINFOQUESTION = 63
    WHICHERROR = 64
    YESHELPERROR = 65
    NOHELPERROR = 66
    YESHELP2 = 67
    NOHELP2 = 68
    YESHELPERROR2 = 69
    NOHELPERROR2 = 70
    MODELGETA = 71
    MODELGETAERROR = 72


# list of tuples that contain information of cars
# cars[0:10] are electric, cars[11:19] are hybrids

cars = [
    # (fueltype,   brand,       model,    year,  country,        mlage,price, range, chgtm)
    # [0]         [1]          [2]       [3]    [4]             [5]   [6]    [7]    [8]
    ["electric", "bmw", "i3", 2013, "germany", None, 44450, 153, 40],
    ["electric", "chevrolet", "bolt", 2017, "united states", None, 37495, 238, 70],
    ["electric", "chevrolet", "spark", 2014, "united states", None, 13220, 81, 30],
    ["electric", "honda", "fit ev", 2013, "japan", None, 36625, 82, 30],
    ["electric", "honda", "clarity", 2017, "japan", None, 33400, 89, 33],
    ["electric", "hyundai", "ioniq", 2017, "south korea", None, 26200, 155, 33],
    ["electric", "hyundai", "kona", 2018, "south korea", None, 36950, 292, 54],
    ["electric", "nissan", "leaf", 2010, "japan", None, 31600, 157, 30],
    ["electric", "tesla", "model s", 2012, "united states", None, 81190, 380, 40],
    ["electric", "tesla", "model x", 2015, "united states", None, 84990, 325, 30],
    ["electric", "tesla", "model 3", 2017, "united states", None, 41190, 348, 30],
    # end electric list
    ["hybrid", "chevrolet", "volt", 2011, "united states", 42, 33520, 420, None],
    ["hybrid", "ford", "fusion", 2006, "united states", 27, 23170, 550, None],
    ["hybrid", "honda", "cr-z", 2010, "japan", 40, 21000, 360, None],
    ["hybrid", "honda", "accord", 2014, "japan", 48, 31870, 610, None],
    ["hybrid", "hyundai", "sonata", 2020, "south korea", 44, 27000, 686, None],
    ["hybrid", "kia", "optima", 2020, "south korea", 41, 29310, 689, None],
    ["hybrid", "lincoln", "mkz", 2020, "united states", 41, 35520, 590, None],
    ["hybrid", "toyota", "avalon", 2020, "japan", 40, 38300, 420, None],
    ["hybrid", "toyota", "prius", 2020, "japan", 60, 24200, 540, None]
]


# end hybrid list

class RANDOMMODEL(Macro):
    def run(self,ngram,vars,args):
        vars['typecar'] = vars['brand'] + vars['fueltype']
        listofmodel = []
        if 'brand' in vars:
            for i in range(len(cars)): #traverse each row
                    if cars[i][0] == vars['fueltype'] and vars['brand'] == cars[i][1]:
                        listofmodel.append(cars[i][2])
            model =random.choice(listofmodel)
            vars['model'] = model
            return "Let me tell you a model by "+vars['brand']+", like " + model +". But I want to know more about you. Which of the following is most important to you: price, mileage, or range?"
        return 'Invalid brand.'

class GIBBERISH(Macro):
    def run(self, ngrams, vars, args):
        listOfReasons = ["price", "lack", "range", "long","money"]
        similarity = 0.0
        var1_synset = []
        word = vars['var1']
        if 'var1' in vars:
            var1split = vars['var1'].split()
            for variable in var1split:
                var1_synset.append(wn.synsets(variable, 'n'))
            for reason in listOfReasons:
                var2_synset = wn.synsets(reason, 'n')
                for var1synset in var1_synset:
                    for var1innersynset in var1synset:
                        for var2synset in var2_synset:
                            if var1innersynset.wup_similarity(var2synset) > similarity:
                                similarity = var1innersynset.wup_similarity(var2synset)
        if similarity > 0.7:
            return word + '.  Yeah, that can be frustrating. However, there are constant innovations that try to improve alternatively fueled cars. Do you ' \
                          'know of any? '
        else:
            return 'I am not sure what you mean. One common downside is limited driving range. ' \
                   'Do you know of any technology that attempts to improve these limitations?'


class WANTQUESTION(Macro):
    def run(self, ngrams, vars, args):
        if 'fueltype' in vars:
            if vars['fueltype'] == 'hybrid':
                return "Yeah, I've heard of that model before. Which of the following is most important to you: price, mileage, or range?"
            else:
                return "Yeah, I've heard of that model before. Which of the following is most important to you: price, charging time, or range?"


class RANGECHECK(Macro):
    def run(self, ngrams, vars, args):
        listAlternatives = []
        if 'environment' in vars and 'model' in vars and 'fueltype' in vars:
            for car in cars:
                if car[0] == vars['fueltype'] and vars['fueltype'] == "electric":
                    if vars['environment'] == "urban":
                        if car[7] < 100:
                            listAlternatives.append(car[1] + " " + car[2])
                    elif vars['environment'] == "suburb":
                        if car[7] < 200:
                            listAlternatives.append(car[1] + " " + car[2])
                    elif vars['environment'] == "rural":
                        if car[7] > 200:
                            listAlternatives.append(car[1] + " " + car[2])
                elif car[0] == vars['fueltype'] and vars['fueltype'] == "hybrid":
                    if vars['environment'] == "urban":
                        if car[7] < 450:
                            listAlternatives.append(car[1] + " " + car[2])
                    elif vars['environment'] == "suburb":
                        if car[7] < 550:
                            listAlternatives.append(car[1] + " " + car[2])
                    elif vars['environment'] == "rural":
                        if car[7] > 550:
                            listAlternatives.append(car[1] + " " + car[2])
            curCar = vars['brand'] + " " + vars['model']
            if curCar in listAlternatives:
                listAlternatives.remove(curCar)
                vars['alternatives'] = listAlternatives
                result = vars['model'] + " is great for the " + vars[
                    'environment'] + " environment that you live in. Some other alternatives that are also great for the " + \
                         vars['environment'] + " environment are "
                for alternative in listAlternatives:
                    result += alternative + ", "
                result = result[:-1]
                result = result[:-1]
                result += ". Would you like to learn more about any of these models?"
                return result
            else:
                vars['alternatives'] = listAlternatives
                result = "For the " + vars[
                    'environment'] + " environment that you live in, you may not need a car with such long range; some alternatives that are great for your environment include "
                for alternative in listAlternatives:
                    result += alternative + ", "
                result = result[:-1]
                result = result[:-1]
                result += ". Would you like to learn more about any of these models?"
                return result


class DISLIKEGIBBERISH(Macro):
    def run(self, ngrams, vars, args):
        reasonsToDislike = ['price', 'mainstream', 'maintenance', 'visual', 'looks', 'aesthetic', 'comfort',
                            'reliability', 'build']
        similarity = 0.0
        var3_synset = []
        word = vars['var3']
        if 'var3' in vars:
            var3split = vars['var3'].split()
            for variable in var3split:
                var3_synset.append(wn.synsets(variable, 'n'))
            for reason in reasonsToDislike:
                reasons_synset = wn.synsets(reason, 'n')
                for var3synset in var3_synset:
                    for var3innersynset in var3synset:
                        for reasonsynset in reasons_synset:
                            if var3innersynset.wup_similarity(reasonsynset) > similarity:
                                similarity = var3innersynset.wup_similarity(reasonsynset)
        vars['typecar'] = vars['brand'] + vars['fueltype']
        if similarity > 0.7:
            return word + ". I can see why you think that. However, " + vars[
                'brand'] + " has many good points as well that I would love to tell you about. Do you know of any models from this brand?"
        else:
            return "I'm not sure what that means; however, " + vars[
                'brand'] + " has many good points that I would love to tell you about. Do you know of any models from this brand in particular?"


class ENVIRONMENT(Macro):
    def run(self, ngrams, vars, args):
        if 'environment' in vars:
            if vars['environment'] == "urban":
                return "Eating more locally sourced goods can be helpful.  In addition, eating less meat and dairy " \
                       "and reducing food waste is another way that city dwellers can reduce their carbon footprint.  " \
                       "In addition, reducing shopping and using public transportation are also good ways that people " \
                       "living in urban environments can reduce their environmental footprint. What other alternatively fueled cars would you like to learn about?"
            elif vars['environment'] == "suburb":
                return "Eating more locally sourced goods can be helpful.  In addition, eating less meat and dairy" \
                       "and reducing food waste is another way that one can reduce their carbon footprint.  Also, trying to " \
                       "use electronics for longer periods of time and not always buying the newest technology" \
                       "helps.  Trying to utilize carpool more often as well to get to places will reduce carbon footprints." \
                       "What other alternatively fueled cars would you like to learn about?"
            elif vars['environment'] == "rural":
                return "Living in a rural environment, it is very easy to go to farmer's markets to get locally sourced " \
                       "foods.  However, to get to places there is usually a longer drive associated; to reduce this downside," \
                       "utilizing carpool as well as planning out trips so that there are not unnecessarily many trips " \
                       "taken are ways that one can reduce their environmental impact. What other alternatively fueled cars would you like to learn about?"


class COMPARE(Macro):
    def run(self, ngrams, vars, args):
        x = {"price": "hybrid", "ecofriendliness": "electric", "range": "hybrid"}
        if 'fueltype' in vars and 'important' in vars:
            typeFuel = vars['fueltype']
            importantFactor = vars['important']

            for factors in x:
                if factors == importantFactor:
                    if x[factors] == typeFuel:
                        return "Yeah, " + typeFuel + " is the best choice for " + importantFactor + ". What brand of " + typeFuel + " car have you heard of?"
                    else:
                        typeFuel = x[factors]
                        return typeFuel + " may be a better choice if you're just looking for " + importantFactor + ". You might want to look into that later. What brand of " + \
                               vars['fueltype'] + " cars have you heard of?"

class MOREINFO(Macro):
    def run(self, ngrams, vars, args):
        resultList = []
        result = ""
        if 'modelMoreInfo' in vars:
            for car in cars:
                if car[2] == vars['modelMoreInfo']:
                    resultList = car
            if resultList[0] == 'electric':
                result += "Fuel Type: " + resultList[0] + ", Brand: "+ resultList[1] + ", Model: "+resultList[2] + ", Year: "+str(resultList[3])+", Country: "+resultList[4]+", Price: "+str(resultList[6])+", Range: "+str(resultList[7])+", Charge Time: "+str(resultList[8])
            elif resultList[0] == 'hybrid':
                result += "Fuel Type: " + resultList[0] + ", Brand: " + resultList[1] + ", Model: " + resultList[2] + ", Year: " + str(resultList[3]) + ", Country: " + resultList[4] + ", Price: " + str(resultList[6]) + ", Range: " + str(resultList[7]) + ", Mileage: " + str(resultList[5])
        result += ". Would you like me to tell you more about other ways to help the environment?"
        return result

# finds whether there is a different model better for the want that the user specifies
class BETTER(Macro):
    def run(self, ngrams, vars, args):
        if 'want' in vars and 'fueltype' in vars and 'model' in vars and 'brand' in vars:
            index = 0
            currentCarIndex = 0
            marker = True
            for car in cars:
                if car[0] == vars['fueltype']:
                    if car[1] == vars['brand']:
                        if car[2] == vars['model']:
                            currentCarIndex = cars.index(car)
            if vars['want'] == "price":
                index = 6
                # True for this marker means that it is better to be less than
                marker = True
            elif vars['want'] == "mileage":
                index = 5
                marker = False
            elif vars['want'] == "range":
                index = 7
                marker = False
            elif vars['want'] == "charging time":
                index = 8
                marker = True
            for car in cars:
                if car[0] == vars['fueltype']:
                    if marker:
                        if car[index] < cars[currentCarIndex][index]:
                            currentCarIndex = cars.index(car)
                    else:
                        if car[index] > cars[currentCarIndex][index]:
                            currentCarIndex = cars.index(car)
            return cars[currentCarIndex][1] + " " + cars[currentCarIndex][2] + " is extremely good for " + vars[
                'want'] + ". You may want to consider this as well. Which of these environments describes the type that you live in the best: urban, rural, suburb?"


class GIBBERISH2(Macro):
    def run(self, ngrams, vars, args):
        listOfReasons = ["mileage", "cost", "environment", "health", "safety", "maintenance", "noise", "tax"]
        listOfNegatives = ["no","not","hate",'dislike']
        similarity = 0.0
        var2_synset = []
        if 'var2' in vars:
            var2split = vars['var2'].split()
            for variable in var2split:
                if variable in listOfNegatives:
                    return "I am sorry to hear that; however "+ vars['brand']+ " has many good points as well that I would love to tell you about. Do you know of any models from this brand?"
                var2_synset.append(wn.synsets(variable, 'n'))
            for reason in listOfReasons:
                var3_synset = wn.synsets(reason, 'n')
                for var2synset in var2_synset:
                    for var2innersynset in var2synset:
                        for var3synset in var3_synset:
                            if var2innersynset.wup_similarity(var3synset) > similarity:
                                similarity = var2innersynset.wup_similarity(var3synset)
        vars['typecar'] = vars['brand'] + vars['fueltype']
        if similarity > 0.7:
            return "Yeah, I definitely agree; that is definitely a great feature of the brand. Have you heard of any models in particular?"
        else:
            return "I'm not quite sure what that is, but I know for sure that energy conservation is a great feature of the brand. Have you heard of any models in particular?"


ontology = {
    "ontology":
        {
            "chevrolethybrid": [
                "volt"
            ],
            "fordhybrid": [
                "fusion"
            ],
            "hondahybrid": [
                "cr-z",
                "accord"
            ],
            "hyundaihybrid": [
                "sonata"
            ],
            "kiahybrid": [
                "optima"
            ],
            "lincolnhybrid": [
                "mkz"
            ],
            "toyotahybrid": [
                "avalon",
                "prius"
            ],
            "bmwelectric": [
                "i3"
            ],
            "chevroletelectric": [
                "bolt",
                "spark"
            ],
            "hondaelectric": [
                "fit ev",
                "clarity"
            ],
            "hyundaielectric": [
                "ioniq",
                "kona"
            ],
            "nissanelectric": [
                "leaf"
            ],
            "teslaelectric": [
                "model s",
                "model x",
                "model 3"
            ]
        }
}

knowledge = KnowledgeBase()
knowledge.load_json(ontology)
df = DialogueFlow(State.START, initial_speaker=DialogueFlow.Speaker.SYSTEM, kb=knowledge,
                  macros={"GIBBERISH": GIBBERISH(), "COMPARE": COMPARE(), "WANTQUESTION": WANTQUESTION(),
                          "GIBBERISH2": GIBBERISH2(), "DISLIKEGIBBERISH": DISLIKEGIBBERISH(), "BETTER": BETTER(),
                          "RANGECHECK": RANGECHECK(), "ENVIRONMENT": ENVIRONMENT(),"MOREINFO": MOREINFO(),"RANDOMMODEL": RANDOMMODEL()})

# S0
df.add_system_transition(State.START, State.PROMPT,
                         '"Hello, what types of alternatively-fueled cars interest you?"')
df.add_user_transition(State.PROMPT, State.ELEC, '$fueltype={electric}')
df.add_user_transition(State.PROMPT, State.HYB, '$fueltype={hybrid}')
df.add_user_transition(State.PROMPT, State.HYDROGEN, '[hydrogen]')
df.set_error_successor(State.PROMPT, State.NOTFUELERROR)
df.add_system_transition(State.NOTFUELERROR, State.PROMPT, 'I am not too sure I know about that one but I can talk '
                                                           'about "electric, hybrid, and hydrogen" "cars." "\n"'
                                                           'Which of these interests you the "most?"')
df.add_system_transition(State.HYDROGEN, State.PROMPT, 'Hydrogen cars are an upcoming form of "transportation." '
                                                       '"Sadly," there are no commercially available models at the '
                                                       '"moment." I would love to talk about electric or hybrid cars '
                                                       '"though." Which of the two would you like to talk "about?"')

# S1
df.add_system_transition(State.ELEC, State.ELECCOMPLAINT, '[! What holds you back from buying a $fueltype "car?"]')
df.add_system_transition(State.HYB, State.HYBCOMPLAINT, '[! What holds you back from buying a $fueltype "car?"]')
df.add_user_transition(State.ELECCOMPLAINT, State.ELECTECH, '$var1=[/^((?!^$).)*$/]')
df.add_user_transition(State.HYBCOMPLAINT, State.HYBTECH, '$var1=[/^((?!^$).)*$/]')

# S2
df.add_system_transition(State.ELECTECH, State.ELECPROS, '#GIBBERISH')
df.add_system_transition(State.HYBTECH, State.HYBPROS, '#GIBBERISH')
df.add_user_transition(State.ELECPROS, State.ELECOPTIONSA, '$tech=[/^(.*?(lithium|battery|system)){2,}.*$/]')
df.add_user_transition(State.HYBPROS, State.HYBOPTIONSA,
                       '$tech=[/^(.*?(regenerative|braking|electric|motor|drive|automatic|start|stop)){2,}.*$/]')
df.set_error_successor(State.ELECPROS, State.ELECPROSERROR)
df.set_error_successor(State.HYBPROS, State.HYBOPTIONSERROR)
df.add_system_transition(State.ELECPROSERROR, State.ELECOPTIONS,
                         '[! Let me give you an "example." For instance, innovations in battery systems enhanced '
                         'battery life and "durability." Which is the most important '
                         'to "you:" "price," "ecofriendliness," "range?"]')
df.add_system_transition(State.HYBOPTIONSERROR, State.HYBOPTIONS, '[! Let me give you an "example." For instance, '
                                                                  'regenerative breaking captures the kinetic energy '
                                                                  'lost by using the break and stores it in the '
                                                                  '"battery." Which is the most important '
                                                                  'to "you:" "price," "ecofriendliness," "range?"]')

#S3
df.add_system_transition(State.ELECOPTIONSA, State.ELECOPTIONS, '[! I agree that $tech is an important innovation in electric '
                                                                '"vehicles." Which is the most important to "you:" '
                                                                '"price," "ecofriendliness," "range?"]')
df.add_system_transition(State.HYBOPTIONSA, State.HYBOPTIONS, '[! I agree that $tech is an important innovation in hybrid "vehicles." '
                                                              'Which is the most important to "you:" "price,'
                                                              '" "ecofriendliness," "range?"]')
df.add_user_transition(State.ELECOPTIONS, State.ELECCOMP, '$important={price,ecofriendliness,range}')
df.add_user_transition(State.HYBOPTIONS, State.HYBCOMP, '$important={price,ecofriendliness,range}')
df.set_error_successor(State.HYBOPTIONS, State.HYBIMPORTANTERROR)
df.set_error_successor(State.ELECOPTIONS, State.ELECIMPORTANTERROR)
df.add_system_transition(State.HYBIMPORTANTERROR, State.HYBOPTIONS,
                         'I am "sorry," but I did not quite catch "that." Could you try one more time and tell me which is most important to "you:price, ecofriendliness, or range?"')
df.add_system_transition(State.ELECIMPORTANTERROR, State.ELECOPTIONS,
                         'I am "sorry," but I did not quite catch "that." Could you try one more time and tell me which is most important to "you: price, ecofriendliness, or range?"')

# S4

df.add_system_transition(State.ELECCOMP, State.ELECBRAND, '#COMPARE')
df.add_system_transition(State.HYBCOMP, State.HYBBRAND, '#COMPARE')
df.add_user_transition(State.ELECBRAND, State.ELECLIKEBRANDQUESTION,
                       '$brand={bmw,chevrolet,honda,hyundai,nissan,tesla}')
df.add_user_transition(State.HYBBRAND, State.HYBLIKEBRANDQUESTION,
                       '$brand={chevrolet,ford,honda,hyundai,kia,lincoln,toyota}')
df.set_error_successor(State.ELECBRAND, State.ELECBRANDERROR)
df.set_error_successor(State.HYBBRAND, State.HYBBRANDERROR)
df.add_system_transition(State.ELECBRANDERROR, State.ELECBRAND,
                         '"Sorry," but I am not sure if that brand creates electric "cars." Some examples of brands "are: bmw, chevrolet, honda, hyundai, nissan, tesla." Please try "again!"')
df.add_system_transition(State.HYBBRANDERROR, State.HYBBRAND,
                         '"Sorry," but I am not sure if that brand creates hybrid "cars." Some examples of brands "are: chevrolet, ford, honda, hyundai, kia, lincoln, toyota" Please try "again!"')

# S5
df.add_system_transition(State.ELECLIKEBRANDQUESTION, State.ELECLIKEBRANDANSWER, 'What about $brand do you "like?"')
df.add_system_transition(State.HYBLIKEBRANDQUESTION, State.HYBLIKEBRANDANSWER, 'What about $brand do you "like?"')

df.add_user_transition(State.ELECLIKEBRANDANSWER, State.POSSIBLELIKE, '$var2=[/^((?!^$).)*$/]')
df.add_user_transition(State.HYBLIKEBRANDANSWER, State.POSSIBLELIKE, '$var2=[/^((?!^$).)*$/]')
df.add_system_transition(State.POSSIBLELIKE, State.CHECKINGGIB, '#GIBBERISH2')
df.add_user_transition(State.CHECKINGGIB, State.MODELGET, '$model=[#ONT($typecar)]')
df.set_error_successor(State.CHECKINGGIB, State.CHECKINGGIBERROR)
df.add_system_transition(State.CHECKINGGIBERROR, State.MODELGETA, '#RANDOMMODEL')
df.add_user_transition(State.MODELGETA, State.WANTANSWER, '$want={price,mileage,charging time,range}')
df.set_error_successor(State.MODELGETA, State.MODELGETAERROR)
df.add_system_transition(State.MODELGETAERROR, State.MODELGETA, 'I did not "understand," could you try choosing again "from: price, mileage, charging time, range?"')

# S6:

df.add_system_transition(State.MODELGET, State.WANT, '#WANTQUESTION')
df.add_user_transition(State.WANT, State.WANTANSWER, '$want={price,mileage,charging time,range}')
df.set_error_successor(State.WANT, State.WANTERROR0)
df.add_system_transition(State.WANTERROR0, State.WANT,
                         'I did not "understand," could you try choosing again "from: price, mileage, charging time, range?"')

# S7:
df.add_system_transition(State.WANTANSWER, State.BETTER, '#BETTER')
df.add_user_transition(State.BETTER, State.ENVIRONMENTGET, '$environment={urban,rural,suburb}')
df.set_error_successor(State.BETTER, State.BETTERERROR)
df.add_system_transition(State.BETTERERROR, State.BETTER,
                         'I did not "understand," could you try choosing again "from: urban, rural, suburb?"')

# S8:
df.add_system_transition(State.ENVIRONMENTGET, State.LEARNMORE, '#RANGECHECK')
df.add_user_transition(State.LEARNMORE, State.NO, '[{no,not,do not,hate,dislike}]')
df.set_error_successor(State.LEARNMORE, State.YESNOERROR)
df.add_system_transition(State.YESNOERROR, State.LEARNMORE, 'I did not "understand," did you want to say yes or "no?"')
df.add_user_transition(State.LEARNMORE, State.YES, '[{yes,yeah,affirmative,of course,please,sure}]')

# S9:
df.add_system_transition(State.YES, State.WHICH, 'Which model would you like to learn more "about?"')
df.add_user_transition(State.WHICH, State.MOREINFO, '$modelMoreInfo={volt,fusion,"cr-z",accord,sonata,optima,mkz,avalon,prius,"i3",bolt,spark,fit ev,clarity,ioniq,kona,leaf,model s,model x,model "3"}')

df.set_error_successor(State.WHICH, State.WHICHERROR)
df.add_system_transition(State.WHICHERROR, State.WHICH,'I did not "understand," please input a valid car model "(just the model)"')

df.add_system_transition(State.MOREINFO, State.MOREINFOQUESTION, '#MOREINFO')
df.add_user_transition(State.MOREINFOQUESTION, State.YESHELP, '[{yes,yeah,affirmative,of course,please,sure}]')
df.add_user_transition(State.MOREINFOQUESTION, State.NOHELP, '[{no,not,do not,hate,dislike}]')

df.set_error_successor(State.MOREINFOQUESTION, State.YESHELPERROR)
df.set_error_successor(State.MOREINFOQUESTION, State.NOHELPERROR)

df.add_system_transition(State.NOHELPERROR, State.MOREINFOQUESTION, 'I did not "understand," did you want to say yes or "no?"')
df.add_system_transition(State.YESHELPERROR, State.MOREINFOQUESTION, 'I did not "understand," did you want to say yes or "no?"')

df.add_system_transition(State.NO, State.OTHERWAYS,
                         '"Alright," would you like me to tell you more about other ways to help the "environment?"')
df.add_user_transition(State.OTHERWAYS, State.YESHELP2, "[{yes,yeah,affirmative,of course,please,sure}]")
df.add_user_transition(State.OTHERWAYS, State.NOHELP2, "[{no,not,do not,hate,dislike}]")

df.set_error_successor(State.OTHERWAYS, State.YESHELPERROR2)
df.set_error_successor(State.OTHERWAYS, State.NOHELPERROR2)

df.add_system_transition(State.NOHELPERROR2, State.OTHERWAYS, 'I did not "understand," did you want to say yes or "no?"')
df.add_system_transition(State.YESHELPERROR2, State.OTHERWAYS, 'I did not "understand," did you want to say yes or "no?"')

# S10:
df.add_system_transition(State.YESHELP, State.PROMPT, '#ENVIRONMENT')
df.add_system_transition(State.NOHELP, State.PROMPT,
                         'what other types of alternatively fueled cars interest "you?"')
df.add_system_transition(State.YESHELP2, State.PROMPT, '#ENVIRONMENT')
df.add_system_transition(State.NOHELP2, State.PROMPT,
                         'what other types of alternatively fueled cars interest "you?"')

df.run(debugging=True)
