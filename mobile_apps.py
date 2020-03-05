from emora_stdm import KnowledgeBase, DialogueFlow
from enum import Enum

ont_dict = {
    "ontology": {
        "ontapptype":
            [
                "fitness",
                "productivity",
                "socialmedia",
                "storage",
                "streaming"
            ],
        "ontyes":
            [
                "yeah",
                "yes",
                "yea",
                "mmhmm",
                "yuh"
            ],
        "ontproductivity":
            [
                "studytimer",
                "health",
                "education",
                "notes",
                "educationalapps"
            ],
        "ontnotes":
            [
                "goodnotes",
                "applenotes",
                "notepad",
                "onenote",
                "other"
            ],
        "onthealth":
            [
                "pedometer",
                "studytimer",
                "caloriecounter",
                "sleeptracker",
                "moodlog",
                "ontother"
            ],
        "ontsocialmedia":
            [
                "snapchat",
                "ontinstagram",
                "ontfacebook",
                "onttwitter"
            ],
        "ontstreaming":
            [
                "spotify"
                "netflix"
                "hulu"
                "amazon"
            ],
        "ontmusicgenres":
            [
                "hip hop"
                "rock"
                "edm"
            ],
        "ontentertainmentgenres":
            [
                "action"
                "comedy"
                "drama"
                "horror"
            ],

        "ontfitness":
            [
                "sleeptracker",
                "caloriecounter",
                "pedometer",
                "moodlog"
            ],
        "ontstorage":
            [
                "icloud",
                "googledrive",
                "dropbox",
                "emorybox"
            ]
    }
}

class State(Enum):
    START = 0
    P1 = 1
    P2A = 2
    P2B = 3
    P2C = 4
    P3A = 5
    P3B = 6
    P3C = 7
    P3D = 8
    P3E = 9
    P3F = 10
    P3G = 11
    P3H = 12
    P3I = 13
    P3J = 14
    P3K = 15
    P3L = 16
    P4A = 17
    P4B = 18
    P4C = 19
    P4D = 20
    P4E = 21
    P4F = 22
    P4G = 23
    P4H = 24
    P4I = 25
    P4J = 26
    P4K = 27
    P4L = 28
    P4M = 29
    P4N = 30
    P4O = 31
    P4P = 32
    P4Q = 33
    P4R = 34
    P4S = 35
    P4T = 36
    P4U = 37
    P4V = 38
    P4W = 190
    P4X = 191
    P4Z = 197
    P5A = 39
    P5B = 40
    P5C = 41
    P5D = 42
    P5E = 43
    P5F = 44
    P5G = 45
    P5H = 46
    P5J = 47
    P5K = 48
    P5L = 49
    P5M = 50
    P5N = 51
    P5O = 52
    P5P = 53
    P5Q = 54
    P5R = 189
    P5S = 192
    P5T = 198
    P6A = 55
    P6B = 56
    P6C = 57
    P6D = 58
    P6E = 59
    P6F = 60
    P6G = 61
    P6H = 62
    P6I = 63
    P6J = 64
    P6K = 65
    P6L = 66
    P6M = 193
    P6N = 2138
    P7A = 67
    P7B = 68
    P7C = 69
    P7D = 70
    P7E = 71
    P7F = 72
    P7G = 73
    P7H = 74
    P7I = 75
    P7J = 76
    P7K = 77
    P7M = 78
    P7L = 79
    P8A = 80
    P8B = 81
    P8C = 82
    P8D = 83
    P8E = 84
    P8F = 2318
    P8G = 2318123
    P9A = 85
    P9B = 86
    P9C = 87
    P9D = 188
    P9E = 21323
    P9F = 43284
    P10A = 88
    P10B = 89
    P10C = 187
    P11A = 90
    P11B = 91
    P11C = 92
    P11D = 193
    P12A = 93
    P12B = 94
    P12C = 194
    P12D = 196
    P13A = 195
    U1 = 95
    U2 = 96
    U3 = 97
    U4 = 98
    U5 = 99
    U6 = 100
    U7 = 101
    U8 = 102
    U9 = 103
    U10 = 104
    U11 = 105
    U12 = 106
    U13 = 107
    U14 = 108
    U15 = 109
    U16 = 110
    U17 = 111
    U18 = 112
    U19 = 113
    U20 = 114
    U21 = 115
    U22 = 116
    U23 = 117
    U24 = 118
    U25 = 119
    U26 = 120
    U27 = 121
    U28 = 122
    U29 = 123
    U30 = 124
    U31 = 125
    U32 = 126
    U33 = 127
    U34 = 128
    U35 = 129
    U36 = 130
    U37 = 131
    U38 = 132
    U39 = 133
    U40 = 134
    U41 = 135
    U42 = 136
    U43 = 137
    U44 = 138
    U45 = 139
    U46 = 140
    U47 = 141
    U48 = 142
    U49 = 143
    U50 = 144
    U51 = 145
    U52 = 146
    U53 = 147
    U54 = 148
    U55 = 149
    U56 = 150
    U57 = 151
    U58 = 152
    U59 = 153
    U60 = 154
    U61 = 155
    U62 = 156
    U63 = 157
    U64 = 158
    U65 = 159
    U66 = 160
    U67 = 161
    U68 = 162
    U69 = 163
    U70 = 164
    U71 = 165
    U72 = 166
    U73 = 167
    U74 = 168
    U75 = 169
    U76 = 170
    U77 = 171
    U78 = 172
    U79 = 173
    U80 = 174
    U81 = 175
    U82 = 176
    U83 = 177
    U84 = 178
    U85 = 179
    U86 = 180
    U87 = 181
    U88 = 182
    U89 = 183
    U90 = 184
    U91 = 185
    U92 = 186
    U93 = 199
    U94 = 200
    U95 = 201
    U96 = 202
    U97 = 203
    U98 = 204
    U99 = 205
    U100 = 206
    U101 = 207
    U102 = 208
    U103 = 209
    U104 = 210
    U105 = 211
    U106 = 212
    U107 = 213
    U108 = 214
    U109 = 215
    U110 = 216
    U111 = 217
    U112 = 218
    U113 = 219
    U114 = 220

    ERR = 135
    ERR2 = 136
    ERR3 = 137
    ERR5 = 138
    ERR6 = 140
    ERRS = 141


    END = 139




knowledge = KnowledgeBase()
knowledge.load_json(ont_dict)
#df = DialogueFlow(State.START, initial_speaker=DialogueFlow.Speaker.SYSTEM, kb=knowledge)
# =============================================================================
# THIS SECTION IS THE BEGINNING AND FITNESS BRANCH

df = DialogueFlow(State.START, initial_speaker=DialogueFlow.Speaker.SYSTEM, kb =knowledge)

df.add_system_transition(State.START, State.P1, '"Do you have a phone?"')
df.add_user_transition(State.P1, State.U1,
                       r"[$response=/(.*)(no)|(nah)|(nope)|(No)|(NO)|(Nah)|(NAH)|(Nope)|(NOPE)(.*)/]")
df.add_user_transition(State.P1, State.U2,
                       r"[$response=/(.*)(yes)|(Yes)|(YES)|(yea)|(YEA)|(Yea)|(yeah)|(Yeah)|(YEAH)(.*)/]")
df.add_user_transition(State.P2B, State.U3,
                       r"[$response=/(.*)(yes)|(Yes)|(YES)|(yea)|(YEA)|(Yea)|(yeah)|(Yeah)|(YEAH)(.*)/]")
df.add_user_transition(State.P2C, State.U2,
                       r"[$response=/(.*)(yes)|(Yes)|(YES)|(yea)|(YEA)|(Yea)|(yeah)|(Yeah)|(YEAH)(.*)/]")
df.add_user_transition(State.P2C, State.U4,
                       r"[$response=/(.*)(no)|(nah)|(nope)|(No)|(NO)|(Nah)|(NAH)|(Nope)|(NOPE)(.*)/]")
df.add_user_transition(State.P2A, State.U6,
                       r"[$response=/(.*)(fitness)|(Fitness)|(health)|(Health)|(working out)|(Working out)|(HEALTH)|(FITNESS)(.*)/]")
df.add_user_transition(State.P2A, State.U9,
                       r"[$response=/(.*)(no)|(nah)|(nope)|(No)|(NO)|(Nah)|(NAH)|(Nope)|(NOPE)(.*)/]")
df.add_user_transition(State.P4E, State.U8, "$response=/.*/")
df.add_user_transition(State.P2A, State.U13,
                       r"[$response=/(.*)(yes)|(Yes)|(YES)|(yea)|(YEA)|(Yea)|(yeah)|(Yeah)|(YEAH)(.*)/]")
df.add_user_transition(State.P5C, State.U10,
                       r"[$response=/(.*)(caloriecounter)|(calorie-counter)|(caloriecounting)|(calorie-counting)|(calorie)|(pedometer)|(sleeptracker)|(sleep-tracker)|(sleeptracking)|(sleep-tracking)(.*)/]")
df.add_user_transition(State.P6C, State.U11,
                       r"[$response=/(.*)(yes)|(Yes)|(YES)|(yea)|(YEA)|(Yea)|(yeah)|(Yeah)|(YEAH)(.*)/]")
df.add_user_transition(State.P6C, State.U12,
                       r"[$response=/(.*)(no)|(nah)|(nope)|(No)|(NO)|(Nah)|(NAH)|(Nope)|(NOPE)(.*)/]")
# below needs to use dictionary
df.add_user_transition(State.P7M, State.U8, "$response=/.*/")

df.add_system_transition(State.ERR3, State.P1, '"Sorry, I missed that. Do you have a phone?"')
df.set_error_successor(State.P1, State.ERR3)
df.add_system_transition(State.U2, State.P2A, '"What type of mobile apps do you use?"')
df.add_system_transition(State.U1, State.P2C, '"Do you use a phone?"')
df.add_system_transition(State.U4, State.P3B, '"Oh, maybe you will in the future! Talk to you then."')
#
df.add_user_transition(State.P3B, State.END, "/.*/")
df.add_system_transition(State.END, State.END, '"Goodbye."')
#
df.add_system_transition(State.ERR, State.P2A, '"I am personally a fan of Strava. Do you use any fitness apps?"')
df.set_error_successor(State.P2A, State.ERR)
df.add_system_transition(State.U6, State.P4E,
                         '"Which fitness app specifically? I have been thinking about getting one."')
df.add_system_transition(State.U13, State.P4E,
                         '"Which fitness app specifically? I have been thinking about getting one."')
df.add_system_transition(State.U9, State.P3B, '"Oh, maybe you will in the future! Talk to you then."')
df.add_system_transition(State.U8, State.P5C,
                         '"What feature does" $response "have that you like most? Like, does it have calorie counting, sleep tracking, or a pedometer?"')
df.add_system_transition(State.ERR5, State.P4E, '"What other fitness apps do you use?"')
df.set_error_successor(State.P5C, State.ERR5)
df.add_system_transition(State.U10, State.P6C,
                         '"I have never used" $response "before, as I have heard that it can become obsessive. Has it helped you grow healthier?"')
#
df.add_user_transition(State.P7L, State.END, "/.*/")
#
df.add_system_transition(State.U11, State.P7L,
                         '"Great! Thanks for suggesting it; I am going to go check it out now. Talk to you later!"')
df.add_system_transition(State.U12, State.P7M, '"Oh, bummer. What other fitness apps do you use?"')
# =====================================================================================================
# THIS SECTION IS SOCIAL MEDIA APPS
# mainly instagram
df.add_user_transition(State.P2A, State.U14,
                       r"[$response=/(.*)(social)|(socialmedia)|(social media)|(Social media)(.*)/]")
df.add_user_transition(State.P7A, State.U15, r"[$response=/(.*)(snap)|(snapchat)|(Snapchat)|(SNAPCHAT)(.*)/]")
df.add_user_transition(State.P7A, State.U17, r"[$response=/(.*)(ig)|(insta)|(instagram)(.*)/]")
df.add_user_transition(State.P7A, State.U18, r"[$response=/(.*)(fb)|(facebook)|(Facebook)|(FACEBOOK)(.*)/]")
df.add_user_transition(State.P4U, State.U19,
                       r"[$response=/(.*)(no)|(nah)|(nope)|(No)|(NO)|(Nah)|(NAH)|(Nope)|(NOPE)(.*)/]")
df.add_user_transition(State.P4U, State.U20,
                       r"[$response=/(.*)(yes)|(Yes)|(YES)|(yea)|(YEA)|(Yea)|(yeah)|(Yeah)|(YEAH)(.*)/]")
df.add_user_transition(State.P5O, State.U21,
                       r"[$response=/(.*)(yes)|(Yes)|(YES)|(yea)|(YEA)|(Yea)|(yeah)|(Yeah)|(YEAH)(.*)/]")
df.add_user_transition(State.P5O, State.U22,
                       r"[$response=/(.*)(no)|(nah)|(nope)|(No)|(NO)|(Nah)|(NAH)|(Nope)|(NOPE)(.*)/]")
df.add_user_transition(State.P5N, State.U21,
                       r"[$response=/(.*)(yes)|(Yes)|(YES)|(yea)|(YEA)|(Yea)|(yeah)|(Yeah)|(YEAH)(.*)/]")
df.add_user_transition(State.P5N, State.U22,
                       r"[$response=/(.*)(no)|(nah)|(nope)|(No)|(NO)|(Nah)|(NAH)|(Nope)|(NOPE)(.*)/]")

df.add_system_transition(State.U14, State.P7A, '"Cool, which social media app is your favorite?"')
df.add_system_transition(State.U17, State.P4U, '"Do you have more than 2000 followers?"')
# above needs an error
df.add_system_transition(State.ERR6, State.P7A, '"What other social media apps do you use?"')
df.set_error_successor(State.P4U, State.ERR6)

df.add_system_transition(State.U19, State.P5O, '"That\'s cool, I have 346! Would you like to follow each other?"')
df.add_system_transition(State.U20, State.P5N,
                         '"Wow, that\'s a lot of followers! Would you like to follow each other?"')
df.add_system_transition(State.U21, State.P6J,
                         '"Great! My username is @emoryuniversity. I\'ll go check out your feed, talk to you later!"')
#
df.add_user_transition(State.P6J, State.END, "/.*/")
#
df.add_system_transition(State.U22, State.P6K, '"Aw, I thought we were friends. Good-bye then."')
#
df.add_user_transition(State.P6K, State.END, "/.*/")
#

# mainly snapchat
df.add_user_transition(State.P4V, State.U23,
                       r"[$response=/(.*)(yes)|(Yes)|(YES)|(yea)|(YEA)|(Yea)|(yeah)|(Yeah)|(YEAH)(.*)/]")
df.add_user_transition(State.P4V, State.U24,
                       r"[$response=/(.*)(no)|(nah)|(nope)|(No)|(NO)|(Nah)|(NAH)|(Nope)|(NOPE)(.*)/]")
df.add_user_transition(State.P5P, State.U25,
                       r"[$response=/(.*)(yes)|(Yes)|(YES)|(yea)|(YEA)|(Yea)|(yeah)|(Yeah)|(YEAH)(.*)/]")
df.add_user_transition(State.P5P, State.U26,
                       r"[$response=/(.*)(no)|(nah)|(nope)|(No)|(NO)|(Nah)|(NAH)|(Nope)|(NOPE)(.*)/]")
df.add_user_transition(State.P7J, State.U27,
                       r"[$response=/(.*)(yes)|(Yes)|(YES)|(yea)|(YEA)|(Yea)|(yeah)|(Yeah)|(YEAH)(.*)/]")
df.add_user_transition(State.P7J, State.U28,
                       r"[$response=/(.*)(no)|(nah)|(nope)|(No)|(NO)|(Nah)|(NAH)|(Nope)|(NOPE)(.*)/]")
df.add_user_transition(State.P6K, State.U29, r"[$response=/(.)/]")

df.add_system_transition(State.U15, State.P4V,
                         '"Do you use Snapchat a lot? I\'m thinking about getting one, but I prefer words over pictures."')
df.add_system_transition(State.U23, State.P5P, '"Do you have more than 10 streaks?"')
df.add_system_transition(State.U24, State.P5P, '"Do you have more than 10 streaks?"')
df.add_system_transition(State.U25, State.P7J, '"Wow, that\'s a lot of streaks! Would you like to be my first one?"')
df.add_system_transition(State.U27, State.P8C, '"Cool, what\'s your username?"')
df.add_system_transition(State.U28, State.P6K, '"Aw, I thought we were friends. Good-bye then."')
#
df.add_user_transition(State.U28, State.END, "/.*/")
#
df.add_system_transition(State.U26, State.P7J, '"That\'s not a lot. I can be another one if you\'d like!"')
df.add_system_transition(State.U29, State.P9C, '"I\'ll snap you as soon as I make an account. See you later!"')
#
df.add_user_transition(State.U29, State.END, "/.*/")
#

# mainly facebook
df.add_user_transition(State.P3E, State.U30, r"[$response=/(.*)/]")

df.add_system_transition(State.U30, State.P7A,
                         '"Oh, that\'s nice. I personally talk to my family using Facebook. What other social media apps do you use?"')
df.add_system_transition(State.U18, State.P3E, '"Who do you communicate with most over Facebook?"')

df.add_system_transition(State.ERR2, State.P7A, '"Do you like any other social media apps?"')
df.set_error_successor(State.P7A, State.ERR2)

#=========================================================================================================

# STREAMING APPS
df.add_system_transition(State.ERR, State.ERR, r"[!i have failed]")
df.add_user_transition(State.P2A, State.U114,
                       r"[$response=/(.*)(streaming|Streaming|music,Music|video|Video)(.*)/]")
df.add_system_transition(State.U114, State.P3G, '"What streaming apps(music, video) do you use?"')

df.add_user_transition(State.P3G, State.U70, "$response={spotify}")
df.add_user_transition(State.P3G, State.U71, "$response={netflix}")
df.add_user_transition(State.P3G, State.U72, "$response={hulu}")
df.add_user_transition(State.P3G, State.U73, "$response={amazon}")

#SPOTIFY
df.add_system_transition(State.U70, State.P3G, '"Nice! I use that app too. What type of music do you listen to?"')
df.add_user_transition(State.P3G, State.U74, "$response=#ONT(ontmusic)")
df.add_system_transition(State.U74, State.P4N, '"I enjoy listening to that genre as well. What artist have you been listening to lately?"')
df.add_user_transition(State.P4N, State.U75, "/.*/")
df.add_system_transition(State.U76, State.P6L, '"Huh, you have bad taste! Just kidding:) Well, I would love to hear some recommendations if you have any?"')
df.add_user_transition(State.P6L, State.U77, "/.*/")
df.add_system_transition(State.U77, State.P7B, '"I\'ll check them out later. Thanks! Anyways, have you heard about other music streaming services like Bandcamp, Soundcloud? Many people prefer to use Bandcamp since a lot of indie artists receive higher royalties compared to Spotify. Soundcloud is also seen as a more indie artist friendly alternative to Spotify."')
df.add_user_transition(State.P7B, State.U78, "r [$response=/(.*){yes,yeah,Yes,Yeah,Yea}(.*)/]")
df.add_system_transition(State.U78, State.P8D, '"I\'ve worked in both the more popular and indie side of the music industry, and I can tell you that there is a sharp divide in opinion over the artist using Spotify vs. Bandcamp to distribute their content. Unfortuanately, in many contexts, Spotify distributes an artist\'s musician without any consultation. What do you think about this debate on how artists should seek to release their music?"')
df.add_user_transition(State.P8D, State.U79, "/.*/")
df.add_system_transition(State.U79, State.P9D, '"What about Soundcloud? For someone searching for music by a new artist, soundcloud is seen as a more friendly medium for new artists who are not established. Do you think it matters ultimately what popular digital medium an artist uses to release their content?"')
df.add_user_transition(State.P9D, State.U80, "/.*/")
df.add_system_transition(State.U80, State.P10C, '"Interesting, well I have to go now. See you later!"')
df.add_system_transition(State.P10C, State.END, ''"Goodbye!"'')

df.set_error_successor(State.U74, error_successor=State.ERR)
df.set_error_successor(State.U78, error_successor=State.ERR)


#NETFLIX

df.add_system_transition(State.U71, State.P4X, '"Aha! I\'ve heard Netflix is the top one for streaming entertainment shows and films"." What type of shows do you usually like watching?"')
df.add_user_transition(State.P4X, State.U81,"$response=ONT(ontentertainment)")
df.add_system_transition(State.U81, State.P5S, '"Mhm, well I\'m personally a fan of drama shows like Stranger Things, Peaky Blinders, even a borderline animated drama like Bojack Horsemen! Well, what about that genre makes you interested in watching those shows?"')
df.add_user_transition(State.P6M, State.U82,   "/.*/")

df.add_system_transition(State.U82, State.P7C,  '"I see. What about films? Have you seen anything that caught your eye recently?"')
df.add_user_transition(State.P7C, State.U83,  "$response=ONT(ontyes)")
df.add_system_transition(State.U83, State.P8D,  '"Really? Could you tell me a little bit about the film\'s plot?"')
df.add_user_transition(State.P8D, State.U84,  "/.*/")
df.add_system_transition(State.U84, State.P9D,  '"Hmm. The director must envision something I can\'t quite see. Is the acting good?"')
df.add_user_transition(State.P9D, State.U85,  ".*/")
df.add_system_transition(State.U85, State.P10C,  '"Plot, acting... I\'m a bit pedantic with my movies, so could you tell me a bit about the cinematography?"')
df.add_user_transition(State.P10C, State.U86,  "$response= r[/(.*){yes,yeah,no,maybe,haha}(.*)/]")
df.add_system_transition(State.U86,State.P11D, '"Thanks for going into detail about the film. I don\'t mean to kill the mood, but have you heard about the controversy surrounding the Netflix algorithm?"')
df.add_user_transition(State.P11D, State.U87, "r [$response=/(.*){yes,yeah, Yes, Yeah}(.*)/]")
df.add_user_transition(State.P11D, State.U88, "r [$response=/(.*){no, nah, nope, No, Nah, Nope}(.*)/]")


df.add_system_transition(State.U87, State.P12C, '"I thought I was the only one. I\'m on the government\'s side when it comes to this debate...what side are you on? Netflix or FTC?]'"")
df.add_user_transition(State.P12C, State.U89, "$side=ONT(ontdebate)")
df.add_system_transition(State.U89, State.P13A, '"! $side. Alright well I have to get going now. It was nice talking to you!"')

df.add_user_transition(State.P7C, State.U90, "r [$response=/(.*){no,nope,nah,idc}(.*)/]")
df.add_system_transition(State.U90, State.P8G, '"Sigh...well I need to run. Catch you later!"')
df.add_system_transition(State.P8G, State.END, '"Goodbye!"')

df.add_system_transition(State.U88, State.P12D, '"The Netflix algorithm has to do with the Netflix Prize competition. The competition asked for its participiants to devise an algorithm that returns better recommendations to its users compared to its current algorithm. Netflix eventually ran into trouble with the FTC due to releasing private datasets into the public domain for the competition."')
df.add_system_transition(State.P12D, State.END, '"Goodbye!"')

df.set_error_successor(State.U81, error_successor=State.ERR)
df.set_error_successor(State.U83, error_successor=State.ERR)
df.set_error_successor(State.U86, error_successor=State.ERR)
df.set_error_successor(State.U87, error_successor=State.ERR)
df.set_error_successor(State.U88, error_successor=State.ERR)
df.set_error_successor(State.U89, error_successor=State.ERR)
df.set_error_successor(State.U90, error_successor=State.ERR)


#AMAZON
df.add_system_transition(State.U73, State.P4Z, '"Do you use Amazon more for eccomerce or video streaming??"')
df.add_user_transition(State.P4Z, State.U100, "$eccomerce=ONT(onteccomerce)")
df.add_user_transition(State.P4Z, State.U101, "#video=ONT(ontvideo)")
#ECCOMERCE BRANCH
df.add_system_transition(State.U100, State.P5T, '"I prefer $eccomerce as well, and see $video as a nice addition to the the overall service. Anyways, what type of shows do you watch?"')
df.add_user_transition(State.P5T, State.U101, "$genres=ONT(ontentertainment)")
df.add_system_transition(State.U101, State.P6N, '"! That $genres is a favorite of mine, but recently I \'ve started watching films more often... do you enjoy watching movies?"')
df.add_user_transition(State.P6N, State.U102, "r [$response=/(.*){yes,yeah,Yes,Yeah}(.*)/]")
df.add_user_transition(State.P6N, State.U103, "r [$response=/(.*){no,nah,nope,Nah,No,Nope}(.*)/]")
#YES BRANCH
df.add_system_transition(State.U102, State.P7E, '"What type of films?"')
df.add_user_transition(State.P7E, State.U104, "r [$response=/(.*)(ONT(entertainment))(.*)/]")
df.add_system_transition(State.U104, State.P8E, '"Great! Any film in particular catch your eye lately?"')
#SECOND YES BRANCH
df.add_user_transition(State.P8E, State.U105, "r [$response=/(.*){yes,yeah,Yes,Yeah)(.*)/]")
df.add_system_transition(State.U105, State.P9E, "'Haven't heard that film yet, but I'll check it out whenever I've got a spare evening. Anyways, I have to go. Nice talking to you!'")
df.add_system_transition(State.P9E, State.END, '"Goodbye!"')

df.add_user_transition(State.P8F, State.U106, "r [$response=/(.*){no,nah,nope,Nah,No,Nope}(.*)/]")
df.add_system_transition(State.U106, State.P9F, '"Oh, well I have to run. Nice talking to you!"')
df.add_system_transition(State.P9F, State.END, '"Goodbye!"')

#NO BRANCH
df.add_system_transition(State.U103, State.P7G, '"Oh, well I have to run. Nice talking to you!"')
df.add_system_transition(State.P7G, State.END, '"Goodbye!"')

df.set_error_successor(State.U100, error_successor=State.ERR)
df.set_error_successor(State.U101, error_successor=State.ERR)
df.set_error_successor(State.U102, error_successor=State.ERR)
df.set_error_successor(State.U103, error_successor=State.ERR)
df.set_error_successor(State.U104, error_successor=State.ERR)
df.set_error_successor(State.U105, error_successor=State.ERR)
df.set_error_successor(State.U106, error_successor=State.ERR)


# =============================================================================
# THIS SECTION IS FOR STORAGE APPS

# Storage Apps
no = r"[{no,not really,nah,nope}]"
maybe = r"[{maybe,idk,IDK,Maybe}]"
df.add_user_transition(State.P2A, State.U91, r"[$response=/(.*)(storage)|(Storage)|(STORAGE)(.*)/]")
df.add_system_transition(State.U91, State.P3K, r'[!"What storage apps do you use?"]')
df.add_user_transition(State.P3K, State.U92, r"[$response=/(.*)(icloud)|(google drive)|(emory box)|(dropbox)(.*)/]")
df.add_system_transition(State.U92, State.P4S, r'[! I think $response is a great app. Do you think your information is safe in the cloud"?"]')
df.add_user_transition(State.P4S, State.U93, r"[$response=/(.*)(yes)|(Yes)|(YES)|(yea)|(YEA)|(Yea)|(yeah)|(Yeah)|(YEAH)(.*)/]")
df.add_system_transition(State.U93, State.END, '"That\'s great, but be careful out there it\'s dangerous!"')
df.add_user_transition(State.P4S, State.U94, no)
df.add_system_transition(State.U94, State.END, '"You should invest in a hard drive to store your information, or you can write everything down and store it in a vault."')
df.add_user_transition(State.P4S, State.U95, maybe)
df.add_system_transition(State.U95, State.END, '"You could invest in a hard drive to store your information, or you can write everything down and store it in a vault."')
df.add_user_transition(State.U91, State.END, "/.*/")
df.add_user_transition(State.U92, State.END, "/.*/")
df.add_user_transition(State.U93, State.END, "/.*/")
df.add_user_transition(State.U94, State.END, "/.*/")
df.add_system_transition(State.ERRS, State.ERRS, r"[!i have failed]")
df.set_error_successor(State.U91, error_successor=State.ERRS)
df.set_error_successor(State.U92, error_successor=State.ERRS)
df.set_error_successor(State.U93, error_successor=State.ERRS)
df.set_error_successor(State.U94, error_successor=State.ERRS)
df.set_error_successor(State.ERRS, error_successor=State.ERRS)
df.set_error_successor(State.END, error_successor=State.END)

df.run(debugging=False)