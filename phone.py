from emora_stdm import KnowledgeBase, DialogueFlow
from enum import Enum
from emora_stdm import Macro
import random



class cheapchoice(Macro):
    def run(self, ngrams, vars, args):
        if 'features' in vars:
             #print(vars['features'])
             choice1= cheapest[vars['features']]
        if 'character' in vars:
             choice2= cheapest[vars['character']]
        # if 'character' not in vars or vars['character']==vars['features']:
        #      return choice1
        return choice1 + " and "+ choice2

class cheapchoices(Macro):
    def run(self, ngrams, vars, args):

        return cheapest[vars['featuress']]


class recommend(Macro):
    def run(self, ngrams, vars, args):
        if  'oldrecommend' in vars:
            return vars["oldrecommend"]
        if 'features' in vars:
            x="ont"+vars['features']
            choice1= random.choice(ont_dict["ontology"][x])
        if 'character' in vars:
            x="ont" +vars['character']
            choice2= random.choice(ont_dict["ontology"][x])
        # if 'character' not in vars or vars['character']==vars['features']:
        #     vars['oldrecommend'] = choice1
        #     return choice1
        vars['oldrecommend'] = choice1 + " and " + choice2
        return choice1 +" and "+choice2

class recommends(Macro):
    def run(self, ngrams, vars, args):
        if 'oldrecommends' in vars:
            return vars["oldrecommends"]
        else:
            x="ont" + vars['featuress']
            choice1= random.choice(ont_dict["ontology"][x])
            vars['oldrecommends']=choice1
        return choice1

class summarize(Macro):
    def run(self, ngrams, vars, args):
        if vars['features']!=vars['character']:
            return vars['features']+" and "+vars['character']
        else:
            return vars['features']+''

class Time(Macro):

    def run(self, ngrams, vars, args):
        year=0
        d_month_to_number = {
            month: i for i, month in enumerate(
                ['january','february','march','april','may','june',
                 'july','august','september','october','november','december'], start=1)}
        curr_year, curr_month = 2020, 1
        if 'number' in vars and 'time_type' in vars:
            d = int(vars['number'])
            m = vars['time_type']
            if m.startswith('year'):
                year = curr_year - d
                month = curr_month
            elif m.startswith('month'):
                year = curr_year - int(d / 12)
                month = curr_month - (d % 12)
                if month <= 0:
                    month_diff = abs(month)
                    month = 12 - month_diff
                    year -= 1
        elif 'year' in vars:
            year = int(vars['year'])
            if year <= 20: year += 2000
            if 'month' in vars:
                month = d_month_to_number[vars['month']]
            else:
                month = 1
        if year<=2018:
            return "long"
        else:
            return "short"

# TODO: Update the State enum as needed


class State(Enum):
    START=0
    PROMPT=1
    STATE1_A_Y=2
    STATE1_A_N=3
    type=4
    answer21=5
    answer22=6
    answer23 = 7
    answer24 = 8
    answer25 = 9
    answer26= 10
    answer27 =11
    howlong =12
    howlong2 = 13
    answer3=14
    howlike=15
    answer4=16
    important_feature=17
    answer5=18
    idea=19
    replaceyes=20
    replaceno=21
    askreason=22
    priceproblem=23
    nopriceproblem=24
    retry=25
    agree=26
    willreplace=27
    usage=28
    rec=29
    whyreplace=30
    findplace=31
    ERROR_final=32
    ERROR_stillnot=33
    ERROR_reason=34
    ERROR_idea=35
    ERROR_askusefor=36
    ERROR_impfeature=37
    ERROR_howlike=38
    ERROR_duration=39
    ERROR_askphone=40
    STATE_END=41
    ERROR_phonetype=42
    ERR=43
    xx=44
    answer6=45
    idea2=46
    no_phone=47
    ERROR_impfeature2=48
    ERROR_idea2=49
    refuse=50
    findplacerec=51
    noask_why=52
    nocheap_choice=53
    replaceno2 = 54
    askreason2 = 55
    priceproblem2 = 56
    retry2 = 57
    agree2 = 58
    refuse2 = 59
    findplacerec2 = 60
    replaceyes2 = 61
    willreplace2 = 62
    findplace2 = 63

cheapest={
    "camera":"lg v30",
    "big screen":"motorola g5s plus",
    "small screen":"galaxy note 7",
    "display":"galaxy s8+",
    "battery":"pixel",
    "design":"lg g4"
}
# TODO: create the ontology as needed
ont_dict = {
    "ontology": {
        "ontcamera":[
            "iphone6 plus",
            "galaxy s10",
            "galaxy note 8",
            "galaxy s7",
            "nokia 6",
            "oneplus 7",
            "motorola g5s",
            "nokia 3"
        ],
        "ontbig screen":[
            "iphone6 s",
            "iphone7",
            "iphone7 plus",
            "motorola e4",
            "motorola z2 force",
            "motorola z2 play",
            "motorola e4 plus",
            "lg q6"
            "motorola x4",
            "galaxy s7 edge"
        ],
        "ontsmall screen": [
            "iphone 8",
            "iphone 8 plus",
            "lg q8",
            "galaxy s9",
            "galaxy note 9",
            "lg g5",
            "lg g6",
            "nokia 5",
            "galaxy s9+"
        ],
        "ontdisplay":[
            "iphone 10s max",
            "iphone 11",
            "galaxy s10e",
            "galaxy s8 active",
            "google pixel xl",
            "galaxy s8",
            "galaxy j7 prime"
        ],
        "ontbattery" :[
            "iphone 10",
            "iphone 10s",
            "galaxy a5",
            "galaxy j5",
            "iphone 6",
            "iphone 6s",
            "galaxy a7",
            "galaxy j7 pro"
        ],
        "ontdesign":[
            "iphone 11 pro",
            "iphone 11 pro max",
            "nokia 8",
            "oneplus 7 pro",
            "galaxy s10 plus",
            "galaxy j7",

        ]

        }
}


knowledge = KnowledgeBase()
knowledge.load_json(ont_dict)
df = DialogueFlow(State.START, initial_speaker=DialogueFlow.Speaker.SYSTEM, kb=knowledge,macros={"Time":Time(), "recommend":recommend(), "cheapchoice":cheapchoice(),"summarize":summarize(),"recommends":recommends(), "cheapchoices":cheapchoices()})
#start
df.add_system_transition(State.START, State.PROMPT, '"Do you use a smartphone?"')
df.add_user_transition(State.PROMPT, State.STATE1_A_Y, '[{yes, yea, yup, yep, i do, i use a smartphone}]')
df.add_user_transition(State.PROMPT, State.STATE1_A_N, '[{no, nope, i dont}]')
df.add_system_transition(State.STATE1_A_N, State.no_phone, '"Why not get one? What do you think is the most important feature for a phone?"')
df.set_error_successor(State.PROMPT, error_successor=State.ERROR_askphone)
df.add_system_transition(State.ERROR_askphone, State.PROMPT,'"I do not think I understand. Can you repeat?"')

#ask type


df.add_system_transition(State.STATE1_A_Y, State.type, '"what is the type of your smartphone?"')


#phonetype
cam=r"[$f={/iphone 6 plus/,/(galaxy s10)(?!\s)/,/galaxy note 8/,/(galaxy s7)(?!\s)/,/nokia 6/,/(oneplus 7)(?!\s)/,/motorola g5s/,/nokia 3/}]"
df.add_user_transition(State.type, State.answer21,cam)
df.add_system_transition(State.answer21, State.howlong,r'[!Your $f has very good camera. How long have you been using it"?"]')

bigscreen=r"[$e={/iphone 6s plus/,/(iphone 7)(?!\s)/,/iphone 7 plus/,/motorola e4/,/motorola z2 force/,/motorola z2 play/,/motorola e4 plus/,/lg q6/,/motorola x4/,/galaxy s7 edge/}]"
df.add_user_transition(State.type, State.answer22,bigscreen)
df.add_system_transition(State.answer22, State.howlong,r'[!Your $e has very good big screen. How long have you been using it"?"]')

smallscreen=r"[$d={/(iphone 8)(?!\s)/,/iphone 8 plus/,/lg q8/,/galaxy s9/,/galaxy note 9/,/lg g5/,/lg g6/,/nokia 5/,/galaxy s9+/}]"
df.add_user_transition(State.type, State.answer23,smallscreen)
df.add_system_transition(State.answer23, State.howlong,r'[!Your $d has very good small screen. How long have you been using it"?"]')

battery=r"[$c={/iphone 10/,/(iphone 10s)(?!\s)/,/galaxy a5/,/galaxy j5/,/(iphone 6)(?!\s)/,/(iphone 6s)(?!\s)/,/galaxy a7/,/galaxy j7 pro/}]"
df.add_user_transition(State.type, State.answer24,battery)
df.add_system_transition(State.answer24, State.howlong,r'[!Your $c has very good battery. How long have you been using it"?"]')

design=r"[$b={/(iphone 11 pro)(?!\s)/,/iphone 11 pro max/,/nokia 8/,/oneplus 7 pro/,/galaxy s10 plus/,/(galaxy j7)(?!\s)/}]"
df.add_user_transition(State.type, State.answer26,design)
df.add_system_transition(State.answer26, State.howlong,r'[!Your $b has very good design. How long have you been using it"?"]')

display=r"[$a={/iphone 10s max/,/(iphone 11)(?!\s)/,/galaxy s10e/,/galaxy s8 active/,/google pixel xl/,/(galaxy s8)(?!\s)/,/galaxy j7 prime/}]"
df.add_user_transition(State.type, State.answer27,display)
df.add_system_transition(State.answer27, State.howlong,r'[!Your $a has very good display. How long have you been using it"?"]')

#phonetype_error

df.set_error_successor(State.type, error_successor=State.ERROR_phonetype)
df.add_system_transition(State.ERROR_phonetype,State.howlong,'"Oh, cool! But I did not hear of that one. How long have you been using it?"')




#duration
duration=r"{[$number=/\d+/,$time_type={month,months,year,years}], [!{since,from},$month={january,february,march,april,may,june,july,august,september,october,november,december},$year=/\d{2,4}/]}"
df.add_user_transition(State.howlong, State.answer3,duration)

df.add_system_transition(State.answer3, State.howlike,r'[!oh that has been a #Time time. How do you like it"?"]')
df.set_error_successor(State.howlong, error_successor=State.ERROR_duration)
df.add_system_transition(State.ERROR_duration,State.howlong,'"I do not think I understand it correctly. Can you repeat?"')



#how do you like
opinion=r"{[$description={good,bad,terrible,excellent,like, dont like, high, low},$character={camera,big screen,small screen,display,battery,design,price}]}"
df.add_user_transition(State.howlike, State.answer4, opinion)
df.set_error_successor(State.howlike, error_successor=State.ERROR_howlike)
df.add_system_transition(State.ERROR_howlike,State.howlike,'"I do not think I understand it correctly. Can you repeat?"')


#important feature
df.add_system_transition(State.answer4, State.important_feature,'"What do you think is the most important feature for a phone?"')
impfeature = r"[$features={camera,big screen,small screen,display,battery,design}]"
df.add_user_transition(State.important_feature, State.answer5,impfeature)
df.set_error_successor(State.important_feature, error_successor=State.ERROR_impfeature)
df.add_system_transition(State.ERROR_impfeature,State.important_feature,'"Thank you for pointing out, but this feature is not currently in our dictionary. Can you name another feature?"')

#use phone for
df.add_system_transition(State.answer5,State.usage,'"what do you usually use your smartphone for?"')
use=r"[$usuallyuse={take photo,play game,social,contact,call,text,search}]"
df.add_user_transition(State.usage,State.rec,use)
df.set_error_successor(State.usage, error_successor=State.ERROR_askusefor)
df.add_system_transition(State.ERROR_askusefor,State.idea,r'[!Thank you for pointing out, but this feature is not currently in our dictionary. Anyway, let me give you some recommendations based on your information. I think #cheapchoice has very good $features and $character Would you like to replace your phone"?"]')

#recommend
df.add_system_transition(State.rec, State.idea,r'[!I think #recommend have very good #summarize and they are also good choices if you $usuallyuse a lot. Would you like to replace your phone"?"]')
df.add_user_transition(State.idea, State.replaceyes, '[{ok, sure, yes, yea, yup, yep, i am, yeah, i am going to replace it, i will replace it, why not}]' )
df.add_user_transition(State.idea, State.replaceno, '[{no, nope, i dont}]')
df.add_system_transition(State.replaceyes, State.findplace,r'[!I think lenox has a store that sells #recommend .What about going to try that one this weekend"?"]')
df.set_error_successor(State.idea, error_successor=State.ERROR_idea)
df.add_system_transition(State.ERROR_idea, State.idea,'"I dont quite understand what you are talking. Would you like to replace your phone?"')

#askwhy(price)
df.add_system_transition(State.replaceno, State.askreason,'"why not?"')
df.add_user_transition(State.askreason,State.priceproblem,'[{expensive,money,cheap,poor,not rich,spend,price}]')
df.set_error_successor(State.askreason, error_successor=State.ERROR_reason)
df.add_system_transition(State.ERROR_reason, State.PROMPT,'"OK, I understand. conversation finished, lets start over. Do you have a smartphone?"')

#cheapchoice
df.add_system_transition(State.priceproblem,State.retry,r'[!I think #cheapchoice might be a good choice for you then.]')
agreeanswer='[{ok, sure, yes, yea, yup, yep, i am, yeah, i am going to replace it, i will replace it, why not}]'
df.add_user_transition(State.retry, State.agree, agreeanswer)
df.add_user_transition(State.retry, State.refuse, '[{no, nope, i dont}]')
df.add_system_transition(State.refuse, State.PROMPT,'"OK, I understand. conversation finished, lets start over. Do you have a smartphone?"')
df.set_error_successor(State.retry, error_successor=State.ERROR_reason)


#no phone
impfeature2 = r"[$featuress={camera,big screen,small screen,display,battery,design,price}]"
df.add_user_transition(State.no_phone, State.answer6,impfeature2)
df.set_error_successor(State.no_phone, error_successor=State.ERROR_impfeature2)
df.add_system_transition(State.ERROR_impfeature2,State.no_phone,'"Thank you for pointing out, but this feature is not currently in our dictionary. Can you name another one?"')

#recommend no phone
df.add_system_transition(State.answer6, State.idea2,r'[!I think #recommends have very good $featuress and do you consider getting one"?"]')
df.add_user_transition(State.idea2, State.replaceyes2, '[{ok, sure, yes, yea, yup, yep, i am, yeah, i am going to replace it, i will replace it, why not}]' )
df.add_user_transition(State.idea2, State.replaceno2, '[{no, nope, i dont}]')
df.set_error_successor(State.idea2, error_successor=State.ERROR_idea2)
df.add_system_transition(State.ERROR_idea2, State.idea2,'"Sorry I dont quite understand what you are saying. Do you consider getting it?"')
df.add_system_transition(State.replaceyes2,State.findplacerec2,r'[!I think lenox has a store that sells #recommends and what about going to try that one this weekend"?"]')
df.add_user_transition(State.findplacerec2,State.willreplace2,'[{ok, sure, yes, yea, yup, yep, i like it, yeah, i am going to replace it, why not}]')


df.set_error_successor(State.findplacerec2, error_successor=State.ERROR_final)

#no phone, askwhy(price)
df.add_system_transition(State.replaceno2,State.askreason2,'"Why not?"')
df.add_user_transition(State.askreason2,State.priceproblem2,'[{expensive,money,cheap,poor,not rich,spend,price}]')
df.set_error_successor(State.askreason2, error_successor=State.ERROR_reason)


#cheapchoice
df.add_system_transition(State.priceproblem2,State.retry2,r'[!I think #cheapchoices might be a good choice for you then.]')
agreeanswers='[{ok, sure, yes, yea, yup, yep, i am, yeah, i am going to replace it, i will replace it, why not}]'
df.add_user_transition(State.retry2, State.agree2, agreeanswers)
df.add_user_transition(State.retry2, State.refuse2, '[{no, nope, i dont}]')
df.add_system_transition(State.refuse2, State.PROMPT,'"OK, I understand. conversation finished, lets start over. Do you have a smartphone?"')
df.set_error_successor(State.retry2, error_successor=State.ERROR_reason)

df.set_error_successor(State.findplacerec2, error_successor=State.ERROR_final)

#go shop
df.add_system_transition(State.agree, State.findplace,r'[!I think lenox has a store that sells #cheapchoice .What about going to try that one this weekend"?"]')
df.add_user_transition(State.findplace,State.willreplace,'[{ok, sure, yes, yea, yup, yep, i like it, yeah, i am going to replace it, why not}]')
df.add_system_transition(State.willreplace, State.PROMPT,'"That is great!  conversation finished, lets start over. Do you have a smartphone?"')

df.set_error_successor(State.findplace, error_successor=State.ERROR_final)

#go shop if no phone
df.add_system_transition(State.agree2, State.findplace2,r'[!I think lenox has a store that sells #cheapchoices .What about going to try that one this weekend"?"]')
df.add_user_transition(State.findplace2,State.willreplace2,'[{ok, sure, yes, yea, yup, yep, i like it, yeah, i am going to replace it, why not}]')
df.add_system_transition(State.willreplace2, State.PROMPT,'"That is great!  conversation finished, lets start over. Do you have a smartphone?"')

df.set_error_successor(State.findplace2, error_successor=State.ERROR_final)


# final
df.add_system_transition(State.ERROR_final, State.PROMPT,'"Conversation finished, lets start over. Do you have a smartphone?"')
df.run(debugging=False)
