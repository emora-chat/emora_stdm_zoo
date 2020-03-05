from emora_stdm import KnowledgeBase, DialogueFlow, Macro
from enum import Enum


class NUMBERCOMP(Macro):
    ##used to compare the number of followers

    def run(self, ngrams, vars, args):
        d = int(vars['followers'])
        if d < 1000:
            return 'You should get more bro'
        else:
            return 'Whoa whoa you are famous!'


class HOURSCOMP(Macro):
    ##used to compare the number of hours spent on insta

    def run(self, ngrams, vars, args):
        h = int(vars['hours'])
        if (h < 3):
            return "That's not too bad. Good work."
        else:
            return "Aren't your eyeballs killing you? That's a long time!"


class State(Enum):
    ##lynda's states
    START = 0
    PROMPT = 1
    ERRWHY = 2
    WHYLIKE = 3
    FEATN = 4
    FEATV = 5
    FEATT = 6
    FEATA = 7
    YN = 8
    MORE = 9
    LESS = 10
    PEOPLE = 11
    USE = 12
    INDIVIDUAL = 13
    EXPLORE = 14
    EPAGE = 15
    CONTENT = 16
    MULT = 17
    TYPES = 18
    BUSINESS = 19
    BUS = 20
    ##seo's states
    INTERACT = 21
    PERSONREASON = 22
    INTERACTQ = 23
    AWEEKQ = 24
    AWEEK = 25
    PERSONREASONANS = 26
    CONTENTREASON = 27
    OFTENQ = 28
    POSTTIME = 29
    FOLLOWERSQ = 30
    FOLLOWERS = 31
    CONTENTQ = 32
    CONTENTTYPE = 33
    ULASTPOST = 34
    CONTENTERR = 35
    LASTPOST = 36
    POSTHOURS = 37
    HOURS = 38
    WORKQ = 39
    ANS_Y = 40
    ANS_N = 41
    # errorhandling
    INTERACTERR = 42
    INTERACTERROR = 43
    ULASTPOSTERROR = 44
    HOURSERR = 45
    HOURSERROR = 46
    FOLLOWERSERR = 47
    FOLLOWERSERROR = 48
    AWEEKERR = 49
    AWEEKERROR = 50
    # more lynda states
    NEWS = 51
    NEWSOURCE = 52
    ENTERTAIN = 53
    ESOURCE = 54
    FOLLOWERSQ2 = 55
    INFLUENCER = 56
    ERRUSE = 57
    ERRYN = 58
    NEWS_END = 59
    ESOURCE_END = 60
    # gene states
    END = 61
    ERR_PROMPT = 62
    NO = 63
    DISLIKE_Q = 64
    DISLIKE = 65
    OTHER_Q = 66
    OTHER = 67
    DISLIKE_NOUN = 68
    ERR_DISLIKE = 69
    DISLIKE_ADJ = 70
    ADJ_Q = 71
    ADJ_YES = 72
    ADJ_NO = 73
    LIKABLE = 74
    ACHIEVE_Q = 75
    ACHIEVE_YES = 76
    ACHIEVE_NO = 77
    ERR_ACHIEVE = 78
    OTH_REASON = 79
    OTH_END = 80
    FACEBOOK_Q = 81
    FACEBOOK = 82
    FACE_ANS = 83
    TIME = 84
    SOCMED = 85
    SOC_REASON = 86
    SOC_END = 87
    IMPROVE_Q = 88
    IMPROVE = 89
    YES = 90
    ERR_WORK = 91


ontology = {
    "ontology": {
        "feature_noun":
            [
                "story",
                "stories"
                "likes",
                "archive"
            ],
        "feature_ing":
            [
                "liking",
                "commenting",
                "following",
                "exploring",
                "archiving"
            ],
        "feature_things":
            [
                "user interface",
                "interface",
                "app"
            ],
        "feature_adj":
            [
                "fast",
                "easy to use",
                "easy to navigate",
                "intuitive",
            ],
        "ontexplore":
            [
                "explore",
                "explore page",
                "new content"
            ],
        "ontmult":
            [
                "multiple accounts",
                "many pages",
                "different accounts"
            ],
        "ontbusiness":
            [
                "business",
                "run a business",
                "company"
            ],
        "creating_content":
        [
            "creating",
            "content",
            "creator",
            "posting",
            "sharing",
            "create",
            "share",
            "post"
        ],
        "ontaffirmative":
            [
                "yes",
                "yeah",
                "definitely",
                "yeh",
                "absolutely",
                "sure",
                "uh huh",
                "of course",
                "it does",
                "yea",
                "yep",
                "yup"
            ],
        "ontnegative":
            [
                "no",
                "nah",
                "nope",
                "not"
            ],
        "ontpeople":
            [
                "celebrities",
                "children",
                "relatives",
                "people",
                "friends",
                "family",
                "family members",
                "famous people",
                "coworkers"
            ],
        "ontindividual":
            [
                "friend",
                "mom",
                "dad",
                "brother",
                "sister",
                "uncle",
                "aunt",
                "grandpa",
                "grandma",
                "cousin",
                "child",
                "daughter",
                "son",
                "grandson",
                "granddaughter",
                "nephew",
                "niece"
            ],
        "ontfollow":
            [
                "follow",
                "connect",
                "keep up",
                "interact"
        ],
        "ontcontentreasons":
                  [
                      "posting",
                      "creating",
                      "stories",
                      "post",
                      "making"
                  ],
        "ontcontents":
                    [
                        "art",
                        "makeup",
                        "pets",
                        "cat",
                        "dog",
                        "sports",
                        "vacation",
                        "vlog",
                        "food",
                        "meal",
                        "eating",
                        "baking",
                        "restaurant",
                        "cooking",
                        "memes",
                        "meme",
                        "funny",
                        "video",
                        "dance"
                    ],
        "ontpostingtime":
                    [
                        "week",
                        "month",
                        "yesterday",
                        "year",
                        "today",
                        "earlier",
                        "morning",
                        "night",
                        "Sunday",
                        "Monday",
                        "Tuesday",
                        "Wednesday",
                        "Thursday",
                        "Friday",
                        "Saturday",
                        "Sunday",
                        "weekend"
                    ],
        "onttimes":
                  [
                    "times",
                      "month",
                      "weekly",
                      "week",
                      "day",
                      "year",
                      "daily",
                      "yearly"
                  ],
        "ontinteract":
                  [
                      "like",
                      "comment",
                      "share",
                      "send",
                      "tag",
                      "dm",
                      "message",
                      "direct message"
                  ],
        "ontnews":
              [
                  "news",
                  "articles",
                  "current events"
              ],
        "ontentertainment":
            [
                "entertainment",
                "memes",
                "videos",
                "viral",
                "tiktok",
                "vines"
            ],
        "ontinfluence":
            [
                "influencer",
                "money",
                "model",
                "sponsor",
                "am famous"
            ],
        "dislike_noun": [
            "ads",
            "sponsors",
            "hashtags",
            "reposts"
        ],
        "dislike_adj": [
            "superficial",
            "fake",
            "vain",
            "basic",
            "unoriginal"
        ],
        "time": [
            "wastes time",
            "waste of time",
            "time",
            "hours",
            "all day",
            "addictive"
        ],
        "likable": [
            "apps",
            "fads",
            "technology",
            "socializing",
            "social media"
        ]
    }
}

knowledge = KnowledgeBase()
knowledge.load_json(ontology)
df = DialogueFlow(State.START, initial_speaker=DialogueFlow.Speaker.SYSTEM, kb=knowledge, macros={"NUMBERCOMP":NUMBERCOMP(), "HOURSCOMP":HOURSCOMP()})

#start
df.add_system_transition(State.START, State.PROMPT, '"Do you like Instagram?"')

#if user says yes (likes Instagram)
df.add_user_transition(State.PROMPT, State.YES, "[#ONT(ontaffirmative)]")
df.add_system_transition(State.YES, State.WHYLIKE, 'What features do you like"?"')

# error handler for first prompt
df.set_error_successor(State.PROMPT, State.ERR_PROMPT)
df.add_system_transition(State.ERR_PROMPT, State.IMPROVE_Q, '"I see. How do you think Instagram can improve?"')

##4 different states depending on what part of speech the feature is
df.add_user_transition(State.WHYLIKE, State.FEATN, "[$feat=#ONT(feature_noun)]")
df.add_system_transition(State.FEATN, State.YN, 'Do you like the [! $feat "feature more than on Facebook?"]')

df.add_user_transition(State.WHYLIKE, State.FEATV, "[$feat=#ONT(feature_ing)]")
df.add_system_transition(State.FEATV, State.YN, 'Do you like [! $feat "on Instagram more than on Facebook?"]')

df.add_user_transition(State.WHYLIKE, State.FEATT, "[$feat=#ONT(feature_things)]")
df.add_system_transition(State.FEATT, State.YN, 'Do you like the [! $feat "more than on Facebook?"]')

df.add_user_transition(State.WHYLIKE, State.FEATA, "[$feat=#ONT(feature_adj)]")
df.add_system_transition(State.FEATA, State.YN, 'Is Instagram more [! $feat "than Facebook?"]')

##if they say they like their explore page
df.add_user_transition(State.WHYLIKE, State.EXPLORE, "[$explore=#ONT(ontexplore)]")
df.add_system_transition(State.EXPLORE, State.EPAGE, 'I also love that"!" What do you tend to see on your explore page"?"')
df.add_user_transition(State.EPAGE, State.CONTENT, '/.*/')

##if they say they have multiple accounts
df.add_user_transition(State.WHYLIKE, State.MULT, "[$explore=#ONT(ontmult)]")
df.add_system_transition(State.MULT, State.TYPES, 'Oh same, I currently manage 3 accounts on my Instagram app"!" What sort of things do you have accounts for"?"')
df.add_user_transition(State.TYPES, State.CONTENT, '/.*/')

##if they use instagram for business
df.add_user_transition(State.WHYLIKE, State.BUSINESS, "[$explore=#ONT(ontbusiness)]")
df.add_system_transition(State.BUSINESS, State.BUS, 'What business do you own"?"')
df.add_user_transition(State.BUS, State.CONTENT, '/.*/')

#connects three above options back into the general flow
df.add_system_transition(State.CONTENT, State.USE, 'Awesome"!" What else do you like to use Instagram for"?"')

df.add_user_transition(State.YN, State.MORE, "[#ONT(ontaffirmative)]")
df.add_user_transition(State.YN, State.LESS, "[#ONT(ontnegative)]")

##what do they use instagram for
df.add_system_transition(State.MORE, State.USE, 'That is great. What do you like to use Instagram for"?"')
df.add_system_transition(State.LESS, State.USE, 'Sorry to hear that. Why do you still use Instagram then"?"')

##following, connecting with people
df.add_user_transition(State.USE, State.PEOPLE, "[$action=#ONT(ontfollow), $person=#ONT(ontpeople)]")
df.add_user_transition(State.USE, State.INDIVIDUAL, "[$action=#ONT(ontfollow), $person=#ONT(ontindividual)]")

##different options for if they say general or specific person
df.add_system_transition(State.PEOPLE, State.PERSONREASON, 'Who are the [! $person] you keep up with"?"')
df.add_system_transition(State.INDIVIDUAL, State.PERSONREASON, 'What is your [! $person] like"?"')

df.add_user_transition(State.PERSONREASON, State.PERSONREASONANS, '/.*/')

##news
df.add_user_transition(State.USE, State.NEWS, "[$news=#ONT(ontnews)]")

df.add_system_transition(State.NEWS, State.NEWSOURCE, 'Which accounts do you follow for [!$news]"?"')
#transition to end
df.add_user_transition(State.NEWSOURCE, State.NEWS_END, '/.*/')
df.add_system_transition(State.NEWS_END, State.END, '"VICE News is my fave. Well, it was nice talking to you. Goodbye!"')

##influencer
df.add_user_transition(State.USE, State.INFLUENCER, "[$influence=#ONT(ontinfluence)]")

df.add_system_transition(State.INFLUENCER, State.FOLLOWERSQ2, '"Whoa that is insane. How many followers do you have""?"')
df.add_user_transition(State.FOLLOWERSQ2, State.FOLLOWERS, r"{[$followers=/\d+/]}")
df.set_error_successor(State.FOLLOWERSQ2, State.FOLLOWERSERR) ##error
##should feed into seo's code

##entertainment
df.add_user_transition(State.USE, State.ENTERTAIN, "[$entertain=#ONT(ontentertainment)]")

df.add_system_transition(State.ENTERTAIN, State.ESOURCE, 'Oh, I also use Instagram for entertainment"!" Are there any accounts you follow or do you just use your explore page"?"')
df.add_user_transition(State.ESOURCE, State.EXPLORE, "[#ONT(ontexplore)]") ##this asks again what they use insta for
#transition to end
df.add_user_transition(State.ESOURCE, State.ESOURCE_END, "[!-#ONT(ontexplore)]")
df.add_system_transition(State.ESOURCE_END, State.END, '"Got it. Well, it was nice talking to you. Goodbye!"')

##error states

##unrecognizable feature
df.set_error_successor(State.WHYLIKE, State.ERRWHY)
df.add_system_transition(State.ERRWHY, State.YN, 'Oh that is an interesting feature"!" Is it nicer than how Facebook works"?"')

##unrecognizable usage
df.set_error_successor(State.USE, State.ERRUSE)
df.add_system_transition(State.ERRUSE, State.IMPROVE_Q, '"That is a great thing to use Instagram for! Personally I like to post stories, but the feature can be improved. How else do you think Instagram can improve?"')

##doesn't capture yes or no
df.set_error_successor(State.YN, State.ERRYN)
df.add_system_transition(State.ERRYN, State.USE, 'I agree with you on that one. What do you tend to use Instagram for"?"')


############### seo's chunk branching from State.USE20

#if they put a person as a reason they like instagram
df.add_system_transition(State.PERSONREASONANS, State.INTERACTQ, '"how do you interact with your" [! $person]')

#error if ontology does not recognize the interaction
df.add_system_transition(State.INTERACTERR, State.INTERACTERROR, '"Im not sure I know that one - how else do you interact with" [! $person]')
df.set_error_successor(State.INTERACTQ, State.INTERACTERR)
df.add_user_transition(State.INTERACTERROR, State.INTERACT, "[$interact=#ONT(ontinteract)]")

df.add_user_transition(State.INTERACTQ, State.INTERACT, "[$interact=#ONT(ontinteract)]")
df.add_system_transition(State.INTERACT, State.AWEEKQ, '"how many times a week do you" [! $interact]')
df.add_user_transition(State.AWEEKQ, State.AWEEK, r"{[$times=/\d+/]}")

#error if not a number
df.add_system_transition(State.AWEEKERR, State.AWEEKERROR, '"Try a number instead! How many times a week do you" [!$interact]')
df.set_error_successor(State.AWEEKQ, State.AWEEKERR)
df.add_user_transition(State.AWEEKERROR, State.AWEEK, r"{[$times=/\d+/]}")
#transition to end
df.add_system_transition(State.AWEEK, State.END, '[!$times] "is a solid number. Well, it was nice talking to you. Goodbye!"')

#if they say creating content as a reason for liking instagram
df.add_user_transition(State.USE, State.CONTENTREASON, "[$reason=#ONT(ontcontentreasons)]")
df.add_system_transition(State.CONTENTREASON, State.OFTENQ, '"how often do you post"')
df.add_user_transition(State.OFTENQ, State.POSTTIME, "[$posttime=#ONT(onttimes)]")
#error
df.set_error_successor(State.OFTENQ, State.POSTTIME)
df.add_system_transition(State.POSTTIME, State.FOLLOWERSQ, '"oh thats not too bad. How many followers do you have"')
df.add_user_transition(State.FOLLOWERSQ, State.FOLLOWERS, r"{[$followers=/\d+/]}")

#error for it not a number entered for followers
df.add_system_transition(State.FOLLOWERSERR, State.FOLLOWERSERROR, '"Try a number instead! How many followers do you have"')
df.set_error_successor(State.FOLLOWERSQ, State.FOLLOWERSERR)
df.add_user_transition(State.FOLLOWERSERROR, State.FOLLOWERS, r"{[$followers=/\d+/]}")

df.add_system_transition(State.FOLLOWERS, State.CONTENTQ, r'[!#NUMBERCOMP . What kind of content do you make]')

df.add_user_transition(State.CONTENTQ, State.CONTENTTYPE, "[$contenttype=#ONT(ontcontents)]")
df.add_system_transition(State.CONTENTTYPE, State.ULASTPOST, '"I love" [! $contenttype]' "posts when did you last post")

##if no type of content is found:
df.add_system_transition(State.CONTENTERR, State.ULASTPOSTERROR, '"I prefer food posts. when did you last post "')
df.set_error_successor(State.CONTENTQ, State.CONTENTERR)
df.add_system_transition(State.ULASTPOSTERROR, State.LASTPOST, "[$lastpost=#ONT(ontpostingtime)]")
df.set_error_successor(State.ULASTPOSTERROR, State.LASTPOST)

df.add_user_transition(State.ULASTPOST, State.LASTPOST, "[$lastpost=#ONT(ontpostingtime)]")
df.set_error_successor(State.ULASTPOST, State.LASTPOST)
df.add_system_transition(State.LASTPOST, State.POSTHOURS, "that wasnt long ago. How many hours a day do you spend on Instagram")
df.add_user_transition(State.POSTHOURS, State.HOURS, r"{[$hours=/\d+/]}")

#error for if not a number
df.add_system_transition(State.HOURSERR, State.HOURSERROR, '"Try a number instead! How many hours a day do you spend on Instagram"')
df.set_error_successor(State.POSTHOURS, State.HOURSERR)
df.add_user_transition(State.HOURSERROR, State.HOURS, r"{[$hours=/\d+/]}")


df.add_system_transition(State.HOURS, State.WORKQ, r'[!#HOURSCOMP Does it affect your work]')
##if yes
df.add_user_transition(State.WORKQ, State.ANS_Y, '[#ONT(ontaffirmative)]')
df.add_system_transition(State.ANS_Y, State.END, '"Oh man. You gotta fix that. Well, it was nice talking to you. Goodbye!"')

##if no
df.add_user_transition(State.WORKQ, State.ANS_N, '[#ONT(ontnegative)]')
df.add_system_transition(State.ANS_N, State.END, '"That\'s great! Well, it was nice talking to you. Goodbye!"')

df.set_error_successor(State.WORKQ, State.ERR_WORK)
df.add_system_transition(State.ERR_WORK, State.WORKQ, '"I\'m sorry, was that a yes or a no?"')

##gene

#if user doesn't like Instagram (this is from first prompt)
df.add_user_transition(State.PROMPT, State.NO, "[#ONT(ontnegative)]")
df.add_system_transition(State.NO, State.DISLIKE_Q, '"Really? Why don\'t you like Instagram?"')

# if reason is dislike_noun
df.add_user_transition(State.DISLIKE_Q, State.DISLIKE_NOUN, "[$reason=#ONT(dislike_noun)]")
df.add_system_transition(State.DISLIKE_NOUN, State.IMPROVE_Q, '[!"Yeah, sometimes" $reason "get annoying. So how do '
                                                              'you think Instagram can improve?"]')
#error for dislike
df.set_error_successor(State.DISLIKE_Q, State.ERR_DISLIKE)
df.add_system_transition(State.ERR_DISLIKE, State.IMPROVE_Q, '"That\'s understandable. So how can Instagram improve?"')

#if reason is dislike_adj
df.add_user_transition(State.DISLIKE_Q, State.DISLIKE_ADJ, "[$reason=#ONT(dislike_adj)]")
df.add_system_transition(State.DISLIKE_ADJ, State.ADJ_Q, '"I can see how you think it\'s" [!$reason] ". But are you '
                                                         'saying you\'ve never been" [!$reason] "?"')

#if user says no
df.add_user_transition(State.ADJ_Q, State.ADJ_NO, "[#ONT(ontnegative)]")
df.add_system_transition(State.ADJ_NO, State.IMPROVE_Q, '"That\'s what I thought. I\'m just kidding. So how do you '
                                                        'think Instagram can improve?"')
#if user says yes
df.add_user_transition(State.ADJ_Q, State.ADJ_YES, "[#ONT(ontaffirmative)]")
df.add_system_transition(State.ADJ_YES, State.IMPROVE_Q, '"I\'m not sure if I believe you. But anyway, how do you"'
                                                         '"think Instagram can improve?"')

#if reason for dislike is likable
df.add_user_transition(State.DISLIKE_Q, State.LIKABLE, "[! -use $reason=#ONT(likable)]")
df.add_system_transition(State.LIKABLE, State.IMPROVE_Q, '[! "For real? I love" $reason". So how do you think Instagram'
                                                         ' can improve?"]')

#how can Instagram improve
df.add_user_transition(State.IMPROVE_Q, State.IMPROVE, "/.*/")
df.add_system_transition(State.IMPROVE, State.ACHIEVE_Q, '"That sounds like a good idea. Do you think it is"'
                                                         '"achievable?"')
df.add_user_transition(State.ACHIEVE_Q, State.ACHIEVE_YES, "[#ONT(ontaffirmative)]")
df.add_user_transition(State.ACHIEVE_Q, State.ACHIEVE_NO, "[#ONT(ontnegative)]")
df.add_system_transition(State.ACHIEVE_YES, State.OTHER_Q, '"Maybe you should work for Instagram. So is there other"'
                                                           '"social media you like to use?"')
df.add_system_transition(State.ACHIEVE_NO, State.OTHER_Q, '"Yeah, that sounds pretty hard. So is there other social"'
                                                          '"media you prefer?"')

#error for achieve
df.set_error_successor(State.ACHIEVE_Q, State.ERR_ACHIEVE)
df.add_system_transition(State.ERR_ACHIEVE, State.OTHER_Q, '"Ok. So is there other social media you prefer?"')

#other social media besides facebook
df.add_user_transition(State.OTHER_Q, State.OTHER, "$other=[! -facebook]")
df.add_system_transition(State.OTHER, State.OTH_REASON, '[! "What about" $other "makes it good?"]')
df.add_user_transition(State.OTH_REASON, State.OTH_END, "/.*/")
df.add_system_transition(State.OTH_END, State.END, '[! "That\'s true. I like" $other "too, but Instagram is my '
                                                   'favorite. Well, it was nice talking to you. Goodbye!"]')

#if user likes facebook
df.add_user_transition(State.OTHER_Q, State.FACEBOOK_Q, "[facebook]")
df.add_system_transition(State.FACEBOOK_Q, State.FACEBOOK, '"Who uses Facebook anymore? Well actually, Instagram is"'
                                                           '"owned by Facebook. Did you know that?"')
df.add_user_transition(State.FACEBOOK, State.FACE_ANS, "/.*/")
df.add_system_transition(State.FACE_ANS, State.END, '"Maybe Facebook will own everything one day. Well, it was nice '
                                                    'talking to you. Goodbye!"')

#if reason for dislike is related to time
df.add_user_transition(State.DISLIKE_Q, State.TIME, "[$reason={#ONT(time)}]")
df.add_system_transition(State.TIME, State.POSTHOURS, "How many hours a day do you spend on Instagram")

#if reason for dislike is not using social media
df.add_user_transition(State.DISLIKE_Q, State.SOCMED, '[dont, use, social media]')
df.add_system_transition(State.SOCMED, State.SOC_REASON, '"Seriously? That\'s pretty unusual. Why don\'t you use"'
                                                         '"social media?"')
df.add_user_transition(State.SOC_REASON, State.SOC_END, "/.*/")
df.add_system_transition(State.SOC_END, State.END, '"Huh, I guess that makes sense. Well, it was nice talking to you. '
                                                   'Goodbye!"')

#end state
df.add_system_transition(State.END, State.END, "END REACHED")
df.set_error_successor(State.END, State.END)

df.run(debugging=False)

class NUMBERCOMP(Macro):
    ##used to compare the number of followers

    def run(self, ngrams, vars, args):
        d = int(vars['followers'])
        if d < 1000:
            return 'You should get more bro'
        else:
            return 'Whoa whoa you are famous!'

df.add_system_transition(State.FOLLOWERS, State.CONTENTQ, r'[!#NUMBERCOMP . What kind of content do you make]')


class HOURSCOMP(Macro):
    ##used to compare the number of hours spent on insta

    def run(self, ngrams, vars, args):
        h = int(vars['hours'])
        if (h < 3):
            return "That's not too bad. Good work."
        else:
            return "Aren't your eyeballs killing you? That's a long time!"

df.add_system_transition(State.HOURS, State.WORKQ, r'[!#HOURSCOMP Does it affect your work]')
