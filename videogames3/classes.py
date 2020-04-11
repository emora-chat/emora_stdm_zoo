from emora_stdm import DialogueFlow, KnowledgeBase, Macro
from enum import Enum, auto
import json
from dialogues import spec_Dict, dict_genre, mpMiniGames_dict, mpCharacter_dict, underChar_dict,\
acVillager_dict, smashStage_dict, smashfighter_dict, mkartChar_dict,\
leagueChamp_dict, dotaHeros_dict, r6sOperator_dict, overHero_dict, pokeChar_dict,\
r6sMode_dict, pokeType_dict,leagueMode_dict, mkartCourse_dict,overMode_dict,\
r6sOperator_dict, dotaMode_dict, acThings_dict, underRoute_dict
import random
import nltk
from nltk import word_tokenize

class SPECIFIC1a(Macro):
    def run(self, ngrams, vars, args) -> str:

         if len(vars['specG']) > 0:
            s = vars['specG']

            #make sure name is uniform
            mario_party = ["super mario party", "jackbox party pack 6", "mario party", "mario party 2", "mario party 3",
                           "mario party 4", "mario party 5", "mario party 6", "mario party 7", "mario party 8",
                           "mario party 9", "mario party 10"]
            pokemon = ["pocket monsters"]
            league_of_legends = ["league", "lol"]
            super_smash_bros = ["super smash bros.", "super smash bros. melee", "super smash bros. wii",
                                "super smash bros. ultimate", "super smash bros. for nintendo 3ds and wii u", "smash",
                                "super smash brothers"]
            mario_kart = ["mario kart 64", "mario kart: super circuit", "mario kart: double dash", "mario kart ds",
                          "mario kart wii", "mario kart 7", "mario kart 8", "mario kart 8 deluxe", "mario kart",
                          "mario cart"]
            overwatch = []
            r6s = ["tom clancy's rainbow six siege", "rainbow six siege", "rainbow 6 siege", "r6s"]
            dota = ["defense of the ancients", "dota2"]
            animal_crossing = ["animal crossing", "animal crossing: wild world", "animal crossing: city folk",
                               "animal crossing: new leaf", "ac", "wild world", "acww", "city folk", "accf", "new leaf",
                               "acnl"]
            undertale = []

            if vars['specG'] in mario_party:
                s = 'mario party'
            elif vars['specG'] in pokemon:
                s = 'pokemon'
            elif vars['specG'] in league_of_legends:
                s = 'league of legends'
            elif vars['specG'] in super_smash_bros:
                s = 'super smash brothers'
            elif vars['specG'] in mario_kart:
                s = 'mario kart'
            elif vars['specG'] in overwatch:
                s = 'overwatch'
            elif vars['specG'] in r6s:
                s = 'r6s'
            elif vars['specG'] in dota:
                s = 'dota'
            elif vars['specG'] in animal_crossing:
                s = 'animal crossing'
            elif vars['specG'] in undertale:
                s = 'undertale'

            #return s
            opinion = spec_Dict.get(s)[0]
            question = spec_Dict.get(s)[1]

            return opinion + " "+question
class SPECIFIC2a(Macro):
    def run(self, ngrams, vars, args) -> str:
         if len(vars['specG']) > 0:
            s = vars['specG']
            ans1= vars['ans1']

            #make sure name is uniform
            mario_party = ["mario party", "super mario party",  "jackbox party pack 6", "mario party", "mario party 2", "mario party 3", "mario party 4", "mario party 5", "mario party 6",  "mario party 7", "mario party 8", "mario party 9", "mario party 10"]
            pokemon = ["pokemon", "pocket monsters"]
            league_of_legends=["league of legends", "league"]
            super_smash_bros = ["super smash brothers","super smash bros.","super smash bros. melee", "super smash bros. wii", "super smash bros. ultimate", "super smash bros. for nintendo 3ds and wii u",  "smash", "super smash brothers"]
            mario_kart= ['mario kart',"mario kart 64","mario kart: super circuit", "mario kart: double dash", "mario kart ds", "mario kart wii", "mario kart 7", "mario kart 8", "mario kart 8 deluxe", "mario kart","mario cart"]
            overwatch= ['overwatch']
            r6s = ['r6s',"tom clancy's rainbow six siege", "rainbow six siege","rainbow 6 siege","r6s"]
            dota = ['dota',"defense of the ancients","dota2"]
            animal_crossing = ['animal crossing',"animal crossing", "animal crossing: wild world","animal crossing: city folk","animal crossing: new leaf", "ac","wild world","acww","city folk","accf","new leaf", "acnl"]
            undertale = ["undertale"]

            res = ""
            if vars['specG'] in mario_party:
                s = 'mario party'
                res = mpMiniGames_dict.get(ans1)
            elif vars['specG'] in pokemon:
                s = 'pokemon'
                res = pokeChar_dict.get(ans1)
            elif vars['specG'] in league_of_legends:
                s = 'league of legends'
                res = leagueChamp_dict.get(ans1)
            elif vars['specG'] in super_smash_bros:
                s = 'super smash brothers'
                res = smashfighter_dict.get(ans1)
            elif vars['specG'] in mario_kart:
                s = 'mario kart'
                res = mkartChar_dict.get(ans1)
            elif vars['specG'] in overwatch:
                s = 'overwatch'
                res = overHero_dict.get(ans1)
            elif vars['specG'] in r6s:
                s = 'r6s'
                res = r6sMode_dict.get(ans1)
            elif vars['specG'] in dota:
                s = 'dota'
                res = dotaHeros_dict.get(ans1)
            elif vars['specG'] in animal_crossing:
                s = 'animal crossing'
                res = acVillager_dict.get(ans1)
            elif vars['specG'] in undertale:
                s = 'undertale'
                res = underChar_dict.get(ans1)

            #return s
            opinion = spec_Dict.get(s)[2]
            question = spec_Dict.get(s)[3]

            return res+" "+ opinion + " "+question

class SPECIFIC2b(Macro):
    def run(self, ngrams, vars, args) -> str:

         if len(vars['specG']) > 0:
            s = vars['specG']

            #make sure name is uniform
            mario_party = ["super mario party", "jackbox party pack 6", "mario party", "mario party 2", "mario party 3",
                           "mario party 4", "mario party 5", "mario party 6", "mario party 7", "mario party 8",
                           "mario party 9", "mario party 10"]
            pokemon = ["pocket monsters"]
            league_of_legends = ["league"]
            super_smash_bros = ["super smash bros.", "super smash bros. melee", "super smash bros. wii",
                                "super smash bros. ultimate", "super smash bros. for nintendo 3ds and wii u", "smash",
                                "super smash brothers"]
            mario_kart = ["mario kart 64", "mario kart: super circuit", "mario kart: double dash", "mario kart ds",
                          "mario kart wii", "mario kart 7", "mario kart 8", "mario kart 8 deluxe", "mario kart",
                          "mario cart"]
            overwatch = []
            r6s = ["tom clancy's rainbow six siege", "rainbow six siege", "rainbow 6 siege", "r6s"]
            dota = ["defense of the ancients", "dota2"]
            animal_crossing = ["animal crossing", "animal crossing: wild world", "animal crossing: city folk",
                               "animal crossing: new leaf", "ac", "wild world", "acww", "city folk", "accf", "new leaf",
                               "acnl"]
            undertale = []

            if vars['specG'] in mario_party:
                s = 'mario party'
            elif vars['specG'] in pokemon:
                s = 'pokemon'
            elif vars['specG'] in league_of_legends:
                s = 'league of legends'
            elif vars['specG'] in super_smash_bros:
                s = 'super smash brothers'
            elif vars['specG'] in mario_kart:
                s = 'mario kart'
            elif vars['specG'] in overwatch:
                s = 'overwatch'
            elif vars['specG'] in r6s:
                s = 'r6s'
            elif vars['specG'] in dota:
                s = 'dota'
            elif vars['specG'] in animal_crossing:
                s = 'animal crossing'
            elif vars['specG'] in undertale:
                s = 'undertale'

            #return s
            opinion = spec_Dict.get(s)[2]
            question = spec_Dict.get(s)[3]

            return opinion + " "+question


class SPECIFIC3a(Macro):
    def run(self, ngrams, vars, args) -> str:
         if len(vars['specG']) > 0:
            s = vars['specG']
            ans2= vars['ans2']

            #make sure name is uniform
            mario_party = ["mario party", "super mario party",  "jackbox party pack 6", "mario party", "mario party 2", "mario party 3", "mario party 4", "mario party 5", "mario party 6",  "mario party 7", "mario party 8", "mario party 9", "mario party 10"]
            pokemon = ["pokemon", "pocket monsters"]
            league_of_legends=["league of legends", "league"]
            super_smash_bros = ["super smash brothers","super smash bros.","super smash bros. melee", "super smash bros. wii", "super smash bros. ultimate", "super smash bros. for nintendo 3ds and wii u",  "smash", "super smash brothers"]
            mario_kart= ['mario kart',"mario kart 64","mario kart: super circuit", "mario kart: double dash", "mario kart ds", "mario kart wii", "mario kart 7", "mario kart 8", "mario kart 8 deluxe", "mario kart","mario cart"]
            overwatch= ['overwatch']
            r6s = ['r6s',"tom clancy's rainbow six siege", "rainbow six siege","rainbow 6 siege","r6s"]
            dota = ['dota',"defense of the ancients","dota2"]
            animal_crossing = ['animal crossing',"animal crossing", "animal crossing: wild world","animal crossing: city folk","animal crossing: new leaf", "ac","wild world","acww","city folk","accf","new leaf", "acnl"]
            undertale = ["undertale"]

            res = ""
            if vars['specG'] in mario_party:
                s = 'mario party'
                res = mpCharacter_dict.get(ans2)
            elif vars['specG'] in pokemon:
                s = 'pokemon'
                res = pokeType_dict.get(ans2)
            elif vars['specG'] in league_of_legends:
                s = 'league of legends'
                res = leagueMode_dict.get(ans2)
            elif vars['specG'] in super_smash_bros:
                s = 'super smash brothers'
                res = smashStage_dict.get(ans2)
            elif vars['specG'] in mario_kart:
                s = 'mario kart'
                res = mkartCourse_dict.get(ans2)
            elif vars['specG'] in overwatch:
                s = 'overwatch'
                res = overMode_dict.get(ans2)
            elif vars['specG'] in r6s:
                s = 'r6s'
                res = r6sOperator_dict.get(ans2)
            elif vars['specG'] in dota:
                s = 'dota'
                res = dotaMode_dict.get(ans2)
            elif vars['specG'] in animal_crossing:
                s = 'animal crossing'
                res = acThings_dict.get(ans2)
            elif vars['specG'] in undertale:
                s = 'undertale'
                res = underRoute_dict.get(ans2)

            #return s
            opinion = spec_Dict.get(s)[4]
            genre = spec_Dict.get(s)[5]

            return res+ " " + opinion + " What do you think about the "+genre + " genre?"


class SPECIFIC3b(Macro):
    def run(self, ngrams, vars, args) -> str:

         if len(vars['specG']) > 0:
            s = vars['specG']

            #make sure name is uniform
            mario_party = ["super mario party", "jackbox party pack 6", "mario party", "mario party 2", "mario party 3",
                           "mario party 4", "mario party 5", "mario party 6", "mario party 7", "mario party 8",
                           "mario party 9", "mario party 10"]
            pokemon = ["pocket monsters"]
            league_of_legends = ["league"]
            super_smash_bros = ["super smash bros.", "super smash bros. melee", "super smash bros. wii",
                                "super smash bros. ultimate", "super smash bros. for nintendo 3ds and wii u", "smash",
                                "super smash brothers"]
            mario_kart = ["mario kart 64", "mario kart: super circuit", "mario kart: double dash", "mario kart ds",
                          "mario kart wii", "mario kart 7", "mario kart 8", "mario kart 8 deluxe", "mario kart",
                          "mario cart"]
            overwatch = []
            r6s = ["tom clancy's rainbow six siege", "rainbow six siege", "rainbow 6 siege", "r6s"]
            dota = ["defense of the ancients", "dota2"]
            animal_crossing = ["animal crossing", "animal crossing: wild world", "animal crossing: city folk",
                               "animal crossing: new leaf", "ac", "wild world", "acww", "city folk", "accf", "new leaf",
                               "acnl"]
            undertale = []

            if vars['specG'] in mario_party:
                s = 'mario party'
            elif vars['specG'] in pokemon:
                s = 'pokemon'
            elif vars['specG'] in league_of_legends:
                s = 'league of legends'
            elif vars['specG'] in super_smash_bros:
                s = 'super smash brothers'
            elif vars['specG'] in mario_kart:
                s = 'mario kart'
            elif vars['specG'] in overwatch:
                s = 'overwatch'
            elif vars['specG'] in r6s:
                s = 'r6s'
            elif vars['specG'] in dota:
                s = 'dota'
            elif vars['specG'] in animal_crossing:
                s = 'animal crossing'
            elif vars['specG'] in undertale:
                s = 'undertale'

            #return s
            opinion = spec_Dict.get(s)[4]
            genre = spec_Dict.get(s)[5]

            return opinion + " What do you think about the "+ genre + " genre?"
# Synonym generator with NLTK tags
# synonym detection
class syn_det(Macro):
    def run(self, ngrams, vars, args):
        temp = vars['input']
        text = word_tokenize(temp)
        adj = [word for word, pos in nltk.pos_tag(text) if pos[0]=='A' or pos=='JJ' or pos=='VBG']
        return_str = 'why do you think the game is '
        for i in range(len(adj)):
            if i == len(adj)-1 and len(adj) > 1:
                return_str = return_str + 'and ' + adj[i]
            else:
                return_str = return_str + adj[i] + ' '
        if len(adj) == 0: return_str = 'why do you feel this way'
        return return_str

class GENRE_OPINION(Macro):
    def run(self, ngrams, vars, args) -> str:
        if 'type' in vars:
            s = vars['type']

            shooter= ["fps", "first person shooter"]
            beat_em_up= ["beat em up","beat them up", "beet-em-up","beet em up"]
            action_rpg= [ "action role playing game","action"]
            mmorpg= ["massively multiplayer online game","mmog", "mmo"]
            tactical_rpg=["tactical role playing game"]
            sandbox_rpg=[ "sandbox","sandbox rpg"]
            simulation= ["sim"]
            real_time_strategy = ["real time strategy"]
            moba=[ "multiplayer online battle arena"]
            tbs= ["turn-based strategy","turn based strategy"]
            tbt= ["turn-based tactic","turn based tactic"]

            if s in shooter:
                s = "shooter"
            elif s in beat_em_up:
                s = "beat-em-up"
            elif s in action_rpg:
                s = "action"
            elif s in mmorpg:
                s = "mmorpg"
            elif s in tactical_rpg:
                s = "tactical rpg"
            elif s in sandbox_rpg:
                s = "sandbox rpg"
            elif s in simulation:
                s = "simulation"
            elif s in real_time_strategy:
                s = "real-time strategy"
            elif s in moba:
                s = "moba"
            elif s in tbs:
                s = "tbs"
            elif s in tbt:
                s = "tbt"



            x = dict_genre.get(s)
        if s:
            return x
class like_macro(Macro):
    def run(self, ngrams, vars, args):
        temp = vars['like']
        if temp == "":
            temp = "video games"
        return temp
class dislike_macro(Macro):
    def run(self, ngrams, vars, args):
        temp = vars['dislike']
        if temp == "":
            temp = "video games"
        return temp
            