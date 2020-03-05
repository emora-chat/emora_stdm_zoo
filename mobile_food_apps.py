from emora_stdm import KnowledgeBase, DialogueFlow
from enum import Enum,auto

import re
from types import SimpleNamespace
from typing import List, Pattern

class State(Enum):
    START=auto()
    PROMPT_0 = auto()
    PROMPT_1A = auto()
    PROMPT_1B = auto()
    PROMPT_2A = auto()
    PROMPT_2B = auto()
    PROMPT_2B_personal = auto()
    PROMPT_3A = auto()
    PROMPT_3B = auto()
    PROMPT_4 = auto()
    PROMPT_4B = auto()
    PROMPT_4C = auto()
    PROMPT_4D = auto()
    PROMPT_4E = auto()
    PROMPT_5A = auto()
    PROMPT_5B = auto()
    PROMPT_5C = auto()
    PROMPT_5D =auto()
    PROMPT_6 = auto()
    PROMPT_7B = auto()
    PROMPT_7A = auto()
    TURN_0_yes = auto()
    TURN_0_no = auto()
    TURN_1A = auto()
    TURN_1B = auto()
    TURN_1B_personal = auto()
    TURN_2A = auto()
    TURN_2B = auto()
    TURN_3A = auto()
    TURN_3B_delivery = auto()
    TURN_3B_rating = auto()
    TURN_4A = auto()
    TURN_4B = auto()
    TURN_4C = auto()
    TURN_4D = auto()
    TURN_5A = auto()
    TURN_5B = auto()
    TURN_5_Comment = auto()
    TURN_6 = auto()
    TURN_6A = auto()
    TURN_6B = auto()
    TURN_7 = auto()
    Ending_1= auto()
    Ending_2 = auto()
    Ending_3 = auto()
    THE_END_1=auto()
    THE_END_2=auto()
    THE_END_3 = auto()
    THE_END_4=auto()
    THE_END_5 = auto()





    #ERR=auto()
    ERR_APP_NAME_UNKNOWN = auto()
    ERR_PROMPT_1A = auto()
    ERR_PROMPT_1B = auto()
    ERR_PROMPT_2B = auto()
    ERR_PROMPT_3B = auto()
    ERR_PROMPT_4 = auto()
    E_PROMPT_4C=auto()
    E_PROMPT_4D=auto()
    ERR_PROMPT_4C =auto()
    ERR_PROMPT_4D =auto()
    ERR_TURN_5B= auto()



# TODO: create the ontology as needed
foodapp_dict ={
    "ontology":
        {
        "onttype":
            [
                "delivery",
                "food delivery",
                "rating",
                "food rating",
            ],
        "onttype_delivery":
            [
                "delivery",
                "delivery app",
                "food delivery app"
            ],
        "onttype_rating":
            [
                "rating",
                "rating app",
                "food rating app"
            ],
        "ontdelivery":

            [
                "DoorDash",
                "Doordash",
                "doordash",
                "GrubHub",
                "Grubhub",
                "grubhub",
                "Uber",
                "Easts",
                "Uber",
                "Eats",
                "ubereats",
                "UberEats",
                "Seamless",
                "Postmates",
                "goPuff",
                "Instcart",
                "Munchery"

            ],
            "ontrating":
            [
                "Yelp",
                "Foursquare",
                "Urbanspoon",
                "Zagat",
                "OpenTable",
                "LocalEats",
                "DiningGrades",
                "Restaruant Finder"
            ],
        "ontyes":
            [
            "yes",
            "Yes",
            "YES",
            "yeah",
            "yea",
            "sure",
            "Of Course",
            "of course",
            "Sure",
            ],
        "ontno":
            [
            "no",
            "not really",
            "nope",
            "don't",
            "none",
            "No",
            "NO",
            "Nope",
            "nope",
            "Nah",
            "nah"

            ],
        "ontreason": ##related to features of food apps themselves
            [
                "delivery speed",
                "speed",
                "slow",
                "fast",
                "service",
                "delivery",
                "discount",
                 "promotion",
                "customer service",
                "customer support",
                "credit card information",
                "wait",
                "waiting",
                "convenient"
            ],
             "ontreason_personal": ##personal reasons
            [
                "cook",
                "cooking",
                "lazy"
            ]
    }
}

knowledge = KnowledgeBase()
knowledge.load_json(foodapp_dict)
df = DialogueFlow(State.START, initial_speaker=DialogueFlow.Speaker.SYSTEM, kb=knowledge)

df.add_system_transition(State.START, State.PROMPT_0, r'[!"Do you use any food apps?"]')
df.add_user_transition(State.PROMPT_0, State.TURN_0_yes, r'<$TURN_0_yes_response={[!#ONT(ontyes)],[!#ONT(ontdelivery)],[!#ONT(ontrating)],[!#ONT(onttype)]}>')

df.add_system_transition(State.TURN_0_yes, State.PROMPT_1A, '"Do you use it for food delivery or rating?"') ##corner
df.add_user_transition(State.PROMPT_1A, State.TURN_1A, r'<$TURN_1A_response={[!#ONT(onttype)]}>')

df.add_user_transition(State.PROMPT_0, State.TURN_0_no, r'<$TURN_0_no_response={[!#ONT(ontno)]}>')
df.add_system_transition(State.TURN_0_no, State.PROMPT_1B, '"Why are you not you using any food-related apps?"') ##corner

df.add_user_transition(State.PROMPT_1B, State.TURN_1B, r'<$TURN_1B_response=[!#ONT(ontreason)]>')
df.add_user_transition(State.PROMPT_1B, State.TURN_1B_personal, r'<[!#ONT(ontreason_personal)]>')
df.add_system_transition(State.TURN_1B, State.PROMPT_2B, r'[!"I understand. I know some great food-related apps out there though might solve your concerns about" $TURN_1B_response ". Would you want to learn about them?"]')
df.add_system_transition(State.TURN_1B_personal, State.PROMPT_2B_personal, r'[! "I see. What will you do when there is no time to cook though?"]')

df.add_user_transition(State.PROMPT_2B_personal,State.Ending_1,r'/[A-Z a-z]+/')
df.add_system_transition(State.Ending_1, State.THE_END_1,r'[! "Well. if you ever change your mind, come back and let me know. I love helping people find the food apps that they will enjoy the most. Goodbye!"]' )

df.add_user_transition(State.PROMPT_2B, State.TURN_2B, r'<$TURN_2B_yes_response={[!#ONT(ontyes)],[!#ONT(ontdelivery)],[!#ONT(ontrating)],[!#ONT(onttype)]}>')
df.add_system_transition(State.TURN_2B, State.PROMPT_3B, r'[!"Specifically, do you prefer to learn about food delivery or food rating app?"]')

df.add_user_transition(State.PROMPT_3B, State.TURN_3B_delivery, r'<$TURN_3B_response_delivery={[!#ONT(onttype_delivery)]}>')
df.add_user_transition(State.PROMPT_3B, State.TURN_3B_rating, r'<$TURN_3B_response_rating={[!#ONT(onttype_rating)]}>')

###### Apps Recommendation
df.add_system_transition(State.TURN_3B_delivery, State.PROMPT_4C, r'[!"Here is a list of options: DoorDash, GrubHub, Uber, Easts, Uber, Eats, Seamless, Postmates, goPuff, Instcart, Munchery... Any app you are interested in?"]')

df.add_user_transition(State.PROMPT_4C, State.TURN_4C, r'<$TURN_4C_response=[!#ONT(ontdelivery)]>')
df.add_system_transition(State.TURN_4C, State.TURN_5B, r'[! $TURN_4C_response " is currently one of the most popular apps on the market; it delivers from over 50,000 restaurants in 1,100+ cities. Do you have certain restaurants that you prefer to order from? "]')

df.add_system_transition(State.TURN_3B_rating, State.PROMPT_4D, r'[!"Here is a list of options: Yelp, Foursquare, Urbanspoon, Zagat, OpenTable, LocalEats, DiningGrades, Restaruant Finder... Any app you are interested in?"]')
df.add_user_transition(State.PROMPT_4D, State.TURN_4D, r'<$TURN_4D_response=[!#ONT(ontrating)]>')
df.add_system_transition(State.TURN_4D, State.TURN_5B, r'[! $TURN_4D_response " is currently one of the most popular apps on the market; it offers over 50 million reviews for businesses across the world (you can easily search for nearby restaurants, read plenty of reviews, and even view great local deals and photos of the place). Do you have certain types of restaurants you would want to know more about throught that app? "]')

df.add_system_transition(State.ERR_PROMPT_3B, State.PROMPT_4E, r'[!"Here is a list of options: Yelp, Foursquare, Urbanspoon, Zagat, OpenTable, LocalEats, DiningGrades, Restaruant Finder, DoorDash, GrubHub, Uber, Easts, Uber, Eats, Seamless, Postmates, goPuff... Any app you are interested in?"]')
df.add_user_transition(State.PROMPT_4E, State.TURN_4C, r'<$TURN_4C_response=[!#ONT(ontdelivery)]>')
df.add_user_transition(State.PROMPT_4E, State.TURN_4D, r'<$TURN_4D_response=[!#ONT(ontrating)]>')

df.add_user_transition(State.TURN_5B,State.PROMPT_5D, r'[!#ONT(ontyes)]')
df.add_system_transition(State.ERR_TURN_5B, State.Ending_2,r'[!"OK. I hope that you will enjoy using this app. Goodbye!"]')

df.add_system_transition(State.TURN_5B, State.THE_END_2, r'[!"OK. If there are not that many options for the type of restaurants you are looking for on this app, please come back to me. I will recommend you a different one! Goodbye!"]')

###### Apps Recommendation

###### Currently using food apps
df.add_system_transition(State.TURN_1A, State.PROMPT_2A, r'[!"Enter the name of one food app you are using"]')
df.add_user_transition(State.PROMPT_2A, State.TURN_2A, r'<$TURN_2A_DICT={[!#ONT(ontdelivery)],[!#ONT(ontrating)]}>')
df.add_system_transition(State.TURN_2A, State.PROMPT_3A, r'[! Do you enjoy using $TURN_2A_DICT "?"]')

df.add_user_transition(State.PROMPT_3A, State.TURN_4A, r'<$TURN_3A_Yes=[!#ONT(ontyes)]>')
df.add_system_transition(State.TURN_4A, State.PROMPT_4, r'[!"Great! What do you like about" $TURN_2A_DICT "?"]')
df.add_user_transition(State.PROMPT_3A, State.TURN_4B, r'<$TURN_3A_No=[!#ONT(ontno)]>')
df.add_system_transition(State.TURN_4B, State.PROMPT_4, r'[! "Sorry to hear that. What do you not like about" 1 "?"]')
df.add_user_transition(State.PROMPT_4, State.TURN_5A, r'<$TURN_4=[!#ONT(ontreason)]>')

df.add_user_transition(State.TURN_5_Comment, State.TURN_5A,r'/[A-Z a-z]+/')##corner
df.add_system_transition(State.TURN_5A, State.PROMPT_5A, r'[! "Then do you think" $TURN_2A_DICT "could improve in any how ?"]')
df.add_user_transition(State.PROMPT_5A, State.TURN_6, r'<$TURN_5={[!#ONT(ontyes)],[! #ONT(ontno)]}>')
df.add_system_transition(State.TURN_6, State.PROMPT_6, r'[!"Will you consider trying a new food app?"]')

df.add_user_transition(State.PROMPT_6, State.TURN_2B, r'<[!#ONT(ontyes)]>') ##6A same=>2B
df.add_user_transition(State.PROMPT_6, State.TURN_6B, r'<[!#ONT(ontno)]>')

df.add_system_transition(State.TURN_6B, State.PROMPT_7A, r'[!"I see. What would be one feature, though, currently unavailable in the market, that will make you immediately want to switch to that app?"]')
df.add_user_transition(State.PROMPT_7A, State.Ending_3,r'/[A-Z a-z]+/')
df.add_system_transition(State.Ending_3, State.THE_END_3, r'[! I hope someday a food app with that type of feature will be out the market. Goodbye.]')
######

###### corner cases
df.add_system_transition(State.ERR_APP_NAME_UNKNOWN, State.PROMPT_2A, r'[! Sorry. I am not familiar with that app. Please enter another app.]')
df.add_system_transition(State.ERR_PROMPT_4, State.TURN_5_Comment, r'[! Wow. That is an interesting aspect of food application that I have never thought about.]')
df.add_system_transition(State.ERR_PROMPT_3B, State.PROMPT_3B,r'[! "Since you did not specify. Can I introduce options for both to you?"]')
df.add_system_transition(State.ERR_PROMPT_4C, State.THE_END_5,r'[! "None of them sounds appealing to you? Sorry I was not helpful. Goodbye!"]')
df.add_system_transition(State.ERR_PROMPT_4D, State.THE_END_5,r'[! "None of them sounds appealing to you? Sorry I was not helpful. Goodbye!"]')
df.add_system_transition(State.ERR_PROMPT_1A, State.THE_END_4, r'[! "Sorry. I am not familiar with this type of apps. Goodbye!"]')
df.add_system_transition(State.ERR_PROMPT_1B, State.PROMPT_1B, r'[! "Alright. Can you choose one from the following that matters the most to you: delivery speed, customer service, customer support, discount or promotion ?"]')

df.set_error_successor(State.PROMPT_2A, State.ERR_APP_NAME_UNKNOWN)
df.set_error_successor(State.TURN_5B, State.ERR_TURN_5B)
df.set_error_successor(State.PROMPT_4, State.ERR_PROMPT_4)
df.set_error_successor(State.PROMPT_2B, State.Ending_1)
df.set_error_successor(State.PROMPT_3B, State.ERR_PROMPT_3B)
df.set_error_successor(State.PROMPT_4C, State.ERR_PROMPT_4C)
df.set_error_successor(State.PROMPT_4D, State.ERR_PROMPT_4D)
df.set_error_successor(State.PROMPT_4E, State.ERR_PROMPT_4D)
df.set_error_successor(State.PROMPT_1A, State.ERR_PROMPT_1A)
df.set_error_successor(State.PROMPT_1B, State.ERR_PROMPT_1B)

######


# TODO: create your own dialogue manager
df.run(debugging=False)