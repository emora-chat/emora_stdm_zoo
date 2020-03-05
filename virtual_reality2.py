from emora_stdm import KnowledgeBase, DialogueFlow, Macro, NatexNLU, NatexNLG
from enum import Enum, auto

class State(Enum):
    START = auto()

    PROMPT = auto()
    BRAND = auto()
    DEVICE = auto()

    IOWN = auto()

    GAME = auto()
    GAME_PROMPT = auto()

    HEARD_PROMPT = auto()
    HEARD_Y = auto()
    HEARD_N = auto()

    USED_PROMPT = auto()
    USED_Y = auto()
    USED_N = auto()

    PLATFORM_GAME_PROMPT = auto()

    LIKE_GAME = auto()
    LIKE_GAME_Y = auto()
    LIKE_GAME_N = auto()

    FAV_GAME = auto()
    FAV_GAME_Y = auto()
    FAV_GAME_N = auto()
    WHY_FAV = auto()
    OTHER_GAME = auto()
    UNFAMILIAR = auto()
    PLAY_VG = auto()
    FAVE_GAME_Q = auto()
    UNKNOWN_GAME = auto()
    NO_VG = auto()
    END = auto()

    GEN_GENRE = auto()
    GENRE = auto()

    GENRE_Y = auto()

    GAME_REC = auto()
    GAME_REC_Y = auto()
    GAME_REC_N = auto()

    GENRE_N = auto()
    GAME_GENRE_ASK = auto()
    UNKNOWN_GAME_PROMPT = auto()
    LIKE_GAME_UNKNOWN = auto()
    LIKE_GAME_Y_UNKNOWN = auto()

    OTHER_DEVICE = auto()
    NOMORE_OTHER_DEVICE = auto()
    USED_OTHER_DEVICE = auto()

    FAVE_GAME_NOVR = auto()
    ACCEPT_GAME = auto()

    USED_PROMPT_ERR = auto()
    UNFAMILIAR_ERR = auto()
    FAVE_GAME_NOVR_ERR = auto()
    GAME_PROMPT_ERR = auto()
    DEVICE_ERR = auto()
    LIKE_GAME_ERR = auto()
    LIKE_GAME_UNKNOWN_ERR = auto()
    FAV_GAME_ERR = auto()
    WHY_FAV_ERR = auto()
    GENRE_ERR = auto()
    GAME_REC_ERR = auto()
    OTHER_DEVICE_ERR = auto()
    PLATFORM_GAME_PROMPT_ERR = auto()
    GAME_GENRE_ASK_ERR = auto()

ont_dict = {
        "ontology": {
            "ontbrand":
            [
                "htc",
                "valve",
                "oculus",
                "google"
            ],
            "ontgame":
            [
                "vrchat",
                "beat saber",
                "superhot",
                "arizona sunshine",
                "tetris effect",
                "job simulator",
                "alyx",
                "half life"

            ],
            "ontdevice":
            [
                "vive",
                "vive pro eye",
                "index",
                "rift",
                "rift s",
                "cardboard"
            ],
            "ontyes":
            [
                "yes",
                "yea",
                "yeah",
                "yah",
                "yahh",
                "yahhh",
                "yuh",
                "yuhh",
                "yuhhh",
                "ye",
                "sure",
                "do"
            ],
            "ontno":
            [
                "no",
                "nope",
                "nah",
                "nahh",
                "nahhh",
                "nyeh",
                "dont",
                "not"
            ],
            "ontfeelings":
            [
                "happy",
                "relaxing",
                "action",
                "fantasize",
                "strategy"
            ],
            "ontgenre":
            [
                "fps",
                "rpg",
                "rhythm",
                "battle royale",
                "simulator"
            ]
        }
}

class MyMacro(Macro):
    # define method to run when macro is evaluated in Natex
    def run(self, ngrams, vars, args):
        genres = ["fps", "rpg", "rhythm", "battle royale", "simulator"]
        feelings = {
            "happy": 2,
            "relaxing": 4,
            "action": 0,
            "fantasize": 1,
            "strategy": 3,
        }
        game_recs = {
            0: "superhot",
            1: "vrchat",
            2: "beat saber",
            3: "arizona sunshine",
            4: "job simulator"
        }
        feeling = args[0]
        mode = args[1]
        genre = feelings.get(feeling)
        if mode == "genre":
            return genres[genre]
        return game_recs.get(genre)

natex_genre = NatexNLG('[!"Okay! Then, do you like the" #MyMacro($feeling,genre) "game genre?"]', macros={'MyMacro': MyMacro()})
natex_game = NatexNLG('[!"You should try" #MyMacro($feeling,game)"! Does that sound interesting?"]', macros={'MyMacro': MyMacro()})

class MyMacro2(Macro):
    # define method to run when macro is evaluated in Natex
    def run(self, ngrams, vars, args):
        device_ages = {
            "vive":"3",
            "cardboard":"5",
            "index":"1",
            "rift":"3",
        }

        model = args[0]

        return device_ages.get(model)

natex_device_age = NatexNLG('[!$device "is" #MyMacro2($device) "years old. Have you tried other brands?"]', macros={'MyMacro2': MyMacro2()})

knowledge = KnowledgeBase()
knowledge.load_json(ont_dict)
df = DialogueFlow(State.START, initial_speaker=DialogueFlow.Speaker.SYSTEM, kb=knowledge)

df.add_system_transition(State.START, State.USED_PROMPT, '"Let\'s talk about virtual reality! Have you used VR before?"')

df.add_system_transition(State.USED_N, State.UNFAMILIAR, '[!"VR is a new immersive video game technology. Do you play video games?"]')

df.add_user_transition(State.UNFAMILIAR, State.PLAY_VG, "[$response=#ONT(ontyes)]")
df.add_user_transition(State.UNFAMILIAR, State.NO_VG, "[$response=#ONT(ontno)]")
df.add_system_transition(State.PLAY_VG, State.FAVE_GAME_NOVR, '[!"Awesome! What\'s your favorite game?"]')
df.add_user_transition(State.FAVE_GAME_NOVR, State.ACCEPT_GAME, "[$game=#ONT(ontgame)]")
df.add_system_transition(State.ACCEPT_GAME, State.END, '"Nice choice! Since you like games I suggest you try VR. Bye for now!"')

df.add_user_transition(State.FAVE_GAME_Q, State.FAV_GAME_Y, "[$game=#ONT(ontgame)]")

df.add_user_transition(State.USED_PROMPT, State.BRAND, "[$brand=#ONT(ontbrand)]", score=2)
df.add_user_transition(State.USED_PROMPT, State.GAME, "[$game=#ONT(ontgame)]", score=2)
df.add_user_transition(State.USED_PROMPT, State.USED_Y, "[$response=#ONT(ontyes)]", score=1)
df.add_user_transition(State.USED_PROMPT, State.USED_N, "[$response=#ONT(ontno)]", score=1)

df.add_system_transition(State.USED_Y, State.GAME_PROMPT, '[!"What games have you played?"]')

df.add_user_transition(State.PLATFORM_GAME_PROMPT, State.BRAND, "[$brand=#ONT(ontbrand)]")
df.add_user_transition(State.GAME_PROMPT, State.GAME, "[$game=#ONT(ontgame)]")

df.add_system_transition(State.BRAND, State.DEVICE, '[! $brand "is so cool!, which" $brand"device do you use?"]')
df.add_system_transition(State.GAME, State.LIKE_GAME, '[! $game "is a pretty cool game! Did you like playing it?"]')

df.add_user_transition(State.LIKE_GAME, State.LIKE_GAME_Y, "[$response=#ONT(ontyes)]")
df.add_user_transition(State.LIKE_GAME, State.LIKE_GAME_N, "[$response=#ONT(ontno)]")
df.add_user_transition(State.LIKE_GAME_UNKNOWN, State.LIKE_GAME_Y_UNKNOWN, "[$response=#ONT(ontyes)]")
df.add_user_transition(State.LIKE_GAME_UNKNOWN, State.LIKE_GAME_N, "[$response=#ONT(ontno)]")

df.add_system_transition(State.LIKE_GAME_Y_UNKNOWN, State.FAV_GAME, '[!"Great! Is that your favorite game?"]')

df.add_system_transition(State.LIKE_GAME_Y, State.FAV_GAME, '[! "Is" $game "your favorite game?"]')
df.add_user_transition(State.FAV_GAME, State.FAV_GAME_Y, "[$response=#ONT(ontyes)]")
df.add_user_transition(State.FAV_GAME, State.FAV_GAME_N, "[$response=#ONT(ontno)]")

df.add_system_transition(State.FAV_GAME_Y, State.WHY_FAV, '"That\'s a cool favorite game! Why do you like it?"')
df.add_system_transition(State.FAV_GAME_N, State.FAVE_GAME_Q, '"Oh ok, what\'s your favorite game then?"')
df.add_system_transition(State.LIKE_GAME_N, State.FAVE_GAME_Q, '"Oh that\'s a shame, what\'s your favorite game?"')

df.add_user_transition(State.WHY_FAV, State.GEN_GENRE, "[$feeling=#ONT(ontfeelings)]")
df.add_system_transition(State.GEN_GENRE, State.GENRE, natex_genre)

df.add_user_transition(State.GENRE, State.GENRE_Y, "[$response=#ONT(ontyes)]")
df.add_user_transition(State.GENRE, State.GENRE_N, "[$response=#ONT(ontno)]")

df.add_system_transition(State.GENRE_Y, State.GAME_REC, natex_game)
df.add_system_transition(State.GENRE_N, State.GAME_GENRE_ASK, '"What\'s your favorite genre, then?"')

df.add_user_transition(State.GAME_GENRE_ASK, State.GENRE_Y, "[$response=#ONT(ontgenre)]")

df.add_user_transition(State.GAME_REC, State.GAME_REC_Y, "[$response=#ONT(ontyes)]")
df.add_user_transition(State.GAME_REC, State.GAME_REC_N, "[$response=#ONT(ontno)]")

df.add_system_transition(State.GAME_REC_Y, State.PLATFORM_GAME_PROMPT, '"Awesome, I hope you try it out! What brand of VR device have you used?"')
df.add_system_transition(State.GAME_REC_N, State.PLATFORM_GAME_PROMPT, '"Drat... at least there are a ton of other games! What brand of VR device have you used?"')

df.add_user_transition(State.DEVICE, State.IOWN,"[$device=#ONT(ontdevice)]")

df.add_system_transition(State.IOWN, State.OTHER_DEVICE, natex_device_age)
df.add_user_transition(State.OTHER_DEVICE, State.BRAND, "[$brand=#ONT(ontbrand)]", score=2)
df.add_user_transition(State.OTHER_DEVICE, State.USED_OTHER_DEVICE, "[$response=#ONT(ontyes)]", score=1)
df.add_user_transition(State.OTHER_DEVICE, State.NOMORE_OTHER_DEVICE, "[$response=#ONT(ontno)]", score=1)

df.add_system_transition(State.USED_OTHER_DEVICE, State.PLATFORM_GAME_PROMPT, '"Wow! You\'re an experienced VR user. What other brand have you tried?"')
df.add_system_transition(State.NOMORE_OTHER_DEVICE, State.END, '"No worries! Thanks for chatting today, goodbye!"')



## Error handling!

df.add_system_transition(State.NO_VG, State.END, '"Sorry to hear that. That\'s all I know about. Goodbye!"')
df.add_system_transition(State.END, State.END, '"That\'s all for now, goodbye!!"')
df.set_error_successor(State.END, State.END)

df.add_system_transition(State.USED_PROMPT_ERR, State.USED_PROMPT, '"Not sure what you said, have you used VR before?"')
df.set_error_successor(State.USED_PROMPT, State.USED_PROMPT_ERR)

df.add_system_transition(State.UNFAMILIAR_ERR, State.UNFAMILIAR, '"I didn\'t catch that, do you play video games?"')
df.set_error_successor(State.UNFAMILIAR, State.UNFAMILIAR_ERR)

df.add_system_transition(State.FAVE_GAME_NOVR_ERR, State.END, '"That\'s a great game! Consider checking out VR if you enjoy video games. Bye for now!"')
df.set_error_successor(State.FAVE_GAME_NOVR, State.FAVE_GAME_NOVR_ERR)

df.add_system_transition(State.GAME_PROMPT_ERR, State.LIKE_GAME_UNKNOWN, '"I don\'t know that game, but it sounds interesting. Did you like it?"')
df.set_error_successor(State.GAME_PROMPT, State.GAME_PROMPT_ERR)

df.add_system_transition(State.PLATFORM_GAME_PROMPT_ERR, State.DEVICE, '"I don\'t know that brand, what device did you use?"')
df.set_error_successor(State.PLATFORM_GAME_PROMPT, State.PLATFORM_GAME_PROMPT_ERR)

df.add_system_transition(State.DEVICE_ERR, State.DEVICE, '"I didn\'t catch that, can you try another device?"')
df.set_error_successor(State.DEVICE, State.DEVICE_ERR)

df.add_system_transition(State.LIKE_GAME_ERR, State.LIKE_GAME, '"Unsure what you said, did you like the game or no?"')
df.set_error_successor(State.LIKE_GAME, State.LIKE_GAME_ERR)

df.add_system_transition(State.LIKE_GAME_UNKNOWN_ERR, State.LIKE_GAME_UNKNOWN, '"Unsure what you said there, did you like the game or no?"')
df.set_error_successor(State.LIKE_GAME_UNKNOWN, State.LIKE_GAME_UNKNOWN_ERR)

df.add_system_transition(State.FAV_GAME_ERR, State.FAV_GAME, '"Hmm... I\'m having trouble understanding, sorry. Is it you favorite?"')
df.set_error_successor(State.FAV_GAME, State.FAV_GAME_ERR)

df.add_system_transition(State.WHY_FAV_ERR, State.PLATFORM_GAME_PROMPT, '"Thanks for sharing! What brand of VR have you used?"')
df.set_error_successor(State.WHY_FAV, State.WHY_FAV_ERR)

df.add_system_transition(State.GENRE_ERR, State.GENRE, '"Can you try again, did you like that genre?"')
df.set_error_successor(State.GENRE, State.GENRE_ERR)

df.add_system_transition(State.GAME_REC_ERR, State.GAME_REC, '"I want to make sure I heard you right, would you be interested in that game?"')
df.set_error_successor(State.GAME_REC, State.GAME_REC_ERR)

df.add_system_transition(State.OTHER_DEVICE_ERR, State.OTHER_DEVICE, '"I didn\'t get that, have you used other brands?"')
df.set_error_successor(State.OTHER_DEVICE, State.OTHER_DEVICE_ERR)

df.add_system_transition(State.UNKNOWN_GAME, State.WHY_FAV, '"I don\'t know that game, why is it your favorite?"')
df.set_error_successor(State.FAVE_GAME_Q, State.UNKNOWN_GAME)

df.add_system_transition(State.GAME_GENRE_ASK_ERR, State.PLATFORM_GAME_PROMPT, '"I like that genre too! What brand of VR have you used?"')
df.set_error_successor(State.GAME_GENRE_ASK, State.GAME_GENRE_ASK_ERR)

df.run(debugging=False)
