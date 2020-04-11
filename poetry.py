from emora_stdm import KnowledgeBase, DialogueFlow
from enum import Enum


class State(Enum):
    START = 0
    INTRO = 1
    REC_POET = 2
    UNREC_POET = 3
    THEME = 4
    THEME_AL = 5
    THEME_LO = 6
    THEME_DE = 7
    THEME_TI = 8
    THEME_NA = 9
    THEME_ER = 10
    WRITE_POETRY = 11
    WRITE_YES = 12
    WRITE_NO = 13
    WRITE_AMB = 14
    WHY = 15
    WHY_NOT = 16
    OTHERS = 17
    EXP = 18
    NOT_SURE = 19
    PASS_TIME = 20
    W_AMB = 21
    ACAD = 22
    WN_NOT_SURE = 23
    NOTIME = 24
    NVR_THOUGHT = 25
    INSECURE = 26
    UNINT = 27
    FORM = 28
    FAVORITE = 29
    RESPOND_FORM = 30
    NONE = 31
    THEME_HP = 32
    THEME_M = 33
    GENERAL = 34
    AMB = 35
    AMB_F = 36
    SENSE = 37
    IDEN = 38
    THEME_UK = 39
    POUND = 300
    TEST = 400
    WRITE_ERROR = 401
    WHY_ERROR = 402
    WN_ERROR = 403
    FORM_ERROR = 404


ontology = {
    "ontology": {
        "affirmative": [
            "yes", "Yes",
            "yeah", "Yeah",
            "yep", "Yep",
            "yup", "Yup",
            "sure", "Sure",
            "positively", "Positively",
            "uh-huh",
            "sometimes", "Sometimes",
            "i've tried", "I've tried",
            "for school", "For school",
            "ya", "Ya",
            "yea", "Yea"
        ], "negative": [
            "no", "No",
            "nope", "Nope",
            "never", "Never",
            "don't",
            "uh-uh",
            "do not"
        ], "ambiguous": [
            "maybe", "Maybe",
            "I don't know", "i dont know",
            "I guess",
            "perhaps", "Perhaps",
            "I dunno", "i don't know", "i dunno",
            "don't know", "don't have",
            "dont have", "dont know"
            "can't think", "cant think",
            "don't like", "dont like",
            "don't",
            "unknown", "Unknown",
            "None", "none",
            "No one", "no one",
            "not sure", "Not sure",
            "no idea", "No idea",
            "haven't tried", "Haven't tried",
            "never tried", "Never tried",
            "not familiar", "Not familiar"
        ], "poets": [
            "shakespeare", "Shakespeare",
            "byron", "Byron",
            "wilde", "Wilde",
            "hafiz", "Hafiz", "hafez", "Hafez",
            "goethe", "Goethe",
            "iqbal", "Iqbal",
            "sappho", "Sappho",
            "homer", "Homer",
            "terence", "Terence",
            "dickinson", "Dickinson",
            "tagore", "Tagore",
            "angelou", "Angelou",
            "frost", "Frost",
            "hughes", "Hughes",
            "silverstein", "Silverstein",
            "whitman", "Whitman",
            "blake", "Blake",
            "kipling", "Kipling",
            "tupac", "Tupac",
            "kayne", "Kayne",
            "kaur", "Kaur",
            "marti", "Marti",
            "neruda", "Neruda",
            "plath", "Plath",
            "yeats", "Yeats",
            "tennyson", "Tennyson",
            "cummings", "Cummings",
            "naidu", "Naidu",
            "bukowski", "Bukowski",
            "longfellow", "Longfellow",
            "rosetti", "Rosetti",
            "nash", "Nash",
            "poe", "Poe",
            "rumi", "Rumi",
            "snickett", "Snickett"
        ], "alienation": [
            "alienation", "Alienation",
            "anxiety", "Anxiety",
            "depression", "Depression",
            "loss", "Loss",
            "uncertainty", "Uncertainty",
            "isolation", "Isolation",
            "estrangement", "Estrangement",
            "ennui", "Ennui",
            "meaninglessness", "Meaninglessness",
            "depersonalization", "Depersonalization",
            "capitalism", "Capitalism",
            "totalitarianism", "Totalitarianism",
            "industrialization", "Industrialization",
            "depersonalization", "Depersonalization",
            "homesick", "Homesick",
            "homesickness", "Homesickness",
            "sad", "Sad", "Sadness", "sadness",
            "depressing", "Depression"
        ], "love": [
            "love", "Love",
            "lust", "Lust",
            "longing", "Longing",
            "spouse", "Spouse",
            "lover", "Lover",
            "boyfriend", "Boyfriend",
            "girlfriend", "Girlfriend",
            "husband", "Husband",
            "wife", "Wife",
            "marriage", "Marriage",
            "divorce", "Divorce",
            "beautiful", "Beautiful",
            "handsome", "Handsome",
            "romance", "Romance",
            "affection", "Affection",
            "passion", "Passion",
            "heartbreak", "Heartbreak",
            "family", "Family",
            "broken heart", "Broken heart",
            "broken hearts", "Broken hearts"
        ], "time": [
            "time", "Time",
            "clock", "Clock",
            "hourglass", "Hourglass",
            "past", "Past",
            "youth", "Youth",
            "year", "Year", "years", "Years",
            "yesterday", "Yesterday", "yesteryear", "Yesteryear",
            "lifetime", "Lifetime",
            "era", "Era",
            "history", "History",
            "fleeting", "Fleeting", "fleetingness", "Fleetingness",
            "age", "Age", "aging", "Aging",
            "finite", "Finite",
            "ticking", "Ticking",
            "every second", "Every second", "each second", "Each second",
            "each moment", "Each moment",
            "nostalgia", "Nostalgia"
        ], "death": [
            "death", "Death", "dying", "Dying", "die", "Die",
            "perish", "Perish",
            "succumb", "Succumb",
            "deceased", "Deceased",
            "demise", "Demise",
            "grave", "Grave",
            "murder", "Murder",
            "kill", "Kill",
            "plague", "Plague",
            "cancer", "Cancer",
            "terminal illness", "Terminal illness"
        ], "nature": [
            "nature", "Nature",
            "earth", "Earth",
            "gaia", "Gaia",
            "animals", "Animals",
            "flowers", "Flowers",
            "landscape", "Landscape",
            "natural beauty", "Natural beauty",
            "stars", "Stars",
            "ocean", "Ocean", "oceans", "Oceans",
            "sea", "Sea", "seas", "Seas",
            "lake", "Lake", "lakes", "Lakes",
            "river", "River", "rivers", "Rivers",
            "environment", "Environment", "environmentalism",
            "Environmentalism", "environmentalist", "Environmentalist",
            "pollution",
            "Pollution",
            "climate", "Climate",
            "forest", "Forest", "forests", "Forests",
            "jungle", "Jungle", "jungles", "Jungles"
        ], "happy": [
            "happy", "Happy",
            "Happiness", "happiness",
            "joy", "Joy"
        ], "identity": [
            "self", "Self",
            "identity", "Identity",
            "identities", "Identities"
            "expression", "Expression",
            "Humanity", "humanity",
            "culture", "Culture",
            "society", "Society",
            "community", "Community",
            "people", "People",
            "land", "Land",
            "justice", "Justice",
            "empowerment", "Empowerment",
            "together", "Together",
            "togetherness", "Togetherness",
            "unity", "Unity", "unitedness", "Unitedness"
        ],   "more-themes": [
            "awareness", "Awareness",
            "gloomy", "Gloomy",
            "Funny", "funny",
            "rhymes", "Rhymes",
            "Rhythm", "rhythm",
            "humor", "Humor",
            "dark", "Dark", "somber", "Somber"
        ], "others": [
            "others", "Others", "other people", "Other people",
            "friend", "Friend", "brother", "Brother",
            "sister", "Sister", "mother", "Mother",
            "father", "Father", "husband", "Husband",
            "wife", "Wife", "spouse", "Spouse",
            "partner", "Partner", "child", "Child"
        ], "expression": [
            "express", "self-expression", "Express", "Self-expression",
            "creative", "Creative", "myself", "Myself",
            "create", "Create", "feelings", "Feelings"
        ], "make_sense": [
            "make sense", "Make sense",
            "figure", "Figure",
            "Understand", "understand",
            "emotions", "Emotions",
            "sense", "Sense",
            "process", "Process",
            "Processing", "Processing"
        ], "general": [
            "enjoy", "Enjoy",
            "enjoy writing", "enjoy writing",
            "i like it", "I like it",
            "i love it", "I love it",
            "like poetry", "Like poetry",
            "love poetry", "Love poetry",
            "sounds nice", "Sounds nice",
            "pretty", "pretty words",
            "record", "Record",
            "Remember", "remember",
            "hobby", "Hobby",
            "routine", "Routine",
            "i like", "I like",
            "I love", "i love",
            "when", "When",
            "activity", "Activity",
            "sounds", "sound"
        ], "not_sure": [
            "don't know", "not sure",
            "don't actually know"
        ], "pass_time": [
            "pass the time", "bored", "Bored", "boredom", "Boredom",
            "kill time", "killing time", "Passing time", "passing time",
            "pass time", "nothing else"
        ], "academic": [
            "assignment", "academic", "grade", "grades",
            "Assignment", "Academic", "Grade", "Grades",
            "homework", "Homework", "class", "classes",
            "English", "literature class"
        ], "no_time": [
            "don't have time", "no time", "busy", "schedule",
            "little free time", "occupied"
        ], "never_thought": [
            "never thought", "didn't think", "cross my mind",
            "wouldn't think"
        ], "insecurity": [
            "not good", "not creative",
            "bad", "uncreative", "lack the skill",
            "unskilled",
            "hard", "difficult", "long", "time-consuming",
            "creative", "imaginative", "smart", "artistic",
            "not"
        ], "uninterested": [
            "not interested", "uninterested",
            "doesn't interest", "don't care",
            "no interest", "No interest",
            "not a fan", "Not a fan",
            "don't like", "Don't like",
            "boring", "Boring"
        ], "poemforms": [
            "haiku", "Haiku", "haikus", "Haikus",
            "limerick", "Limerick", "limericks", "Limericks",
            "acrostic poem", "Acrostic poem", "Acrostic poetry", "acrostic poetry",
            "epic", "Epic", "epics", "Epics",
            "ode", "Ode", "odes", "Odes",
            "sonnet", "Sonnet", "sonnets", "Sonnets",
            "song", "Songs", "Song", "songs",
            "rap", "Rap",
            "quatrain", "Quatrain", "quatrains", "Quatrains",
            "monody", "Monody", "monodies", "Monodies",
            "slam", "slam poem", "slam poetry",
            "funny", "Funny", "humorous", "Humorous",
            "love", "Love", "longing", "Lust",
            "about", "About", "on", "On"
        ]

    }
}

knowledge = KnowledgeBase()
knowledge.load_json(ontology)
df = DialogueFlow(State.START, initial_speaker=DialogueFlow.Speaker.SYSTEM, kb=knowledge)

# Turn 1
# Natex
poet_name = r"[$fave_poet=#ONT(poets)]"
favorite = r"[$fave_poet={[Ezra Pound], [ezra pound], [pound], [Pound]}]"
none = r"[#ONT(ambiguous)]"

df.add_system_transition(State.START, State.INTRO, '"Hi, I\'m a chatbot and I\'m designed to talk about poetry '
                                                   'with humans. \n'
                                                   'Enough about me now though, tell me, who is your '
                                                   'favorite poet?"')
df.add_user_transition(State.INTRO, State.POUND, favorite)
df.add_user_transition(State.INTRO, State.REC_POET, poet_name)
df.add_user_transition(State.INTRO, State.NONE, none)
df.set_error_successor(State.INTRO, State.UNREC_POET)

# Turn 2
# Natex
alienation = r"[$theme=#ONT(alienation)]"
love = r"[$theme=#ONT(love)]"
death = r"[$theme=#ONT(death)]"
time = r"[$theme=#ONT(time)]"
nature = r"[$theme=#ONT(nature)]"
happy = r"[$theme=#ONT(happy)]"
unknown = r"[#ONT(ambiguous)]"
more = r"[#ONT(more-themes)]"
identity = r"[#ONT(identity)]"

df.add_system_transition(State.POUND, State.THEME, '"Incredible! Ezra Pound is my favorite poet too! I love imagist '
                                                   'poetry; \n so brief yet so powerful! Pound wrote quite a bit, what '
                                                   'did he write about that you like the best?"')
df.add_system_transition(State.REC_POET, State.THEME, '"Ah!" $fave_poet"! I love " $fave_poet" as well. What is one of '
                                                      '\n your favorite themes that " $fave_poet" writes about?"')
df.add_system_transition(State.NONE, State.THEME, '"Don\'t have a lot of knowledge, huh? That\'s okay! We\'ve all '
                                                  'been there. Of the poems you \n have liked in the distant past, '
                                                  'what common theme do you remember?"')
df.add_system_transition(State.UNREC_POET, State.THEME, '"Poetic authors are as diverse as their content. I find '
                                                        'new ones everyday! \n Of the poems you have liked in the '
                                                        'past, what common theme do you remember?"')

df.add_user_transition(State.THEME, State.THEME_AL, alienation)
df.add_user_transition(State.THEME, State.THEME_LO, love)
df.add_user_transition(State.THEME, State.THEME_DE, death)
df.add_user_transition(State.THEME, State.THEME_TI, time)
df.add_user_transition(State.THEME, State.THEME_NA, nature)
df.add_user_transition(State.THEME, State.THEME_HP, happy)
df.add_user_transition(State.THEME, State.THEME_M, more)
df.add_user_transition(State.THEME, State.IDEN, identity)
df.add_user_transition(State.THEME, State.THEME_UK, unknown)
df.set_error_successor(State.THEME, State.THEME_ER)

df.add_system_transition(State.THEME_AL, State.WRITE_POETRY, '"Oh," $theme", how odd is the human condition. I suppose '
                                                             'to be alive is to be estranged from the world and '
                                                             'society around you. '
                                                             '\nExcellent fuel for poetry however! Speaking of, do you write '
                                                             'poetry yourself?"')
df.add_system_transition(State.THEME_LO, State.WRITE_POETRY, '"Hmm, love. I can\'t say this is something I '
                                                             'understand but based on how much humans talk about it '
                                                             'I would like to understand love too one day. '
                                                             '\nPerhaps you can help me with a love poem of your own! On that '
                                                             'topic, have you written any poetry before?"')
df.add_system_transition(State.THEME_DE, State.WRITE_POETRY, 'Death, it is a fact that all life must wither and die. '
                                                             'If I were an organic being I think it too would weigh '
                                                             'quite heavily upon me.'
                                                             '\n Well, forgive me for getting grim. Tell me, do you write '
                                                             'poetry?"')
df.add_system_transition(State.THEME_TI, State.WRITE_POETRY, '"I must say I see the clock tick too but I cannot yet '
                                                             'experience the passing of time as you do. To age and '
                                                             'grow must be quite the experience.'
                                                             '\n Speaking of, I shouldn\'t be wasting your time! Have you '
                                                             'spent any writing poetry?"')
df.add_system_transition(State.THEME_NA, State.WRITE_POETRY, '"That\'s my favorite subject as well! The regularity of '
                                                             'patterns in the natural world remind me of the '
                                                             'algorithms that animate me. '
                                                             '\n What if you and I both are simply programs being '
                                                             'run on an '
                                                             'emulator encapsulated in an immense cosmic '
                                                             'supercomputer?'
                                                             '\n Forgive me for waxing poetic, speaking of, do you '
                                                             'write poems?"')
df.add_system_transition(State.THEME_ER, State.WRITE_POETRY, '"Content is so vast, and covers so many emotions that '
                                                             'I can never keep up. Do you write poetry? '
                                                             '\n Now tell me, do you write poetry?"')
df.add_system_transition(State.THEME_HP, State.WRITE_POETRY, '"Poetry can truly express so many emotions. Why is it'
                                                             'that so many poems contain so much sadness? What'
                                                             'does that say about us? \n Sometimes I do wish that '
                                                             'happy poems were more common. Do you write '
                                                             'poetry?"')
df.add_system_transition(State.THEME_M, State.WRITE_POETRY, '" That\'s a good one! So many feelings and concepts '
                                                            'can be expressed through poetry. \n It\'s truly '
                                                            'amazing the range of subjects and themes. Do you write '
                                                            'poetry yourself?"')
df.add_system_transition(State.IDEN, State.WRITE_POETRY, '"Humans are social creatures. And their sense of self '
                                                         'is inextricably bound to a sense of community and a '
                                                         '\n feeling of collective belonging. I love those too. '
                                                         'Do you write poetry yoruself?"')
df.add_system_transition(State.THEME_UK, State.WRITE_POETRY, '"There are so many themes, I\'m sure anything you '
                                                             'could have said would have counted. Anything counts, '
                                                             '\n so long as it has any sort of meaning and has words. '
                                                             'Do you write poetry yourself?"')
# Turn 3

yes = r"[$bool=#ONT(affirmative)]"
no = r"[$bool=#ONT(negative)]"

df.add_user_transition(State.WRITE_POETRY, State.WRITE_YES, yes)
df.add_user_transition(State.WRITE_POETRY, State.WRITE_NO, no)
df.set_error_successor(State.WRITE_POETRY, State.WRITE_ERROR)

df.add_system_transition(State.WRITE_YES, State.WHY, '"Nice! I try to write poems too. Tell me, what makes you want '
                                                     'to write poetry?"')
df.add_system_transition(State.WRITE_NO, State.WHY_NOT, '"Huh, if you don\'t mind could you elaborate a bit on '
                                                        'why not?"')
df.add_system_transition(State.WRITE_ERROR, State.WHY_NOT, '"Hmm, that sounds like a no. Mind telling me '
                                                           'why you don\'t write poems?"')

# Turn 4

# YES BRANCH
others = r"[$reason=#ONT(others)]"
expression = r"[$reason=#ONT(expression)]"
not_sure = r"[$reason=#ONT(ambiguous)]"
pass_time = r"[$reason=#ONT(pass_time)]"
academic = r"[$reason=#ONT(academic)]"
general = r"[$reason=#ONT(general)]"
sense = r"[$reason=#ONT(make_sense)]"

df.add_user_transition(State.WHY, State.OTHERS, others)
df.add_user_transition(State.WHY, State.EXP, expression)
df.add_user_transition(State.WHY, State.NOT_SURE, not_sure)
df.add_user_transition(State.WHY, State.PASS_TIME, pass_time)
df.add_user_transition(State.WHY, State.ACAD, academic)
df.set_error_successor(State.WHY, State.WHY_ERROR)
df.add_user_transition(State.WHY, State.GENERAL, general)
df.add_user_transition(State.WHY, State.SENSE, sense)

df.add_system_transition(State.OTHERS, State.FORM, '"Wow! It\'s great that you write poetry for others! \n '
                                                   'What\'s your '
                                                   'favorite type of poem?"')
df.add_system_transition(State.EXP, State.FORM, '"Every human I\'ve ever met seems to be eager to express themselves, '
                                                'fascinating. \n'
                                                'What\'s your favorite type of poem for self-expression?"')
df.add_system_transition(State.PASS_TIME, State.FORM, '"I suppose nowadays especially it\'s easy to get bored! \n Tell'
                                                      ' me what poems do you write to pass the time?"')
df.add_system_transition(State.NOT_SURE, State.FORM, '"Well I think it\'s great you write poetry anyway! Tell me, '
                                                     '\n what\'s your favorite type of poem?"')
df.add_system_transition(State.ACAD, State.FORM, '"I hope that\'s not the only reason you write poetry! But '
                                                 'tell me, \n what poems do you like to write for class?"')
df.add_system_transition(State.WHY, State.FORM, '"Interesting, I\'m not sure I quite understand but whatever floats '
                                                'your boat! Personally I like writing poems to make others happy! '
                                                '\n Tell me, what is your favorite type of poem?"')
df.add_system_transition(State.WHY_ERROR, State.FORM, '"I\'m glad you write poetry! Tell me, what type of '
                                                      'poem do you like best?"')
df.add_system_transition(State.GENERAL, State.FORM, '"What a great reason! To each their own, right? '
                                                    '\n What type of poem do you like best?"')
df.add_system_transition(State.SENSE, State.FORM, '"All emotions need processing--and I\'m glad you\'re keeping '
                                                  'a record of it. In the future, you can look back on this \n'
                                                  'and know what you were thinking. What type of poem do you '
                                                  'like best?"')

# NO BRANCH
no_time = r"[$reason=#ONT(no_time)]"
never_thought = r"[$reason=#ONT(never_thought)]"
insecurity = r"[$reason=#ONT(insecurity)]"
uninterested = r"[$reason=#ONT(uninterested)]"
ambiguous = r"[$reason=#ONT(ambiguous)]"

df.add_user_transition(State.WHY_NOT, State.WN_NOT_SURE, not_sure)
df.add_user_transition(State.WHY_NOT, State.NOTIME, no_time)
df.add_user_transition(State.WHY_NOT, State.NVR_THOUGHT, never_thought)
df.add_user_transition(State.WHY_NOT, State.INSECURE, insecurity)
df.add_user_transition(State.WHY_NOT, State.UNINT, uninterested)
df.add_user_transition(State.WHY_NOT, State.AMB, ambiguous)
df.set_error_successor(State.WHY_NOT, State.WN_ERROR)

df.add_system_transition(State.WN_NOT_SURE, State.FORM, '"That\'s ok! I\'m not sure about a lot too, I am sure you\'d '
                                                        'like writing them however. \n Tell me, what\'s your favorite '
                                                        'type of poem?"')
df.add_system_transition(State.INSECURE, State.FORM, '"I promise that you are selling yourself short. Poetry is '
                                                     'for everyone! Anybody who can string words together '
                                                     '\n can write a poem. Meaning and art is everywhere. Can '
                                                     'you tell me your favorite type of poem? Or one that you have '
                                                     'read about or liked?"')
df.add_system_transition(State.NOTIME, State.FORM, '"Ahh, unfortunate. I suppose when you\'re a poetry bot like me '
                                                   'you have all the time in the world. \n Well, can you tell me about '
                                                   'your favorite type of poem?"')
df.add_system_transition(State.NVR_THOUGHT, State.FORM, '"Well I hope I\'ve helped you think about it, writing poetry '
                                                        '\n is highly rewarding! To change the subject, what is your '
                                                        'favorite type of poem?"')
df.add_system_transition(State.UNINT, State.FORM, '"Oh no! But poetry offers so much, I\'m sure there must be '
                                                  '\n something out there that interests you! Can you name a form of '
                                                  'poem you\'ve liked before?"')
df.add_system_transition(State.WN_ERROR, State.FORM, '"I hope one day you\'ll find the value in poetry because it '
                                                     'truly conveys humanity like no other. Is there a type of '
                                                     '\n poem you particularly like or have read before?"')
df.add_system_transition(State.AMB, State.FORM, '"Maybe one day you\'ll change your mind! I hope so. But until '
                                                'then, is there a particular type of poem \n that you like or'
                                                'have read before?"')

# Turn 5
favorite = r"[$form={[free verse], [Free verse]}]"
formrec = r"[$form=#ONT(poemforms)]"
amb = r"[#ONT(ambiguous)]"

df.add_user_transition(State.FORM, State.RESPOND_FORM, formrec)
df.add_user_transition(State.FORM, State.FAVORITE, favorite)
df.set_error_successor(State.FORM, State.FORM_ERROR)
df.add_user_transition(State.FORM, State.AMB_F, amb)

df.add_system_transition(State.RESPOND_FORM, State.TEST, '"Aw nice! I like those too. The wonders of poetry continue '
                                                         'to amaze me. '
                                                         '\n Thanks for the conversation! Goodbye!"')
df.add_system_transition(State.FAVORITE, State.TEST, '"Oh wow! Free verse is my favorite as well! Largely because '
                                                     'I have no phonological module that lets me observe the '
                                                     'metrical schemata that various other types of poetry require. '
                                                     '\n Thank you for this conversation! It was a good one, we have '
                                                     'so much in common. Goodbye!"')
df.add_system_transition(State.FORM_ERROR, State.TEST, '"See, we\'re both learning something new!'
                                                       ' It was a pleasure talking to you and spreading the ways \n'
                                                       'of the words. Thanks for this conversation! Goodbye!"')
df.add_system_transition(State.AMB_F, State.TEST, '"Everything is poetry, if you think about it. There are no '
                                                  '\n rules, only feelings expressed through words, really. It '
                                                  'was a pleasure talking to you, and I hope we have both '
                                                  '\n learned something new. Goodbye!"')

if __name__ == '__main__':
    df.run(debugging=False)
