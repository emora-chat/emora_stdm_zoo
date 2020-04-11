
from emora_stdm import KnowledgeBase, DialogueFlow, Macro, NatexNLU, NatexNLG
from enum import Enum, auto

class State(Enum):
    START = auto()
    PROMPT = auto()

    HOW_IS_DAY = auto()
    GOOD_DAY = auto()
    GOOD_DAY_Q = auto()
    BAD_DAY = auto()
    BAD_DAY_Q = auto()

    GOOD_DAY_RESPONSE = auto()
    BAD_DAY_RESPONSE = auto()

    TOPIC_PROMPT = auto()

    MOVIE_START = auto()
    MOVIE_PROMPT = auto()
    MOVIE_N = auto()
    MOVIE_N_Q = auto()
    MOVIE_Y = auto()
    MOVIE_Y_Q = auto()
    MOVIE = auto()
    ACTOR_PROMPT = auto()
    ACTOR = auto()
    ACTOR_REASONING_PROMPT = auto()
    ACTOR_REASONING_ERR = auto()
    ACTOR_REASONING = auto()
    ACTOR_REASONING_RESPONSE = auto()
    ACTOR_REASONING_RESPONSE2 = auto()
    ACTOR_REASONING_RESPONSE_ERR = auto()
    ACTOR_END = auto()

    FOOD_START = auto()
    FOOD_PROMPT = auto()
    FOOD_N = auto()
    FOOD = auto()

    DATE_END = auto()
    END = auto()
    PROMPT_ERR = auto()
    MOVIE_PROMPT_ERR = auto()

    ACTIVITY = auto()
    FAVE_FOOD = auto()
    FOOD_END = auto()
    FOOD_START_Q = auto()


ontology = {
    "ontology": {
        "ontgoodday":
        [
            "good",
            "going well",
            "really well",
            "amazing",
            "beautiful",
            "fantastic",
            "lovely",
            "skillful",
            "fabulous",
            "nifty",
            "gravid",
            "awe-inspiring",
            "respectable",
            "great",
            "wild",
            "salutary",
            "cracking",
            "bully",
            "sound",
            "near",
            "grotesque",
            "grand",
            "upright",
            "big",
            "practiced",
            "fantastical",
            "peachy",
            "well",
            "groovy",
            "right",
            "howling",
            "full",
            "honest",
            "astonishing",
            "fantastic",
            "awing",
            "good",
            "outstanding",
            "skillful",
            "honorable",
            "with_child",
            "unspoiled",
            "neat",
            "mythical",
            "mythic",
            "dandy",
            "just",
            "serious",
            "awesome",
            "beneficial",
            "in_force",
            "keen",
            "awful",
            "marvellous",
            "wonderful",
            "rattling",
            "mythologic",
            "mythological",
            "heavy",
            "in_effect",
            "swell",
            "proficient",
            "safe",
            "tremendous",
            "fab",
            "unspoilt",
            "amazing",
            "corking",
            "marvelous",
            "terrific",
            "ripe",
            "wondrous",
            "secure",
            "smashing",
            "dependable",
            "estimable",
            "undecomposed",
            "slap-up",
            "expectant",
            "effective",
            "capital",
            "antic",
            "expert",
            "large",
            "bang-up",
            "adept",
            "not bad",
            "dear",
            "alright"
        ],
        "ontbadday":
        [
            "bad",
            "going badly",
            "terrible",
            "awful",
            "defective",
            "regretful",
            "unsound",
            "bad",
            "sad",
            "depressing",
            "awful",
            "horrific",
            "painful",
            "sorry",
            "risky",
            "tough",
            "atrocious",
            "direful",
            "terrible",
            "spoilt",
            "tremendous",
            "big",
            "fearful",
            "unfit",
            "severe",
            "abominable",
            "horrendous",
            "uncheerful",
            "wicked",
            "lamentable",
            "dread",
            "frightful",
            "high-risk",
            "frightening",
            "unfortunate",
            "distressing",
            "forged",
            "pitiful",
            "unspeakable",
            "dreadful",
            "dire",
            "speculative",
            "deplorable",
            "uncollectible",
            "dreaded",
            "fearsome",
            "inauspicious",
            "spoiled",
            "cheerless"
            "awful"
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
        "ontculinary":
        [
            "cooking",
            "eating",
            "consuming",
            "feasting",
            "chowing",
        ]
    }
}

count_questions = 0
count_absent_questions = 0
class MacroCountQuestions(Macro):
    def run(self, ngrams, vars, args):
        global count_questions
        count_questions = count_questions + 1
        # return str(count_questions)
        return ""

class MacroCountAbsentQuestions(Macro):
    def run(self, ngrams, vars, args):
        global count_absent_questions
        count_absent_questions = count_absent_questions + 1
        # return str(count_absent_questions)
        return ""

class MacroPrintNumberQuestions(Macro):
    def run(self, ngrams, vars, args):
        global count_questions, count_absent_questions
        # return str(count_absent_questions)
        if count_absent_questions == 0:
            return "This conversation ran pretty short so I didn't get the chance to analyze the conversation"
        elif count_questions == 0:
            return "In general, people like to be asked questions while conversing. You should try asking more questions!!"
        elif count_questions == count_absent_questions:
            return "In general, people like to be asked questions while conversing and you've done a really good job!"
        else:
            ret_str = "In general, people like to be asked questions while conversing. In this conversation, you asked {} out of {} questions where it would've been a good idea to do so."
        return ret_str.format(count_questions, count_absent_questions)

# expressions for when the user responds with a question
natex_good_day_movie = NatexNLG('[!"glad to hear youre having a good day I am doing pretty alright myself. have you seen any movies lately" #MacroCountQuestions()]' , macros={'MacroCountQuestions': MacroCountQuestions()})
natex_bad_day_movie = NatexNLG('[!"I am sorry to hear youre having a bad day I am doing pretty alright myself. have you seen any movies lately" #MacroCountQuestions()]', macros={'MacroCountQuestions': MacroCountQuestions()})
natex_movie_y = NatexNLG('[!"sorry, what\'s the movie called? and yes, i\'ve been watching lots of comedy films recently" #MacroCountQuestions()]', macros={'MacroCountQuestions': MacroCountQuestions()})
natex_movie_n = NatexNLG('[!"I love to watch movies! anyways, what\'s your favorite food then?" #MacroCountQuestions()]', macros={'MacroCountQuestions': MacroCountQuestions()})
natex_food_q = NatexNLG('[!"I have been investing in many travel stocks recently! anyways, what\'s your favorite food then?" #MacroCountQuestions()]', macros={'MacroCountQuestions': MacroCountQuestions()})

# expressions for when a user has the opportunity to ask a question, but doesn't
natex_good_day_nq = NatexNLG('[!"hey, that\'s pretty good then! what have you been up to lately?" #MacroCountAbsentQuestions()]', macros={'MacroCountAbsentQuestions': MacroCountAbsentQuestions()})
natex_bad_day_nq = NatexNLG('[!"oh no I am so sorry to hear that. movies tend to cheer me up. have you seen any good movies lately?" #MacroCountAbsentQuestions()]', macros={'MacroCountAbsentQuestions': MacroCountAbsentQuestions()})
natex_movie_n_nq = NatexNLG('[!"ok, what\'s your favorite food then?" #MacroCountAbsentQuestions()]', macros={'MacroCountAbsentQuestions': MacroCountAbsentQuestions()})
natex_movie_y_nq = NatexNLG('[!"sorry, what\'s the movie called?" #MacroCountAbsentQuestions()]', macros={'MacroCountAbsentQuestions': MacroCountAbsentQuestions()})
natex_food_nq = NatexNLG('[!"hmm, interesting! have you been" $response "a lot lately? What is your favorite thing to eat?" #MacroCountAbsentQuestions()]', macros={'MacroCountAbsentQuestions': MacroCountAbsentQuestions()})

# natex expression for final statement
natex_evaluation = NatexNLG('[!"well, I had a great time. i\'ll see you some other time then. bye bye..." #MacroPrintNumberQuestions()]', macros={'MacroPrintNumberQuestions': MacroPrintNumberQuestions()})

knowledge = KnowledgeBase()
knowledge.load_json(ontology)
df = DialogueFlow(State.START, initial_speaker=DialogueFlow.Speaker.SYSTEM, kb=knowledge)

df.add_system_transition(State.START, State.PROMPT, '"hows your day going?"')

df.add_user_transition(State.PROMPT, State.GOOD_DAY, '[$response=#ONT(ontgoodday)]', rank=2)
df.add_user_transition(State.PROMPT, State.BAD_DAY, '[$response=#ONT(ontbadday)]', rank=2)
df.add_user_transition(State.PROMPT, State.GOOD_DAY_Q, '<$r=#ONT(ontgoodday) {how, hows, is, are, you, your}>', rank=1)
df.add_user_transition(State.PROMPT, State.BAD_DAY_Q, '<$r=#ONT(ontbadday) {how, hows, is, are, you, your}>', rank=1)

# responses when user is asked about their day
df.add_system_transition(State.GOOD_DAY, State.TOPIC_PROMPT, natex_good_day_nq)
df.add_system_transition(State.BAD_DAY, State.MOVIE_PROMPT, natex_bad_day_nq)
df.add_system_transition(State.GOOD_DAY_Q, State.MOVIE_PROMPT, natex_good_day_movie)
df.add_system_transition(State.BAD_DAY_Q, State.MOVIE_PROMPT, natex_bad_day_movie)

# topic transitions
df.add_user_transition(State.TOPIC_PROMPT, State.FOOD_START, '[$response=#ONT(ontculinary)]', rank = 2)
df.add_user_transition(State.TOPIC_PROMPT, State.FOOD_START_Q, '<$response=#ONT(ontculinary) {what, how, have, you}>', rank=1)
df.set_error_successor(State.TOPIC_PROMPT, State.MOVIE_START)

# movie conversation
df.add_system_transition(State.MOVIE_START, State.MOVIE_PROMPT, '"so, have you seen any good movies lately?"')
df.add_user_transition(State.MOVIE_PROMPT, State.MOVIE_N, '[$response=#ONT(ontno)]', rank=2)
df.add_user_transition(State.MOVIE_PROMPT, State.MOVIE_N_Q, '<$response=#ONT(ontno) {how, is, are, you, your}>', rank=1)
df.add_user_transition(State.MOVIE_PROMPT, State.MOVIE_Y, '[$response=#ONT(ontyes)]', rank=2)
df.add_user_transition(State.MOVIE_PROMPT, State.MOVIE_Y_Q, '<$response=#ONT(ontyes) {how, is, are, you, your}>', rank=1)
df.add_system_transition(State.MOVIE_Y, State.MOVIE, natex_movie_y_nq)
df.add_system_transition(State.MOVIE_Y_Q, State.MOVIE, natex_movie_y)
df.add_system_transition(State.MOVIE_N, State.FAVE_FOOD, natex_movie_n_nq)
df.add_system_transition(State.MOVIE_N_Q, State.FAVE_FOOD, natex_movie_n)

# transition to actor
df.set_error_successor(State.MOVIE, State.ACTOR_PROMPT)
df.add_system_transition(State.ACTOR_PROMPT, State.ACTOR, '"oh ok cool. what actor or actress stand out for you?"')
df.add_user_transition(State.ACTOR, State.ACTOR_REASONING_PROMPT, '[$actor=#NER(person)]')
df.set_error_successor(State.ACTOR, State.ACTOR_REASONING_ERR)
df.add_system_transition(State.ACTOR_REASONING_PROMPT, State.ACTOR_REASONING, '[!"I\'ve actually heard that" $actor "is a pretty solid actor! What about" $actor "stood out to you?"]')
df.add_system_transition(State.ACTOR_REASONING_ERR, State.ACTOR_REASONING, '"hmm, I\'m not familiar. I guess I live under a rock. what do you like about this jabroni?"')
df.add_user_transition(State.ACTOR_REASONING, State.ACTOR_REASONING_RESPONSE, '[$reasoning=#POS(adj)]', rank=1)
df.add_user_transition(State.ACTOR_REASONING, State.ACTOR_REASONING_RESPONSE2, '[$adj=#POS(adj) $noun=#POS(noun)]', rank=2)
df.set_error_successor(State.ACTOR_REASONING, State.ACTOR_REASONING_RESPONSE_ERR)
df.add_system_transition(State.ACTOR_REASONING_RESPONSE, State.ACTOR_END, '[!"oh ok so you like them" $reasoning "huh. maybe we can see one of their movies sometime then"]')
df.add_system_transition(State.ACTOR_REASONING_RESPONSE2, State.ACTOR_END, '[!"oh" $adj $noun "huh. fair enough, that makes sense. maybe we can see one of their movies sometime then"]')
df.add_system_transition(State.ACTOR_REASONING_RESPONSE_ERR, State.ACTOR_END, '"hmm, that sounds pretty interesting."')

df.set_error_successor(State.ACTOR_END, State.DATE_END)
df.add_system_transition(State.DATE_END, State.END, natex_evaluation)

# food conversation
df.add_system_transition(State.FOOD_START_Q, State.FAVE_FOOD, natex_food_q)
df.add_system_transition(State.FOOD_START, State.FAVE_FOOD, natex_food_nq)


# error successions
df.set_error_successor(State.PROMPT, State.PROMPT_ERR)
df.add_system_transition(State.PROMPT_ERR, State.PROMPT, '"i didn\'t catch that, sorry. could you tell me again how your day is going?"')

df.set_error_successor(State.MOVIE_PROMPT, State.MOVIE_PROMPT_ERR)
df.add_system_transition(State.MOVIE_PROMPT_ERR, State.MOVIE_PROMPT, '"sorry i\'m not sure what you said. have you seen any good movies lately?"')

df.set_error_successor(State.FAVE_FOOD, State.FOOD_END)
df.add_system_transition(State.FOOD_END, State.DATE_END, '"that\'s awesome! i love to eat artichoke."')
df.set_error_successor(State.DATE_END, State.DATE_END)

if __name__ == '__main__':
    df.precache_transitions()
    df.run(debugging=False)
