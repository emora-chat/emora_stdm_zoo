from emora_stdm import DialogueFlow, KnowledgeBase, Macro
from enum import Enum, auto
import json
from dialogues import spec_Dict, dict_genre, mpMiniGames_dict, mpCharacter_dict, underChar_dict,\
acVillager_dict, pokeType_dict, smashStage_dict, smashfighter_dict, mkartChar_dict,\
leagueChamp_dict, dotaHeros_dict, r6sOperator_dict, overHero_dict
from classes import SPECIFIC1a, SPECIFIC2a, SPECIFIC2b, SPECIFIC3a, SPECIFIC3b, GENRE_OPINION,\
syn_det, like_macro, dislike_macro
import random
import nltk
from nltk import word_tokenize

# Opening the json dictionary
with open('ont_dict.json') as json_file:
    ontology = json.load(json_file)

#######################################################################################
# CLASSES
# global list so that there is no repeat in conversation topic
talked = []
not_talked = ontology["ontology"]["specificGame"].copy()

# favorite games discussion
class fave_games(Macro):
    def run(self, ngrams, vars, args):
        temp = not_talked
        game = random.choice(temp)
        # update list of discussed topics
        not_talked.remove(game)
        talked.append(game)
        vars['specG'] = game
        if len(not_talked) <= 7:
            game = "maybe we should talk about something else...what is your favorite video game genre?"
        else:
            game = 'well one of my favorite games is ' + game + '. are you interested in the game?'
        return game
class GENRE_RECOMMENDER(Macro):
    def run(self, ngrams, vars, args):
        temp = vars['genre']
        if temp == 'action': temp = 'adventure'
        dialogue = ""
        if temp in ontology["ontology"]:
            select_from = ontology["ontology"][temp]
            game=random.choice(select_from)
            dialogue = "i definitely know of some " + temp + " games. try " + game
        else:
            dialogue = "sorry i dont know any games of that genre"
        return dialogue

######################################################################################################

class State(Enum):
    # Initialize
    S0 = auto()

    # General Gaming / Experience
    gU0 = auto()

    gS1a = auto()
    gS1b = auto()
    gS1c = auto()
    gS1d = auto()
    gS1e = auto()
    gS1f = auto()
    gS1g = auto()
    gS1i = auto()

    gU1aa = auto()
    gU1ab = auto()
    gU1ac = auto()
    gU1ad = auto()
    gU1b = auto()

    gS2a = auto()
    gS2b = auto()
    gtS2a = auto()
    gtS2b = auto()
    gS2c = auto()
    gS2d = auto()
    gS2e = auto()
    gS3a = auto()
    gS3aa = auto()
    gS3ab = auto()
    gS3b = auto()
    gS3c = auto()
    gS4a = auto()

    # General Type
    gU1c = auto()
    gU1d = auto()
    gS1ca = auto()
    gS1cb = auto()
    gU2a = auto()
    gU2b = auto()
    gU2c = auto()
    gU2d = auto()
    gU3a = auto()
    gU3aa = auto()
    gU3b = auto()
    gU3c = auto()
    gU4a = auto()
    gU4b = auto()
    # Favorite Gaming
    fU0 = auto()

    fS1a = auto()
    fS1b = auto()
    fS1ba = auto()
    fS1bb = auto()
    fS1cc = auto()
    fS1c = auto()
    fS1d = auto()
    fS1e = auto()
    fS1f = auto()

    fU2a = auto()
    fU2aa = auto()
    fU2ab = auto()
    fU2ac = auto()
    fU2b = auto()

    fS2aa = auto()
    fS2ab = auto()
    fS2ac = auto()
    fS2ba = auto()
    fS2bb = auto()
    

    fU3a = auto()
    fU3b = auto()
    

    fS3ab = auto()
    fS3aa = auto()
    fS3ac = auto()
    fS3ad = auto()
    fS3ae = auto()
    fS3af = auto()
    fS3ba = auto()
    fS3bb = auto()
    
    fS4a = auto()
    fS4aa= auto()
    fS4ab = auto()
    fS4ac = auto()
    fS4ad = auto()
    fS4ae = auto()
    fS4af = auto()
    fS4ag = auto()
    fS4ah = auto()
    fS4aey = auto()
    fS4aen = auto()
    fS4ai = auto()

    fS4b = auto()
    fS4ba= auto()
    fS4bb = auto()
    fS4bc = auto()
    fS4bd = auto()
    fS4be = auto()
    fS4bf = auto()
    fS4bg = auto()

    fU4a = auto()
    fU4b = auto()

    #social
    sS1a = auto()
    sS1b = auto()
    sS1c = auto()
    sS2a = auto()
    sS2b = auto()
    sS2c = auto()
    sS3a = auto()
    sS3b = auto()
    sS3c = auto()
    sU1a = auto()
    sU1b = auto()
    sU1c = auto()
    sU2a = auto()
    sU2b = auto()
    sU2c = auto()

    #genre 
    rS1a = auto()
    rU1a = auto()


    endMario = auto()
    endGen = auto()
    endRec = auto()
    endMeta = auto()
    endOtherGames = auto()
    endSpecGame = auto()
    endStory = auto()
    endChallenge = auto()
    endPuzzle = auto()
    endSocial = auto()
    endGenre = auto()


    END = auto()
    ERR = auto()
knowledge = KnowledgeBase()
knowledge.load_json(ontology)



## NaTex - Affirmation / Denial / Question
# affirm = r"[!-{[#ONT(since)],[#ONT(often)],[#ONT(sometimes)],[#ONT(question)],[#ONT(negative)]},[#ONT(positive)]]"
affirm = r"{[#ONT(positive)], #ONT(agree), #ONT(like)}"
# affirmQ = r"[!-[#ONT(negative)],<[#ONT(positive)],[#ONT(question)]>]"
# deny = r"[!-[#ONT(positive)],[#ONT(negative)]]"
deny = r"{[#ONT(negative)], #ONT(disagree), #ONT(dislike)}"
# denyQ = r"[!-[#ONT(positive)],<[#ONT(negative)],[#ONT(question)]>]"
question = r"[!-{[#ONT(positive)],[#ONT(negative)]}, [#ONT(question)]]"

## NaTex - Often / Sometimes / Never
often = r"[!-[#ONT(negative)], [#ONT(often)]]"
#multiple
#[{#ONT(like), #ONT(yes)}]

#### Module - General Gaming / Experience Gaming
# Regularly used natex inputs
# Anything: '/.*/'
# Affirm: '<[#ONT(positive)]>'
# Deny: '<[#ONT(negative)]>'
knowledge = KnowledgeBase()
knowledge.load_json(ontology)
df = DialogueFlow(State.S0, initial_speaker=DialogueFlow.Speaker.SYSTEM, kb=knowledge,
                  macros={"syn_det":syn_det(), "fave_games":fave_games(), "SPECIFIC1a": SPECIFIC1a(),
                          "SPECIFIC2a": SPECIFIC2a(), "SPECIFIC2b": SPECIFIC2b(),"SPECIFIC3a":SPECIFIC3a(),
                          "SPECIFIC3b": SPECIFIC3b(), "GENRE_OPINION": GENRE_OPINION(), "GENRE_RECOMMENDER": GENRE_RECOMMENDER(),
                          "like_macro": like_macro(), "dislike_macro":dislike_macro()})


### Main Prompt - Do you play video games?
df.add_system_transition(State.S0, State.gU0, '"Do you play video games?"')
df.add_user_transition(State.gU0, State.gS1a, '[#ONT(negative)]')
df.add_user_transition(State.gU0, State.gS1b, '[#ONT(positive)]')
df.add_user_transition(State.gU0, State.gS1d, '[$word=#ONT(dislike), $dislike=/.*/]')
df.add_user_transition(State.gU0, State.gS1c, '[$word=#ONT(like), $like=/.*/]')
df.set_error_successor(State.gU0, State.gS1f)


### Negative Response
df.add_system_transition(State.gS1a, State.gU1aa, '"video games are great, and there are games for everyone. in general would you prefer a game you can play by yourself, or with others?"')
df.add_system_transition(State.gS1c, State.gU1ac, '"why do you " $word #like_macro')
df.add_system_transition(State.gS1d, State.gU1ad, '"why do you " $word #dislike_macro')
df.add_user_transition(State.gU1ac, State.gS2c, '/.*/') # continues from why do you like
df.add_user_transition(State.gU1ad, State.gS2c, '/.*/') # continues from why do you dislike
df.add_system_transition(State.gS1f, State.gU2d, '"sorry im only interested in video games."')
df.add_user_transition(State.gU2d, State.gS1a, '/.*/')

#TODO: expand accepted phrases
df.add_user_transition(State.gU1aa, State.gS2a,"[$response=#ONT(alone)]") # alone
df.add_user_transition(State.gU1aa, State.gS2b, "[$response=#ONT(team)]") # with others
df.set_error_successor(State.gU1aa, State.gS2c)

df.add_system_transition(State.gS2a, State.gU2a, '"there are a lot of fun games for people that are more introverted. i highly recommend the" $specG=pokemon "franchise! would you be interested in them?"')
df.add_system_transition(State.gS2b, State.gU2b, '"thats awesome! being with people is great and games are a great way to be more sociable. i highly recommend the" $specG=mario kart "games! would you be interested in them?"')

df.add_user_transition(State.gU2a, State.fS1a, '[#ONT(positive)]')
df.add_user_transition(State.gU2b, State.fS1a, '[#ONT(positive)]')
df.set_error_successor(State.gU2b, State.fS1a)
df.set_error_successor(State.gU2a, State.fS1a)
df.add_user_transition(State.gU2a, State.gS2c, '[#ONT(negative)]')
df.add_user_transition(State.gU2b, State.gS2c, '[#ONT(negative)]')

# conversation about how great games are for social growth
# SOCIAL MODULE
df.add_system_transition(State.sS1a, State.sU1a, '"in my opinion, video games are great for building social skills and kids should play more games. by playing more games, we can learn how to be kinder to each other and more respectful. wouldnt you agree?"')
df.add_user_transition(State.sU1a, State.sS2a, '[{#ONT(agree), #ONT(positive), #ONT(like)}]') # contains the words agree, social?
df.add_user_transition(State.sU1a, State.sS2b, '[{#ONT(disagree), #ONT(negative), #ONT(dislike)}]') # contains negative words, disagree, antisocial
df.set_error_successor(State.sU1a, State.sS2c)

df.add_system_transition(State.sS2a, State.sU2a, '"what an interesting opinion! can you expand on your perspective?"')
df.add_system_transition(State.sS2b, State.sU2b, '"im not sure i agree with your sentiments. can you elaborate on what you mean by that?"')
df.add_user_transition(State.sU2a, State.sS3a, '/.*/')
df.add_user_transition(State.sU2b, State.sS3b, '/.*/')

df.add_system_transition(State.sS2c, State.sU2c, '"could you elaborate on what you mean"')
df.add_user_transition(State.sU2c, State.sS3a, '[{#ONT(agree), #ONT(positive), #ONT(like)}]') # this is to try again to understand the statement
df.add_user_transition(State.sU2c, State.sS3b, '[{#ONT(disagree), #ONT(negative), #ONT(dislike)}]') # this is to try again to understand the statement
df.add_system_transition(State.sS3a, State.endSocial, '"i think that is a good point. there are many games that can help us be better people. end for now more will be added later"')
df.add_system_transition(State.sS3b, State.endSocial, '"i think that is a good point but there are many games that can help us be better people. end for now more will be added later"')

df.set_error_successor(State.sU2c, State.sS3c)
df.add_system_transition(State.sS3c, State.endSocial, '"i think that is a very interesting opinion."')
#end social

df.add_system_transition(State.gS2c, State.gU2c, '"video games can create a multitude of interesting worlds. are there maybe particular types of stories you enjoy? like horror or adventure stories?"')
df.add_user_transition(State.gU2c, State.gS3aa, '[$genre=#ONT(genre)]')
df.set_error_successor(State.gU2c, State.sS1a)

df.add_system_transition(State.gS3aa, State.gU3a, '[!#GENRE_RECOMMENDER]')
df.add_user_transition(State.gU3a, State.gS4a, '[{#ONT(question)}]')
df.add_system_transition(State.gS4a, State.gU4a, '"sorry. i dont know much about the game because ive never played it but i hear from my friend siri that its pretty fun.\
would you like to hear about some games i really like?"')
df.add_user_transition(State.gU4a, State.gS4a, affirm)
df.add_system_transition(State.gS4a, State.fU2a, '[!#fave_games]')
df.set_error_successor(State.gS4a, State.gS3c)
df.set_error_successor(State.gU3a, State.gS3c)
df.add_system_transition(State.gS3c, State.endGen, "We will add more stuff here in the future, end for now")


### Positive Response
df.add_system_transition(State.gS1b, State.fU0, '"I like to game in my free time, too. What\'s your favorite game?"') #at this point, go for genre, game name detection, or i dont have one

#### Module - General Type Conversation

### Main Prompt - What's your favorite type of game?

#### Favorite Gaming Conversation
df.add_user_transition(State.fU0, State.fS1a, '[$specG=#ONT(specificGame)]') # If the user talks about a game we know about
df.add_user_transition(State.fU0, State.fS1b, '[$generalG=#ONT(generalGame)]') # If the user has a specific game they like but it's not something we know a lot about
df.set_error_successor(State.fU0, State.fS1c) # If user answers anything not in general game or specific game list

# sub dialogue
df.add_system_transition(State.fS1b, State.fU2aa, '"oh! ive heard of that game but i have never played it. how would you describe the game"')

### new stuff for flow diagram maybe
df.add_user_transition(State.fU2aa, State.fS1ba, '$input=/.*/')
df.add_system_transition(State.fS1ba, State.fU2ac, '[!#syn_det()]')
df.add_user_transition(State.fU2ac, State.fS1bb, '/.*/')
###



# Continuation'[! $familiar " huh?" #char_macro($familiar)]'
df.add_system_transition(State.fS1bb, State.fU2a, '[!"thats really interesting."#fave_games]')
df.add_system_transition (State.fS1c, State.fU2a, '[!#fave_games]')
df.add_system_transition(State.fS1a, State.fU2b, r'[!#SPECIFIC1a]')

# Specific
df.add_user_transition(State.fU2b, State.fS2ba, '[$ans1=#ONT(specAnswer1)]') #Specific
df.set_error_successor(State.fU2b, State.fS2bb)
df.set_error_successor(State.fU2a, State.fS2bb)

# General
df.add_user_transition(State.fU2a, State.fS1a, '[{#ONT(positive)}]') #affirmative; this starts the conversation about specific games
df.add_user_transition(State.fU2a, State.fS2ab, '<[#ONT(negative)]>') #negative
df.add_system_transition(State.fS2ab, State.fU2a, '[!#fave_games]') # this loops from negative
# df.add_user_transition(State.fU2a, State.fS2ac, '') # if the user asks what the game is about
df.add_user_transition(State.fU2a, State.rS1a, '[$type=#ONT(genre)]')
df.set_error_successor(State.fU2a, State.sS1a) #TODO: change this later

# GENRE OPINION MODULE
df.add_system_transition(State.rS1a, State.rU1a, r'[!#GENRE_OPINION]')
df.add_user_transition(State.rU1a, State.endRec, '/.*/')

df.add_system_transition(State.fS2bb, State.fU3b, r'[!#SPECIFIC2b]')
df.add_system_transition(State.fS2ba, State.fU3b, r'[!#SPECIFIC2a]') #type / champion or something
df.add_user_transition(State.fU3b, State.fS3ba, '[$ans2=#ONT(specAnswer2)]')
df.set_error_successor(State.fU3b, State.fS3bb)

df.add_system_transition(State.fS3bb, State.fU4a, r'[!#SPECIFIC3b]')
df.add_system_transition(State.fS3ba, State.fU4b, r'[!#SPECIFIC3a]')
df.add_user_transition(State.fU4a, State.fS4a, '/.*/')
df.add_user_transition(State.fU4b, State.fS4a, '/.*/')
df.set_error_successor(State.fU4a, State.fS4a)
df.set_error_successor(State.fU4b, State.fS4b)
df.add_system_transition(State.fS4a, State.endSpecGame, '"end for now more to add later"')
df.add_system_transition(State.fS4b, State.endSpecGame, '"end for now more to add later"')



#Future Module Ends
df.add_system_transition(State.endMeta, State.END, "Future Meta Module")
df.add_system_transition(State.endMario, State.END, "Future Mario Module")
df.add_system_transition(State.endRec, State.END, "will add more later Future Recommender Module")
df.add_system_transition(State.endChallenge, State.END, "Future Challenge Module")
df.add_system_transition(State.endPuzzle, State.END, "Future Challenge Module")
df.add_system_transition(State.endSocial, State.END, "Future Challenge Module")
df.add_system_transition(State.endOtherGames, State.END, "Future Other Games Module")
df.add_system_transition(State.endGenre, State.END, "Future Genre Module")
df.add_system_transition(State.endSpecGame, State.END, "Future Spec Games Module") #this exisits?
df.add_system_transition(State.endGen, State.END, "Future General Module") #this exisits




if __name__ == '__main__':
    df.run(debugging=False)