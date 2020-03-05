from emora_stdm import KnowledgeBase, DialogueFlow, Macro
from enum import Enum


# TODO: Update the State enum as needed
class State(Enum):
    START = 0
    Knowledge = 1
    Knowledge_No = 2
    Explain = 3
    Ask_About_Apps = 4
    Gives_App = 5
    Explain_App = 6
    Explain_Response = 7
    Explain_Response_Disint = 8
    Gives_App_Unknown = 9
    User_Understands = 10
    Ask_About_Cloud_Providers = 11
    Ask_About_Cloud_Providers_Yes = 12
    Ask_About_Cloud_Providers_Yes2 = 13
    Ask_About_Cloud_Providers_No = 14
    Cloud_Provider_OV = 15
    Cloud_Provider_Spec = 16
    Explain_App_Unknown = 17
    User_Surprised_Provider = 18
    User_Response_Provider = 19
    Explain_Again = 300
    User_Still_Confused = 301
    Bash_Amazon = 21
    User_Likes_Amazon = 22
    User_Wants_Break_Tech = 23
    Explain_Politics = 24 # NON OFFENSIVE, We are not advocating, only explaining
    User_Questions_Options = 25
    User_Response_Amazon_Minimal =26
    Support_Breakup = 27
    No_Support_Breakup = 28
    Whatever_Breakup = 29
    All_Other_Breakup = 30
    Back_On_Topic = 31
    End_User_Statement = 32
    Ask_For_Improvement = 33
    Give_Improvement = 34
    Goodbye = 35
    Knowledge_Kinda = 36
    User_Confused = 200
    Knowledge_Yes = 50
    Knowledge_Yes_Info = 51
    Ask_Which = 52
    Answer_Platform = 53
    Ask_Experience = 54
    Experience_Yes_Generic = 55
    Experience_Yes_Info = 56
    Experience_No = 57
    Ask_Services = 58
    Services_Response = 59
    Ask_Opinion = 60
    Opinion = 61
    Ask_Projects = 62
    Projects_Yes = 63
    Learn = 64
    Learn_Response = 65
    Experience_Yes = 66
    Projects_Kinda = 996
    Opinion_Response = 997
    Go_Google = 998
    ERR = 999
    ERR1 = 1000
    ERR2 = 1001
    ERR3 = 1002
    ERR4 = 1004
    ERR5 = 1005
    ERR6 = 1006
    ERR7 = 1007
    ERR8 = 1008
    ERR9 = 1009

'''-------------------------------------------------------------------
System (#)
User (#)
These indicate that which state it is on
-------------------------------------------------------------------'''

# TODO: create the ontology as needed
ontology = {
    "ontology": {
            "cloudproviders": [
                "amazon",
                "aws",
                "google",
                "gcp",
                "microsoft",
                "azure",
                "cisco",
                "oracle",
                "salesforce"
                "alibaba",
                "aliyun"
            ],
            "AWS": [
                "sthree",
                "ectwo",
                "lambda",
                "glacier",
                "sns",
                "kinesis",
                "dynamoDB"
                "dynamodb",
                "redshift",
                "cloudfront"
            ],
            "Azure": [
                "devops",
                "cosmosdb"
                "cosmosDB",
                "virtual machines",
                "active directory",
                "api management",
                "backup",
                "logic apps",
                "bots"
            ],
            "confused": [
                "dont get it",
                "dont understand",
                "what?",
                "huh",
                "confusing",
                "confused"
            ],
            "understand": [
              "get it",
              "understand",
              "i see",
              "sure"
            ],
            "disinterested": [
                "boring",
                "dumb",
                "not cool",
                "whatever"
            ],
            "agree": [
                "yes",
                "yeah",
                "yea",
                "absolutely",
                "i do",
                "do",
                "of course"
            ],
            "disagree": [
                "no",
                "not really",
                "nah"
                "i dont"
                "don't"
                "not"
            ],
            "cloudytech": [
                "storage",
                "computing",
                "database",
                "processing"
            ],
            "apps": [
                "facebook",
                "twitter",
                "youtube",
                "google",
                "snapchat",
                "instagram",
                "spotify"
            ],
            "surprised": [
                "wow",
                "crazy",
                "insane",
                "surprise"
            ],
            "angry": [
                "messed up",
                "ugh",
                "stupid",
                "ridiculous",
                "hate"
            ],
            "amazonpro":[
                "low prices",
                "low cost",
                "economies of scale",
                "scalable",
                "elastic",
                "secure",
                "reliable"
            ],
            "taxtech": [
                "tax",
                "vat",
            ],
            "breaktech": [
                "break up tech",
            ],
            "questionwords":[
                "What",
                "Why",
                "Where",
                "How",
                "Who",
                "Is"
            ],
            "good":[
                "great",
                "awesome",
                "brilliant",
                "smart",
                "amazing",
                "cool",
                "not bad"
            ],
            "bad":[
                "bad"
                "awful",
                "horrible",
                "horrendous",
                "short-sighted",
                "not good"
            ],
            "kinda": [
                "maybe",
                "a little",
                "kinda",
                "kind of",
                "somewhat",
                "eh"
            ]
        }
}

class appCheck(Macro):
    def run(self, ngrams, vars, args):
        if args[0] == "facebook":
            return "Facebook actually manages their own data centers to provide storage for all your photos, posts, " \
                   "messages, and other things on your account"
        elif args[0] == "twitter":
            return "Your 200-ish word tweet might not seem like a lot, but all those tweets added up make over 12 terabytes of data per day " \
                   "for twitter to process and store in cloud servers"
        elif args[0] == "youtube":
            return "Across the world, people watch over 1 billion hours of video every day, and all those videos are stored" \
                   " and accessed from Google's data centers"
        elif args[0] == "google":
            return "Google is the epitome of big data. Every time you do a search on google, they make thousands of " \
                   "computations in their web/index servers to find the most relevant search results based on your prior data"
        elif args[0] == "snapchat":
            return "While they delete photos, the sheer volume of the photos means that they have data centers which your phone can access" \
                   "to receive snaps"
        elif args[0] == "instagram":
            return "Ever since instagram integrated with facebook, all their photos (millions of gigabytes) have been stored " \
                   "in facebook's data servers"
        elif args[0] == "spotify":
            return "While you can download music, the bulk of spotify's streamable music library, which is like thousands of terabytes," \
                   " are in Google data centers"
        else:
            return ""

class providerInfo(Macro):
    def run(self, ngrams, vars, args):
        if args[0] == "amazon" or args[0] == "aws":
            return "Amazon controls about 47% of the cloud market. The next closest are Microsoft at 15% and Google at 7%"
        elif args[0] == "google" or args[0] == "gcp":
            return "Google has a pretty small share of the market, with only about 7%. Amazon controls an overwhelming amount at around 47%"
        elif args[0] == "microsoft" or args[0] == "azure":
            return "Microsoft actually is the second largest cloud provider at around 15%. Amazon, however, has three times as much at 47% of market share"
        elif args[0] == "alibaba" or args[0] == "aliyun":
            return "They actually control 7% of the global market, but they are very concentrated in China. " \
                   "Even then, they can't compare to Amazon's 47% of global market share"
        elif args[0] == "salesforce" or args[0] == "oracle" or args[0] == "cisco":
            return "They aren't that big, but they still provide some services, especially internally. Amazon, however, is the big player of the" \
                   "cloud market with 47% of market share"
        else:
            return ""

knowledge = KnowledgeBase()
knowledge.load_json(ontology)
df = DialogueFlow(State.START, initial_speaker=DialogueFlow.Speaker.SYSTEM, kb=knowledge, macros={'appCheck': appCheck(), 'providerInfo': providerInfo()})
# System (1)
df.add_system_transition(State.START, State.Knowledge, r'[!"Hi, do you know anything about cloud computing?"]')
# transition for no or kinda: User (1)
df.add_user_transition(State.Knowledge, State.Knowledge_No, "[#ONT(disagree)]")
df.add_user_transition(State.Knowledge, State.Knowledge_Kinda, "[#ONT(kinda)]")
# System (2)
df.add_system_transition(State.Knowledge_No, State.Explain, r'[! "Oh thats okay. Cloud computing just means that the storage, ' 
                                                            r'management, and processing of your app data happens offsite"]')
df.add_system_transition(State.Knowledge_Kinda, State.Explain, r'[! "Oh dont worry, Ill give you a quick refresher. Cloud computing just means that the storage, ' 
                                                            r'management, and processing of your app data happens offsite"]')
# user responses to the basics of cloud computing, split b/w some response vs disinterested response : User (2)
df.add_user_transition(State.Explain, State.Explain_Response, "-{#ONT(disinterested)}")
df.add_user_transition(State.Explain, State.Explain_Response_Disint, "[#ONT(disinterested)]")

# Converge back to asking about apps on phone : System (3)
df.add_system_transition(State.Explain_Response_Disint, State.Ask_About_Apps, r'[! "Actually, this is super interesting! '
                                                                              r'All the apps on your phone actually use the cloud. '
                                                                              r'What apps do you have on your phone right now?"]')
df.add_system_transition(State.Explain_Response, State.Ask_About_Apps, r'[!"Yea, so to illustrate, what apps do you have on your phone right now?"]')

# user responses to being asked about apps : User (3)
# TODO: prob add a transition in case they dont give an app at all
df.add_user_transition(State.Ask_About_Apps, State.Gives_App, "[$app={#ONT(apps)}]")
df.add_user_transition(State.Ask_About_Apps, State.Gives_App_Unknown, "-{#ONT(apps)}")

# System (4)
df.add_system_transition(State.Gives_App_Unknown, State.Explain_App_Unknown, r'[! "That app probably cannot store all your data'
                                                                             r' on your personal phone. Thats why they use offsite servers to store and later show you'
                                                                             r' all your activity. I think thats super cool!"]')

df.add_system_transition(State.Gives_App, State.Explain_App, "[! $app utilizes cloud technology. #appCheck($app)]") # okay this macro isn't working

# User understands/confused about the explanation of cloud : User (4)
df.add_user_transition(State.Explain_App, State.User_Confused, "[{#ONT(confused)}]")
df.add_user_transition(State.Explain_App, State.User_Understands, "-{#ONT(confused)}")
df.add_user_transition(State.Explain_App_Unknown, State.User_Confused, "[#ONT(confused)]")
df.add_user_transition(State.Explain_App_Unknown, State.User_Understands, "-{#ONT(confused)}")

# detour branch if user is confused
df.add_system_transition(State.User_Confused, State.Explain_Again, r'[! "No worries! Cloud computing is pretty confusing definitely. Just think of '
                                                                   r'it like this invisible box that floats next to you.'
                                                                   r' Its there and you always have access to the stuff, your data, inside. Does that make sense?"]')

df.add_user_transition(State.Explain_Again, State.User_Understands, "-{#ONT(confused)}")
df.add_user_transition(State.Explain_Again, State.User_Still_Confused, "[#ONT(confused)]")

df.add_system_transition(State.User_Still_Confused, State.Go_Google, r'[! "Hmm, okay yea Im not sure if I can explain it better, but I think doing some'
                                                                                     r' Googling would help!"]') # End of conversation
# Transition to talking about providers of cloud : System (5)
df.add_system_transition(State.User_Understands, State.Ask_About_Cloud_Providers, r'[! "Of course, there are businesses that operate the cloud. '
                                                                                  r'Do you know any of the major ones?"]')
# User splits between yes, yes with some major business, no : User (5)
df.add_user_transition(State.Ask_About_Cloud_Providers, State.Ask_About_Cloud_Providers_No, "[#ONT(disagree)]")
df.add_user_transition(State.Ask_About_Cloud_Providers, State.Ask_About_Cloud_Providers_Yes, "[!{#ONT(agree)} -{#ONT(cloudproviders)}]")

df.add_user_transition(State.Ask_About_Cloud_Providers, State.Ask_About_Cloud_Providers_Yes2, "[$provider={#ONT(cloudproviders)}]")

# Transition from yes to talking about cloud provider in general: System (6)
df.add_system_transition(State.Ask_About_Cloud_Providers_Yes, State.Cloud_Provider_OV, r'[! "Great! Yea, Amazon actually controls'
                                                                                       r' about 47 percent of the market. Microsoft has about 15'
                                                                                       r' percent"]')

df.add_system_transition(State.Ask_About_Cloud_Providers_Yes2, State.Cloud_Provider_Spec, r'[! "Yea!" $provider is a cloud provider. #providerInfo($provider)]')
df.add_system_transition(State.Ask_About_Cloud_Providers_No, State.Cloud_Provider_OV, r'[! "Totally okay. Amazon is the major player and they control'
                                                                                       r' about 47 percent of the market. Microsoft has about 15'
                                                                                       r' percent and Google has 7 percent."]')

# Transition for user reactions to learning about cloud providers: User (6)
df.add_user_transition(State.Cloud_Provider_OV, State.User_Surprised_Provider, "[{#ONT(surprised), #ONT(angry)}]")
df.add_user_transition(State.Cloud_Provider_Spec, State.User_Surprised_Provider, "[{#ONT(surprised), #ONT(angry)}]")
df.add_user_transition(State.Cloud_Provider_OV, State.User_Response_Provider, "-{#ONT(surprised), #ONT(angry)}")
df.add_user_transition(State.Cloud_Provider_Spec, State.User_Response_Provider, "-{#ONT(surprised), #ONT(angry)}")

# Transition to system bash Amazon: System (7)
df.add_system_transition(State.User_Surprised_Provider, State.Bash_Amazon, r'[! "I know right? Its crazy how one company can own so much of the market.'
                                                        r' While it means really good prices, Amazon basically controls everything."]')
df.add_system_transition(State.User_Response_Provider, State.Bash_Amazon, r'[! I think this is pretty messed up. Like imagine controlling so much of the market'
                                                                          r' and not being called a monopoly.]')
# Transition to user inputting response to us bashing Amazon: User (7)
# "wait but low prices are good"
df.add_user_transition(State.Bash_Amazon, State.User_Likes_Amazon, "[{#ONT(amazonpro)}]")
# lets break up tech
df.add_user_transition(State.Bash_Amazon, State.User_Wants_Break_Tech, "[{#ONT(taxtech), #ONT(breaktech)}]")
# pick up question from user ex. "what are we gonna do?"
#df.add_user_transition(State.Bash_Amazon, State.User_Questions_Options, "[{#ONT(questionwords)}, /\w+\?\s*/]")
# Pick up rest of the responses
df.add_user_transition(State.Bash_Amazon, State.User_Response_Amazon_Minimal, "-{#ONT(amazonpro), #ONT(taxtech), #ONT(breaktech)}")

# Transition to system talking about liking amazon or breaking up tech: System (8)
df.add_system_transition(State.User_Likes_Amazon, State.Explain_Politics, r'[! "I mean, yea Amazon and economies of scale bring lots of benefits,'
                                                                          r' but controlling that much data could be very bad for reasons like privacy. Thats why politicians'
                                                                          r' like Bernie Sanders are trying to break up tech. What do you think?"]')
df.add_system_transition(State.User_Wants_Break_Tech, State.Explain_Politics, r'[! "Luckily for you, my comrade, some politicians like Bernie have also noticed the problem and are actively'
                                                                              r' trying to break tech. What do you think?"]')
df.add_system_transition(State.User_Response_Amazon_Minimal, State.Explain_Politics, r'[! "This is actually pretty politically salient, as a lot of candidates like '
                                                                                     r'Bernie Sanders and Elizabeth Warren have called for breaking big tech corporations. What do you think?"]')

# Transition to user inputting response to political situation
    # In support
    # Not in support
    # meh whatever
    # all other responses

df.add_user_transition(State.Explain_Politics, State.Support_Breakup, "[{#ONT(agree), #ONT(good)}]")
df.add_user_transition(State.Explain_Politics, State.No_Support_Breakup, "[{#ONT(disagree), #ONT(bad)}]")
df.add_user_transition(State.Explain_Politics, State.Whatever_Breakup, "[{#ONT(disinterested)}]")
df.add_user_transition(State.Explain_Politics, State.All_Other_Breakup, "-{#ONT(agree), #ONT(disagree), #ONT(good),"
                                                                        "#ONT(bad), #ONT(disinterested)}")
# Transition to system response to user's support: System (9)
df.add_system_transition(State.Support_Breakup, State.Back_On_Topic, r'[! "Glad you think thats a great idea! That was a pretty big digression. Where were we...'
                                                                     r' Oh yea, so cloud computing is basically the de facto standard for tech now"]')
df.add_system_transition(State.No_Support_Breakup, State.Back_On_Topic, r'[! "Well okay, thats fair, to each their own! That was a pretty big digression. Where were we...'
                                                                     r' Oh yea, so cloud computing is basically the de facto standard for tech now"]')
df.add_system_transition(State.Whatever_Breakup, State.Back_On_Topic, r'[! "I think you should be at least a little interested, its our data! Anyway, that was a pretty big digression. Where were we...'
                                                                     r' Oh yea, so cloud computing is basically the de facto standard for tech now"]')
df.add_system_transition(State.All_Other_Breakup, State.Back_On_Topic, r'[! "Fair enough. I think that was a pretty big digression. Where were we...'
                                                                     r' Oh yea, so cloud computing is basically the de facto standard for tech now"]')

# Transition user response can be anything: User (9)
df.add_user_transition(State.Back_On_Topic, State.End_User_Statement, "/[A-Z a-z]*/")

# Transition to goodbye from system: System (10)
df.add_system_transition(State.End_User_Statement, State.Ask_For_Improvement, r'[! "Honestly I dont think I can talk more about cloud computing. Im '
                                                                          r'kinda tired. I hope you enjoyed it though! Leave a comment on what can be improved!"]')
# Transition to user giving an input comment: User (10)
df.add_user_transition(State.Ask_For_Improvement, State.Give_Improvement, "$improvement=/[A-Z a-z]*/")

# Transition to system
df.add_system_transition(State.Give_Improvement, State.Goodbye, r'[! "Thank you so much! I really appreciate your comment. This is goodbye for now, '
                                                                r'but dont forget to check back for more updates on my knowledge about cloud!"]') # end of conversation
# transition to yes
# TODO: Need to create two pathways for saying just yes vs yes I've tried sth
# User (1)-1
df.add_user_transition(State.Knowledge, State.Knowledge_Yes, "[!#ONT(agree) -{#ONT(kinda), #ONT(cloudproviders), #ONT(AWS), #ONT(Azure)}]")
#either just services or cloudproviders + services
df.add_user_transition(State.Knowledge, State.Knowledge_Yes_Info, "<#ONT(agree), <$providers={#ONT(cloudproviders)},"
                                                                  " $services={#ONT(AWS), #ONT(Azure)}>>")

# TODO: Transition for case where user gives yes with additional information

# Transition to system asking which cloud provider user has used: System (2)-1
df.add_system_transition(State.Knowledge_Yes, State.Ask_Which, r'[! "Sweet. So I assume you already know at least basic concept of cloud. '
                                                               r'Have you used any of the major cloud providers?"]')
# Transitions to user input of either: User (2)-1
    # some provider
    # just saying yes with no provider'
    # saying none
df.add_user_transition(State.Ask_Which, State.Answer_Platform, "[!-{#ONT(disagree)} $providers={#ONT(cloudproviders)}]")
df.add_user_transition(State.Ask_Which, State.Experience_Yes_Generic, "[!{#ONT(agree)} -{#ONT(cloudproviders)}]")
df.add_user_transition(State.Ask_Which, State.Experience_No, "[#ONT(disagree)]")
# Transition to system
    # asking for specific service if user was generic
    # OR asking about a specific experience if they knew the provider
df.add_system_transition(State.Experience_Yes_Generic, State.Ask_Services, r'[! "Did you use a specific service from them?"]')
df.add_system_transition(State.Answer_Platform, State.Ask_Experience, r'[! "Cool! have you ever tried using services provided by" $providers"?"]')
df.add_system_transition(State.Knowledge_Yes_Info, State.Ask_Projects, r'[! "Cool! have you ever tried implementing" $services "for your projects?"]')

# Transition for user:
    # Ask Exp ->
        # Yes have experience, but doesnt specify which
        # Specifies which service
        # No experience
df.add_user_transition(State.Ask_Experience, State.Experience_Yes, "[{#ONT(agree)}, -{#ONT(AWS), #ONT(Azure)}]") #yes takes any with yes rn
df.add_user_transition(State.Ask_Experience, State.Services_Response, "[$answer={#ONT(AWS), #ONT(Azure)}]")
df.add_user_transition(State.Ask_Experience, State.Experience_No, "[!#ONT(disagree)]") #no
df.add_user_transition(State.Ask_Projects, State.Projects_Yes, "[!#ONT(agree) -{#ONT(kinda)}]")
df.add_user_transition(State.Ask_Projects, State.Projects_Kinda, "[! -{#ONT(agree), #ONT(disagree)}]")
df.add_user_transition(State.Ask_Projects, State.Experience_No, "[! #ONT(disagree) -{#ONT(kinda)}]")

# System (4)-1
df.add_system_transition(State.Ask_Opinion, State.Learn, r'[! "Oh cool! Did you think it was a good service?"]')
df.add_system_transition(State.Experience_Yes, State.Learn, r'[! "Okay, in that case, lets talk about some fun facts about cloud."]')
df.add_system_transition(State.Projects_Kinda, State.Learn, r'[! "Okay, in that case, we can talk about some fun facts about the cloud."]')
df.add_system_transition(State.Experience_No, State.Learn, r'[! "hm... well then I guess going deeper into conversation might bore you. '
                                                           r'How about I tell you fun facts about cloud computing!"]')
# User (4)-1
df.add_user_transition(State.Learn, State.Learn_Response, '/[A-Z a-z]*/')
df.add_user_transition(State.Ask_Services, State.Services_Response, "[$providers={#ONT(cloudproviders)}, $answer={#ONT(AWS), #ONT(Azure)}]") # doesnt match
# System (5)-1
df.add_system_transition(State.Services_Response, State.Ask_Opinion, '[! $answer " is actually one of the most commonly used services from " $providers ". What is your opinion on " $answer "?"]') #variable saves?
df.add_user_transition(State.Ask_Opinion, State.Opinion_Response, '/[A-Z a-z]*/')
df.add_system_transition(State.Opinion_Response, State.Cloud_Provider_OV, r'[! "Thats a fair opinion. So heres a fun fact: Amazon'
                                                                          r' is the major player of the cloud market and they control about'
                                                                          r' 47 percent of the market. Microsoft has 15 and Google has 7!"]')
df.add_system_transition(State.Learn_Response, State.Cloud_Provider_OV, r'[! "So heres a fun fact.'
                                                                    r' Amazon is the major player of the cloud market and they control'
                                                                    r' about 47 percent. Microsoft has about 15'
                                                                    r' percent and Google has 7 percent."]')
df.add_system_transition(State.Projects_Yes, State.Ask_For_Improvement, r'["Thats impressive. Understanding what things do and actually implementing them is completely different task'
                                                            'It was nice talking with you. My intention was to educate users if they have no experience in cloud'
                                                            'Maybe if you could leave some comments, I could try to better myself to have deeper conversation"]')
#df.add_user_transition(State.Ask_For_Improvement, State.Give_Improvement, "$improvement=/[A-Z a-z]*/")
#df.add_system_transition(State.Give_Improvement, State.Goodbye, r'[! "Thank you so much! I really appreciate your comment. This is goodbye for now, '
                                                                #r'but dont forget to check back for more updates on my knowledge about cloud!"]') # end of conversation

df.set_error_successor(State.Knowledge, State.ERR)
df.add_system_transition(State.ERR, State.Knowledge, r'[!"Sorry, couldnt understand. please give yes or no"]')
df.set_error_successor(State.Ask_About_Apps, State.ERR1)
df.add_system_transition(State.ERR1, State.Ask_About_Apps, r'[! "Sorry I couldnt understand. Also even if you dont have an app, let me know about an app that you do have"]')
df.set_error_successor(State.Ask_About_Cloud_Providers, State.ERR2)
df.add_system_transition(State.ERR2, State.Ask_About_Cloud_Providers, r'[! "Sorry I didnt quite get that. Do you know any cloud providers"]')
df.set_error_successor(State.Ask_Which, State.ERR3)
df.add_system_transition(State.ERR3, State.Ask_Which, r'[! "Sorry, I didnt quite get that. So did you use a cloud provider before?"]')
df.set_error_successor(State.Ask_Experience, State.ERR4)
df.add_system_transition(State.ERR4, State.Ask_Experience, r'[! "Sorry, I didnt quite get that. So have you tried to use the services before?"]')
df.set_error_successor(State.Ask_Projects, State.ERR5)
df.add_system_transition(State.ERR5, State.Ask_Projects, r'[! "Wot? I didnt get that. Have you implemented the service in your projects before?"]')
df.set_error_successor(State.Ask_Services, State.ERR6)
df.add_system_transition(State.ERR6, State.Ask_Services, r'[! "Aight apparently I only know about services from AWS and Azure. Pretend you know about aws sthree really quick"]')
# TODO: create your own dialogue manager


df.run(debugging=False)