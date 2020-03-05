from emora_stdm import KnowledgeBase, DialogueFlow
from enum import Enum, auto


# TODO: Update the State enum as needed
class State(Enum):
    START = auto()
    turn_1 = auto()
    turn_2a = auto()
    turn_2b = auto()
    turn_2c = auto()
    yes = auto()
    no_1a = auto()
    no_1b = auto()
    no_1c = auto()
    turn_3y = auto()
    turn_3na = auto()
    turn_3nb = auto()
    turn_3nc = auto()
    turn_4a = auto()
    turn_4b = auto()
    turn_4c = auto()
    turn_5 = auto()
    new = auto()
    turn_6y = auto()
    turn_6n = auto()
    iphone = auto()  # which phone they have
    samsung = auto()
    android = auto()
    iphone_2 = auto()  # which phone they have
    samsung_2 = auto()
    android_2 = auto()
    phone_ft = auto()
    ERR = auto()
    ft_a = auto()  # ask which features they like
    ft_b = auto()
    ft_c = auto()
    ft_q = auto()  # is this the only thing they like about phone
    t = auto()
    n = auto()
    n_1 = auto()
    n_2 = auto()
    n_3 = auto()
    n_4 = auto()
    another = auto()
    suggestion_1 = auto()
    suggestion_2 = auto()
    suggestion_3 = auto()
    nophone = auto()
    laptop = auto()
    included = auto()
    notincluded = auto()
    t1a = auto()
    t1b = auto()
    t2a = auto()
    t2b = auto()
    t2c = auto()
    t2d = auto()
    t2e = auto()
    t3 = auto()
    t4a = auto()
    t4b = auto()
    t5a = auto()
    t5b = auto()
    t6 = auto()
    t7 = auto()
    t8 = auto()
    t9 = auto()
    t10y = auto()
    t10n = auto()
    t11 = auto()
    t12 = auto()
    t13 = auto()
    dunno = auto()
    end = auto()
    output = auto()
    t14 = auto()
    t15 = auto()
    t16 = auto()
    t17a = auto()
    t17b = auto()
    t18 = auto()
    t19 = auto()
    t20 = auto()
    t21 = auto()
    t22 = auto()
    t23 = auto()
    t24 = auto()


# TODO: create the ontology as needed
ontology = {
    "ontology": {
        "apple phone":
            [
                "iphone",
                "apple"
            ],
        "google phone":
            [
                "pixel",
                "android",
                "htc",
                "huawei",
                "sony",
                "lg",
                "blackberry",
                "black berry",
                "nokia"
            ],
        "samsung phone":
            [
                "galaxy",
                "samsung",
                "note"
            ],
        "apple laptop":
            [
                "mac",
                "macbook",
                "mac pro",
                "macbook pro",
                "mac air",
                "macbook air"
            ],
        "y":
            [
                "yes",
                "yeah",
                "yup",
                "sure",
                "of course",
                "why not",
                "a lot"
            ],
        "n":
            [
                "no",
                "not really",
                "nah",
                "not",
                "don't",
                "dont"
            ],
        "google_ft": [
            "unlimited storage",
            "google assistant",
            "fast charging",
            "wireless charging",
            "battery",
            "operating system",
            "speed",
            "price"
        ], "iphone_ft": [
            "screen",
            "design",
            "connectability",
            "airdrop",
            "water resistant",
            "sleek",
            "camera",
            "cameras"
        ], "samsung_ft": [
            "display",
            "navigation",
            "nougat",
            "resolution",
            "usb type c"
        ], "macbook pro_ft": [
            "thin",
            "light",
            "sleek",
            "touch bar"
        ], "surface_ft": [
            "design",
            "operating system",
            "touch screen",
            "keyboard",
            "kickstand",
            "connectivity",
            "display",
            "price",
            "thin"
        ], "hp_ft": [
            "light",
            "durable",
            "display",
            "touchscreen",
            "back light",
            "price",
            "affordable"
        ], "macbook air_ft": [
            "display",
            "keyboard",
            "trackpad",
            "thin",
            "sleek"
        ], "hp laptop": [
            "hp"
        ], "surface laptop": [
            "surface"
        ], "phone_types": [
            "iphone",
            "apple",
            "pixel",
            "android",
            "blackberry",
            "samsung"
        ],
        "chromebook laptop": [
            "chromebook"
        ],
        "apple laptop": [
            "mac",
            "macbook",
            "apple"
        ]

    }
}

knowledge = KnowledgeBase()
knowledge.load_json(ontology)
df = DialogueFlow(State.START, initial_speaker=DialogueFlow.Speaker.SYSTEM, kb=knowledge)

# ask what phone does the user have
df.add_system_transition(State.START, State.turn_1, '"Hi, what phone do you have?"')

# get answer from the user
df.add_user_transition(State.turn_1, State.iphone, r"[$phone=#ONT(apple phone)]")
df.add_user_transition(State.turn_1, State.samsung, r"[$phone=#ONT(samsung phone)]")
df.add_user_transition(State.turn_1, State.android, r"[$phone=#ONT(google phone)]")
df.add_user_transition(State.turn_1, State.nophone, r"[#ONT(n)]")

# ask if the user like the phone
df.add_system_transition(State.iphone, State.turn_2a, '[! "Do you like your"$phone"?"]')
df.add_system_transition(State.samsung, State.turn_2b, '[! "Do you like your"$phone"?"]')
df.add_system_transition(State.android, State.turn_2c, '[! "Do you like your"$phone"?"]')

# get yes from the user
df.add_user_transition(State.turn_2a, State.yes, r"[#ONT(y)]")
df.add_user_transition(State.turn_2b, State.yes, r"[#ONT(y)]")
df.add_user_transition(State.turn_2c, State.yes, r"[#ONT(y)]")

# get no from the user
df.add_user_transition(State.turn_2a, State.no_1a, r"[#ONT(n)]")
df.add_user_transition(State.turn_2b, State.no_1b, r"[#ONT(n)]")
df.add_user_transition(State.turn_2c, State.no_1c, r"[#ONT(n)]")

# ask why if yes
df.add_system_transition(State.yes, State.turn_3y, '[! "Why do you like it?"]')

# ask why if no
df.add_system_transition(State.no_1a, State.turn_3na, '[! "Why don\'t you like it?"]')
df.add_system_transition(State.no_1b, State.turn_3nb, '[! "Why don\'t you like it?"]')
df.add_system_transition(State.no_1c, State.turn_3nc, '[! "Why don\'t you like it?"]')

# get whatever answer if the user doesn't like their phone
df.add_user_transition(State.turn_3na, State.turn_4a, '/.*/')
df.add_user_transition(State.turn_3nb, State.turn_4b, '/.*/')
df.add_user_transition(State.turn_3nc, State.turn_4c, '/.*/')

# answer which features of their phone they like
df.add_user_transition(State.turn_3y, State.n, '/.*/')

# ask if it’s the only thing that they like
df.add_system_transition(State.n, State.another, '[! "Is there any other thing you like about it?"]')

df.add_user_transition(State.another, State.turn_5, '/.*/')

# follow up to why don’t you like it
df.add_system_transition(State.turn_4a, State.iphone_2, '[! "Do you at least like airdrop?"]')
df.add_system_transition(State.turn_4b, State.samsung_2, '[! "Do you at least like"$phone"’s durability?"]')
df.add_system_transition(State.turn_4c, State.android_2, '[! "Do you at least like"$phone"’s system?"]')

# get whatever answer from state 4
df.add_user_transition(State.iphone_2, State.turn_5, '/.*/')
df.add_user_transition(State.samsung_2, State.turn_5, '/.*/')
df.add_user_transition(State.android_2, State.turn_5, '/.*/')

# ask if they would get a new one
df.add_system_transition(State.turn_5, State.new, '[!"Then, would you like to get a new phone?"]')

# if they want a new phone or not
df.add_user_transition(State.new, State.turn_6y, r'[#ONT(y)]')
df.add_user_transition(State.new, State.turn_6n, r'[#ONT(n)]')

# what kind of feature do they want
df.add_system_transition(State.turn_6y, State.phone_ft,
                         '[! "Which feature of phone do you care the most? (eg. camera, battery life, design) Sorry, I only know a limited number of features."]')

# get response of feature
df.add_user_transition(State.phone_ft, State.suggestion_1, r'[#ONT(iphone_ft)]')
df.add_user_transition(State.phone_ft, State.suggestion_2, r'[#ONT(google_ft)]')
df.add_user_transition(State.phone_ft, State.suggestion_3, r'[#ONT(samsung_ft)]')

# make suggestions based on feature
df.add_system_transition(State.suggestion_1, State.laptop,
                         '[! "I would suggest you to get an iphone. What about laptops? Do you have an HP, Apple, a Chromebook or Surface? (yes or no)"]')
df.add_system_transition(State.suggestion_2, State.laptop,
                         '[! "I would suggest you to get a huawei phone. What about laptops? Do you have an HP, Apple, a Chromebook or Surface? (yes or no)"]')
df.add_system_transition(State.suggestion_3, State.laptop,
                         '[! "I would suggest you to get a samsung galaxy. What about laptops? Do you have an HP, Apple, a Chromebook or Surface? (yes or no)"]')

# if they dont want a new phone
df.add_system_transition(State.turn_6n, State.laptop,
                         '[! "Too bad! What about laptops? Do you have an HP, Apple, a Chromebook or Surface? (yes or no)"]')

# if they dont have a phone
df.add_system_transition(State.nophone, State.new,
                         '[! "Ridiculous! You really need to get a phone. Do you need any suggestions on smart phones?"]')

# if the brand is included
df.add_user_transition(State.laptop, State.included, r'[#ONT(y)]')
df.add_user_transition(State.laptop, State.notincluded, r'[#ONT(n)]')

df.add_system_transition(State.included, State.t1a, '[! "Which brand do you have then?"]')
df.add_system_transition(State.notincluded, State.t1b, '[! "What kind of computer do you have then?"]')

df.add_user_transition(State.t1a, State.t2a, r'[$laptop=#ONT(apple laptop)]')
df.add_user_transition(State.t1a, State.t2b, r'[$laptop=#ONT(surface laptop)]')
df.add_user_transition(State.t1a, State.t2c, r'[$laptop=#ONT(hp laptop)]')
df.add_user_transition(State.t1a, State.t2d, r'[$laptop=#ONT(chromebook laptop)]')
df.add_user_transition(State.t1b, State.t2e, '/.*/')

df.add_system_transition(State.t2a, State.t3, '[! "Do you like the features of Apple\'s OS?"]')
df.add_system_transition(State.t2b, State.t3, '[! "Do you like the flexibility of the Surface?"]')
df.add_system_transition(State.t2c, State.t3, '[! "Do you like the light weight of the HP?"]')
df.add_system_transition(State.t2d, State.t3, '[! "Do you like the benefits that Google provides?"]')
df.add_system_transition(State.t2e, State.dunno,
                         '[! "Hmm, I have never heard about it. Could you tell me more about it?"]')

df.add_user_transition(State.dunno, State.t6, '/.*/')

df.add_user_transition(State.t3, State.t4a, r"[#ONT(y)]")
df.add_user_transition(State.t3, State.t4b, r"[#ONT(n)]")

df.add_system_transition(State.t4a, State.t5a, '[! "What do like about your computer?"]')
df.add_system_transition(State.t4b, State.t5a, '[! "Why don\'t you like about your computer?"]')

df.add_user_transition(State.t5a, State.t6, '/.*/')

df.add_system_transition(State.t6, State.t7, '[! "What kind of things do you use your computer for?"]')

df.add_user_transition(State.t7, State.t8, '/.*/')

df.add_system_transition(State.t8, State.t12, '[! "How much was it?"]')

df.add_user_transition(State.t12, State.t13, '/.*/')

df.add_system_transition(State.t13, State.t9,
                         '[! "Considering all that, do you ever get frustrated by the processing speed?"]')

df.add_user_transition(State.t9, State.t10y, r"[#ONT(y)]")
df.add_user_transition(State.t9, State.t10n, r"[#ONT(n)]")

df.add_system_transition(State.t10y, State.t11, '[! "What do you do to speed it up?"]')
df.add_system_transition(State.t10n, State.t16,
                         '[! "I\'m jealous. My grandma can run faster than my processing speed. What does your computer look like? Does it have a lot of stickers?"]')

df.add_user_transition(State.t11, State.t14, '/.*/')

df.add_system_transition(State.t14, State.t16,
                         '[! "Good suggestion! I\'ll try it out. What does your computer look like? Does it have a lot of stickers?"]')

# answer to qt of stickers
df.add_user_transition(State.t16, State.t17a, r"[#ONT(y)]")
df.add_user_transition(State.t16, State.t17b, r"[#ONT(n)]")

# what is fav sticker/why none
df.add_system_transition(State.t17a, State.t18, '[! "What is your favorite sticker?"]')
df.add_system_transition(State.t17b, State.t19, '[! "Why don\'t you have any stickers?"]')

# answer
df.add_user_transition(State.t19, State.t20, '/.*/')
df.add_user_transition(State.t18, State.t20, '/.*/')

df.add_system_transition(State.t20, State.t21,
                         '[! "Yeah, I\'m thinking about getting some more stickers to reflect my personality. Do you think your computer matches yours?"]')

df.add_user_transition(State.t21, State.t22, '/.*/')

df.add_system_transition(State.t22, State.t23, '[! "It\'s been so nice talking to you! Goodbye!"]')

df.add_user_transition(State.t23, State.t24, '/.*/')

# get back to the start
df.add_system_transition(State.t24, State.turn_1,
                         '[! "Aw! Sweet of you to stick around! Let\'s go back to phones. What phone do you have?"]')

df.set_error_successor(State.turn_1, State.START)
df.set_error_successor(State.turn_2a, State.iphone)
df.set_error_successor(State.turn_2b, State.samsung)
df.set_error_successor(State.turn_2c, State.android)
df.set_error_successor(State.new, State.turn_5)
df.set_error_successor(State.phone_ft, State.turn_6y)
df.set_error_successor(State.laptop, State.turn_6n)
df.set_error_successor(State.t1a, State.included)
df.set_error_successor(State.t1b, State.notincluded)
df.set_error_successor(State.t3, State.t2e)
df.set_error_successor(State.t9, State.t13)
df.set_error_successor(State.t16, State.t14)

# TODO: create your own dialogue manager


df.run(debugging=False)
