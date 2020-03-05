from emora_stdm import KnowledgeBase, DialogueFlow, NatexNLU
from enum import Enum, auto



# Define the states that your conversation will use
# All states that you use in transitions later need to be in this class

class State(Enum):
    S0 = auto()
    U0 = auto()
    S1A = auto()
    S1B = auto()
    U1 = auto()
    S2_google = auto()
    S2_htc = auto()
    S2_samsung = auto()
    S2_oculus = auto()
    S2_playstation = auto()
    U2 = auto()
    S3A = auto()
    S3B = auto()
    U3A = auto()
    U3B = auto()
    S4A = auto()
    S4B = auto()
    S4C = auto()
    U4 = auto()
    S5A = auto()
    S5B = auto()
    U5 = auto()
    S6_ugly= auto()
    S6_expensive = auto()
    U6 = auto()
    S7A = auto()
    S7B = auto()
    U7 = auto()
    S8A = auto()
    S8B = auto()
    U8 = auto()
    S9 = auto()
    U9 = auto()
    S10A = auto()
    S10B = auto()
    U10 = auto()
    END = auto()
    ERR = auto()


VR_company = {"ontology":
                {
                "company":
                 [
                     "google",
                     "htc",
                     "samsung",
                     "oculus"
                 ],
                 "ontgoogle":
                 [
                     "cardboard",
                     "google"
                 ],
                 "onthtc":
                 [
                     "vive",
                     "htc"
                 ],
                 "ontsamsung":
                 [
                     "gear",
                     "samsung"
                 ],
                 "ontoculus":
                 [
                     "rift",
                     "oculus"
                 ],
                 "ontsony":
                 [
                     "morpheus",
                     "vr",
                     "sony",
                     "playstation"
                 ]
                }
           }


knowledge = KnowledgeBase()
knowledge.load_json(VR_company)
df = DialogueFlow(State.S0, initial_speaker=DialogueFlow.Speaker.SYSTEM, kb=knowledge)

#Initalize Yes, Yes+vr, and No for first question



df.add_system_transition(State.S0, State.U0, r'[!Have you ever used Virtual Reality before"?"]')

#Yes+VR Company Answer
df.add_user_transition(State.U0, State.S2_google, "<$VR=#ONT(ontgoogle)>")
df.add_user_transition(State.U0, State.S2_htc, "<$VR=#ONT(onthtc)>")
df.add_user_transition(State.U0, State.S2_samsung, "<$VR=#ONT(ontsamsung)>")
df.add_user_transition(State.U0, State.S2_oculus, "<$VR=#ONT(ontoculus)>")
df.add_user_transition(State.U0, State.S2_playstation, "<$VR=#ONT(ontsony)>" )

df.add_system_transition(State.S2_google, State.U2, r'[!Google Cardboard is really amazing and my personal favorite, it lets anyone with a smartphone '
                                                    r'experience the future with Virtual Reality"!" When was the last time you tried VR "?"]')

df.add_system_transition(State.S2_htc, State.U2, r'[!HTC Vive, although expensive, uses futuristic 3D tracked controllers to let you '
                                                 r'feel even closer to the Virtual Environment"!" When was the last time you tried VR "?"]')

df.add_system_transition(State.S2_samsung, State.U2, r'[!Samsung Gear are glasses that make use of a samsung phone along with a controller '
                                                     r'to allow you to do cool things like browse the web or watch netflix in a seemingly theater "-" sized room"!" '
                                                     r'When did you try it last "?"]')

df.add_system_transition(State.S2_oculus, State.U2, r'[!Oculus Rift was the first PC powered gaming headset, letting you delve into your '
                                                    r'favorite games"!" When was the last time you tried VR"?"]')

df.add_system_transition(State.S2_playstation, State.U2, r'[!Playstation morpheus was revolutionary to bring the full VR experience to console gaming'
                                                         r' "!" When was the last time you tried VR "?"]')



#Yes Answer
yes_natex = NatexNLU('{yes,yeah,have}')
df.add_user_transition(State.U0, State.S1B, yes_natex)
df.add_system_transition(State.S1B, State.U1, r'[!Which VR system model did you use "?"]')
df.add_user_transition(State.U1, State.S2_google, "<$VR=#ONT(ontgoogle)>")
df.add_user_transition(State.U1, State.S2_htc, "<$VR=#ONT(onthtc)>")
df.add_user_transition(State.U1, State.S2_samsung, "<$VR=#ONT(ontsamsung)>")
df.add_user_transition(State.U1, State.S2_oculus, "<$VR=#ONT(ontoculus)>")
df.add_user_transition(State.U1, State.S2_playstation, "<$VR=#ONT(ontsony)>")


#No Answer
no = r"[{no,not really, not}]"
no_natex = NatexNLU(no)
df.add_user_transition(State.U0, State.S1A, no_natex)
df.add_system_transition(State.S1A, State.U4, r'[!Oh that is unfortunate, you should definitely try it sometime "," VR is slowly becoming the future of gaming and even '
                                              r' industrial uses. My favorite is Google Cardboard because of how accessible it is to everyone "!" Another emerging area'
                                              r' is augmented reality, why do you think it would be growing so quickly compared to VR "?"]')


#Time since used
#Short Time

short= r"[{today,hour,hours,yesterday,week,weeks,day, days,month,months}]"
short_natex = NatexNLU(short)

df.add_user_transition(State.U2, State.S3A, short_natex)
df.add_system_transition(State.S3A, State.U3A, r'[!Thats great "!" You may have used one of the newer models with many new features such as higher resolution displays and '
                                              r' faster refresh rates to help with motion sickness "!" What about your $VR headset captivated you to buy one "?"]')

sentence_natex = NatexNLU('/.*/')
df.add_user_transition(State.U3A, State.S4A, sentence_natex)
df.add_system_transition(State.S4A, State.U4, r'[!That is a really good reason "!" Just wait, with time this technology will progress so much more "!" But, there has been '
                                              r'a decrease in the progression of VR, as it gives way to Augmented Reality "("AR")". Do you know why this could be "?"]')

#Long Time
long= r"[{year,years,long,while}]"
long_natex = NatexNLU(long)

df.add_user_transition(State.U2, State.S3B, long_natex)
df.add_system_transition(State.S3B, State.U3B, r'[!It may have been some time since you have used a $VR headset, there have been many new upgrades since the older models. '
                                            r' Did you remember ever feeling motion sickness or nauseousness from using the headset "?"]')

yes_nat = r"[{yes,yeah,have,did}]"
yes_natex_reader = NatexNLU(yes_nat)
df.add_user_transition(State.U3B, State.S4B, yes_natex_reader)
df.add_system_transition(State.S4B, State.U4, r'[!You most likely felt sick because the older generation of headsets had lower resolution screens and low refresh rates '
                                              r'that would cause motion sickness. Today"," computation has gotten much more efficient and these issues have been mostly '
                                              r'allieviated. But, there has been a decrease in the progression of VR, as it gives way to '
                                              r'Augmented Reality "("AR")". Do you know why this could be "?"]')

df.add_user_transition(State.U3B, State.S4C, no_natex)
df.add_system_transition(State.S4C, State.U4, r'[!That is really interesting"," studies have found 40 to 60 percent of people on VR headsets were motion sick after playing. '
                                              r'But, there has been a decrease in the progression of VR, as it gives way to Augmented Reality "("AR")". Do you know'
                                              r' why this could be "?"]')


#AR Section:
#Gaming
game = r"[{game,games,gaming}]"
game_natex = NatexNLU(game)
df.add_user_transition(State.U4, State.S5B, game_natex)
df.add_system_transition(State.S5B, State.U6, r'[!Gaming has been one of the forefronts of AR today. Companies like Apple are pushing '
                                             r' things such as the ARkit, bringing games to the space around you with the aid of the camera.'
                                             r' The most popularized AR game has been pokemon go, do you know why this may be the case "?"]' )




#Glasses
glass = r"[{glass,glasses,wearable,wearables}]"
glass_natex = NatexNLU(glass)
df.add_user_transition(State.U4, State.S5A, glass_natex)
df.add_system_transition(State.S5A, State.U5, r'[!Different types of AR glasses have slowly been growing in popularity, '
                                              r'but why do you think they are not as common "?"]')

#why not glasses
#Ugly
ugly = r"[{ugly,clunky,poor ergonomics,bad,dont,stylish,fashionable}]"
ugly_natex = NatexNLU(ugly)
df.add_user_transition(State.U5, State.S6_ugly, ugly_natex)
df.add_system_transition(State.S6_ugly, State.U6, r'[!That is very true. Glasses today have become more of a fashion statement"," and '
                                                  r'the aesthetics of todays AR glasses are not pleasing. But AR is '
                                                  r'still accessible to everyone"," pokemon go revolutionized the way mobile games can be '
                                                  r'played"," why do you think they were so successful "?"]')

#Expensive
expensive = r"[{pricey,expensive,money,cost}]"
expensive_natex = NatexNLU(expensive)
df.add_user_transition(State.U5, State.S6_expensive, expensive_natex)
df.add_system_transition(State.S6_expensive, State.U6, r'[!Because of the low amount of AR glasses in the market and their complex design"," '
                                                       r'they are very expensive compared to regular prescription glasses. '
                                                       r'But AR is still accssible to everyone"," pokemon go revolutionized '
                                                       r'the way mobile gaming can be played"," why do you think this is "?"]')


#Reasons for Pokemon Go success
#Health
health = r"[{physical,exercise,roam,outdoors,outside,walk,walking,adventure,nature,sun,sunlight}]"
health_natex = NatexNLU(health)
df.add_user_transition(State.U6, State.S7A ,health_natex)
df.add_system_transition(State.S7A, State.U7, r'[!This game is so unique because it encourages individuals to go outside and'
                                              r' move around to progress in the game. In a world where individuals'
                                              r' are glued to their phone, this is revolutionary, and only made '
                                              r'possible through the power of AR. As of now, AR is a digital overlay over the reality we have now"," '
                                              r'how do you think this will effect the people as it becomes more mainstream "?"]')

#Social Interaction
social = r"[{social,interaction,talk,interact,friends,communication,teamwork}]"
social_natex = NatexNLU(social)
df.add_user_transition(State.U6, State.S7B ,social_natex)
df.add_system_transition(State.S7B, State.U7, r'[!Pokemon Go has a powerful ability to increase physical '
                                              r'social interactions rather than the virtual one found in other games. As of now, AR is a digital overlay over the reality we have now"," '
                                              r'how do you think this will effect the people as it becomes more mainstream "?"]' )



#Effects of AR
#positive
positive = r"[{efficiency,good,positive,positively}]"
positive_natex = NatexNLU(positive)
df.add_user_transition(State.U7, State.S8A ,positive_natex)
df.add_system_transition(State.S8A, State.U8, r'[!The effects of AR is highly debated. I believe that AR has the power to improve'
                                              r' human life by giving a constant monitoring of metrics such as our health. It can play'
                                              r' such a huge role in daily life such as how we shop for things or even '
                                              r'improve the technical training of complex medical procedures. Studies have even shown that'
                                              r' schools that implement AR mobile learning have students with higher attention and satisfaction "!" How do you feel '
                                              r'about the current state of mobile AR"?"]')


#Negative
negative = r"[{distractions,distraction,distracted,distract,unaware annoying,negative,antisocial}]"
negative_natex = NatexNLU(negative)
df.add_user_transition(State.U7, State.S8B ,negative_natex)
df.add_system_transition(State.S8B, State.U8, r'[!I can see why you would think about the negative impacts of AR. Even with pokemon go, many people got hurt while'
                                              r' distractedly roaming the streets. Even more dangerous would be to have a screen always in our vision while '
                                              r'doing daily tasks such as driving. Still, this technology will have a future, it just has to be carefully'
                                              r' thought out and implemented to preserve safety. How do you feel '
                                              r'about the current state of VR and mobile AR"?"]')


#Current State of Mobile AR
df.add_user_transition(State.U8, State.S9, sentence_natex)

#Is AR a good investment today
df.add_system_transition(State.S9, State.U9, r'[!Do you think that augmented and virtual realities are developed enough and good investments for people to make today, to push'
                                             r' forward the technology "?"]')
#AR/VR is developed enough
df.add_user_transition(State.U9, State.S10A, yes_nat)
df.add_system_transition(State.S10A, State.U10, r'[!Although AR and VR may seem a little gimmicky right now, there is a lot of potential and fun to be had with '
                                                r'the current technology today "!"AR and VR are the futures of gaming '
                                                r'and entertainment, but they also have many commercial and educational uses.'
                                              r' The next stage of this technology will be Mixed Reality, where virtual and mutatable objects can be placed in '
                                              r'an augmented world. The future is very exciting and all of this is coming much quicker than we expect "!" '
                                              r'I hope you will invest in AR and VR products in the future "!"]')

#More time is still needed
df.add_user_transition(State.U9, State.S10B, no_natex)
df.add_system_transition(State.S10B, State.U10, r'[!AR and VR may seem not as impressive just yet, but as more people start to invest in these products, '
                                                r'the more content that will be created by developers "!" AR and VR are the futures of gaming and'
                                                r' entertainment, but they also have many commercial and educational uses.'
                                              r' The next stage of this technology will be Mixed Reality, where virtual and mutatable objects can be placed in '
                                              r'an augmented world. The future is very exciting and all of this is coming much quicker than we expect "!" '
                                              r'I hope you will invest in AR and VR products in the future "!"]')


df.add_user_transition(State.U10, State.END, "/.*/")
df.add_system_transition(State.END, State.END, r'[!Thank you for the wonderful conversation, have a nice rest of your day "!"]')



#ERROR STATES
df.add_system_transition(State.ERR, State.ERR, r"[!Oops...I Broke]")
df.set_error_successor(State.U0, error_successor=State.S1B)
df.set_error_successor(State.U1, error_successor=State.S2_google)
df.set_error_successor(State.U2, error_successor=State.S3A)
df.set_error_successor(State.U3A, error_successor=State.S4C)
df.set_error_successor(State.U3B, error_successor=State.S4C)
df.set_error_successor(State.U4, error_successor=State.S5B)
df.set_error_successor(State.U5, error_successor=State.S6_ugly)
df.set_error_successor(State.U6, error_successor=State.S7A)
df.set_error_successor(State.U7, error_successor=State.S8A)
df.set_error_successor(State.U8, error_successor=State.S9)
df.set_error_successor(State.U9, error_successor=State.S10B)




df.run(debugging=False)