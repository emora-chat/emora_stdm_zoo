# This is v2 - April 10, 2020

from emora_stdm import KnowledgeBase, DialogueFlow
from enum import Enum
from random import seed
from random import random
from nltk.corpus import wordnet as wn
from collections import OrderedDict
from typing import Set, Optional, List
from nltk.corpus.reader import Synset

# add changes Mar.26 2020 to commit #
# add changes April.10 2020 to commit #
#
# 1. Don't do error-handling as infinite loop
#    Fixed, removed all infinite loop error handlings.
# 2. Seems to repeat the same world wonder even if talked about before in the conversation
#    Fixed, will go in a certain fashion from wonders to wonders and won't repeat
# 3. Doesnt seem to consistently know that the user is talking about a world wonder because it later asks "should this place be added to the list"
#    Fixed, Adjusted wording so that the user knows what wonders are included in the "Eight Wonders List" and they can then decide whether they think the new historic site belongs in the list or not.
# 4. typo: "sciencetist" ==> "scientist"
#    Fixed

class State(Enum):
    START = 0
    WONDER_Q = 1
    WONDER_N = 2
    WONDER_Y = 3
    SITE_Q = 4

    PYRAMID = 100
    PYRAMID_VISIT_Q = 101
    PYRAMID_VISIT_N = 102
    PYRAMID_VISIT_Y = 103
    PYRAMID_BUILD_Q = 104
    PYRAMID_ALIEN = 105
    PYRAMID_WATER = 106
    PYRAMID_RAMP = 107
    PYRAMID_ENGINEERING = 108
    PYRAMID_VISIT_ERR = 109
    PYRAMID_LINKED = 110
    PYRAMID_BUILD_ERR = 111

    PYRAMID_WATER_DETAIL = 120
    PYRAMID_ENGINEERING_DETAIL = 121
    PYRAMID_ALIEN_DETAIL = 122
    PYRAMID_RAMP_DETAIL = 123

    PYRAMID_WATER_TRANSPORT = 130
    PYRAMID_ALIEN_TIMETRAVEL = 131
    PYRAMID_WATER_OTHER = 132
    PYRAMID_ALIEN_OTHER = 133
    PYRAMID_ENGINEERING_RAMP = 134
    PYRAMID_ENGINEERING_PHYSICS = 135
    PYRAMID_ENGINEERING_OTHER = 136

    PYRAMID_ALIEN_TIMETRAVEL_DETAIL = 140
    PYRAMID_ALIEN_OTHER_DETAIL = 141

    PYRAMID_WATER_TRANSPORT_DETAIL = 142
    PYRAMID_WATER_OTHER_DETAIL = 143

    PYRAMID_ENGINEERING_RAMP_DETAIL = 144
    PYRAMID_ENGINEERING_PHYSICS_DETAIL = 145
    PYRAMID_ENGINEERING_OTHER_DETAIL = 146
    PYRAMID_ENGINEERING_OTHER_OPTIONS = 147
    PYRAMID_ENGINEERING_RAMP_DETAIL_1 = 148
    PYRAMID_ENGINEERING_PHYSICS_DETAIL_1 = 149

    PYRAMID_ALIEN_WHY_1 = 150
    PYRAMID_ALIEN_WHY_2 = 151
    PYRAMID_GENERIC_WHY_1 = 152
    PYRAMID_GENERIC_WHY_2 = 153
    PYRAMID_ALIEN_WHY_3 = 154
    PYRAMID_GENERIC_WHY_3 = 155

    PYRAMID_NEG = 156

    PYRAMID_END = 160

    GREATWALL_VISITED_Q = 201
    GREATWALL_VISITED_N = 202
    GREATWALL_VISITED_Y = 203
    GREATWALL_VISITED_Q_ERR = 204
    GREATWALL_WHEN = 205
    GREATWALL_DATE = 206
    GREATWALL_WHY = 207
    GREATWALL_FAR = 208
    GREATWALL_DETAIL = 209
    GREATWALL_REASON = 210
    GREATWALL_MOON = 211
    GREATWALL_LOWEARTH = 212
    GREATWALL_SPACE = 213
    GREATWALL_OTHER = 214
    GREATWALL_END = 215
    GREATWALL_REASON_1 = 216

    GREATWALL = 200
    PETRA = 300
    COLOSSEUM = 400
    CHICHENITZA = 500
    MACHUPICCHU = 600
    TAJMAHAL = 700
    REDEEMER = 800

    PYRAMID_GUESS = 2001
    GREATWALL_GUESS = 2002
    PETRA_GUESS = 2003
    COLOSSEUM_GUESS = 2004
    CHICHENITZA_GUESS = 2005
    MACHUPICCHU_GUESS = 2006
    TAJMAHAL_GUESS = 2007
    REDEEMER_GUESS = 2008

    SITE_OTHER = 900
    SITE_OTHER_LOCATION_Q = 901
    SITE_OTHER_LOCATION_Y = 902
    SITE_OTHER_DATE_Q = 903
    SITE_OTHER_DATE_Y = 904
    SITE_OTHER_DATE_N= 911
    SITE_OTHER_OPINION_Q = 905
    SITE_OTHER_OPINION_Y = 906
    SITE_OTHER_OPINION_N = 907
    SITE_OTHER_PYRAMID = 908
    TO_PYRAMID = 909
    SITE_OTHER_LOCATION_N = 910
    SITE_OTHER_OPINION_Q_ERR = 912

    WONDER_Q_ERR = 1000
    PYRAMID_ENGINEERING_OTHER_OPTIONS_ERR = 999

# ontology #
ontology = {
    "ontology": {
        "NO":
            ["no", "not", "nah", "changed my mind", "disagree", "never", "not"],
        "YES":
            ["fine", "yes", "yeah", "yea", "sure", "of course", "right", "i am",  "i do", "I have", "agree", "Yes", "Yes,", "yes,", "definitely"],
        "PYRAMID":
            ["pyramid","egypt","giza", "Pyramids", "Pyramid", "pyramids", "desert"],
        "PYRAMID_FEATURE":
            ["tomb", "body", "pharaoh", "death", "grave", "graveyard", "eternal", "life", "god"],
        "GREATWALL":
            ["great wall", "greatwall", "china", "beijing","Great Wall", "Greatwall", "Great wall"],
        "PETRA":
            ["petra", "rose city", "jordan"],
        "COLOSSEUM":
            ["colosseum", "italy", "rome"],
        "CHICHENITZA":
            ["chichen", "itza", "mexico", "yucatan", "kukulcan", "castillo"],
        "MACHUPICCHU":
            ["machu picchu", "peru"],
        "TAJMAHAL":
            ["taj", "mahal", "india"],
        "REDEEMER":
            ["redeemer", "brazil", "rio de janeiro", "rio", "Rio"]
        }
}

# start #
knowledge = KnowledgeBase()
knowledge.load_json(ontology)
df = DialogueFlow(State.START, initial_speaker=DialogueFlow.Speaker.SYSTEM, kb=knowledge)

df.add_system_transition(State.START, State.WONDER_Q, '"Hi, I have been fascinated by the historic sites of human civilizations. Do you know about the New Seven Wonders of the World?"')
df.add_user_transition(State.WONDER_Q, State.WONDER_N, '[#ONT(NO)]')
df.add_user_transition(State.WONDER_Q, State.WONDER_Y, '[#ONT(YES)]')

df.add_system_transition(State.WONDER_N, State.SITE_Q,'"Well, the New Seven Wonders of the World is a list of historic sites based on more than 100 million votes. The idea originated from the original Seven Wonders of the World compiled by Philo of Byzantium in 225 B.C.E. Which historic site do you think was included in the new World Wonders?"')
df.add_system_transition(State.WONDER_Y, State.SITE_Q, '"Great! Those historic sites were chosen by more than 100 million votes and I think all of them are magnificant. Which World Wonder is your favorite?"')

# wonders menu #
df.add_user_transition(State.SITE_Q, State.PYRAMID, '[{pyramid, egypt, egyptian, giza, pyramids}]')
df.add_user_transition(State.SITE_Q, State.GREATWALL, '[{great wall, china, chinese}]')
df.add_user_transition(State.SITE_Q, State.PETRA, '[{petra, jordan, nabatean, rose city}]')
df.add_user_transition(State.SITE_Q, State.COLOSSEUM, '[{colosseum, italy, rome}]')
df.add_user_transition(State.SITE_Q, State.CHICHENITZA, '[{chichen, itza, mexico, yucatan, kukulcan, castillo}]')
df.add_user_transition(State.SITE_Q, State.MACHUPICCHU, '[{machu picchu, peru}]')
df.add_user_transition(State.SITE_Q, State.TAJMAHAL, '[{taj, mahal, india}]')
df.add_user_transition(State.SITE_Q, State.REDEEMER, '[{redeemer, brazil, rio de janeiro}]')
df.add_user_transition(State.SITE_Q, State.PYRAMID_NEG, '[{#ONT(NO), know, dont}]')

df.add_system_transition(State.PYRAMID_NEG, State.PYRAMID_VISIT_Q, '"Well, since you have no idea, why not start with the pyramids first? You see, the Great Pyramid of Giza was not part of the seven world wonders. But it was later added to the list with a honorary status. Have you visited the Great Pyramid of Giza before?"')

# PYRAMID #
# https://www.theguardian.com/world/2018/nov/06/new-discovery-throws-light-on-mystery-of-pyramids-construction
# https://curiosity.com/topics/we-may-finally-know-how-the-pyramids-were-built-curiosity/
# https://www.bbvaopenmind.com/en/science/physics/physics-unveils-the-mysteries-of-the-egyptian-pyramids/
# https://www.express.co.uk/news/weird/940347/Time-travel-speed-of-light-prof-aliens-built-pyramids-UFO
df.add_user_transition(State.PYRAMID_LINKED, State.PYRAMID, '[#ONT(YES)]')
df.add_system_transition(State.PYRAMID, State.PYRAMID_VISIT_Q, '"Well, let us start with a little history about the the pyramids. You see, the Great Pyramid of Giza was not part of the seven world wonders. But it was later added to the list with a honorary status. Have you visited the Great Pyramid of Giza before?"')
df.add_user_transition(State.PYRAMID_VISIT_Q, State.PYRAMID_VISIT_N, '[#ONT(NO)]')
df.add_user_transition(State.PYRAMID_VISIT_Q, State.PYRAMID_VISIT_Y, '[#ONT(YES)]')
df.add_system_transition(State.PYRAMID_VISIT_N, State.PYRAMID_BUILD_Q, '"You should go when you get a chance! It was a mystery how ancient Egyptians were able to cut and transport heavy stones. How do you think they built it?"')
df.add_system_transition(State.PYRAMID_VISIT_Y, State.PYRAMID_BUILD_Q, '"That must be an amazing experience! It was a mystery how ancient Egyptians were able to cut and transport heavy stones. How do you think they built it?"')
df.add_user_transition(State.PYRAMID_BUILD_Q, State.PYRAMID_ALIEN, '[{alien, god, supernatural}]' )
df.add_user_transition(State.PYRAMID_BUILD_Q, State.PYRAMID_WATER, '[{water, canal, wet, humid}]')
df.add_user_transition(State.PYRAMID_BUILD_Q, State.PYRAMID_RAMP, '[{ramp, pull, incline, slope}]')
df.add_user_transition(State.PYRAMID_BUILD_Q, State.PYRAMID_ENGINEERING, '[{engineering, machine, device, structure}]')

# PYRAMID PART TWO - ALIEN #
df.add_system_transition(State.PYRAMID_ALIEN, State.PYRAMID_ALIEN_DETAIL, '"Indeed. The construction of the pyramids were far beyond the means of the early Egyptians, so some people believed that they must have had outside help. Do you have any thoughts on how the aliens might have built the pyramids?"')

df.add_user_transition(State.PYRAMID_ALIEN_DETAIL, State.PYRAMID_ALIEN_TIMETRAVEL, '[{time, travel, speed, future, past}]')
df.add_user_transition(State.PYRAMID_ALIEN_DETAIL, State.PYRAMID_ALIEN_OTHER, '[{know, idea, #ONT(NO)}]')

# PYRAMID PART THREE - ALIEN - TIMETRAVEL
df.add_system_transition(State.PYRAMID_ALIEN_TIMETRAVEL, State.PYRAMID_ALIEN_TIMETRAVEL_DETAIL, '"Yeah. Some people believed that aliens traveled back in time to build the pyramid. The speed of light is 299792458 metres per second and the geographic coordinates for the Great Pyramid are 29 point 9792458 north. What a coincidence! Why do you think the aliens would help humans build the pyramid though?"')

# PYRAMID PART THREE - ALIEN - OTHER
df.add_system_transition(State.PYRAMID_ALIEN_OTHER, State.PYRAMID_ALIEN_OTHER_DETAIL, '"Umm, I do not know about that. The speed of light is 299792458 metres per second and the geographic coordinates for the Great Pyramid are 29 point 9792458 north. What a coincidence! Why do you think the aliens would help humans build the pyramid though?"')

# PYRAMID PART TWO - WATER #
df.add_system_transition(State.PYRAMID_WATER, State.PYRAMID_WATER_DETAIL,'"Well, we have proofs that the Ancient Egyptians built the pyramids. However, there are many theories about how the Egyptians built the pyramids. Some people believed that the Ancient Egyptians used water shafts to build pyramids sounds probable. How do you think the Ancient Egyptians used the water shafts in order to help with the pyramid building process?"')

df.add_user_transition(State.PYRAMID_WATER_DETAIL, State.PYRAMID_WATER_TRANSPORT, '[{transport, transportation, shaft, force, up, down, go, travel, smooth}]')
df.add_user_transition(State.PYRAMID_WATER_DETAIL, State.PYRAMID_WATER_OTHER, '[{know, idea, #ONT(NO)}]')

# PYRAMID PART THREE - WATER - TRANSPORT
df.add_system_transition(State.PYRAMID_WATER_TRANSPORT, State.PYRAMID_WATER_TRANSPORT_DETAIL, '"Indeed. Some people believed that the water canals near the pyramids lead to a moat that went all the way around the build site perimeter, allowing blocks to be floated to the side where they were needed. Also, the Ancient Egyptians could have used the water currents to shape the rocks for the pyramids. Why do you think the Ancient Egyptians build the pyramids?"')

# PYRAMID PART THREE - WATER - OTHER
df.add_system_transition(State.PYRAMID_WATER_OTHER, State.PYRAMID_WATER_OTHER_DETAIL, '"Umm, I do not know about that. However, ome people believed that the water canals near the pyramids lead to a moat that went all the way around the build site perimeter, allowing blocks to be floated to the side where they were needed. Also, the Ancient Egyptians could have used the water currents to shape the rocks for the pyramids. Why do you think the Ancient Egyptians build the pyramids?"')


# PYRAMID PART TWO - ENGINEERING AND RAMP #
df.add_system_transition(State.PYRAMID_RAMP, State.PYRAMID_RAMP_DETAIL, '"Well, we have proofs that the Ancient Egyptians built the pyramids. However, there are many theories about how the Egyptians built the pyramids. Some people believed that the Ancient Egyptians usedramps to transport raw materials for pyramids. How do you think the Ancient Egyptians used the ramps to transport those materials?"')
df.add_system_transition(State.PYRAMID_ENGINEERING, State.PYRAMID_ENGINEERING_DETAIL, '"Well, we have proofs that the Ancient Egyptians built the pyramids. However, there are many theories about how the Egyptians built the pyramids. Some people believed that the Ancient Egyptians used a combination of physics, simple tools and engineering techniques in order to build the pyramid. What engineering techniques do you think they used?"')

df.add_user_transition(State.PYRAMID_RAMP_DETAIL, State.PYRAMID_ENGINEERING_RAMP, '[{ramp, transport, transportation, travel, smooth}]')
df.add_user_transition(State.PYRAMID_RAMP_DETAIL, State.PYRAMID_ENGINEERING_PHYSICS, '[{physics, science, engineering, tools}]')
df.add_user_transition(State.PYRAMID_RAMP_DETAIL, State.PYRAMID_ENGINEERING_OTHER, '[{know, idea, #ONT(NO)}]')
df.add_user_transition(State.PYRAMID_ENGINEERING_DETAIL, State.PYRAMID_ENGINEERING_RAMP, '[{ramp, transport, transportation, travel, smooth}]')
df.add_user_transition(State.PYRAMID_ENGINEERING_DETAIL, State.PYRAMID_ENGINEERING_PHYSICS, '[{physics, science, engineering, tools}]')
df.add_user_transition(State.PYRAMID_ENGINEERING_DETAIL, State.PYRAMID_ENGINEERING_OTHER, '[{know, idea, #ONT(NO)}]')

# PYRAMID PART THREE - ENGINEERING AND RAMP - RAMP
df.add_system_transition(State.PYRAMID_ENGINEERING_RAMP, State.PYRAMID_ENGINEERING_RAMP_DETAIL, '"Indeed. Some people and scientists believed that mud brick ramps were used to move blocks up the side of the partially built pyramid. They claim that the Ancient Egyptians dragged the stones and rocks up ramps made of mud bricks using timber rollers. Why do you think the Ancient Egyptians build the pyramids?"')

# PYRAMID PART THREE - ENGINEERING AND RAMP - PHYSICS
df.add_system_transition(State.PYRAMID_ENGINEERING_PHYSICS, State.PYRAMID_ENGINEERING_PHYSICS_DETAIL, '"Indeed. Some people and scientists believed that the Ancient Egyptians used simple physics and tools and built the pyramids. Some scientists suggested that the ancient Egyptians could have attached cylindrical pieces of wood to the stones on all four sides. By doing so, the Ancient Egyptians could roll them instead of dragging them, on surfaces they laid along the way ahead of time to make the work easier. Anyway, why do you think the Ancient Egyptians build the pyramids?"')

# PYRAMID PART THREE - ENGINEERING AND RAMP - OTHER
df.add_system_transition(State.PYRAMID_ENGINEERING_OTHER, State.PYRAMID_ENGINEERING_OTHER_OPTIONS, '"Umm, I do not know about that. There are mainly two theories about how the Ancient Egyptians used engineering to build the pyramids. The ramp theory and the physics theory. Which sounds more probable to you?"')

df.add_user_transition(State.PYRAMID_ENGINEERING_OTHER_OPTIONS, State.PYRAMID_ENGINEERING_RAMP_DETAIL_1, '[{ramp, transport, transportation, travel, smooth}]')
df.add_user_transition(State.PYRAMID_ENGINEERING_OTHER_OPTIONS, State.PYRAMID_ENGINEERING_PHYSICS_DETAIL_1, '[{physics, science, engineering, tools}]')

df.add_system_transition(State.PYRAMID_ENGINEERING_RAMP_DETAIL_1, State.PYRAMID_ENGINEERING_RAMP_DETAIL, '"I agree with you. Ramp theory sounds more probable to me personally. Why do you think they built the pyramids?"')
df.add_system_transition(State.PYRAMID_ENGINEERING_PHYSICS_DETAIL_1, State.PYRAMID_ENGINEERING_PHYSICS_DETAIL, '"I agree with you. Physics sounds more probable to me personally. Why do you think they built the pyramids?"')

# PYRAMID WHY BUILD - USER #
df.add_user_transition(State.PYRAMID_ALIEN_TIMETRAVEL_DETAIL, State.PYRAMID_ALIEN_WHY_1, '[$user_1=#ONT(PYRAMID_FEATURE)]')
df.add_user_transition(State.PYRAMID_ALIEN_OTHER_DETAIL, State.PYRAMID_ALIEN_WHY_1, '[$user_1=#ONT(PYRAMID_FEATURE)]')

df.add_user_transition(State.PYRAMID_ALIEN_TIMETRAVEL_DETAIL, State.PYRAMID_ALIEN_WHY_2, '[$user_1=#POS(noun)]')
df.add_user_transition(State.PYRAMID_ALIEN_OTHER_DETAIL, State.PYRAMID_ALIEN_WHY_2, '[$user_1=#POS(noun)]')

df.set_error_successor(State.PYRAMID_ALIEN_TIMETRAVEL_DETAIL, State.PYRAMID_ALIEN_WHY_3)
df.set_error_successor(State.PYRAMID_ALIEN_OTHER_DETAIL, State.PYRAMID_ALIEN_WHY_3)

df.add_user_transition(State.PYRAMID_WATER_TRANSPORT_DETAIL, State.PYRAMID_GENERIC_WHY_1, '[$user_1=#ONT(PYRAMID_FEATURE)]')
df.add_user_transition(State.PYRAMID_WATER_OTHER_DETAIL, State.PYRAMID_GENERIC_WHY_1, '[$user_1=#ONT(PYRAMID_FEATURE)]')

df.add_user_transition(State.PYRAMID_WATER_TRANSPORT_DETAIL, State.PYRAMID_GENERIC_WHY_2, '[$user_1=#POS(noun)]')
df.add_user_transition(State.PYRAMID_WATER_OTHER_DETAIL, State.PYRAMID_GENERIC_WHY_2, '[$user_1=#POS(noun)]')

df.set_error_successor(State.PYRAMID_WATER_TRANSPORT_DETAIL, State.PYRAMID_GENERIC_WHY_3)
df.set_error_successor(State.PYRAMID_WATER_OTHER_DETAIL, State.PYRAMID_GENERIC_WHY_3)

df.add_user_transition(State.PYRAMID_ENGINEERING_RAMP_DETAIL, State.PYRAMID_GENERIC_WHY_1, '[$user_1=#ONT(PYRAMID_FEATURE)]')
df.add_user_transition(State.PYRAMID_ENGINEERING_PHYSICS_DETAIL, State.PYRAMID_GENERIC_WHY_1, '[$user_1=#ONT(PYRAMID_FEATURE)]')

df.add_user_transition(State.PYRAMID_ENGINEERING_RAMP_DETAIL, State.PYRAMID_GENERIC_WHY_2, '[$user_1=#POS(noun)]')
df.add_user_transition(State.PYRAMID_ENGINEERING_PHYSICS_DETAIL, State.PYRAMID_GENERIC_WHY_2, '[$user_1=#POS(noun)]')

df.set_error_successor(State.PYRAMID_ENGINEERING_RAMP_DETAIL, State.PYRAMID_GENERIC_WHY_3)
df.set_error_successor(State.PYRAMID_ENGINEERING_PHYSICS_DETAIL, State.PYRAMID_GENERIC_WHY_3)

# PYRAMID WHY BUILD - SYSTEM #

df.add_system_transition(State.PYRAMID_ALIEN_WHY_1, State.GREATWALL_VISITED_Q, '"Indeed, I believe the Giza Pyramids were built for that! It is well accepted by the general public that the pyramids were built by ancient egyptians and the alien theory is generally considered as a conspiracy theory and is incorrect. Enough about the pyramids, let us head to the Great Wall in China next! Have you visited the Great Wall?"')
df.add_system_transition(State.PYRAMID_ALIEN_WHY_2, State.GREATWALL_VISITED_Q, '"I do not know that the Giza Pyramids were built for that! I always thought the the pyramids were meant to be tombs for the ancient egyptian pharaohs. It is well accepted by the general public that the pyramids were built by ancient egyptians and the alien theory is generally considered as a conspiracy theory and is incorrect. Enough about the pyramids, let us head to the Great Wall in China next! Have you visited the Great Wall?"')
df.add_system_transition(State.PYRAMID_ALIEN_WHY_3, State.GREATWALL_VISITED_Q, '"Well, I do not know about that, but I always thought the the pyramids were meant to be tombs for the ancient egyptian pharaohs. It is well accepted by the general public that the pyramids were built by ancient egyptians and the alien theory is generally considered as a conspiracy theory and is incorrect. Enough about the pyramids, let us head to the Great Wall in China next! Have you visited the Great Wall?"')

df.add_system_transition(State.PYRAMID_GENERIC_WHY_1, State.GREATWALL_VISITED_Q, '"Yes! That is what I thought! The Giza Pyramids were built for that! Enough about the pyramids, let us head to the Great Wall in China next! Have you visited the Great Wall?"')
df.add_system_transition(State.PYRAMID_GENERIC_WHY_2, State.GREATWALL_VISITED_Q, '"I do not know that the Giza Pyramids were built for that! I always thought the the pyramids were meant to be tombs for the ancient egyptian pharaohs. Enough about the pyramids, let us head to the Great Wall in China next! Have you visited the Great Wall?"')
df.add_system_transition(State.PYRAMID_GENERIC_WHY_3, State.GREATWALL_VISITED_Q, '"Well, I do not know about that, but I always thought the the pyramids were meant to be tombs for the ancient egyptian pharaohs. Enough about the pyramids, let us head to the Great Wall in China next! Have you visited the Great Wall?"')

# PYRAMID TRANSITION - PART FOUR #

#df.add_user_transition(State.PYRAMID_END, State.GREATWALL, '[#ONT(GREATWALL)]')
#df.add_user_transition(State.PYRAMID_END, State.PETRA, '[#ONT(PETRA)]')
#df.add_user_transition(State.PYRAMID_END, State.COLOSSEUM, '[#ONT(COLOSSEUM)]')
#df.add_user_transition(State.PYRAMID_END, State.CHICHENITZA, '[#ONT(CHICHENITZA)]')
#df.add_user_transition(State.PYRAMID_END, State.MACHUPICCHU, '[#ONT(MACHUPICCHU)]')
#df.add_user_transition(State.PYRAMID_END, State.TAJMAHAL, '[#ONT(TAJMAHAL)]')
#df.add_user_transition(State.PYRAMID_END, State.REDEEMER, '[#ONT(REDEEMER)]')
#df.set_error_successor(State.PYRAMID_END, State.SITE_OTHER)


# GREATWALL - PART ONE #
df.add_system_transition(State.GREATWALL, State.GREATWALL_VISITED_Q, '"Well, the Great Wall in China is definitely magnificient! Have you visited the Great Wall before?"')
df.add_user_transition(State.GREATWALL_VISITED_Q, State.GREATWALL_VISITED_Y, '[#ONT(YES)]')
df.add_user_transition(State.GREATWALL_VISITED_Q, State.GREATWALL_VISITED_N, '[#ONT(NO)]')

df.set_error_successor(State.GREATWALL_VISITED_Q, State.GREATWALL_VISITED_Q_ERR)
df.add_system_transition(State.GREATWALL_VISITED_Q_ERR, State.GREATWALL_WHY, '"It does not matter whether you have visited the Great Wall before. The great wall is magnificent and is more than 13000 miles! Why do you think the Chinese people build the Great Wall?"')

# GREATWALL - PART TWO #
df.add_system_transition(State.GREATWALL_VISITED_Y, State.GREATWALL_WHEN, '"Oh that is fantastics! I have never been there but I would definitely want to visit the great wall some day myself! When did you visit the great wall?"')
df.add_user_transition(State.GREATWALL_WHEN, State.GREATWALL_DATE, '[{$date_1=#NER(date)}]')
df.set_error_successor(State.GREATWALL_WHEN, State.GREATWALL_DATE)
df.add_system_transition(State.GREATWALL_DATE, State.GREATWALL_WHY, '"That seems like a long time ago. I doubt whether you remeber how long the great wall is. It is more than 13000 miles long.  Why do you think the Chinese people build the Great Wall?"')

df.add_system_transition(State.GREATWALL_VISITED_N, State.GREATWALL_WHY, '"I have never been there either. You should definitely go there some day! I heard it is more than 13000 miles long. Why do you think the Chinese people build the Great Wall?"')

# GREATWALL - PART THREE #
df.add_user_transition(State.GREATWALL_WHY, State.GREATWALL_REASON, '[$reason_greatwall=#POS(noun,verb)]')
df.set_error_successor(State.GREATWALL_WHY, State.GREATWALL_REASON_1)
df.add_system_transition(State.GREATWALL_REASON, State.GREATWALL_FAR, '"Well, what you said definitely makes sense and is a great point. A popular belief is that the Chinese people built the Great Wall to protect and consolidate territories of Chinese states and empires against various nomadic groups of the steppe and their polities. Now, let me ask you a question. One of this most interesting stories about the Great Wall is its visibility from space. How far from the Earth do you think we can see the Great Wall?"')
df.add_system_transition(State.GREATWALL_REASON_1, State.GREATWALL_FAR, '"Well, let me tell you about it. A popular belief is that the Chinese people built the Great Wall to protect and consolidate territories of Chinese states and empires against various nomadic groups of the steppe and their polities. Now, let me ask you a question. One of this most interesting stories about the Great Wall is its visibility from space. How far from the Earth do you think we can see the Great Wall?"')

# GREATWALL - PART FOUR #
df.add_user_transition(State.GREATWALL_FAR, State.GREATWALL_MOON, '[{moon}]')
df.add_user_transition(State.GREATWALL_FAR, State.GREATWALL_LOWEARTH, '[{earth, orbit, low}]')
df.add_user_transition(State.GREATWALL_FAR, State.GREATWALL_SPACE, '[{space}]')
df.add_user_transition(State.GREATWALL_FAR, State.GREATWALL_OTHER, '[{know, idea, #ONT(NO)}]')
df.set_error_successor(State.GREATWALL_FAR, State.GREATWALL_OTHER)

df.add_system_transition(State.GREATWALL_MOON, State.GREATWALL_END, '"It is a common misconception that we can see the great wall from the moon. The apparent width of the Great Wall from the Moon would be the same as that of a human hair viewed from two miles away. However, the great wall is visible to the naked eye from low Earth orbit. Can you guess which other wonder is visible from low Earth orbit?\n DIALOGUE ENDS HERE FOR NOW"')
df.add_system_transition(State.GREATWALL_LOWEARTH, State.GREATWALL_END, '"Yes that is right. The great wall is visible to the naked eye from low Earth orbit. Can you guess which other wonder is visible from low Earth orbit?\n DIALOGUE ENDS HERE FOR NOW"')
df.add_system_transition(State.GREATWALL_SPACE, State.GREATWALL_END, '"The concept of space is a little vague. It is a common misconception that we can see the great wall from the moon. The apparent width of the Great Wall from the Moon would be the same as that of a human hair viewed from two miles away. However, the great wall is visible to the naked eye from low Earth orbit. Can you guess which other wonder is visible from low Earth orbit?\n DIALOGUE ENDS HERE FOR NOW"')
df.add_system_transition(State.GREATWALL_OTHER, State.GREATWALL_END, '"Well I can tell you that the great wall is visible to the naked eye from low Earth orbit but not from the moon. Can you guess which other wonder is visible from low Earth orbit? \n DIALOGUE ENDS HERE FOR NOW"')

# GREATWALL - PART FIVE - TRANSITION #
df.add_user_transition(State.GREATWALL_END, State.PYRAMID_GUESS, '[#ONT(PYRAMID)]')
df.add_user_transition(State.GREATWALL_END, State.PETRA_GUESS, '[#ONT(PETRA)]')
df.add_user_transition(State.GREATWALL_END, State.COLOSSEUM_GUESS, '[#ONT(COLOSSEUM)]')
df.add_user_transition(State.GREATWALL_END, State.CHICHENITZA_GUESS, '[#ONT(CHICHENITZA)]')
df.add_user_transition(State.GREATWALL_END, State.MACHUPICCHU_GUESS, '[#ONT(MACHUPICCHU)]')
df.add_user_transition(State.GREATWALL_END, State.TAJMAHAL_GUESS, '[#ONT(TAJMAHAL)]')
df.add_user_transition(State.GREATWALL_END, State.REDEEMER_GUESS, '[#ONT(REDEEMER)]')
df.set_error_successor(State.GREATWALL_END, State.SITE_OTHER)

# PETRA
df.add_system_transition(State.PETRA, State.PYRAMID_LINKED, '"Well, the petra in the desert of Jordan is definitely magnificient! Do you know the Great Pyramid of Giza? The Great Pyramid of Giza was not part of the seven world wonders. But it was later added to the list with a honorary status. Have you visited the Great Pyramid of Giza before?"')
# COLOSSEUM
df.add_system_transition(State.COLOSSEUM, State.PYRAMID_LINKED, '"Well, the oval amphitheatre in the centre of the city of Rome, called the colosseum, is definitely magnificient! Do you know the Great Pyramid of Giza? The Great Pyramid of Giza was not part of the seven world wonders. But it was later added to the list with a honorary status. Have you visited the Great Pyramid of Giza before?"')
# CHICHENITZA
df.add_system_transition(State.CHICHENITZA, State.PYRAMID_LINKED, '"Well, the large pre-Columbian city built by the Maya people, called the Chichen Itza, is definitely magnificient! Do you know the Great Pyramid of Giza? The Great Pyramid of Giza was not part of the seven world wonders. But it was later added to the list with a honorary status. Have you visited the Great Pyramid of Giza before?"')
# MACHUPICCHU
df.add_system_transition(State.MACHUPICCHU, State.PYRAMID_LINKED, '"Well, the Incan citadel set high in the Andes Mountains in Peru, called Machu Picchu, is definitely magnificient! Do you know the Great Pyramid of Giza? The Great Pyramid of Giza was not part of the seven world wonders. But it was later added to the list with a honorary status. Have you visited the Great Pyramid of Giza before?"')
# TAJMAHAL
df.add_system_transition(State.TAJMAHAL, State.PYRAMID_LINKED, '"Well, the Taj Mahal, which is an ivory-white marble mausoleum on the south bank of the Yamuna river in the Indian city of Agra, is definitely magnificient! Do you know the Great Pyramid of Giza? The Great Pyramid of Giza was not part of the seven world wonders. But it was later added to the list with a honorary status. Have you visited the Great Pyramid of Giza before?"')
# REDEEMER
df.add_system_transition(State.REDEEMER, State.PYRAMID_LINKED, '"Well, Christ the redeemer in Rio de Janeiro is definitely magnificient! Do you know the Great Pyramid of Giza? The Great Pyramid of Giza was not part of the seven world wonders. But it was later added to the list with a honorary status. Have you visited the Great Pyramid of Giza before?"')

# other site #
df.add_system_transition(State.SITE_OTHER, State.SITE_OTHER_LOCATION_Q, '"Hmm...I have never heard about this site but I bet it is amazing! Where is it located?"')
df.add_user_transition(State.SITE_OTHER_LOCATION_Q, State.SITE_OTHER_LOCATION_Y, '[{$location=#NER(loc)}]')
df.add_system_transition(State.SITE_OTHER_LOCATION_Y, State.SITE_OTHER_DATE_Q, '"Oh I always wanted to learn more about the history of"$location". When was that historic site built? Do you know what was it for?"')
df.add_system_transition(State.SITE_OTHER_LOCATION_N, State.SITE_OTHER_DATE_Q, '"I see. I truly do not know this historic site. When was that historic site built? Do you know what was it for?"')
df.add_user_transition(State.SITE_OTHER_DATE_Q, State.SITE_OTHER_DATE_Y, '[{$date=#NER(date)}]')

df.add_system_transition(State.SITE_OTHER_DATE_Y, State.SITE_OTHER_OPINION_Q, '"There was definitely had an interesting history in"$date". Do you think they should add this historic site to the World Wonders? The Eight Wonders of the World include the Great Pyramids of Giza, the Great Wall in China, the Petra in Jordan, the Colosseum in the city of Rome, the Chichen Itza in Mexico, Machu Picchu in Peru, Taj Mahal in India, and the redeemer in Brazil."')

df.add_user_transition(State.SITE_OTHER_OPINION_Q,State.SITE_OTHER_OPINION_Y, '[{#ONT(YES)}]')
df.add_user_transition(State.SITE_OTHER_OPINION_Q,State.SITE_OTHER_OPINION_N, '[{#ONT(NO)}]')


df.add_system_transition(State.SITE_OTHER_OPINION_Y, State.SITE_OTHER_PYRAMID, '"I agree. They should consider expanding the list to include more sites. There are so many world wonders out there beyond the current seven. Have your heard about the Egyptian pyramids?"')
df.add_system_transition(State.SITE_OTHER_OPINION_N, State.SITE_OTHER_PYRAMID, '"I agree. This historic site sounds interesting but it is not really a world wonder. Have your heard about the Egyptian pyramids?"')
df.add_user_transition(State.SITE_OTHER_PYRAMID, State.TO_PYRAMID,'[/.*/]')
df.add_system_transition(State.TO_PYRAMID, State.PYRAMID_VISIT_Q, '"You see, the Great Pyramid of Giza was also not part of the seven world wonders. But it was later added to the list with a honorary status as number eight. Have you visited the Great Pyramid of Giza before?"')

# error handling #
df.set_error_successor(State.WONDER_Q, State.WONDER_Q_ERR)
df.add_system_transition(State.WONDER_Q_ERR, State.SITE_Q, '"OK. The New Seven Wonders of the World is a list of historic sites based on more than 100 million votes. The idea originated from the original Seven Wonders of the World compiled by Philo of Byzantium in 225 B.C.E. Can you guess which historic site was included in the new World Wonders? "')
df.set_error_successor(State.SITE_Q, State.SITE_OTHER)
df.set_error_successor(State.SITE_OTHER_LOCATION_Q, State.SITE_OTHER_LOCATION_N)

df.set_error_successor(State.SITE_OTHER_DATE_Q, State.SITE_OTHER_DATE_N)
df.add_system_transition(State.SITE_OTHER_DATE_N, State.SITE_OTHER_OPINION_Q, '"I see. Do you think they should add this historic site to the World Wonders? The Eight Wonders of the World include the Great Pyramids of Giza, the Great Wall in China, the Petra in Jordan, the Colosseum in the city of Rome, the Chichen Itza in Mexico, Machu Picchu in Peru, Taj Mahal in India, and the redeemer in Brazil."')

df.set_error_successor(State.SITE_OTHER_OPINION_Q, State.SITE_OTHER_OPINION_Q_ERR)
df.add_system_transition(State.SITE_OTHER_OPINION_Q_ERR, State.PYRAMID_VISIT_Q, '"Well, I think this should definitely be added to the existing Wonder of the World List! The great pyramids of giza was also not part of the seven world wonders originally, but it was later added to the list with a honorary status as number eight. Have you visited the Great Pyramid of Giza before?"')

df.set_error_successor(State.PYRAMID_VISIT_Q, State.PYRAMID_VISIT_ERR)
df.add_system_transition(State.PYRAMID_VISIT_ERR, State.PYRAMID_BUILD_Q, '"Well, it does not matter whether you have visited the Giza Pyramids before. How do you think they built it though?"')
df.set_error_successor(State.PYRAMID_BUILD_Q, State.PYRAMID_BUILD_ERR)
df.add_system_transition(State.PYRAMID_BUILD_ERR, State.PYRAMID_RAMP_DETAIL, '"Well, one of the theories is that they used a ramp in order to transport the stones and raw materials for the pyramids. How do you think the Ancient Egyptians used the ramps to transport those materials?"')

df.set_error_successor(State.PYRAMID_ALIEN_DETAIL, State.PYRAMID_ALIEN_OTHER)
df.set_error_successor(State.PYRAMID_WATER_DETAIL, State.PYRAMID_WATER_OTHER)
df.set_error_successor(State.PYRAMID_ENGINEERING_DETAIL, State.PYRAMID_ENGINEERING_OTHER)
df.set_error_successor(State.PYRAMID_RAMP_DETAIL, State.PYRAMID_ENGINEERING_OTHER)

df.set_error_successor(State.PYRAMID_ENGINEERING_OTHER_OPTIONS, State.PYRAMID_ENGINEERING_OTHER_OPTIONS_ERR)
df.add_system_transition(State.PYRAMID_ENGINEERING_OTHER_OPTIONS_ERR, State.PYRAMID_ENGINEERING_RAMP_DETAIL, '"Well, there are only two mainstream theories about how the Egyptians used engineering techniques to build to pyramids. The ramp theory and the physics theory, I personally think the ramp theory sounds more probable. Why do you think the ancient egyptians build the pyramids though?"')

if __name__ == '__main__':
    df.run(debugging=False)