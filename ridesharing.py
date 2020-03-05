from emora_stdm import KnowledgeBase, DialogueFlow
from enum import Enum
from emora_stdm import NatexNLU


# TODO: Update the State enum as needed
class State(Enum):
    START = 0
    PROMPT = 1
    INFORMED = 2
    UNINFORMED = 3
    FREQUENCY = 4
    NEVER = 5
    INFREQUENT = 6
    FREQUENT = 7

    ERR1 = 9
    INFOQUESTION = 10
    OCCASION = 11
    TIME = 12
    CONVO = 13
    READY1 = 14
    CHOICE = 15
    READY2 = 16
    READY3 = 17
    LYFTUBER = 18
    REASON = 19
    COST = 20
    SAFETY = 21
    EFFICIENCY = 22
    AMBIGUOUS = 23
    ERR2 = 24
    ERR3 = 25
    ERR4 = 26
    COST1 = 27
    SAFETY1 = 28
    EFFICIENCY1 = 29
    AMBIGUOUS1 = 30
    CONCERNS = 31
    INFOQUESTION1 = 32
    ERR5 = 33
    ERR6 = 34
    READY4 = 35

    #CONVO sequence
    NO_TALK = 36
    DESTINATION = 37
    CAREER_AC = 38
    PREV_CD = 39

    #SATISFACTION sequence
    SATISFACTION = 40
    CAREER = 41
    CHANGES = 42
    RESPONSE = 43
    GREAT = 44
    UNFORT = 45
    FB_THANKS = 46

    #SELFDRIVE sequence
    SELFDRIVE = 47
    HAPPY = 48
    HURT = 49

    #PREF sequence
    PREF = 50
    WALK = 51
    PRIV = 52
    PUBLIC = 53
    RIDESHARE = 54
    TERMINAL = 55

    EXCUSE = 56
    FEEDBACK = 57

    #additional error states
    ERR7 = 58
    ERR8 = 59
    ERR9 = 60
    ERR10 = 61
    ERR11 = 62
    ERR12 = 63



# TODO: create the ontology as needed
ontology = {
    "ontology": {

        }
}


knowledge = KnowledgeBase()
knowledge.load_json(ontology)
df = DialogueFlow(State.START, initial_speaker=DialogueFlow.Speaker.SYSTEM, kb=knowledge)

#Turn 1
#Natex
yes_nlu = r"[$answer={[yes], [yeah], [yep], [yup], [definitely], [of course]}]"
no_nlu = r"[$answer={[no], [not], [nah], [nope], [little], [maybe]}]"

#Transitions
df.add_system_transition(State.START, State.PROMPT, '"Are you familiar with Uber and Lyft?"')
df.add_user_transition(State.PROMPT, State.INFORMED, yes_nlu)
df.add_user_transition(State.PROMPT, State.UNINFORMED, no_nlu)

df.add_system_transition(State.ERR1, State.PROMPT, r'[!Sorry, was that yes or no"?"]')

#Turn 2a - INFORMED
#Natex
never_nlu = r"[$answer={[never], [do not], [have not], [havent], [I dont], [none], [bus], [cab]}]"
infr_nlu = r"[$answer={[sometimes], [occasionally], [not much], [once], [few], [month], [monthly], [hardly], [rarely], [not sure], [dont know]}]"
freq_nlu = r"[$answer={[often], [a lot], [always], [too much], [daily], [weekly], [regularly], [day], [week], [all]}]"

#Transitions
df.add_system_transition(State.INFORMED, State.FREQUENCY, '"How often do you use ride sharing apps?"')
df.add_user_transition(State.FREQUENCY, State.NEVER, never_nlu)
df.add_user_transition(State.FREQUENCY, State.INFREQUENT, infr_nlu)
df.add_user_transition(State.FREQUENCY, State.FREQUENT, freq_nlu)

df.add_system_transition(State.ERR2, State.FREQUENCY, r'[!hm, Im confused. Can you use different words please"?"]')

#Turn 2b1 - UNINFORMED
cost_natex = r"[$answer={[cost], [fare], [money], [cheap], [inexpensive], [expensive], [cheaper], [costs], [credit], [wallet], [dollar], [dollars], [spend]}]"
safety_natex = r"[$answer={[safe], [safer], [safely], [danger], [dangerous], [safest], [scared], [trust], [dark], [night]}]"
efficiency_natex = r"[$answer={[easy], [convenient], [efficient], [useful], [handy], [easier], [intuitive]}]"

df.add_system_transition(State.UNINFORMED, State.INFOQUESTION, '"Two of the most common ridesharing apps are Uber and Lyft. Uber started about 10 years ago and Lyft started about 7 years ago. What other information would you like to know?"')
df.add_user_transition(State.INFOQUESTION, State.COST1, cost_natex)
df.add_user_transition(State.INFOQUESTION, State.SAFETY1, safety_natex)
df.add_user_transition(State.INFOQUESTION, State.EFFICIENCY1, efficiency_natex)
df.set_error_successor(State.INFOQUESTION, State.AMBIGUOUS1)

#Turn 2b2 - INFOQUESTION
df.add_system_transition(State.INFOQUESTION1, State.INFOQUESTION, '"What is another question you have?"')

#Turn 3a - NEVER
df.add_system_transition(State.NEVER, State.EXCUSE,'"Why not?"')
df.add_user_transition(State.EXCUSE, State.READY1, "/.*/")

#Turn 3b - INFREQUENT
df.add_system_transition(State.INFREQUENT, State.OCCASION,'"For what occasions do you use it?"')
df.add_user_transition(State.OCCASION, State.READY2, "/.*/")

#Turn 3c - FREQUENT
time_natex = r"{[$number=/\d+/,$time_type={month,months,year,years}]}"
vars_dict = {"f": "good"}
df.add_system_transition(State.FREQUENT, State.TIME,'"How long have you been using it?"')
df.add_user_transition(State.TIME, State.READY3, time_natex)

df.add_system_transition(State.ERR3, State.TIME, r'[!Hm, Im confused. How many months or years has it been"?"]')

#Turn 3d - COST1
df.add_system_transition(State.COST1, State.CONCERNS,'"Both Uber and Lyft provide a range of options. For Uber, UberPool is the cheapest, then UberX, then premium options. Similarly, Lyft Shared is cheapest, then Lyft, then premium options. Exact prices range depending on location and time of day (surge charges during busy times). Customers are generally satisfied with the cost of both. Do you have any other questions about Uber and Lyft?"')

#Turn 3e - EFFICIENCY1
df.add_system_transition(State.EFFICIENCY1, State.CONCERNS,'"Both Lyft and Uber connect you to rides in minutes. Their algorithms calculate the fastest way to get where you need to be. Certain cities are known for being more Uber friendly, while others are more Lyft friendly, but even in smaller towns both are expanding their reach. With Uber, beware the new express Pool walking option, which can take longer. Both also have scooters, though some cities are struggling to accomodate them. Generally, customers are satisfied with the convenience of both ridesharing. Do you have any other questions about Uber and Lyft?"')

#Turn 3f - SAFETY1
df.add_system_transition(State.SAFETY1, State.CONCERNS,'"Both hide your personal information from drivers, and include information about the car and license plate so you know where you are stepping into. They both have built in 911 calls, you can share your trip with your friends/family, and all drivers are screened. One main difference is with Lyft you can end your trip at any time, and Uber provides insurrance. I could not find information on each feature on the others website. Do you have any other questions about Uber and Lyft?"')

#Turn 3g - AMBIGUOUS1
df.add_system_transition(State.AMBIGUOUS1, State.CONCERNS,'"Hm I dont know about that, but Im sure its on their websites: lyft.com and uber.com. Do you have any other questions about Uber and Lyft?"')

df.add_user_transition(State.CONCERNS, State.INFOQUESTION1, yes_nlu)
df.add_user_transition(State.CONCERNS, State.READY4, no_nlu)
df.add_user_transition(State.CONCERNS, State.COST1, cost_natex)
df.add_user_transition(State.CONCERNS, State.SAFETY1, safety_natex)
df.add_user_transition(State.CONCERNS, State.EFFICIENCY1, efficiency_natex)
df.set_error_successor(State.CONCERNS, State.AMBIGUOUS1)

#Turn 4 - READY
lyftOrUber_natex = r"[$uberlyft={[Uber], [uber], [Lyft], [lyft]}]"
df.add_system_transition(State.READY1, State.CHOICE, r'[!Ok, that makes sense"," but if you had to use ridesharing, between Uber and Lyft, which would you use"?"]')
df.add_system_transition(State.READY2, State.CHOICE, r'[!Ok, that makes sense"," so if you had to use ridesharing, between Uber and Lyft, which would you use"?"]')
df.add_system_transition(State.READY3, State.CHOICE, r'[!Oh $number $time_type is a good amount of time. Between Uber and Lyft, which would you use"?"]')
df.add_system_transition(State.READY4, State.CHOICE, '"Now that you know more about ride sharing, between Uber and Lyft, which would you use?"')

df.add_user_transition(State.CHOICE, State.LYFTUBER, lyftOrUber_natex)

df.add_system_transition(State.ERR4, State.CHOICE, r'[!While you may prefer another option or have no preference, the purpose of this survey is to track preference between Uber and Lyft. Which do you prefer"?"]')

#Turn 5
df.add_system_transition(State.LYFTUBER, State.REASON, r'[!Ah, a popular choice, $uberlyft has many benefits. Why do you prefer $uberlyft"?"]')
df.add_user_transition(State.REASON, State.COST, cost_natex)
df.add_user_transition(State.REASON, State.SAFETY, safety_natex)
df.add_user_transition(State.REASON, State.EFFICIENCY, efficiency_natex)
df.set_error_successor(State.REASON, State.AMBIGUOUS)

df.add_system_transition(State.ERR7, State.REASON, r'[!Sorry, could you rephrase that"?"]')

#Turn 6
quiet_natex = r"[$answer={[like talking], [silence], [quiet]}]"
going_natex = r"[$answer={[where], [going to], [destination], [event], [place], [location]}]"
career_natex = r"[$answer={[college], [grades], [major], [school], [academics], [study]}]"
past_natex = r"[$answer={[previous], [in the past], [had before], [ridiculous], [insane], [crazy]}]"



df.add_system_transition(State.COST, State.CONVO, r'[!Yeah, $uberlyft is pretty easy on your wallet. So what do you usually talk about with your driver"?"]')
df.add_system_transition(State.SAFETY, State.CONVO, r'[!Yeah I agree, $uberlyft cares a lot about your safety. So what do you usually talk about with your driver"?"]')
df.add_system_transition(State.EFFICIENCY, State.CONVO, r'[!Yeah, $uberlyft is definitely super convenient. So what do you usually talk about with your driver"?"]')
df.add_system_transition(State.AMBIGUOUS, State.CONVO, r'[!Yeah that makes sense. So what do you usually talk about with your driver"?"]')

df.add_user_transition(State.CONVO, State.NO_TALK, quiet_natex)
df.add_user_transition(State.CONVO, State.DESTINATION, going_natex)
df.add_user_transition(State.CONVO, State.CAREER_AC, career_natex)
df.add_user_transition(State.CONVO, State.PREV_CD, past_natex)

df.add_system_transition(State.ERR8, State.CONVO, r'[!Sorry, what was that"?"]')

#Turn 7
soso_natex = r"[$answer={[bad], [unpleasant], [awful], [not good], [poor], [moderately], [somewhat], [kinda], [kind of], [a bit]}]"
good_natex = r"[$answer={[very], [great], [awesome], [love], [satisfied], [fantastic]}]"

df.add_system_transition(State.NO_TALK, State.SATISFACTION, r'[!Ahh, quiet type I see. By the way, how satisfied are you with ridesharing apps in general"?"]')
df.add_system_transition(State.DESTINATION, State.SATISFACTION, r'[!Where are we going"?" I ask that myself all the time. By the way, how satisfied are you with ridesharing apps in general"?"]')
df.add_system_transition(State.CAREER_AC, State.SATISFACTION, r'[!Interesting, I always love hearing about what people are doing with their lives"!" By the way, how satisfied are you with ridesharing apps in general"?"]')
df.add_system_transition(State.PREV_CD, State.SATISFACTION, r'[!Those are always good stories. By the way, how satisfied are you with ridesharing apps in general"?"]')

df.add_user_transition(State.SATISFACTION, State.CHANGES, soso_natex)
df.add_user_transition(State.SATISFACTION, State.CAREER, good_natex)

df.add_system_transition(State.ERR11, State.SATISFACTION, r'[!Wait, how do you feel about ride sharing apps again "?"]')

#Turn 8
df.add_system_transition(State.CAREER, State.RESPONSE, r'[!Awesome, would you be open to pursuing a career as a ride share driver"?"]')
df.add_system_transition(State.CHANGES, State.FEEDBACK, r'[!Thanks for the honesty, could you provide us with some feedback as to how we could improve your experience"?"]')

df.add_user_transition(State.RESPONSE, State.GREAT, yes_nlu)
df.add_user_transition(State.RESPONSE, State.UNFORT, no_nlu)
df.add_user_transition(State.FEEDBACK, State.FB_THANKS, "/.*/")

df.add_system_transition(State.ERR12, State.CAREER, r'[!Didnt quite catch that, could you try to put it in different words "?"]')

#Turn 9
df.add_system_transition(State.GREAT, State.SELFDRIVE, r'[!Great to hear that"!" I also considered that before. Tell me, would you trust a ride share car driven by an AI"?"]')
df.add_system_transition(State.UNFORT, State.SELFDRIVE, r'[!That is unfortunate, I have considered it before though. Do you think you would trust a ride share car driven by an AI"?"]')

df.add_user_transition(State.SELFDRIVE, State.HAPPY, yes_nlu)
df.add_user_transition(State.SELFDRIVE, State.HURT, no_nlu)

df.add_system_transition(State.ERR9, State.SELFDRIVE, r'[!Come again"?"]')


#Turn 10
walk_natex = r"[$answer={[walking], [walk], [excercise], [biking], [bike]}]"
priv_natex = r"[$answer={[own], [car], [personal], [private], [I have], [my own]}]"
public_natex = r"[$answer={[subway], [tram], [MARTA], [public], [taxi], [train], [AMTRAK], [tube]}]"
rideshare_natex = r"[$answer={[ride share], [ride sharing], [Lyft], [Uber], [lyft], [uber]}]"

df.add_system_transition(State.HURT, State.PREF, r'[!Aww, that hurts. Good thing I only have to deal with you for one more question. After taking this survey, what is your preferred method of transportation"?"]')
df.add_system_transition(State.HAPPY, State.PREF, r'[!Glad you have faith in this bot"!" Just one more question. After taking this survey, what is your preferred method of transportation"?"]')

df.add_user_transition(State.PREF, State.WALK, walk_natex)
df.add_user_transition(State.PREF, State.PRIV, priv_natex)
df.add_user_transition(State.PREF, State.PUBLIC, public_natex)
df.add_user_transition(State.PREF, State.RIDESHARE, rideshare_natex)

df.add_system_transition(State.ERR10, State.PREF, r'[!Sorry, I need you to use different words.]')



#END
df.add_system_transition(State.WALK, State.TERMINAL, r'[!I think I would enjoy that too if I had feet. Thanks for taking this survey"!"]')
df.add_system_transition(State.PRIV, State.TERMINAL, r'[!I wish I had a car to myself. Anyway, thanks for taking this survey"!"]')
df.add_system_transition(State.PUBLIC, State.TERMINAL, r'[!Not bad, I still think ride sharing apps are better though. Anyway, thanks for taking this survey"!"]')
df.add_system_transition(State.RIDESHARE, State.TERMINAL, r'[!Awesome"!" Thanks for taking this survey"!"]')

#Error states
df.set_error_successor(State.PROMPT, State.ERR1)
df.set_error_successor(State.FREQUENCY, State.ERR2)
df.set_error_successor(State.TIME, State.ERR3)
df.set_error_successor(State.CHOICE, State.ERR4)
df.set_error_successor(State.LYFTUBER, State.ERR7)
df.set_error_successor(State.CONVO, State.ERR8)
df.set_error_successor(State.SELFDRIVE, State.ERR9)
df.set_error_successor(State.PREF, State.ERR10)
df.set_error_successor(State.SATISFACTION, State.ERR11)
df.set_error_successor(State.CAREER, State.ERR12)

df.run(debugging=False)