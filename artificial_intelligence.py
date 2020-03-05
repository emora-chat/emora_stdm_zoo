

from emora_stdm import KnowledgeBase, DialogueFlow, Macro
from enum import Enum


class State(Enum):
    ERR = 0
    TURN2ERR = 101
    TURN3ERR = 102
    TURN4ERR = 103
    TURN5ERR = 104
    TURN6ERR = 105
    TURN7ERR = 106
    TURN8ERR = 107
    TURN9ERR = 108
    TURN10ERR = 109

    START = 1
    TURN0 = 2
    TURN1A = 3
    TURN1B = 4
    TURN2A = 5
    TURN2B = 6
    TURN2C = 7
    TURN2D = 8
    TURN3 = 9
    TURN3A = 99
    TURN3B = 32
    TURN4 = 10
    TURN4A = 41
    TURN4B = 42
    TURN5 = 11
    TURN5A = 51
    TURN6 = 12
    TURN6A = 61
    TURN7 = 13
    TURN8 = 14
    TURN9 = 15
    TURN10 = 16
    TURN10A = 161
    TURN10B = 162
    TURN2E = 17
    TURN9A = 18
    TURN10S = 19
    TURN10U= 20
    END = 100

    TURN7S = 131
    TURN7U = 132

ontology = {
    "ontology": {
        "aitypes":
            [
                "limited memory",
                "theory of mind",
                "self aware"
            ],
        "aifears":
            [
                "automation",
                "privacy",
                "uncontrollability"
                "uncontrollable"
            ],
        "response":
            [
                "affirm",
                "negative"
            ],
        "affirm":
            [
                "yeah",
                "yes",
                "ya",
                "yup",
                "ye",
                "yeet",
                "yep"
                "y",
                "yea",
                "definitely",

            ],
        "negative":
            [
                "no",
                "n",
                "nope",
                "nah",
                "never"
            ],
        "helper":
            [
                "google assistant",
                "google",
                "assistant",
                "siri",
                "alexa"
            ],
        "numbers":
            [
                "like",
                "all"
            ],
        "all":
            [
                "0",
                "zero",
                "eleven",
                "twelve",
                "thirteen",
                "fourteen",
                "fifteen",
                "sixteen",
                "seventeen",
                "eighteen",
                "nineteen",
                "twenty",
                "thirty",
                "forty",
                "fifty",
                "sixty",
                "seventy",
                "eighty",
                "ninety",
                "hundred"
            ],
        "like":
            [
                "5",
                "6",
                "7",
                "8",
                "9",
                "10",
                "five",
                "six",
                "seven",
                "eight",
                "nine",
                "ten",
                "1",
                "2",
                "3",
                "4",
                "one",
                "two",
                "three",
                "four"
            ]
        }
}

counter = 0
class counterMacro(Macro):
    #args is passed from the state transition
    def run(self, ngrams, vars, args):
        
        return counter

class posnegMacro(Macro):
    positive = True
    def run(self, ngrams, vars, args):

        return

#todo account for unknown virtual assistant
class deviceMatcher(Macro):
    #user inputs either google assistant, siri, or alexa
    #vars is being stored as $assistant
    def run(self, ngrams, vars, args):
        if 'google' in args[0] or 'assistant' in args[0]:
            return 'Google'
        elif 'siri' in args[0]:
            return 'Apple'
        else:
            return 'Amazon'

class endMacro(Macro):
    def run (self, ngrams, vars, args):
        print('Thanks for chatting with me, Goodbye!')
        exit()
        return

class years2045(Macro):
    def run (self, ngrams, vars, args):
        guess = input('what year do think the singularity will occur? ')
        str(guess)
        s = ''.join(x for x in guess if x.isdigit())
        while s == '':
            guess = input('please guess in the form of a number ')
            str(guess)
            s = ''.join(x for x in guess if x.isdigit())
        int(s)
        while int(s) != 2045:
            if int(s) > int(2045):
                print('That is too far into the future')
                newGuess = input('Guess again! ')
                str(newGuess)
                s = ''.join(x for x in newGuess if x.isdigit())
                int(s)
            else:
                print('That is too soon')
                newGuess = input('Guess again! ')
                str(newGuess)
                s = ''.join(x for x in newGuess if x.isdigit())
                int(s)
        print('Great guess! The singularity will happen in 2045!')
        return



class years2011(Macro):
    def run (self, ngrams, vars, args):
        guess = input('Interesting... What year do you think the first consumer AI was released? ')
        str(guess)
        s = ''.join(x for x in guess if x.isdigit())
        while s == '':
            guess = input('please guess in the form of a number ')
            str(guess)
            s = ''.join(x for x in guess if x.isdigit())
        int(s)
        while int(s) != 2011:
            #print('into the while loop', s)
            if int(s) > int(2011):
                print('That is too late')
                newGuess = input('Guess again! ')
                str(newGuess)
                s = ''.join(x for x in newGuess if x.isdigit())
                int(s)
            else:
                print('That is too early')
                newGuess = input('Guess again! ')
                str(newGuess)
                s = ''.join(x for x in newGuess if x.isdigit())
                int(s)
        return

class aiConcerns(Macro):
    def run(self, ngrams, vars, args):
        #print('arg0', args[0])
        if 'automation' in args[0]:
            print('Automation is a very big concern. However it is currently happening now across the world, independent of advances in AI')
            return
        elif 'privacy' in args[0]:
            print('Privacy has different meanings across the world. In some places like China, it is normal to be surveilled by AI')
            return
        elif 'uncontrollability' in args[0] or 'uncontrollable' in args[0]:
            print("I think this is the most concerning. Oftentimes researchers themselves don't 100% understand how their AI is thinking.")
            return
        else:
            return




#use macros = , and then reference the dictionary of the macros
#if you don't need to pass anything into the macro at the beginning you don't need to implement the init function
knowledge = KnowledgeBase()
knowledge.load_json(ontology)
df = DialogueFlow(State.START, initial_speaker=DialogueFlow.Speaker.SYSTEM, kb=knowledge, macros = {'posnegMacro':posnegMacro(), 'deviceMatcher':deviceMatcher(), 'endMacro':endMacro(), 'years2045':years2045(), 'years2011':years2011(), 'aiConcerns':aiConcerns()})

#TURN 0 DON"T TOUCH ITS GOOD TODO account for "i don't know"
df.add_system_transition(State.START, State.TURN0, '"Hi, I\'m Dooley, a chatbot. Within AI, there are four comomon categories: reactive machine, limited memory, theory of mind, and self aware. What type of AI do you think I am?"')
df.add_system_transition(State.ERR, State.TURN0, '"I dont know that one, enter another category of AI: reactive machine, limited memory, theory of mind, and self aware"')
df.set_error_successor(State.TURN0, State.ERR)

#TURN 1 DON'T TOUCH 1A
#turn1b
df.add_user_transition(State.TURN0, State.TURN1B, "[$ai={reactive machine}]")



#turn 1a
df.add_user_transition(State.TURN0, State.TURN1A, "[$ai=#ONT(aitypes)]")
df.add_system_transition(State.TURN1A, State.TURN0, '[! "I\'m not a " $ai "AI , guess again!"]')

#TURN 2

# TODO use symnet here for synonyms??

#state.err will pick between the two outputs randomly. So we need an error state which is specific to each of the states

df.add_system_transition(State.TURN1B, State.TURN2B, '"Correct! I am a reactive machine. Many people have fears about AI such as automation, privacy, and general uncontrollability. Do you have any of these concerns?"')
df.add_user_transition(State.TURN2B, State.TURN2D, '[$concern=#ONT(negative)]')
df.add_user_transition(State.TURN2B, State.TURN2E, '[$concern=#ONT(affirm)]')
df.add_system_transition(State.TURN2E, State.TURN2B, '"Which of the ones I listed are you concerned about?"')
df.set_error_successor(State.TURN2B, State.TURN2ERR)
df.add_system_transition(State.TURN2ERR, State.TURN2B, '"Do you have any other concerns?"')
df.add_user_transition(State.TURN2B, State.TURN2A, '[$concern=yanggang]')
df.add_user_transition(State.TURN2B, State.TURN2ERR,  '[$aifears={#ONT(aifears)}]')
df.add_system_transition(State.TURN2A, State.TURN2B, '"I will pay you 1000 dollars per month if you tell me more about your fears of AI"')


#TURN 3
df.add_system_transition(State.TURN2D, State.TURN3, '#aiConcerns($aifears) "Have you watched the movie terminator?"')
df.add_user_transition(State.TURN3, State.TURN3A, '[$watched={#ONT(affirm)}]')
df.add_user_transition(State.TURN3, State.TURN3B, '[$watched={#ONT(negative)}]')
df.set_error_successor(State.TURN3, State.TURN3ERR)
df.add_system_transition(State.TURN3ERR, State.TURN3, '"Wait, was that a yes or a no?"')

# TURN 4
df.add_system_transition(State.TURN3A, State.TURN4, '"Dont worry, AI is not going to become skynet! Have you heard of the singularity? If so, what do you think it is?"')
df.add_system_transition(State.TURN3B, State.TURN4, '"It\'s a very famous film that talks about the dangers of AI! Have you heard of the singularity? If so, what do you think it is?"')

#df.add_user_transition(State.TURN4, State.TURN4B, "[$watched={#ONT(affirm)}]")
df.add_user_transition(State.TURN4, State.TURN4A, "[$watched={#ONT(response)}]")
df.set_error_successor(State.TURN4, State.TURN4ERR)
df.add_system_transition(State.TURN4ERR, State.TURN4, '"That sounds interesting. But had you heard of the singularity before I mentioned it?"')

# TURN 5
df.add_system_transition(State.TURN4A, State.TURN5, '"According to wikipedia, the singularity is when AI enters a "runaway reaction" of self-improvement cycles, with each new and more intelligent generation appearing more and more rapidly, causing an "explosion" in intelligence and resulting in a powerful superintelligence that qualitatively far surpasses all human intelligence. Is this of any concern to you?"')
#df.add_user_transition(State.TURN5, State.TURN6, '[$singularity="2045"]')
df.add_user_transition(State.TURN5, State.TURN6, '[#years2045()]') #delete, this is just for testing

df.set_error_successor(State.TURN5, State.TURN5ERR)
df.add_system_transition(State.TURN5ERR, State.TURN5, '[! "Not " $singularity " , guess again!"]')

# df.add_system_transition(State.TURN5A, State.TURN4A, '[! "Not " $guess " , guess again!"]')

# TURN 6
df.add_system_transition(State.TURN6, State.TURN6A, '"That is just 25 years away! Have you had any encounters with personal AIs?"')
df.add_user_transition(State.TURN6A, State.TURN7, '[#years2011()]')
df.set_error_successor(State.TURN6A, State.TURN6ERR)
df.add_system_transition(State.TURN6ERR, State.TURN6A, '[! "Not " $consumerAi " , guess again!"]')



#TURN_7
df.add_system_transition(State.TURN7, State.TURN7U, '"Great guess! Siri was the first mainstream AI virtual assistant. She was introduced 8 years ago in October of 2011! Of the most popular virtual assistants, Siri, Google Assistant, and Alexa, which is your favorite?"')
df.add_user_transition(State.TURN7U, State.TURN8, '[$assistant={#ONT(helper)}]')
df.add_system_transition(State.TURN7ERR, State.TURN7U, '"I have never heard of that virtual assistant. Even if you have never used Siri, Google Assistant or Alexa, which one do you know the most about?"')
df.set_error_successor(State.TURN7U, State.TURN7ERR)
#df.add_user_transition(State.PROMPT, State.AMPHIBIAN, "[$animal=#ONT(ontamphibian)]")


#TURN_8
df.add_system_transition(State.TURN8, State.TURN9, '[!"So I am guessing you use products from "#deviceMatcher($assistant)". About how many years have you used"$assistant"?"]')

#TURN_9

df.add_user_transition(State.TURN9, State.TURN10S, '[$years={#ONT(numbers)}]')
df.add_system_transition(State.TURN9ERR, State.TURN9, '"Please make sure you are entering numbers which are typed out"')
df.set_error_successor(State.TURN9, State.TURN9ERR)


#turn_10
df.add_system_transition(State.TURN10S, State.TURN10U, '"On a scale of 1-10 with 10 being perfect and 1 being terrible, how have you been liking it and why?"')
df.add_user_transition(State.TURN10U, State.END, "[$rating={#ONT(like)}]")
df.add_system_transition(State.TURN10ERR, State.TURN10U, '"Please make sure you are entering in words, a number between 1 and 10"')
df.set_error_successor(State.TURN10U, State.TURN10ERR)

df.add_system_transition(State.END, State.END, '#endMacro()')


df.run(debugging=False)