
from emora_stdm import KnowledgeBase, DialogueFlow, NatexNLU
from enum import Enum


# TODO: Update the State enum as needed
class State(Enum):
    START = 0
    PROMPT = 1
    ERR = 2
    NOSTREAM = 3
    WHATEV = 4
    SPOTIFY = 5
    VERSION = 6
    PAID = 7
    STUDENT = 8
    YESSTUDENT = 9
    NOSTUDENT = 10
    STUDISCOUNT = 11
    REASONPAY = 12
    YESSTUDISCOUNT = 13
    NOSTUDISCOUNT = 14
    FREETV = 15
    NOADS = 16
    FAMILYPLAN = 17
    FAVESHOW = 18
    UFAVESHOW = 19
    ERR1 = 20
    ERR3 = 21
    ERR4 = 22
    NOOTHER = 23
    BORING = 24
    PANDORA = 25
    OTHERSTREAM = 26
    APPLE = 27
    AMAZON = 28
    YOUTUBE = 29
    YESOTHER = 30
    OFFLINE = 31
    DISCOVERNEW = 32
    DISCOUNT = 33
    CREATEPLAYLISTS = 34
    DISCOVERY2 = 35
    ERR5 = 36
    HULUSHOWTIME = 37
    ERR6 = 38
    UHULU = 39
    ERR7 = 40
    YESHULU = 41
    YESSHOWTIME = 42
    BOTHSHOWS = 43
    NEITHERSHOW = 44
    ENDNO = 45
    ERR8 = 46
    END = 47
    SPOTIFYWRONG = 48
    CREATEPLAYLISTS1 = 49
    PLAYLISTANS = 50
    ERR9 = 51
    DOWNLOAD1 = 52
    DOWNLOADANS = 53
    ERR10 = 54
    ENDHERE = 55
    FREESPOT = 56
    REASONFREE = 57
    MONEYREASON = 58
    INFREQUENT = 59
    STUDENT2 = 60
    YESSTUDENT2 = 61
    DISCOUNTINFO = 62
    YESDOWNLOAD = 63
    ERROR = 64
    MUSICOFFLINE = 65
    MUSICPREF = 66
    OLDMUS = 67
    NEWMUS = 68
    LIKEPLAYLIST = 69
    YESPLAYLIST = 70
    NOPLAYLIST = 71
    ERR11 = 72
    ERR12 = 73
    MUSTIME = 74
    UMUSTIME = 75
    FAMMEMBERS = 76
    UFAMMEMBERS = 77
    ERRTRANSITION = 78
    EXITLOOP = 79
    NODOWNLOAD = 80
    PREFERENCEANS = 81
    KNOWN = 82
    DISCOVER = 83
    NOSTUDENT2 = 84
    LIKEPLAYLIST1 = 85
    YESPERSONAL = 86
    NOPERSONAL = 87
    DISCOVERY3 = 88
    NEWARTISTS = 89
    NONEW = 90
    YEARINREV = 91
    LIKEPLAYLIST2 = 92
    YESPERSONAL2 = 93
    NOPERSONAL2 = 94
    YESYEAR = 95
    NOYEAR = 96
    ADS = 97
    ADOPINION1 = 98
    ADOPINION2 = 99
    ERR13 = 100
    ERR14 = 101
    ERR15 = 102
    ERR16 = 103
    ERR18 = 104
    ERR19 = 105
    ERR20 = 106
    ERR21 = 107
    PLAYERROR = 108
    DOWNLOADNO = 109
    PLAYLISTANS2 = 110
    HULUSHOWTIME1 = 111
    SYSRESYES = 112
    SYSRESNO = 113
    SYSVERSIONF = 114
    SYSVERSIONP = 115
    SYSPREFKNOW = 116
    SYSPREFDIS = 117
    SYSRESDIS3Y = 118
    SYSRESDIS3N = 119
    CONVENIENCE = 120
    SELECTION = 121
    SYSFAVESHOW = 122
    FINAL = 123


# TODO: create the ontology as needed
ontology = {
    "ontology": {
        "ontotherstream":
            [
                "ontoffline", "ontdiscount", "ontplaylists", "ontdiscovery", "ontfreeshows", "ontdownload", "ontads",
                "ontfamily", "ontconvenience", "ontstop"
            ],
        "ontoffline":
            [
                "download", "offline", "downloading"
            ],
        "ontdiscount":
            [
                "price", "reduced", "discount", "cheap", "cheaper", "expensive", "money", "free", "affordable", "inexpensive", "cost"
            ],
        "ontplaylists":
            [
                "create", "playlist", "playlists", "share", "choose"
            ],
        "ontdiscovery":
            [
                "discover", "new", "mix", "discovering", "find", "finding", "uncover", "uncovering", "different"
            ],
        "ontfreeshows":
            [
                "hulu", "showtime", "tv", "television", "shows", "video", "videos", "movie", "movies"
            ],
        "ontads":
            [
                "ads", "advertisements", "commercials", "interruptions", "uninterrupted", "ad"
            ],
        "ontfamily":
            [
                "family", "mom", "dad", "sister", "brother", "siblings", "friend", "friends"
            ],
        "ontstop":
            [
                "exit", "stop", "nothing", "else", "bye", "good bye", "goodbye", "not sure"
            ],
        "ontconvenience":
            [
                "easy", "simple", "convenient", "good", "install", "installed"
            ],
        "ontselection":
            [
                "variety", "selection", "lots", "many", "songs", "diverse", "options", "any", "favorite", "song", "favorites"
            ]
    }
}

knowledge = KnowledgeBase()
knowledge.load_json(ontology)
df = DialogueFlow(State.START, initial_speaker=DialogueFlow.Speaker.SYSTEM, kb=knowledge)

# intro, spotify or not?
df.add_system_transition(State.START, State.PROMPT, '"hi, do you use spotify for music streaming?"')
df.add_user_transition(State.PROMPT, State.SPOTIFY, '[{yes, yea, yup, yep, i do, yeah, sometimes, sure}]')
df.add_user_transition(State.PROMPT, State.SYSRESYES,
                       '<{yes, yea, yup, yep, i do, yeah, sometimes, sure}, {what, whats, you, your}>')
df.add_system_transition(State.SYSRESYES, State.VERSION,
                         '"I use Spotify too! do you use the free version or do you use premium?"')
df.add_user_transition(State.PROMPT, State.SYSRESNO, '<{no, nah, nope, never, not}, {what, whats, you, your}>')
df.add_system_transition(State.SYSRESNO, State.WHATEV,
                         '"I use Spotify to stream music. What other music streaming services do you use?"')
df.add_system_transition(State.ERR1, State.PROMPT, '"i dont understand. do you use spotify?"')
df.set_error_successor(State.PROMPT, State.ERR1)

# free or paid?
df.add_system_transition(State.SPOTIFY, State.VERSION,
                         '"thats awesome! do you use the free version or do you use premium?"')
df.add_user_transition(State.VERSION, State.FREESPOT, '[{free, trial}]')
df.add_user_transition(State.VERSION, State.SYSVERSIONF, '<{free, trial}, {what, whats, you, your}>')

df.add_user_transition(State.VERSION, State.PAID, '[{premium, paid, pay}]')
df.add_user_transition(State.VERSION, State.SYSVERSIONP, '<{premium, paid, pay}, {what, whats, you, your}>')

df.add_system_transition(State.SYSVERSIONF, State.REASONFREE,
                         '"I use the premium version. why did you choose to use the free version over premium?"')
df.add_system_transition(State.SYSVERSIONP, State.STUDENT, '"I use the paid version too! Are you a student then?"')
df.add_system_transition(State.ERROR, State.VERSION, '"i dont understand. do you use the free or paid version?"')
df.set_error_successor(State.VERSION, State.ERROR)

# free spotify
df.add_system_transition(State.FREESPOT, State.REASONFREE,
                         '"why did you choose to use the free version instead of the paid version?"')
df.add_user_transition(State.REASONFREE, State.MONEYREASON, '[{money, expensive, worth it, cost, pay, cheap, cheaper, costs less}]')
df.add_user_transition(State.REASONFREE, State.INFREQUENT,
                       '[{often, frequent, frequently, never, rarely, dont listen, dont use, dont, listen, use}]')
df.add_system_transition(State.ERR13, State.REASONFREE,
                         '"sorry i dont understand. did you choose the free version because premium is expensive or do you just not listen that often?"')
df.set_error_successor(State.REASONFREE, State.ERR13)
df.add_system_transition(State.INFREQUENT, State.PREFERENCEANS,
                         '"oh thats sad. when you do use spotify, do you prefer to listen to music you know and like or would you rather discover new music?"')
df.add_system_transition(State.MONEYREASON, State.STUDENT2, '"well, are you a student?"')
df.add_user_transition(State.STUDENT2, State.NOSTUDENT2, '[{no, nope, nah, not}]')
df.add_system_transition(State.NOSTUDENT2, State.PREFERENCEANS,
                         '"oh, well theres a student discount. the base price of premium is 10 dollars a month but the free version still has a lot of features. do you prefer to listen to music you know and like or would you rather discover new music?"')
df.add_user_transition(State.STUDENT2, State.YESSTUDENT2, '[{yes, yea, yup, yep, i am, yeah, sure}]')
df.add_system_transition(State.YESSTUDENT2, State.DISCOUNTINFO,
                         '"you can get spotify premium for just 5 dollars a month instead of 10. premium also lets you download playlists. is that a feature you would use?"')
df.add_system_transition(State.ERR15, State.STUDENT2,
                         '"sorry i dont understand. are you a student? do you have an email that ends with edu?"')
df.set_error_successor(State.STUDENT2, State.ERR15)
df.add_user_transition(State.DISCOUNTINFO, State.YESDOWNLOAD, '[{yes, yea, yup, yep, i am, yeah, maybe, sometimes, sure}]')
df.add_user_transition(State.DISCOUNTINFO, State.NODOWNLOAD, '[{no, nope, nah, i dont, not really, not}]')
df.add_system_transition(State.ERR16, State.DISCOUNTINFO,
                         '"im confused, do you like downloading playlists to listen to music offline?"')
df.set_error_successor(State.DISCOUNTINFO, State.ERR16)
df.add_system_transition(State.YESDOWNLOAD, State.PREFERENCEANS,
                         '"maybe you should consider getting premium. do you prefer to listen to music you know and like or would you rather discover new music?"')
df.add_system_transition(State.NODOWNLOAD, State.PREFERENCEANS,
                         '"in that case, the free version seems like a good fit for you. it still has a lot of the same features that premium has. do you prefer to listen to music you know and like or would you rather discover new music?"')

# music listening preferences
df.add_user_transition(State.PREFERENCEANS, State.KNOWN, '[{know, familiar, already, my, personal, like}]')
df.add_user_transition(State.PREFERENCEANS, State.SYSPREFKNOW,
                       '<{know, familiar, already, my, personal}, {what, whats, you, your}>')
df.add_system_transition(State.SYSPREFKNOW, State.LIKEPLAYLIST1,
                         '"i also like listening to music I already know. spotify free lets you create your own playlists. it also makes playlists for you. do you ever like any of the playlists that spotify creates for you?"')
df.add_user_transition(State.PREFERENCEANS, State.SYSPREFDIS,
                       '<{discover, new, mix, discovering, find, finding, uncover, uncovering, different}, {what, whats, you, your}>')
df.add_system_transition(State.SYSPREFDIS, State.LIKEPLAYLIST2,
                         '"i also like discovering new music. spotify recommends new music for you based on what you like! do you ever like any of the playlists that spotify creates for you?"')
yesnewartists = r"[#ONT(ontdiscovery)]"
df.add_user_transition(State.PREFERENCEANS, State.DISCOVER, yesnewartists)
df.add_system_transition(State.ERR14, State.PREFERENCEANS,
                         '"sorry i dont understand. which do you like more: listening to music you already know or discovering new music?"')
df.set_error_successor(State.PREFERENCEANS, State.ERR14)
df.add_system_transition(State.KNOWN, State.LIKEPLAYLIST1,
                         '"spotify free lets you create your own playlists so you can listen to those songs you know you like. it also makes playlists for you. do you ever like any of the playlists that spotify creates for you?"')
df.add_system_transition(State.PLAYERROR, State.LIKEPLAYLIST1,
                         '"im confused, do you like the playlists that spotify creates for you?"')
df.set_error_successor(State.LIKEPLAYLIST1, State.PLAYERROR)
df.add_user_transition(State.LIKEPLAYLIST1, State.YESPERSONAL, '[{yes, yea, yup, yep, yeah, maybe, sometimes, sure}]')
df.add_system_transition(State.YESPERSONAL, State.DISCOVERY3,
                         '"spotify is really good at personalizing your music. do you also like to discover new music and artists?"')
df.add_user_transition(State.LIKEPLAYLIST1, State.NOPERSONAL, '[{no, not, not really, nope, never}]')
df.add_system_transition(State.NOPERSONAL, State.DISCOVERY3,
                         '"well spotify creates new playlists for you every day so im sure you wont hate all of them. spotify is also always learning about your preferences so they can improve. do you like to discover new music and artists?"')

# features of spotify free
df.add_user_transition(State.DISCOVERY3, State.SYSRESDIS3Y,
                       '<{yes, yea, yup, yep, yeah, maybe, sometimes, sure}, {what, whats, you, your}>')
df.add_system_transition(State.SYSRESDIS3Y, State.YEARINREV,
                         '"i also love discovering new music. it keeps things fresh and a lot of up and coming artists are on spotify. have you heard of year in review?"')
df.add_user_transition(State.DISCOVERY3, State.SYSRESDIS3N,
                       '<{no, not, not really, nope, never}, {what, whats, you, your}>')
df.add_system_transition(State.SYSRESDIS3N, State.YEARINREV,
                         '"i personally like discovering new music but sometimes it is nice to listen to the classics! have you heard of year in review?"')
df.add_user_transition(State.DISCOVERY3, State.NEWARTISTS, '[{yes, yea, yup, yep, yeah, maybe, sometimes, sure}]')
df.add_user_transition(State.DISCOVERY3, State.NONEW, '[{no, not, not really, nope, never}]')
df.add_system_transition(State.ERR18, State.DISCOVERY3,
                         '"sorry i dont understand. do you like to discover new music and artists?"')
df.set_error_successor(State.DISCOVERY3, State.ERR18)





df.add_system_transition(State.NEWARTISTS, State.YEARINREV,
                         '"a lot of up and coming artists are on spotify! have you heard of year in review?"')
df.add_system_transition(State.NONEW, State.YEARINREV,
                         '"its always nice to listen to the classics! have you heard of year in review?"')
df.add_system_transition(State.DISCOVER, State.LIKEPLAYLIST2,
                         '"spotify recommends new music for you based on what you like! do you ever like any of the playlists that spotify creates for you?"')
df.add_user_transition(State.LIKEPLAYLIST2, State.YESPERSONAL2, '[{yes, yea, yup, yep, yeah, maybe, sometimes, sure}]')
df.add_user_transition(State.LIKEPLAYLIST2, State.NOPERSONAL2, '[{no, not, not really, nope, never}]')
df.add_system_transition(State.ERR19, State.LIKEPLAYLIST2,
                         '"sorry i dont understand. do you like the playlists that spotify automatically creates for you?"')
df.set_error_successor(State.LIKEPLAYLIST2, State.ERR19)

# year in review
df.add_system_transition(State.YESPERSONAL2, State.YEARINREV,
                         '"spotify is really good at personalizing your music. they have another feature thats very personalized. have you heard of year in review?"')
df.add_system_transition(State.NOPERSONAL2, State.YEARINREV,
                         '"well spotify creates new playlists for you every day so im sure you wont hate all of them. spotify is also always learning about your preferences so they can improve. have you heard of year in review?"')
df.add_user_transition(State.YEARINREV, State.YESYEAR, '[{yes, yea, yup, yep, yeah, of course, sure}]')
df.add_user_transition(State.YEARINREV, State.NOYEAR, '[{no, nope, what, nah, not sure}]')
df.add_system_transition(State.ERR20, State.YEARINREV, '"im confused. have you heard of year in review or not?"')
df.set_error_successor(State.YEARINREV, State.ERR20)

# ads on free spotify
df.add_system_transition(State.YESYEAR, State.ADS,
                         '"isnt it a great service! i love looking at the statistics of my music streaming. i wonder how much time i spend listening to ads though, do that ads from spotify free ever bother you?"')
df.add_system_transition(State.NOYEAR, State.ADS,
                         '"its my favorite feature of spotify. every year spotify will compile all the statistics of your music streaming so you can see how many minutes of each artist you listened to, which song you played the most, etc. i wonder how much time i spend listening to ads though. do the ads on spotify free ever bother you?"')
df.add_system_transition(State.ERR21, State.ADS, '"i dont understand. do the ads ever bother you?"')
df.set_error_successor(State.ADS, State.ERR21)
df.add_user_transition(State.ADS, State.ADOPINION1, '[{no, nope, never, nah, not really, okay}]')
df.add_system_transition(State.ADOPINION1, State.ENDHERE,
                         '"i think the ads can be annoying but if you dont mind them then the free version of spotify sounds like a good fit for you"')
df.add_user_transition(State.ADS, State.ADOPINION2, '[{yes, yea, yup, yep, yeah, sometimes, sure}]')
df.add_system_transition(State.ADOPINION2, State.ENDHERE,
                         '"the ads are annoying to me too. the premium version of spotify is much better since its ad free. it might be worth it for you. you should look into it!"')
df.add_user_transition(State.ENDHERE, State.FINAL, '/.*/')

# user doesn't use spotify
df.add_user_transition(State.PROMPT, State.NOSTREAM, '[{no, nope, nah, i dont}]')
df.add_system_transition(State.NOSTREAM, State.WHATEV,
                         '"thats unfortunate. what other streaming service do you use then?"')
df.add_user_transition(State.WHATEV, State.YESOTHER, '[{yes, yea, yup, yep, i do, yeah, sometimes, sure}]')
df.add_system_transition(State.YESOTHER, State.WHATEV, '"what streaming services do you use instead of spotify?"')
df.add_user_transition(State.WHATEV, State.SPOTIFYWRONG, '[spotify]')
df.add_system_transition(State.SPOTIFYWRONG, State.VERSION,
                         '"what?! you just told me you dont use spotify! do you have the free or paid subscription?"')

# other streaming services
df.add_user_transition(State.WHATEV, State.PANDORA, '[{pandora, pandora radio}]')
df.add_system_transition(State.PANDORA, State.OTHERSTREAM,
                         '"pandora is great for discovering new music, and the free version allows you unlimited skips but has ads! what do you like about pandora?"')
df.add_user_transition(State.WHATEV, State.APPLE, '[{apple, iphone, siri}]')
df.add_system_transition(State.APPLE, State.OTHERSTREAM,
                         '"apple music is well integrated with siri! what do you like about apple music?"')
df.add_user_transition(State.WHATEV, State.AMAZON, '[{amazon, amazonplus, amazonpremium}]')
df.add_system_transition(State.AMAZON, State.OTHERSTREAM,
                         '"amazon music is well integrated with alexa! what do you like about amazon music?"')
df.add_user_transition(State.WHATEV, State.YOUTUBE, '[youtube]')
df.add_system_transition(State.YOUTUBE, State.OTHERSTREAM,
                         '"you can watch thousands of music videos on youtube, all for free! what do you like about youtube?"')
df.add_system_transition(State.ERR5, State.OTHERSTREAM, '"hm, im not familiar with that feature. what else do you like about your streaming service?"')
df.set_error_successor(State.OTHERSTREAM, State.ERR5)

# reason: download
yesotheroffline = r"[#ONT(ontoffline)]"
df.add_user_transition(State.OTHERSTREAM, State.OFFLINE, yesotheroffline)
df.add_system_transition(State.OFFLINE, State.DISCOVERNEW,
                         '"well spotify premium also lets you download music so you can listen offline! do you like to discover new music?"')
df.add_user_transition(State.DISCOVERNEW, State.HULUSHOWTIME, '[{yes, yea, sure, yup, yep, i do, yeah, sometimes}]')
df.add_user_transition(State.DISCOVERNEW, State.HULUSHOWTIME1, '[{no, nope, nah, not really, not, i dont}]')
df.add_system_transition(State.ERR6, State.DISCOVERNEW, '"i dont understand. do you like to discover new music?"')
df.set_error_successor(State.DISCOVERNEW, State.ERR6)

# tv included
df.add_system_transition(State.HULUSHOWTIME, State.UHULU,
                         '"spotify creates personalized playlists based on what kind of music youve been listening to and generates playlists of new music for you every week. spotify also comes with other free perks. do you watch hulu, showtime, both, or neither?"')
df.add_system_transition(State.HULUSHOWTIME1, State.UHULU,
                         '"if you dont like discovering new music or want to download your music and take up space on your phone, then you can always listen to your old music online. spotify also comes with other free perks. do you watch hulu, showtime, both, or neither?"')
df.add_user_transition(State.UHULU, State.YESHULU, '[{hulu, Hulu}]')
df.add_system_transition(State.YESHULU, State.ENDNO,
                         '"well if you buy spotify premium, you wont even have to pay for your hulu subscription, and you will get free access to showtime. maybe you should consider switching to spotify!"')
df.add_user_transition(State.UHULU, State.YESSHOWTIME, '[{showtime, SHOWTIME, showtime}]')
df.add_system_transition(State.YESSHOWTIME, State.ENDNO,
                         '"well if you buy spotify premium, a subscription to showtime is included for free, along with free access to hulu! maybe you should consider switching to spotify!"')
df.add_user_transition(State.UHULU, State.BOTHSHOWS, '[both]')
df.add_system_transition(State.BOTHSHOWS, State.ENDNO,
                         '"if you buy spotify premium, you wont have to pay for either hulu or showtime! maybe you should consider switching to spotify!"')
df.add_user_transition(State.UHULU, State.NEITHERSHOW, '[{neither, none of the above, no}]')
df.add_system_transition(State.NEITHERSHOW, State.ENDNO,
                         '"well if you buy spotify premium, you can start watching hulu or showtime, all for free! maybe you should consider switching to spotify!"')
df.add_system_transition(State.ERR7, State.UHULU, '"i dont understand. do you watch hulu or showtime?"')
df.set_error_successor(State.UHULU, State.ERR7)
df.add_user_transition(State.ENDNO, State.ENDHERE, "/.*/")
df.add_system_transition(State.ENDHERE, State.END,
                         '"next time we talk i want you to share with me your spotify playlists! Nice talking to you, goodbye!"')
df.add_user_transition(State.END, State.FINAL, "/.*/")
df.add_system_transition(State.FINAL, State.END, '"goodbye!"')


# reason: discount
yesotherdiscount = r"[#ONT(ontdiscount)]"
df.add_user_transition(State.OTHERSTREAM, State.DISCOUNT, yesotherdiscount)
df.add_system_transition(State.DISCOUNT, State.CREATEPLAYLISTS1,
                         '"spotify has different discounted plans, such as for students or families. there are over 30 million songs in the spotify library, across many music genres that you can listen to and create playlists from. do you like creating your own music playlists?"')
df.add_user_transition(State.CREATEPLAYLISTS1, State.PLAYLISTANS, '[{yes, yea, sure, yup, yep, i do, yeah, sometimes}]')
df.add_user_transition(State.CREATEPLAYLISTS1, State.PLAYLISTANS2, '[{no, nope, nah, not really, i dont}]')
df.add_system_transition(State.PLAYLISTANS2, State.DISCOVERNEW,
                         '"well, if you dont like to spend time creating your own playlists, spotify generates new playlists for you every day based on what youve been listening to. its a great way to discover new music. do you like to discover new music?"')
df.add_system_transition(State.ERR8, State.CREATEPLAYLISTS1,
                         '"i dont understand. do you like to create your own music playlists?"')
df.set_error_successor(State.CREATEPLAYLISTS1, State.ERR8)
df.add_system_transition(State.PLAYLISTANS, State.DISCOVERNEW,
                         '"spotify allows you to create your own playlist to listen whenever you want. you can also share music with friends and vice versa. do you like to discover new music?"')

# reason: playlists, download, tv included
yescreateplaylists = r"[#ONT(ontplaylists)]"
df.add_user_transition(State.OTHERSTREAM, State.CREATEPLAYLISTS, yescreateplaylists)
df.add_system_transition(State.CREATEPLAYLISTS, State.DISCOVERY2,
                         '"spotify lets you create your own playlists too so you can listen whenever you want. you can also share music with friends. do you like discovering new music?"')
df.add_user_transition(State.DISCOVERY2, State.DOWNLOAD1, '[{yes, yea, sure, yup, yep, i do, yeah, sometimes}]')
df.add_user_transition(State.DISCOVERY2, State.DOWNLOADNO, '[{no, nope, nah, not really, not, i dont}]')
df.add_system_transition(State.ERR9, State.DISCOVERY2, '"i dont understand. do you like discovering new music?"')
df.set_error_successor(State.DISCOVERY2, State.ERR9)
df.add_system_transition(State.DOWNLOADNO, State.DOWNLOADANS,
                         '"well you can always listen to your old music! i imagine itd get quite boring listening to the same songs though. do you like to download the music you like so that you can listen offline?"')
df.add_system_transition(State.DOWNLOAD1, State.DOWNLOADANS,
                         '"spotify creates personalized playlists for you based on what youve been listening to. do you like to download your music so that you can listen offline?"')
df.add_user_transition(State.DOWNLOADANS, State.HULUSHOWTIME, '[{yes, yea, sure, yup, yep, i do, yeah, sometimes}]')
df.add_user_transition(State.DOWNLOADANS, State.HULUSHOWTIME1, '[{no, nope, nah, not really, not, i dont}]')
df.add_system_transition(State.ERR10, State.DOWNLOADANS, '"i dont understand. do you like to download music?"')
df.set_error_successor(State.DOWNLOADANS, State.ERR10)

# reason: discovery
df.add_user_transition(State.OTHERSTREAM, State.DISCOVERY2, yesnewartists)
df.add_system_transition(State.DISCOVERY2, State.DOWNLOADANS,
                         '"spotify creates for you personal playlists based on what youve been listening to. do you like to download your music so you can listen offline?"')

# reason: convenient
convenient = r"[#ONT(ontconvenience)]"
df.add_user_transition(State.OTHERSTREAM, State.CONVENIENCE, convenient)
df.add_system_transition(State.CONVENIENCE, State.CREATEPLAYLISTS1,
                         '"Spotify is also very convenient. theres a mobile app and a desktop web player so you can listen anytime and anywhere. do you like creating your own playlists?"')

# reason: wide selection
selection = r"[#ONT(ontselection)]"
df.add_user_transition(State.OTHERSTREAM, State.SELECTION, selection)
df.add_system_transition(State.SELECTION, State.CREATEPLAYLISTS1,
                         '"Spotify also has hundreds of songs, podcasts, and radio stations to listen to. with so much content, listeners have to make their own playlist to sort through everything thats available. do you like to create your own playlists?"')

# user doesnt use a streaming service
df.add_user_transition(State.WHATEV, State.NOOTHER, '[{no, nope, nah, i dont, none, nothing}]')
df.add_system_transition(State.NOOTHER, State.BORING,
                         '"you are too boring. everyone listens to music! i simply cannot continue the conversation. bye!"')
df.add_user_transition(State.BORING, State.FINAL, "/.*/")


# reason: unknown
df.add_system_transition(State.ERR, State.WHATEV,
                         '"i dont know that one, please enter another streaming service that you may be interested in using"')
df.set_error_successor(State.WHATEV, State.ERR)

#reason: none
exitloop = r"[#ONT(ontstop)]"
df.add_user_transition(State.OTHERSTREAM, State.ENDHERE, exitloop)

# spotify premium
df.add_system_transition(State.PAID, State.STUDENT, '"are you a student then?"')
df.add_system_transition(State.ERR3, State.STUDENT, '"i dont understand. are you a student?"')
df.set_error_successor(State.STUDENT, State.ERR3)
df.add_user_transition(State.STUDENT, State.NOSTUDENT, '[{no, nope, im not}]')
df.add_system_transition(State.NOSTUDENT, State.REASONPAY,
                         '"aww, that means you cant use the student discount. why do you still prefer spotify premium over the free version?"')
df.add_user_transition(State.STUDENT, State.YESSTUDENT, '[{yes, yea, sure, yup, yep, i am, yeah}]')
df.add_system_transition(State.YESSTUDENT, State.STUDISCOUNT,
                         '"oh great! does that mean you are using the student discount?"')
df.add_system_transition(State.ERR4, State.STUDISCOUNT,
                         '"i dont understand. since you are a student, are you using the student discount?"')
df.set_error_successor(State.STUDISCOUNT, State.ERR4)

# using student discount
df.add_user_transition(State.STUDISCOUNT, State.YESSTUDISCOUNT, '[{yes, yea, sure, yup, yep, i am, yeah}]')
df.add_system_transition(State.YESSTUDISCOUNT, State.REASONPAY,
                         '"wonderful! you only have to pay 5 dollars/month instead of 10. why do you like spotify premium over the free version?"')

# not using student discount
df.add_user_transition(State.STUDISCOUNT, State.NOSTUDISCOUNT, '[{no, nope, im not}]')
df.add_system_transition(State.NOSTUDISCOUNT, State.REASONPAY,
                         '"well you should! you would be saving 5 dollars/month! why do you like spotify premium over the free version?"')

# reason paid: free shows
yesfreeshows = r"[#ONT(ontfreeshows)]"
df.add_user_transition(State.REASONPAY, State.FREETV, yesfreeshows)
df.add_system_transition(State.FREETV, State.FAVESHOW,
                         '"yes, spotify premium gives you free hulu as well as showtime! whats the name of your favorite show?"')
df.add_user_transition(State.FAVESHOW, State.SYSFAVESHOW, '[{what, whats, you, your}]')
df.add_system_transition(State.SYSFAVESHOW, State.REASONPAY,
                         '"my favorite show is brooklyn 99. i love that i can watch it on hulu for free with spotify paid. why else do you like premium?"')
df.add_user_transition(State.FAVESHOW, State.UFAVESHOW, "/.*/")
df.add_system_transition(State.UFAVESHOW, State.REASONPAY,
                         '"hmm, ive never heard of it, but ill be sure to put it on my watchlist! why else do you like spotify premium?"')

# reason paid: download
yesdownloading = r"[#ONT(ontoffline)]"
df.add_user_transition(State.REASONPAY, State.MUSICOFFLINE, yesdownloading)
df.add_system_transition(State.MUSICOFFLINE, State.MUSICPREF,
                         '"downloading music is great for plane rides. do you prefer to listen to music you know and like or discover new music?"')
df.add_user_transition(State.MUSICPREF, State.OLDMUS, '[{know, old, classics, already}]')
df.add_system_transition(State.OLDMUS, State.LIKEPLAYLIST,
                         '"interesting! i think id be quite bored just listening to old music. do you every like any of the playlists that spotify creates for you?"')
df.add_user_transition(State.LIKEPLAYLIST, State.YESPLAYLIST, '[{yes, yea, sure, yup, yep, i do, yeah, sometimes}]')
df.add_system_transition(State.YESPLAYLIST, State.REASONPAY,
                         '"spotify is great at personalizing your music based on the songs youve listened to before. what other features do you like about spotify premium?"')
df.add_user_transition(State.LIKEPLAYLIST, State.NOPLAYLIST, '[{no, nope, nah, i dont, never}]')
df.add_system_transition(State.NOPLAYLIST, State.REASONPAY,
                         '"aww, thats unfortunate. you can actually click dislike on songs that you really dont enjoy so that spotify will know to never put those songs on your playlist again. what else do you like about spotify premium?"')
df.add_system_transition(State.ERR12, State.LIKEPLAYLIST,
                         '"i dont understand. do you like the playlists that spotify creates for you?"')
df.set_error_successor(State.LIKEPLAYLIST, State.ERR12)
df.add_user_transition(State.MUSICPREF, State.NEWMUS, '[{new, discover, disovering, find, finding, different}]')
df.add_system_transition(State.NEWMUS, State.REASONPAY,
                         '"yeah, spotify has great features for discovering new music! spotify will generate discover weekly playlists every monday! what else do you like about spotify premium?"')
df.add_system_transition(State.ERR11, State.MUSICPREF,
                         '"can you say that again please? do you prefer to listen to music you know or discover new music?"')
df.set_error_successor(State.MUSICPREF, State.ERR11)

# reason paid: no ads
yesnoads = r"[#ONT(ontads)]"
df.add_user_transition(State.REASONPAY, State.NOADS, yesnoads)
df.add_system_transition(State.NOADS, State.MUSTIME,
                         '"agreed! ads are the worst, especially when im listening to spotify when trying to sleep. when do you listen to music?"')
df.add_user_transition(State.MUSTIME, State.UMUSTIME, "/.*/")
df.add_system_transition(State.UMUSTIME, State.REASONPAY,
                         '"thats a little weird, but im just a bot, what other features do you like about spotify premium?"')

# reason paid: family plan
yesfamily = r"[#ONT(ontfamily)]"
df.add_user_transition(State.REASONPAY, State.FAMILYPLAN, yesfamily)
df.add_system_transition(State.FAMILYPLAN, State.FAMMEMBERS,
                         '"the family plan offers a great discount of 15 dollars/month. which of your family members do you share your account with?"')
df.add_user_transition(State.FAMMEMBERS, State.UFAMMEMBERS, '[{parents, sister, brother, friends}]')
df.add_system_transition(State.UFAMMEMBERS, State.REASONPAY,
                         '"yes, the family plan can cover up to 6 people. what else do you like about spotify premium?"')

# no more reasons
df.add_user_transition(State.REASONPAY, State.EXITLOOP, exitloop)
df.add_system_transition(State.EXITLOOP, State.ENDHERE, '"well bye then! im off to listen to spotify!"')

# reason paid: unknown
df.add_system_transition(State.ERRTRANSITION, State.REASONPAY,
                         '"hmm, ive never heard of it. what else do you like about spotify premium?"')
df.set_error_successor(State.REASONPAY, State.ERRTRANSITION)

df.run(debugging=False)

df.set_error_successor(State.PROMPT, State.ERR)