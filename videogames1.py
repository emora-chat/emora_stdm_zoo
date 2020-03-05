#!/usr/bin/env python
# coding: utf-8

# In[691]:


from enum import Enum
import emora_stdm
from emora_stdm import NatexNLU, NatexNLG
from emora_stdm import DialogueFlow, KnowledgeBase
import re
from emora_stdm import Macro
import random

# Use case:
# if __name__ == '__main__':
#     natex = NatexNLU('[!oh #MyMacro(there) how are you]', macros={'MyMacro': MyMacro(2)})
#     assert natex.match('oh hello there hello there how are you')

class State(Enum):
    ERR = 100
    ERR2= 101
    GAME_ERROR=102
    START = 0
    START_REPLY = 1
    LIKE_GAME_Y = 2
    LIKE_GAME_N = 3
    SMART_PERSON=12
    SMART_PERSON_REPLY=13
    
    GAME_TYPE = 4
    GAME_TYPE_REPLY = 5
    GAME_TYPE_OK = 6
    
    GAME_INTEREST = 7
    TEAM_GAMES = 8
    TEAM_OK = 9
    SOLO_OK = 10
    
    TEAM_REPLY= 11
    SOLO_REPLY=14
    MULTI_LIST=15
    SOLO_LIST=16
    SOLO_REPLY2=17
    MULTI_REPLY=18
    CARE=19
    
    DONT_CARE=20
    RUDE=21
    INTEREST=22
    FAVORITE_CHAR=23
    CHAR_DISCUSSION=24
    CHAR_EXPLAIN=25
    CHAR_UNDERSTAND=26
    
    SINGLE_P=27
    SOLO_LIST_GUESS = 30
    SOLO_LIST_GUESS_Y = 28
    SOLO_LIST_GUESS_N = 29
    DUMB_PERSON_REPLY=31
    
    DISLIKE_LOL=32
    DISLIKE_RESPONSE=33
    GAME_TYPE_REPLY_N=34
    MULTI_ADD=35
    MULTI_ADD_CONT=36
    LEARN_MULTI=37
    LEARN_CONF=38
    
    GENRE = 40
    GENRE_REPLY = 41
    GENRE_REDIR = 42
    GENRE_SUGGEST=43
    GENRE_DISCUSS=44
    
    UNDERTALE_N=45
    GENRE_REC=46
    GENRE_AFFIRM=47
    SOLO_LIST_GUESS_Q=48
    SOLO_LIST_GUESS_W=49
    SOLO_ENGAGE=50
    SOLO_DECLINE=51
    SOLO_URGE=52
    SOLO_END = 53
    
    GUESS_GAME=54
    SOLO_ANSWER=55
    NEW_GAME_TALK=57
    GUESS_CORRECT=58
    GUESS_INCORRECT=59
    UNDERTALE_Y=56
    
    #
        
# Dictionary

ont_dict = {"ontology": 
                {
                "game_type":
                 [
                     "fps",
                     "rpg",
                     "action",
                     "simulation",
                     "strategy",
                     "puzzle",
                     "horror" 
                 ],
                 "fps": 
                 [
                     "call of duty", 
                     "rainbow six seige"
                 ], 
                 "rpg": 
                 [
                     "pokemon",
                     "monster hunter",
                     "undertale"
                 ],
                "action":
                [
                    "demons souls",
                    "dark souls",
                    "dark souls: artorias of the abyss",
                    "dark souls ii",
                    "dark souls ii: the lost crowns",
                    "dark souls ii: scholar of the first sin",
                    "dark souls iii",
                    "dark souls iii: ashes of ariandel",
                    "dark souls iii: the ringed city",
                    "dark souls remastered"
                ],
                "simulation":
                [
                    "the sims",
                    "the sims 2",
                    "the sims 3",
                    "the sims 4",
                    "animal crossing",
                    "ac",
                    "animal crossing: wild world",
                    "acww",
                    "animal crossing: city folk",
                    "accf",
                    "animal crossing: new leaf",
                    "acnl",
                    "animal crossing: new horizons",
                    "acnh"
                ],
                "strategy":
                [
                    "plants vs. zombies",
                    "pvz",
                    "plants vs. zombies 2",
                    "pvz2",
                    "plants vs. zombies: garden warfare",
                    "pvz:gw",
                    "plants vs. zombies. garden warfare 2",
                    "pvz:gw2",
                    "dota",
                    "defense of the ancients",
                    "dota 2",
                    "defense of the ancients 2",
                    "lol",
                    "league of legends",
                    "league"
                ],
                "puzzle":
                [
                    "portal",
                    "portal 2",
                    "minesweeper",
                    "bejeweled",
                    "tetris",
                    "baba is you",
                    "human: fall flat"
                ],
                "horror":
                [
                    "silent hill",
                    "alien: isolation",
                    "resident evil 7: biohazard",
                    "outlast",
                    "outlast ii",
                    "the outlast trials",
                    "outlast: whistleblower",
                    "five nights at freddys",
                    "fnaf",
                    "five nights at freddys 2",
                    "fnaf2",
                    "five nights at freddys 3",
                    "fnaf3",
                    "five nights at freddys 4",
                    "fnaf4",
                    "five nights at freddys: sister location",
                    "freddy fazbears pizzeria simulator",
                    "five nights at freddys: help wanted",
                    "fnaf world",
                    "ultimate custom night",
                    "five nights at freddys ar: special delivery",
                    "freddy in space 2"
                ],
                 "multiplayer":
                    [
                        "league of legends",
                        "monster hunter",
                        "dota",
                        "defense of the ancients",
                        "dota 2",
                        "defense of the ancients 2",
                        "lol",
                        "plants vs. zombies: garden warfare",
                        "pvz:gw",
                        "plants vs. zombies. garden warfare 2",
                        "pvz:gw2",
                        "animal crossing: new horizons",
                        "acnh",
                        "rainbow six siege",
                        "call of duty"
                    ],
                "singleplayer":
                    [
                        "pokemon",
                        "nier",
                        "demons souls",
                        "dark souls",
                        "dark souls: artorias of the abyss",
                        "dark souls ii",
                        "dark souls ii: the lost crowns",
                        "dark souls ii: scholar of the first sin",
                        "dark souls iii",
                        "dark souls iii: ashes of ariandel",
                        "dark souls iii: the ringed city",
                        "dark souls remastered",
                        "the sims",
                        "the sims 2",
                        "the sims 3",
                        "the sims 4",
                        "animal crossing",
                        "ac",
                        "animal crossing: wild world",
                        "acww",
                        "animal crossing: city folk",
                        "accf",
                        "animal crossing: new leaf",
                        "acnl"
                        "silent hill",
                        "alien: isolation",
                        "resident evil 7: biohazard",
                        "outlast",
                        "outlast ii",
                        "the outlast trials",
                        "outlast: whistleblower",
                        "five nights at freddys",
                        "fnaf",
                        "five nights at freddys 2",
                        "fnaf2",
                        "five nights at freddys 3",
                        "fnaf3",
                        "five nights at freddys 4",
                        "fnaf4",
                        "five nights at freddys: sister location",
                        "freddy fazbears pizzeria simulator",
                        "five nights at freddys: help wanted",
                        "fnaf world",
                        "ultimate custom night",
                        "five nights at freddys ar: special delivery",
                        "freddy in space 2"
                        "portal",
                        "portal 2",
                        "minesweeper",
                        "bejeweled",
                        "tetris",
                        "baba is you",
                        "human: fall flat"
                        "plants vs. zombies",
                        "pvz",
                        "plants vs. zombies 2",
                        "pvz2",
                        "undertale"
                    ]
                }
           }


# In[687]:


# Useful regex 
#/(?:^|\s)(yea|yes|yeah|i do|i like)(?:\s|,|\.|$)/
# Used for finding input after a certain word
#/((?(?=.*?(\b(?:was)\b).*?)\2|.*))/
# all inputs accepted
#/.*/ 


#idea: would not be useful to have macros for everything; use them to handle edge cases


# In[695]:


# Function to add user transition states that uses "yes" regex
def yes_add():
    tup_list = [(State.START_REPLY, State.LIKE_GAME_Y), (State.GAME_TYPE, State.GAME_TYPE_REPLY),
                (State.SMART_PERSON, State.SMART_PERSON_REPLY), (State.GAME_TYPE_OK, State.GAME_INTEREST),
               (State.CHAR_UNDERSTAND, State.SOLO_ENGAGE), (State.SOLO_REPLY2, State.UNDERTALE_Y)]
    regex = "<$response=/(?:^|\s)(yea|ya|ye|yes|yeah|do|into|like|ok|love|enjoy|really|appreciate|fun|sure|why|i will|type of game|kind of game)(?:\s|,|\.|$)/>"
    for i in tup_list:
        df.add_user_transition(i[0], i[1], regex)
    
def no_add():
    tup_list = [(State.START_REPLY, State.LIKE_GAME_N), (State.GAME_TYPE, State.GAME_TYPE_REPLY_N),
               (State.SMART_PERSON, State.DUMB_PERSON_REPLY), (State.MULTI_REPLY, State.DONT_CARE),
               (State.SOLO_REPLY2, State.UNDERTALE_N), (State.CHAR_UNDERSTAND, State.SOLO_DECLINE)]
    regex = "<$response={/(?:^|\s)(no|not|nah|nope|dont want to|im not smart|stupid|i am dumb|i dont like|i nope|i dislike)(?:\s|,|\.|$)/}>"
    for i in tup_list:
        df.add_user_transition(i[0], i[1], regex)


# In[ ]:



class MyMacro(Macro):

    # optionally, define constructor if macro needs access to additional data
    def __init__(self, x):
        self.x = x

    # define method to run when macro is evaluated in Natex
    def run(self, ngrams, vars, args):
        """
        :param ngrams: an Ngrams object defining the set of all ngrams in the
                       input utterance (for NLU) or vocabulary (for NLG). Treat
                        like a set for all ngrams, or get a specific ngram set
                        using ngrams[n]. Get original string using .text()
        :param vars: a reference to the dictionary of variables
        :param args: a list of arguments passed to the macro from the Natex
        :returns: string, set, boolean, or arbitrary object
                  returning a string will replace the macro call with that string
                  in the natex
                  returning a set of strings replaces macro with a disjunction
                  returning a boolean will replace the macro with wildcards (True)
                  or an unmatchable character sequence (False)
                  returning an arbitrary object is only used to pass data to other macros
        """
        temp = ont_dict["ontology"]
        return random.choice(temp[args[0]])


# In[713]:


knowledge = KnowledgeBase()
knowledge.load_json(ont_dict)
df = DialogueFlow(State.START, initial_speaker=DialogueFlow.Speaker.SYSTEM, kb=knowledge, macros={'MyMacro':MyMacro(1)})

# Function to add user transition states that uses "yes" regex
yes_add()
no_add()

df.add_system_transition(State.START, State.START_REPLY, '"hi! my name is roko. i love playing video games, and its kind of the only thing i do. do you like games?"')
# df.add_user_transition(State.START_REPLY, State.LIKE_GAME_Y, "<$response=/(?:^|\s)(yea|ya|ye|yes|yeah|i do|i like)(?:\s|,|\.|$)/>")
# df.add_user_transition(State.START_REPLY, State.LIKE_GAME_N, "<$response={no, nope, nah, no way, i dont}>")
df.set_error_successor(State.START_REPLY, State.ERR)
df.add_system_transition(State.ERR, State.START_REPLY, '"Hmm.. i only like video games"')

# df.add_system_transition(State.LIKE_GAME_Y, State.GAME_TYPE, '[!oh #MyMacro(there) how are you]')
df.add_system_transition(State.LIKE_GAME_Y, State.GAME_TYPE, '"cool beans. are you into strategy games? i love strategy games."')
df.add_system_transition(State.LIKE_GAME_N, State.SMART_PERSON, '"thats crazy! you should try playing some. maybe i can recommend some. are you a smart person?"')

# df.add_user_transition(State.GAME_TYPE, State.GAME_TYPE_REPLY, "<$response={/(?:^|\s)(yea|ye|ya|yes|yeah|i do|i like)(?:\s|,|\.|$)/, #ONT(game_type)}>")
# df.add_user_transition(State.GAME_TYPE, State.GAME_TYPE_REPLY_N, "<$response={/(?:^|\s)(no|not|nah|i dont like|i nope|i dislike)(?:\s|,|\.|$)/, #ONT(game_type)}>")

df.add_system_transition(State.GAME_TYPE_REPLY_N, State.GENRE, '"well what genre of games do you like?"')
df.add_user_transition(State.GENRE, State.GENRE_REPLY, "<$genre={horror, fps, rpg}>")
df.set_error_successor(State.GENRE, State.GENRE_REDIR)
df.add_system_transition(State.GENRE_REDIR, State.GAME_TYPE_OK, '"hmmm...sorry i dont play too many games of that genre but might i suggest league of legends? its my favorite game"')
df.add_system_transition(State.GENRE_REPLY, State.GENRE_DISCUSS, '[! $genre " games huh? i know a couple of good ones. have you tried" #MyMacro($genre)]')
df.add_user_transition(State.GENRE_DISCUSS, State.GENRE_REC, '/.*/')
df.add_system_transition(State.GENRE_REC, State.GENRE_AFFIRM, '"its a super game!but do you know what my favorite game is?"')
df.add_user_transition(State.GENRE_AFFIRM, State.GAME_TYPE_REPLY, '/.*/')
                         
# System
df.add_system_transition (State.GAME_TYPE_REPLY, State.GAME_TYPE_OK, '"league of legends is fun. its one of my favorite games"')
# Error
df.set_error_successor(State.GAME_TYPE_OK, State.ERR2)
df.add_system_transition(State.ERR2, State.GENRE, '"this conversation isnt going to go anywhere if you dont expand your horizons...is there a genre of game you like?"')


# df.add_user_transition(State.SMART_PERSON, State.SMART_PERSON_REPLY, "<$response={/(?:^|\s)(yea|ye|yes|yeah|i am smart|i am)(?:\s|,|\.|$)/}>")
# df.add_user_transition(State.SMART_PERSON, State.DUMB_PERSON_REPLY, "<$response={/(?:^|\s)(no|not|nah|nope|im not smart |i am dumb)(?:\s|,|\.|$)/}>")
df.add_system_transition(State.DUMB_PERSON_REPLY, State.GAME_TYPE_OK,'"you should try playing league of legends"."its a pretty braindead game"."its my favorite game"')
df.add_system_transition(State.SMART_PERSON_REPLY, State.GAME_TYPE_OK, '"smart people enjoy strategy games. you should try league of legends"')

# df.add_user_transition(State.GAME_TYPE_OK, State.GAME_INTEREST, "<$response={ok, sure, why, i will, type of game, kind of game, like, enjoy}>")
df.add_system_transition(State.GAME_INTEREST, State.TEAM_GAMES, '"league of legends is a team based game. i like team based games because theyre more social. do you like playing games with a team or by yourself?"')

df.add_user_transition(State.TEAM_GAMES, State.TEAM_OK, "<$response={team, with people, teams}>")
df.add_user_transition(State.TEAM_GAMES, State.SOLO_OK, "<$response={alone, by myself, solo}>")
df.add_user_transition(State.GAME_TYPE_OK, State.DISLIKE_LOL, "<$response={dislike, dont like, hate}>")

df.add_system_transition(State.TEAM_OK, State.TEAM_REPLY, '"playing with people is definitely more fun. what multiplayer games do you like?"')
df.set_error_successor(State.TEAM_REPLY, State.MULTI_ADD)
df.add_system_transition(State.MULTI_ADD, State.MULTI_ADD_CONT, '"wow ive never heard of that game before but i would like to learn about it. what did you say the name was?"')
df.add_user_transition(State.MULTI_ADD_CONT, State.LEARN_MULTI, "$multi={/((?(?=.*?(\b(?:was|said)\b).*?)\2|.*))/}")
df.add_system_transition(State.LEARN_MULTI, State.MULTI_REPLY, '$multi " sounds like a dope game ill try it out. do you know why i love multiplayer games?"')


df.add_system_transition(State.SOLO_OK, State.SOLO_REPLY, '"What solo games do you like?"')
df.add_system_transition(State.DISLIKE_LOL, State.DISLIKE_RESPONSE, '"how can you say you dislike something without trying it out?"')

df.add_user_transition(State.TEAM_REPLY, State.MULTI_LIST, "<$multi={#ONT(multiplayer)}>")
df.add_user_transition(State.SOLO_REPLY, State.SOLO_LIST, "<$single={#ONT(singleplayer)}>")
df.set_error_successor(State.SOLO_REPLY, State.MULTI_ADD)

df.add_system_transition(State.MULTI_LIST, State.MULTI_REPLY, '[! i also like $multi"." do u want to know why i like these sorts of multiplayer games"?"]')
df.add_system_transition(State.SOLO_LIST, State.SOLO_REPLY2, '"If you like solo games, you should try undertale. have you heard of the game before?"')
# user_add(undertale_n)
df.add_system_transition(State.UNDERTALE_Y, State.GAME_TYPE_OK, '"of course you have! its a great game. but league of legends is even better i would say. do u want to know why?"')
df.add_system_transition(State.UNDERTALE_N, State.GAME_TYPE_OK, '"its a fun game! but you should try league of legends. league is my favorite game"')

df.add_user_transition(State.MULTI_REPLY, State.CARE, "<$response={why}>")
# df.add_user_transition(State.MULTI_REPLY, State.DONT_CARE, "<$response={dont care, no, nah, im ok}>")
df.add_system_transition(State.DONT_CARE, State.RUDE, "how rude. are there other games you would like to talk to me about")
df.add_user_transition(State.RUDE, State.NEW_GAME_TALK, "<$response={/.*/}>")
df.add_system_transition(State.NEW_GAME_TALK, State.MULTI_ADD_CONT, '"that sounds like a fun game. what is the name of it exactly?"')
df.add_system_transition(State.CARE, State.INTEREST, 'its because multiplayer games are very interactive"." playing interactive games helps me understand people"..." whats your favorite character in $multi"?"')

df.add_user_transition(State.INTEREST, State.FAVORITE_CHAR, "$character={/((?(?=.*?(\b(?:like|love|use|play|is)\b).*?)\2|.*))/}")
df.add_system_transition(State.FAVORITE_CHAR, State.CHAR_DISCUSSION, '"Sounds like an awesome character. why do you enjoy playing him?"')
df.add_user_transition(State.CHAR_DISCUSSION, State.CHAR_EXPLAIN, "<$response={/.*/}>")
df.add_system_transition(State.CHAR_EXPLAIN, State.CHAR_UNDERSTAND, '[! thats interesting i will try that character out the next time i play $multi"." thank you for the recommendation. in all honesty, though, sometimes i get bored of multiplayer games and i swap to singleplayer games. guess which single player game i like the most"!"]')

df.add_user_transition(State.CHAR_UNDERSTAND, State.SOLO_LIST_GUESS, '<$single={#ONT(singleplayer)}>')
df.add_user_transition(State.CHAR_UNDERSTAND, State.SOLO_LIST_GUESS_W, '<$response={/(?:^|\s)(which|undertale)(?:\s|,|\.|$)/}>')
#df.add_user_transition(State.CHAR_UNDERSTAND, State.SOLO_ENGAGE) yes
#char understand, solo decline, no
df.add_system_transition(State.SOLO_LIST_GUESS, State.SOLO_LIST_GUESS_Y, '"how did u guess? i love that game! the story is very good"')
df.add_system_transition(State.SOLO_LIST_GUESS, State.SOLO_LIST_GUESS_Q, '"i like the game undertale. have played it before?"')
df.add_system_transition(State.SOLO_ENGAGE, State.GUESS_GAME, '"well go ahead and try!"')
df.add_system_transition(State.SOLO_LIST_GUESS_W, State.SOLO_ANSWER, "i love the game undertale. it fills me with determination. i highly recommend it")
df.add_system_transition(State.SOLO_DECLINE, State.SOLO_URGE, "awww ok well i guess then i will just tell you. i love the game undertale. it fills me with determination. i highly recommend it")
df.add_user_transition(State.SOLO_URGE, State.SOLO_END, '<$response={/.*/}>')
df.add_user_transition(State.SOLO_ANSWER, State.SOLO_END, '<$response={/.*/}>')
df.add_system_transition(State.SOLO_END, State.GAME_TYPE_OK, "but my favorite game is definitely league of legends. its such a great game")
df.add_user_transition(State.GUESS_GAME, State.GUESS_CORRECT, '<$response={undertale}>')
df.set_error_successor(State.GUESS_GAME,State.GUESS_INCORRECT)
df.add_system_transition(State.GUESS_INCORRECT, State.SOLO_ANSWER, "i actually love the game undertale. it fills me with determination and love.")
df.add_system_transition(State.GUESS_CORRECT, State.GAME_TYPE_OK, '"great guess. undertale is a great game"')
# df.add_system_transition(State.GUESS_INCORRECT, State.GAME_TYPE_OK, "Nope! its undertale. is give the game 10 stars out of 10")

df.run(debugging=False)

