from emora_stdm import KnowledgeBase, DialogueFlow
from enum import Enum


# TODO: Update the State enum as needed
class State(Enum):
    START = 0
    PROMPT = 1
    SCHOOL = 2
    GAME = 3
    APPLE = 4
    PROMPT1 = 5
    PROMPT0ERR = 6
    ERR0 = 7
    Unknown = 8
    YNERR = 9
    Y1 = 10
    N1 = 11
    ERR1 = 12
    PROMPT2 = 13
    PROMPT2ERR = 14
    NORMAL = 15
    NEW = 16
    OLD = 17
    PROMPT3 = 18
    ERR2 = 19
    Y2 = 20
    N2 = 21
    YNERR1 = 22
    PROMPT4A = 23
    PROMPT4B = 24
    LIKE = 25
    DISLIKE = 26
    Y3 = 27
    N3 = 28
    PROMPT5ERR = 29
    ERR3 = 30
    PROMPT6ERR = 31
    ERR4 = 32
    CHEAP_S = 33
    GAMING_S = 34
    SCHOOL_S = 35
    LIGHT_S = 36
    DELL_S = 37
    APPLE_S = 38
    LENOVO_S = 39
    ASUS_S = 40
    HP_S = 41
    ACER_S = 42
    PROMPT5 = 43
    PROMPT6 = 44
    PROMPT7 = 45
    PROMPT7ERR = 46
    ERR5 = 47
    Y4 = 48
    N4 = 49
    PROMPT8 = 50
    PROMPT8ERR = 51
    ERR6 = 52
    BAD = 53
    OK = 54
    GOOD = 55
    PROMPT9 = 56
    NAME = 57
    PROMPT9ERR = 58
    END = 59
    ERR7 = 60


# TODO: create the ontology as needed
ontology = {
    "ontology": {
            "Dell":
            [
                'xps',
                'inspiron',
                'alienware',
                'g',
                'dell',
                'chromebook'
            ],
            "Apple":
            [
                'macbook',
                'macbook air',
                'macbook pro',
                'apple',
                'mac'
            ],
            "Lenovo":

            [
                'thinkpad',
                'thinkbook',
                'ideabook',
                'yoga',
                'legion',
                'lenovo',
                'chromebook'
            ],
            "Asus":
            [
                'rog',
                'zenbook',
                'vivobook',
                'asus',
                'chromebook'
            ],
            "HP":
            [
                'envy',
                'elite',
                'essential',
                'pavilion',
                'spectre',
                'zbook',
                'hp',
                'chromebook'
            ],
            "Microsoft":
            [
                'surface',
                'microsoft',
                'chromebook'
            ],
            "Acer":
            [
                'predetor',
                'aspire',
                'nitro',
                'spin',
                'shift',
                'switch',
                'acer',
                'chromebook'
            ],
            "gaming":
            [
                'predetor',
                'rog',
                'razer',
                'alienware',
                'msi',
                'nitro',
                'omen',
                'legion'
            ],
            "school":
            [
                'xps',
                'inspiron',
                'chromebook',
                'thinkpad',
                'thinkbook',
                'ideabook',
                'yoga',
                'zenbook',
                'vivobook',
                'envy',
                'elite',
                'essential',
                'pavilion',
                'spectre',
                'zbook',
                'surface',
                'aspire',
                'spin',
                'shift',
                'switch',
                'dell',
                'hp',
                'acer',
                'asus',
            ],
            "cheap":
            [
                'Dell inspiron',
                'Lenovo ideapad',
                'Samsung chromebook',
                'Acer aspire'
            ],
            "light":
            [
                'Acer swift',
                'Lenovo ideapad',
                'Apple macbook air',
                'Dell xps',
                'HP spectre'
            ]

        }
}


knowledge = KnowledgeBase()
knowledge.load_json(ontology)
df = DialogueFlow(State.START, initial_speaker=DialogueFlow.Speaker.SYSTEM, kb=knowledge)

df.add_system_transition(State.START, State.PROMPT, '"Hi, just wondering what laptop are you using?"')
df.set_error_successor(State.PROMPT, State.PROMPT0ERR)
# TODO: create your own dialogue manager
df.add_user_transition(State.PROMPT, State.SCHOOL, "[{$model=#ONT(school)}]")
df.add_user_transition(State.PROMPT, State.APPLE, "[{$model=#ONT(Apple)}]")
df.add_user_transition(State.PROMPT, State.GAME, "[{$model=#ONT(gaming)}]")
df.add_user_transition(State.ERR0, State.Unknown, '$model={/.*/}')

df.add_system_transition(State.SCHOOL, State.PROMPT1, '"Okay let me guess...you are a sad, depressed and stressed college student that cant wait until spring break?"')
df.add_system_transition(State.APPLE, State.PROMPT1, '"Okay let me guess...you have an iphone, ipad, iwatch, ipod, and i...something right?"')
df.add_system_transition(State.GAME, State.PROMPT1, '"Okay let me guess...you love GTA, call of duty, and think pokemon go is a joke right?"')
df.add_system_transition(State.Unknown, State.PROMPT1, r'[!I guess $model is pretty expensive"?"]')
df.set_error_successor(State.PROMPT1, State.YNERR)

df.add_user_transition(State.PROMPT1, State.Y1, "[{yes, yeah, yea, ye, right, correct, do, know}]")
df.add_user_transition(State.PROMPT1, State.N1, "[{no, nope, nah, dont}]")

df.add_system_transition(State.Y1, State.PROMPT2, r'[!Ah HA I knew it"!" By the way, how long have you been using $model"?"]')
df.add_system_transition(State.N1, State.PROMPT2, r'[!You must be lying... Okay whatever. How long have you been using '
                                                  '$model"?"]')
df.set_error_successor(State.PROMPT2, State.PROMPT2ERR)

df.add_user_transition(State.PROMPT2, State.NEW, r'/.*(1|a)\s\byear\b.*|.*(month|months|day|days).*((?!year|years).)*/')
df.add_user_transition(State.PROMPT2, State.NORMAL, r'/.*[2-3]\s\b(year|years)\b.*/')
df.add_user_transition(State.PROMPT2, State.OLD, r'/.*([4-9]|[0])\s\b(year|years)\b.*/')

df.add_system_transition(State.NEW, State.PROMPT3, r'[!Wait you just bought a new laptop"?" Do you like $model so far]')
df.add_system_transition(State.NORMAL, State.PROMPT3, r'[!Do you like $model so far"?"]')
df.add_system_transition(State.OLD, State.PROMPT3, r'[!What the...Your $model is older than me"!" You really like $model huh"?"]')
df.set_error_successor(State.PROMPT3, State.YNERR1)

df.add_user_transition(State.PROMPT3, State.Y2, "[{yes, yeah, yea, ye, right, correct, do, ok, alright, good}]")
df.add_user_transition(State.PROMPT3, State.N2, "[{no, nope, nah, dont, bad, not good, not}]")

df.add_system_transition(State.Y2, State.PROMPT4A, '"Oh really? why?"')
df.add_system_transition(State.N2, State.PROMPT4B, r'[!Ohh..Im sorry...Whats the problem with your $model"?"]')

df.add_user_transition(State.PROMPT4A, State.LIKE, '/.*/')
df.add_user_transition(State.PROMPT4B, State.DISLIKE, '/.*/')

df.add_system_transition(State.LIKE, State.PROMPT5, '"I should take note of that! Just out of curiosity, are you '
                                                    'thinking of changing your laptop anytime soon?"')
df.add_system_transition(State.DISLIKE, State.PROMPT5, '"Ohh...Im so sorry...Are you thinking of changing your '
                                                       'laptop? I think you really need to LOL"')
df.set_error_successor(State.PROMPT5, State.PROMPT5ERR)

df.add_user_transition(State.PROMPT5, State.Y3, "[{yes, yeah, yea, ye, right, correct, do, probably, might, maybe}]")
df.add_user_transition(State.PROMPT5, State.N3, "[{no, nope, nah, dont}]")

df.add_system_transition(State.Y3, State.PROMPT6, '"Yes! Im glad I can help!  What kind of laptop are you looking '
                                                  'for? Cheap? Gaming? For school? Lightweight? or any specific brand like...Apple LOL?"')
df.add_system_transition(State.N3, State.PROMPT6, '"Ok BYE!! Just joking, I mean its pretty important to know the '
                                                  'market right? What kind of laptop do you want to know? Cheap? '
                                                  'Gaming? For school? Lightweight? or any specific brand like...Apple LOL?"')
df.set_error_successor(State.PROMPT6, State.PROMPT6ERR)

df.add_user_transition(State.PROMPT6, State.CHEAP_S, '[{cheap, inexpensive}]')
df.add_user_transition(State.PROMPT6, State.GAMING_S, '[{gaming, game, games, play, league, cs, cs go, call of duty}]')
df.add_user_transition(State.PROMPT6, State.SCHOOL_S, '[{school, work, word, excel, homework, daily}]')
df.add_user_transition(State.PROMPT6, State.LIGHT_S, '[{light, thin, small, tiny, not big, smaller, lightweight}]')
df.add_user_transition(State.PROMPT6, State.DELL_S, '[{dell, Dell}]')
df.add_user_transition(State.PROMPT6, State.APPLE_S, '[{Apple, apple, mac, macbook}]')
# df.add_user_transition(State.PROMPT6, State.LENOVO_S, '$sugg=#ONT(Lenovo)')
# df.add_user_transition(State.PROMPT6, State.ASUS_S, '$sugg=#ONT(Asus)')
df.add_user_transition(State.PROMPT6, State.HP_S, '[{HP, hp, Hp}]')
# df.add_user_transition(State.PROMPT6, State.ACER_S, '$sugg=#ONT(Acer)')

df.add_system_transition(State.CHEAP_S, State.PROMPT7, '"In terms of cheap laptop which is under 500, my favorite one is '
                                                       'Acer switch 3! It has excellent build quality, superb value '
                                                       'and is a 2-in-1 laptop/tablet. It is using Intel Core i3 '
                                                       '7100U CPU with Intel HD Graphics 505 graphic card. The price '
                                                       'is around 600, and you can always upgrade the CPU. How does '
                                                       'it sound?"')
df.add_system_transition(State.GAMING_S, State.PROMPT7, '"If you are looking for a gaming laptop, I will suggest '
                                                        'Alienware Area-51m. It is extremely powerful, aethetic, '
                                                        'and has a perfecty keyboard. This is one of the most '
                                                        'powerful gaming laptops in 2020. It is using Intel Core '
                                                        'i7-9700 – i9-9900K CPU and NVIDIA GeForce RTX 2060 – 2080 '
                                                        'graphic card. The price is around 2000 (which is a little '
                                                        'expensive for me :p). How does it sound?"')
df.add_system_transition(State.SCHOOL_S, State.PROMPT7, '"As for laptops for students, I will go with Google '
                                                        'PixelBook Go. It has incredible battery life, amazing Hush '
                                                        'keyboard, and an affordable price. It is using Intel Core m3 '
                                                        '– i7 CPU and Intel UHD Graphics 615 (300MHz) graphic card. '
                                                        'The price is around 650. How does it sound?"')
df.add_system_transition(State.LIGHT_S, State.PROMPT7, '"If you are looking for a light and thin laptop, I think Dell '
                                                       'XPS 13 is a really good choice. Dell XPS 13 has been if not, '
                                                       'the king of the ultrabooks for years, it has nice screen, '
                                                       'elegnat design, and a compact build. It is using  '
                                                       '8th-generation Intel Core i3 – i7 CPU with Intel UHD Graphics '
                                                       '620 graphic card. The price is around 1000. How does it sound?"')
df.add_system_transition(State.DELL_S, State.PROMPT7, '"Out of all Dell laptops, I like XPS 15 2-in-1 the most. It '
                                                      'has a stunning design, impressive integrated graphic, '
                                                      'and a no corner screen. It is thin, light, and powerful at the '
                                                      'same time. It is using Intel Core i5-i7 CPU with Radeon RX '
                                                      'Vega M GL Graphics with 4GB HMB2 graphic card. The price is '
                                                      'around 1200. How does it sound?"')
df.add_system_transition(State.APPLE_S, State.PROMPT7, '"Yes Apple yes! Buying a 13-inch MacBook Pro can never be '
                                                       'wrong can never be wrong. It has very fast performance, '
                                                       'relatively affordable price, great battery life, bright and '
                                                       'colorful display, as well as a powerful speaker. It is using '
                                                       '8th Gen Intel Core i5/Core i7 CPU with Intel UHD Graphics '
                                                       'graphic card. The price is around 1500. How does it sound?"')
# df.add_system_transition(State.LENOVO_S, State.PROMPT7, )
# df.add_system_transition(State.ASUS_S, State.PROMPT7, )
df.add_system_transition(State.HP_S, State.PROMPT7, '"The new model HP Elite Dragonfly is a well-rounded laptop. It '
                                                    'is among the best laptops for travelers, has a impeccable '
                                                    'design, and an excellent battery life. It is using '
                                                    '8th-generation Intel Core i5 – i7 CPU with a Intel UHD Graphics '
                                                    '620 graphic card. The price is around 1700. How does it sound?"')
# df.add_system_transition(State.ACER_S, State.PROMPT7, )
df.set_error_successor(State.PROMPT7, State.PROMPT7ERR)

df.add_user_transition(State.PROMPT7, State.Y4, '[{yes, yeah, yea, ye, right, correct, do, agree, nice, want, ok, not bad, pretty, good}]')
df.add_user_transition(State.PROMPT7, State.N4, '[{no, nope, nah, dont, but, not, not really, a little, expensive, doesnt, does not, bad, though, however, cannot, cant}]')

df.add_system_transition(State.Y4, State.PROMPT8, '"Yay Im so glad you like my suggestion. Okay before you leave, '
                                                  'I have one last question. Rating from 1 to 5, how much do you '
                                                  'enjoy chatting with me? (1=im the worst chatter, 5=im the best chatter)"')
df.add_system_transition(State.N4, State.PROMPT8, '"Ill do better next time. Okay before you leave, '
                                                  'I have one last question. Rating from 1 to 5, how much do you '
                                                  'enjoy chatting with me? (1=im the worst chatter, 5=im the best chatter)"')
df.set_error_successor(State.PROMPT8, State.PROMPT8ERR)

df.add_user_transition(State.PROMPT8, State.BAD, '/[0-1]/')
df.add_user_transition(State.PROMPT8, State.OK, '/[2]/')
df.add_user_transition(State.PROMPT8, State.GOOD, '/[3-5]/')

df.add_system_transition(State.BAD, State.PROMPT9, '"Im so sorry for you awful experience...I will try to improve '
                                                   'next time. Wait I did not even know your name...what is your name?"')
df.add_system_transition(State.OK, State.PROMPT9, '"I guess I did ok but still need a lot of improvement. Im still '
                                                  'learning but Ill improve next time! Wait I did not even know your '
                                                  'name...what is your name?"')
df.add_system_transition(State.GOOD, State.PROMPT9, '"Im so happy that you enjoying chatting with me! You are a '
                                                    'really nice person to chat to too! Wait I did not even know your'
                                                    ' name...what is your name?"')
df.set_error_successor(State.PROMPT9, State.PROMPT9ERR)

df.add_user_transition(State.PROMPT9, State.NAME, r'$name=/(\w+)|(\w+\s\w+)/')

df.add_system_transition(State.NAME, State.END, r'[! It is my pleasure chatting with you $name ":)"]')


#ERRORS
df.add_system_transition(State.PROMPT0ERR, State.ERR0, '"Hmm...I do not know that one...Can you repeat the name of the laptop again?"')
df.add_system_transition(State.YNERR, State.ERR1, 'Sorry I do not understand"," is that a yes"?"')
df.add_user_transition(State.ERR1, State.Y1, "[{yes, yeah, yea, ye, right, correct, do}]")
df.add_user_transition(State.ERR1, State.N1, "[{no, nope, nah, dont}]")
df.add_system_transition(State.PROMPT2ERR, State.PROMPT2, 'I dont quite understand... How many years approximately"?"')
df.add_system_transition(State.YNERR1, State.ERR2, 'Sorry I do not understand"," is that a yes"?"')
df.add_user_transition(State.ERR2, State.Y2, "[{yes, yeah, yea, ye, right, correct, do}]")
df.add_user_transition(State.ERR2, State.N2, "[{no, nope, nah, dont}]")
df.add_system_transition(State.PROMPT5ERR, State.ERR3, 'Sorry I do not understand"," is that a yes"?"')
df.add_user_transition(State.ERR3, State.Y3, "[{yes, yeah, yea, ye, right, correct, do}]")
df.add_user_transition(State.ERR3, State.N3, "[{no, nope, nah, dont}]")
df.add_system_transition(State.PROMPT6ERR, State.ERR4, '"I dont quite get what you mean...How about Apple?? (Hint: you have no choice hehe)"')
df.add_user_transition(State.ERR4, State.APPLE_S, '/.*/')
df.add_system_transition(State.PROMPT7ERR, State.ERR5, '"umm...you have a good point. Do you think my suggestion is useful?"')
df.add_user_transition(State.ERR5, State.Y4, "[{yes, yeah, yea, ye, right, correct, do}]")
df.add_user_transition(State.ERR5, State.N4, "[{no, nope, nah, dont}]")
df.add_system_transition(State.PROMPT8ERR, State.ERR6, '"Please enter the number between 1 to 5"')
df.add_user_transition(State.ERR6, State.BAD, '/[0-1]/')
df.add_user_transition(State.ERR6, State.OK, '/[2]/')
df.add_user_transition(State.ERR6, State.GOOD, '/[3-5]/')
df.add_system_transition(State.PROMPT9ERR, State.ERR7, '"Oops sorry I got distracted, what is your first name?"')
df.add_user_transition(State.ERR7, State.NAME, r'$name=/(\w+)|(\w+\s\w+)/')


df.run(debugging=False)