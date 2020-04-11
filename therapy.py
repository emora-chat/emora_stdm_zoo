from emora_stdm import KnowledgeBase, DialogueFlow
from enum import Enum, auto


# TODO: Update the State enum as needed
class State(Enum):
    START = 0
    PROMPT = 1
    ERR = 2
    END = 3
    EXIT = auto()
    PROMPT2 = 4
    Ending = auto()
    # These are for the first response
    First_feeling_positive = auto()
    First_feeling_negative = auto()
    Catch_feeling_positive = auto()
    Catch_feeling_negative = auto()
    First_feeling_good = auto()

    # Positivity Tree
    First_positive_prompt = auto()

    # Negative Tree
    First_negative_prompt = auto()
    First_negative_response = auto()
    U2A = auto()
    U2B = auto()

    # 3rd
    P3 = auto()
    P3B = auto()
    U3A = auto()
    ERR2 = auto()

    ###ANGER STATES###
    ANGER1 = auto()
    ANGER2 = auto()
    QUESTION1 = auto()
    QUESTION2 = auto()
    PERSON = auto()
    ACTIVITY = auto()
    INEVITABLE = auto()
    AVOIDABLE = auto()
    IDENTIFYPERSON = auto()
    IDENTIFYACTIVITY = auto()
    INEVDESCRIP = auto()
    AVOIDDESCRIP = auto()
    TRIED = auto()
    NOTTRIED = auto()
    FRIEND = auto()
    FAMILY = auto()
    INEVITABLERESPYES = auto()
    INEVITABLERESPNO = auto()
    AVOIDABLERESPCONTROL = auto()
    AVOIDABLERESPINABILITY = auto()
    CHECKIN = auto()
    CHECKIN1 = auto()
    CHECKIN2 = auto()
    CHECKIN3 = auto()
    CHECKIN4 = auto()
    CHECKIN5 = auto()
    CHECKIN6 = auto()
    CHECKIN7 = auto()
    CHECKINRESP = auto()
    CHECKINRESP1 = auto()
    CHECKINRESP2 = auto()
    CHECKINRESP3 = auto()
    CHECKINRESP4 = auto()
    CHECKINRESP5 = auto()
    CHECKINRESP6 = auto()
    CHECKINRESP7 = auto()
    TRIEDINTERMISSION = auto()
    NOTTRIEDINTERMISSION = auto()
    FRIENDINTERMISSION = auto()
    FAMILYINTERMISSION = auto()
    INEVITABLEINTERMISSION = auto()
    NOTINEVITABLEINTERMISSION = auto()
    CONTROLINTERMISSION = auto()
    NOTCONTROLINTERMISSION = auto()
    ERRANG = auto()
    ERRANG1 = auto()
    ERRANG2 = auto()
    ERRANG3 = auto()
    ERRANG4 = auto()
    ERRANG5 = auto()

    # DEPRESSION
    P4CD = auto()
    P4C = auto()
    P4C1 = auto()
    U4C1 = auto()
    U4C2 = auto()
    U4C3 = auto()
    U4C4 = auto()
    U4C5 = auto()
    P4C1A = auto()
    P4C1Asecond = auto()
    P4C2B = auto()
    P4C3C = auto()
    P4C4D = auto()
    P4C4E = auto()
    U4C4E1 = auto()
    U4C4D2 = auto()
    U4C4D1 = auto()
    U4C4D1A1 = auto()
    P4C4D2A = auto()
    P4C4D1A = auto()
    P4C4E1A = auto()
    P4C2B1A = auto()
    P4C2B2A = auto()
    U4C4E1A1 = auto()
    U4C4D1A2 = auto()
    U4C4E1A2 = auto()
    P4C4E1A1A = auto()
    U4C4E1A1A = auto()
    U4C4E1A1B = auto()
    U4C4D2A1 = auto()
    U4C2B1 = auto()
    U4C2B2 = auto()
    U4C2B3 = auto()
    U4C2B4 = auto()
    P4C2B4A = auto()
    U4C2B2A3 = auto()
    U4C2B2A2 = auto()
    U4C2B2A1 = auto()
    U4C2B1A2 = auto()
    U4C2B1A1 = auto()
    P4C2B1A1A = auto()
    P4C4E1A2A = auto()
    U4C4E1A2A1 = auto()
    U4C4E1A2A2 = auto()
    P4C2B2A3A = auto()
    P4C4D1A1A = auto()
    P4C2B2A1A = auto()
    P4C2B1A2A = auto()
    U4C2B1A1A1 = auto()
    P4C2B1A1A1A = auto()
    U4C2B1A1A1A1 = auto()
    U4C2B1A1A1A2 = auto()
    U4C2B2A1A1 = auto()
    U4C4D1A1A1 = auto()
    P4C4D1A2A = auto()
    U4C4D1A2A2 = auto()
    U4C4D1A2A1 = auto()
    U4C2B1A2A1 = auto()
    U4C2B1A2A2 = auto()
    P4C2B1A2A1A = auto()
    U4C2B1A2A1A1 = auto()
    U4C2B1A2A1A2 = auto()
    P4C4D1A1A1A = auto()
    P4C2B1A2A2A = auto()
    P4C2B2A1A1A = auto()
    U4C4D1A1A1A1 = auto()
    U4C2B2A1A1A2 = auto()
    U4C2B2A1A1A1 = auto()
    U4C2B1A2A2A1 = auto()
    P4C2B2A1A1A1A = auto()
    U4C2B2A1A1A1A1 = auto()
    U4C2B2A1A1A1A2 = auto()
    U4C2B2A1A1A2A1 = auto()
    P4C2B2A1A1A2A = auto()
    U4C2B2A1A1A2A2 = auto()
    P4C4D1A1A1A1A = auto()
    P4CE = auto()
    P4CERR = auto()
    P4CERR2 = auto()
    P4CERR3 = auto()
    P4CERR4 = auto()
    P4CERR5 = auto()
    P4CERR6 = auto()
    P4CERR7 = auto()
    P4CERR8 = auto()
    P4CERR9 = auto()
    P4CERR10 = auto()
    P4CERR11 = auto()
    P4CERR12 = auto()
    P4CERR13 = auto()
    P4CERR14 = auto()
    P4CERR15 = auto()
    P4CERR16 = auto()
    P4CERR17 = auto()
    P4CERR18 = auto()
    P4CERR19 = auto()
    P4CERR20 = auto()
    P4CERR21 = auto()
    A11 = auto()
    A111 = auto()
    A1111 = auto()

    P4D = auto()
    U4D1 = auto()
    P4D1 = auto()

    # eating
    P4E = auto()
    U4E1 = auto()
    U4E2 = auto()
    P4E1A = auto()
    P4E2A = auto()
    U4E1A2 = auto()
    U4E1A1 = auto()
    U4E2A1 = auto()
    U4E2A2 = auto()
    P4E1A2A = auto()
    P4E1A2B = auto()
    P4E2A1A = auto()
    P4E2A2A = auto()
    U4E1A2B1 = auto()
    U4E2A1A1 = auto()
    U4E2A1A2 = auto()
    U4E2A2A1 = auto()
    U4E2A2A2 = auto()
    U4E2A2A1A1 = auto()
    P4E2A2A1A = auto()
    P4E2A2A2A = auto()
    U4EA = auto()
    P4EERR = auto()
    P4E1AERR = auto()
    P4E1A2AERR = auto()
    P4E1A2BERR = auto()
    P4E2AERR = auto()
    P4E2A1AERR = auto()
    P4E2A2AERR = auto()
    P4E2A2A2AERR = auto()
    S1 = auto()
    S2 = auto()
    S3 = auto()
    S4 = auto()
    S5 = auto()
    S6 = auto()
    S7 = auto()
    S8 = auto()
    S9 = auto()
    S10 = auto()
    S11 = auto()
    S12 = auto()
    S13 = auto()
    S14 = auto()
    S15 = auto()
    S16 = auto()
    S17 = auto()
    S18 = auto()
    S19 = auto()
    S20 = auto()
    S21 = auto()
    S22 = auto()
    S23 = auto()
    S24 = auto()
    S25 = auto()
    S26 = auto()
    S27 = auto()
    S28 = auto()
    S29 = auto()
    S30 = auto()
    S31 = auto()
    S32 = auto()
    S33 = auto()
    S34 = auto()
    S35 = auto()
    S36 = auto()
    S37 = auto()
    S38 = auto()
    S39 = auto()
    S40 = auto()
    S41 = auto()
    S42 = auto()
    S43 = auto()
    S44 = auto()
    S45 = auto()
    S46 = auto()
    S47 = auto()
    S48 = auto()
    S49 = auto()
    S50 = auto()
    S51 = auto()
    S52 = auto()
    S53 = auto()
    S54 = auto()
    S55 = auto()
    S56 = auto()
    S57 = auto()
    S58 = auto()
    S59 = auto()
    S60 = auto()
    S61 = auto()
    S62 = auto()
    S63 = auto()
    S64 = auto()
    S65 = auto()
    S66 = auto()
    S67 = auto()
    S68 = auto()
    S69 = auto()
    S70 = auto()
    S71 = auto()
    S72 = auto()
    S73 = auto()
    S74 = auto()
    S75 = auto()
    S76 = auto()
    S77 = auto()
    S78 = auto()
    S79 = auto()
    S80 = auto()
    S81 = auto()
    S82 = auto()
    S83 = auto()
    S84 = auto()
    S85 = auto()
    S86 = auto()
    S87 = auto()
    S88 = auto()
    S89 = auto()
    S90 = auto()
    S91 = auto()
    S92 = auto()
    S93 = auto()
    S94 = auto()
    S95 = auto()
    S96 = auto()
    S97 = auto()
    S98 = auto()
    S99 = auto()
    S100 = auto()

    U1 = auto()
    U2 = auto()
    U3 = auto()
    U4 = auto()
    U5 = auto()
    U6 = auto()
    U7 = auto()
    U8 = auto()
    U9 = auto()
    U10 = auto()
    U11 = auto()
    U12 = auto()
    U13 = auto()
    U14 = auto()
    U15 = auto()
    U16 = auto()
    U17 = auto()
    U18 = auto()
    U19 = auto()
    U20 = auto()
    U21 = auto()
    U22 = auto()
    U23 = auto()
    U24 = auto()
    U25 = auto()
    U26 = auto()
    U27 = auto()
    U28 = auto()
    U29 = auto()
    U30 = auto()
    U31 = auto()
    U32 = auto()
    U33 = auto()
    U34 = auto()
    U35 = auto()
    U36 = auto()
    U37 = auto()
    U38 = auto()
    U39 = auto()
    U40 = auto()
    U41 = auto()
    U42 = auto()
    U43 = auto()
    U44 = auto()
    U45 = auto()
    U46 = auto()
    U47 = auto()
    U48 = auto()
    U49 = auto()
    U50 = auto()
    U51 = auto()
    U52 = auto()
    U53 = auto()
    U54 = auto()
    U55 = auto()
    U56 = auto()
    U57 = auto()
    U58 = auto()
    U59 = auto()
    U60 = auto()
    U61 = auto()
    U62 = auto()
    U63 = auto()
    U64 = auto()
    U65 = auto()
    U66 = auto()
    U67 = auto()
    U68 = auto()
    U69 = auto()
    U70 = auto()
    U71 = auto()
    U72 = auto()
    U73 = auto()
    U74 = auto()
    U75 = auto()
    U76 = auto()
    U77 = auto()
    U78 = auto()
    U79 = auto()
    U80 = auto()
    U81 = auto()
    U82 = auto()
    U83 = auto()
    U84 = auto()
    U85 = auto()
    U86 = auto()
    U87 = auto()
    U88 = auto()
    U89 = auto()
    U90 = auto()
    U91 = auto()
    U92 = auto()
    U93 = auto()
    U94 = auto()
    U95 = auto()
    U96 = auto()
    U97 = auto()
    U98 = auto()
    U99 = auto()
    U100 = auto()

    First_positive_answer = auto()
    First_positive_end= auto()
    First_positive_reply= auto()
    First_positive_ending= auto()
    First_positive_alone= auto()
    First_positive_end2= auto()
    First_positive_ending2= auto()

    # Yuewu Zhou ######################################################################################################
    # confrontation branch ###################################################################

    # Confrontation prompt
    confrontation_prompt = auto()
    # A: We had an argument/fight
    confrontation_answer = auto()

    # - How did it start?
    confrontation_cause_prompt = auto()

    # - A: Other person / self / don't know (don't know leads to improvement branch)
    confrontation_cause_answer = auto()
    confrontation_cause_self = auto()
    confrontation_cause_other = auto()
    confrontation_cause_dontknow = auto()
    confrontation_cause_error = auto()

    # -- Do you think it was intentional?
    confrontation_intentional_yn = auto()

    # -- Yes / No
    confrontation_intentional_answer = auto()

    # --- Why do you think they said that?
    confrontation_intentional_motive_prompt = auto()

    # --- A: Positive / negative sentiment
    confrontation_intentional_motive_answer = auto()

    # ---- Is it justified to argue because (reason) ?
    confrontation_intentional_motive_yn = auto()

    # ---- TO DO: Handle positive vs negative answers

    # -- Is this something that usually happens?
    confrontation_usual_prompt = auto()

    # -- A: Yes / No (Yes leads to advice branch)
    confrontation_usual_yn = auto()

    # --- When was the last time this has happened?
    confrontation_usual_when = auto()

    # --- A: time
    confrontation_usual_when_answer = auto()

    # ---- Have you met with (pronoun) since (time) where you haven't had a (confrontation)?
    confrontation_usual_when_yn = auto()

    confrontation_usual_when1 = auto()
    confrontation_usual_when2 = auto()
    confrontation_usual_when3 = auto()
    confrontation_usual_when_answer1 = auto()
    confrontation_usual_when_answer2 = auto()
    confrontation_usual_when_answer3 = auto()

    # caught self & other branch ###################################################################
    # A: I (catch verb)
    confrontation_self_answer = auto()

    # - How do you think that made them feel?
    confrontation_self_feel_prompt = auto()

    # - A: good / bad
    confrontation_self_feel_answer = auto()

    # -- What do you think could have gone better?
    confrontation_self_improvement_prompt = auto()

    # -- A: verbs (could have) / I don't know or nothing
    confrontation_self_improvement_answer = auto()

    # --- That's sounds great! / Interesting. / I think that would work! Anything else?
    confrontation_self_improvement_yn = auto()

    # --- A: Yes / No (yes returns to confrontation_self_improvement_yn, no transitions to advice)
    confrontation_self_improvement_yn_answer = auto()

    # A: He/She/They (catch verb)
    confrontation_other_answer = auto()

    # - Why do you think they (caught verb) (transitions to intentionality in argument branch)
    confrontation_other_why_prompt = auto()

    # no catch branch ###################################################################
    # A: (no catch)
    confrontation_noCatch_answer = auto()

    # - Was it something that you did?
    confrontation_noCatch_self_prompt = auto()

    # - A: Yes / No (yes leads to self branch)
    confrontation_noCatch_self_answer = auto()

    # -- Was it something that someone else did?
    confrontation_noCatch_other_prompt = auto()

    # -- A: Yes / No (yes leads to other branch branch)
    confrontation_noCatch_other_answer = auto()

    # advice branch ###################################################################
    # Could I offer you some advice?
    confrontation_advice_yn = auto()

    # A: Yes / No (no ends the conversation)
    confrontation_advice_yn_answer = auto()

    # - Would a calmer attitude have helped the situation?
    confrontation_advice_calmer_yn = auto()

    # - A: Yes / No / Maybe (no transitions to other treatment)
    confrontation_advice_calmer_answer = auto()

    # -- Here are some techniques to calm yourself down
    # TO DO: offer advice to calm down

    # usual branch ###################################################################
    # Why do you spend time with this person?
    confrontation_exposure_prompt = auto()

    # because ...
    confrontation_exposure_answer = auto()

    # Will you keep spending time with them?
    confrontation_exposure_why = auto()

    # Yes / No
    confrontation_exposure_yn = auto()

    # Is it maybe a good idea to spend some time away from them and cool off?
    confrontation_exposure_end = auto()

    # treatment branch ###################################################################
    # Still researching treatments, placeholder for advice
    confrontation_treatment_placeholder = auto()

    # Relaxed breathing recommendation
    confrontation_treatment_relaxedbreathing = auto()
    confrontation_treatment_relaxedbreathing_response = auto()
    confrontation_treatment_relaxedbreathing2 = auto()
    confrontation_treatment_relaxedbreathing_response2 = auto()

    # Journaling
    confrontation_treatment_journaling = auto()
    confrontation_treatment_journaling_response = auto()
    confrontation_treatment_journaling2 = auto()
    confrontation_treatment_journaling_response2 = auto()
    # END
    ENDwGREET = auto()

    ############# END Confrontation #####################

    corona_prompt  = auto()

    school_prompt = auto()
    club_prompt = auto()
    club_answer = auto()
    club_enjoy = auto()
    club_enjoy_y= auto()
    club_enjoy_n= auto()

    # family branch

    family_prompt = auto()
    family_answer = auto()
    family_self = auto()
    family_talk = auto()
    family_talk_answer = auto()
    family_talk_end = auto()
    family_talk_suggestion = auto()
    family_self_pressure = auto()
    family_self_pressure_y = auto()
    family_self_pressure_college = auto()
    family_self_pressure_job = auto()
    family_self_pressure_job_answer = auto()

    #work states
    work_prompt = auto()
    work_answer = auto()
    work_enjoy = auto()
    work_enjoy_yn = auto()
    work_enjoy_y = auto()
    work_enjoy_n = auto()
    work_stress_y = auto()
    work_stress_not = auto()

# TODO: create the ontology as needed
ontology = {
    "ontology": {
        "ontP4C":
            [
                "ontschool",
                "onttired",
                "ontfunclub",
                "ontbadclub",
                "ontsad",
                "ontfamily",
                "ontdunno",
                "ontclubs",
                "ontwork",
                "ontunsure",
                "onthotline",
                "onteating",
                "onteatingtoolittle",
                "onteatingtoomuch",
                "ontangry",
                "ontnewyork",
                "ontnewjersey",
                "ontcalifornia",
                "ontmichigan",
                "ontbadstate",
                "ontokaystate",
                "ontcorona",
                "ontstillbusy",
                "ontgoodactivities",
                "ontbadactivities",
                "ontwasteoftime"
            ],
        "ontstillbusy":
            [
                "still busy",
                "lots of work",
                "stressed",
                "too much work",
                "busy",
                "work"
            ],
        "ontgoodactivities":
            [
                "knitting",
                "draw",
                "drew",
                "drawing",
                "knit",
                "knitted",
                "baking",
                "bakes",
                "made",
                "making",
                "homework",
                "school",
                "schoolwork",
                "family",
                "mom",
                "dad",
                "mother",
                "father",
                "sister",
                "brother",
                "sibling",
                "siblings",
                "creating",
                "create",
                "created",
                "hobby",
                "exploring",
                "explore",
                "explored",
                "reading",
                "book",
                "books",
                "read",
                "growing",
                "grow",
                "grew",
                "building",
                "build",
                "built",
                "yoga",
                "job",
                "organizing",
                "cleaning",
                "organize",
                "organized",
                "clean",
                "cleaned"
                "staying home",
                "social distancing",
                "social distance",
                "quarantine",
                "journaling",
                "scrapbooking",
                "journal",
                "scrapbook",
                "singing",
                "violin",
                "piano",
                "practice",
                "practicing",
                "write",
                "writing",
                "guitar",
                "camera",
                "photography",
                "photos",
                "photographs",
                "editing",
                "dancing",
                "singing",
                "sing",
                "dance",
                "exercising",
                "exercise",
                "running",
                "pilates",
                "run",
                "stretching",
                "stretch",
                "jog",
                "jogging",
                "blogilates",
                "recipes",
                "recipe",
                "novels",
                "novel"
            ],
        "ontbadactivities":
            [
                "stressing",
                "worrying",
                "money",
                "financial",
                "finances",
                "lost my job",
                "lost job",
                "unemployed,",
                "crying",
                "cry",
                "cried",
                "sad",
                "depressed",
                "depression",
                "shock",
                "shocked",
                "news",
                "checking",
                "refreshing",
                "videogames",
                "gaming",
                "games"
            ],
        "ontwasteoftime":
            [
                "netflix",
                "movies",
                "tv",
                "television",
                "hulu",
                "nothing",
                "blanking out",
                "instagram",
                "scrolling",
                "phone",
                "bed",
                "sleeping",
                "social media",
                "tik tok",
                "memes",
                "youtube",
                "facebook",
                "scrolling",
                "napping",
                "napped",
                "naps",
                "slept",
                "sleep"
            ],
        "ontcorona":
            [
                "corona",
                "coronavirus",
                "the virus",
                "virus",
                "covid",
                "covid-19"
            ],
        "ontnewjersey":
            [
                "new jersey",
                "nj",
                "garden"
            ],
        "ontcalifornia":
            [
                "california",
                "cali"
            ],
        "ontmichigan":
            [
                "michigan",
                "mich"
            ],
        "ontbadstate":
            [
                "louisiana",
                "la",
                "pennsylvania",
                "pa",
                "florida",
                "massachusetts",
                "ma",
                "illinois",
                "georgia",
                "ga",
                "texas",
                "washington",
                "connecticut",
                "indiana",
                "maryland",
                "md",
                "colorado",
                "ohio",
                "tennessee",
                "virginia",
                "north carolina",
                "nc",
                "missouri",
                "arizona",
                "wisconsin",
                "south carolina",
                "sc",
                "alabama",
                "nevada",
                "mississippi",
                "utah",
                "oklahoma",
                "district of columbia",
                "washington dc",
                "dc",
                "kentucky",
                "rhode island",
                "ri",
                "idaho",
                "oregon",
                "minnesota",
                "iowa",
                "arkansas",
                "ar",
                "kansas"
            ],
        "ontokaystate":
            [
                "delaware",
                "new mexico",
                "nm",
                "new hampshire",
                "nh",
                "puerto rico",
                "pr",
                "vermont",
                "vm",
                "maine",
                "nebraska",
                "west virginia",
                "wv",
                "hawaii",
                "south dakota",
                "sd"
                "montana",
                "guam",
                "north dakota",
                "wyoming",
                "alaska",
                "ak",
                "virgin islands",
                "northern mariana islands",
            ],
        "ontnewyork":
            [
              "new york",
              "nyc"
            ],
        "ontangry":
            [
                "angry",
                "mad",
                "terrifying",
                "anger"
            ],
        "onteating":
            [
                "eat",
                "eating",
                "feasting",
                "feast",
                "food",
                "nutrition",
                "vitamins",
                "calorie",
                "calories"
                "hungry",
                "binge",
                "binge-eating"
            ],
        "onteatingtoolittle":
            [
                "little",
                "enough",
                "hungry",
                "malnourished",
                "nourished",
                "small",
                "skinny",
                "wee",
                "bite-sized",
                "bitesized",
                "mini",
                "tiny"
            ],
        "onteatingtoomuch":
            [
                "lot",
                "indulge",
                "binge",
                "binging",
                "binge-eating",
                "too",
                "much",
                "bad",
                "overeat",
                "overeating",
                "over-eating",
                "feasting",
                "feast"
            ],
        "onthotline":
            [
                "die",
                "kill",
                "murder",
                "commit",
                "suicide"
            ],
        "ontunsure":
            [
                "unsure",
                "dunno",
                "uncertain",
                "not",
                "idk",
                "don't",
                "know",
                "don't know",
                "no idea",
                "confused",
                "confuse"
            ],
        "ontwork":
            [
                "work",
                "job",
                "money",
                "pay",
                "income",
                "Income",
                "money",
                "cash",
                "paycheck",
                "bills"
            ],
        "ontclubs":
            [
                "club",
                "Club",
                "sport",
                "Sport",
                "team",
                "Team",
                "group",
                "Group",
                "extracurricular",
                "Extracurricular",
                "activity",
                "Activity",
                "watch",
                "relax",
                "chill",
                "netflix",
                "movie",
                "movies",
                "hulu"
            ],
        "ontfamily":
            [
                "family",
                "parent",
                "sister",
                "brother",
                "kid",
                "child",
                "sibling",
                "cousin",
                "dad",
                "mom",
                "father",
                "mother",
                "Parent",
                "Family",
                "PARENTS",
                "cousin",
                "uncle",
                "nephew",
                "aunt",
                "grandparents",
                "grandma",
                "grandpa",
                "grandmother",
                "grandfather",
                "greatgrandfather",
                "maternal",
                "removed"
            ],
        "ontsad":
            [
                "sad",
                "down",
                "unhappy",
                "depressed",
                "depressing",
                "lost",
                "purposeless"
                "blue",
                "dumps",
                "gross",
                "bad",
                "sorrow",
                "sorrowful",
                "regretful",
                "downcast",
                "heavy",
                "miserable",
                "gloom",
                "gloomy",
                "low-spirited",
                "broken-hearted",
                "broken",
                "low",
                "wretched",
                "desolate",
                "crestfallen",
                "mournful",
                "doleful",
                "mourn",
                "mourning",
                "despondent",
                "out of sorts",
                "dejected",
                "awful",
                "inconsolable",
                "falling",
                "apart",
                "broken",
                "fell"
            ],
        "ontbadclub":
            [
                "resume",
                "looks",
                "appears",
                "not",
                "dunno",
                "don't",
                "Dunno",
                "no idea",
                "don't know",
                "not sure",
                "unsure",
                "idk",
                "Resume",
                "Idk"
            ],
        "ontfunclub":
            [
                "fun",
                "enjoy",
                "destress",
                "relaxing",
                "entertaining",
                "socializing",
                "friends",
                "entertain",
                "relax",
                "people",
                "social",
                "friend",
                "Fun",
                "great",
                "calming",
                "calm",
                "invigorate",
                "invigorating",
                "chill",
                "laid back",
                "vibe",
                "amusing",
                "amuse",
                "break"
            ],
        "onttired":
            [
                "hours",
                "shifts",
                "shift",
                "tired",
                "fatigue",
                "fatigued",
                "sleeping",
                "exhausted",
                "sleep",
                "too",
                "exhaust",
                "worn",
                "overtired",
                "weary",
                "sleepy",
                "drowsy",
                "wearied",
                "sapped",
                "dog-tired",
                "spent",
                "drained",
                "debilitated",
                "prostrate",
                "enervated",
                "enervate",
                "jaded",
                "dead",
                "deadbeat",
                "shattered",
                "burnt",
                "knackered",
                "pooped"
            ],
        "ontschool":
            [
                "grades",
                "midterm",
                "final",
                "college",
                "exam",
                "school",
                "class",
                "test",
                "course",
                "balance",
                "balancing"
                "Grades",
                "Midterm",
                "Final",
                "College",
                "Exam",
                "Test",
                "study",
                "Study",
                "course",
                "studying",
                "professor",
                "teacher",
                "canvas",
                "assignment",
                "assignments"
            ],
        "ontemotion":
            [
                "ontnegative",
                "onpositive",
                "ontneutral",
                "ontunexpected"
            ],
        "ontnegative":
            [
                "anger",
                "disgust",
                "sadness",
                "fear",
                "bad",
                "scared",
                "scare",
                "scary",
                "onttired",
                "ontschool",
                "ontsad",
                "ontfamily",
                "ontdunno",
                "ontwork",
                "ontunsure",
                "lonely",
                "loneliness",
                "alone",
                "isolated",
                "sick",
                "fever",
                "corona",
                "coronavirus",
                "worried",
                "worry",
                "worrying",
                "not"
            ],
        "ontpositive":
            [
                "happiness",
                "happy",
                "Happy",
                "joy",
                "love",
                "great",
                "euphoria",
                "euphoric",
                "super",
                "best",
                "amazing",
                "amaze",
                "amazed",
                "gold",
                "luck",
                "good",
                "positive",
                "radiated",
                "radiating",
                "delight",
                "delighted",
                "fantastic",
                "ecstatic",
                "generous",
                "loving",
                "grateful",
                "loved"
            ],
        "ontneutral":
            [
                "good",
                "ok",
                "fine",
                "okay",
                "neutral",
                "okay",
                "nothing",
                "don\'t care",
                "dont care",
                "bored",
                "boring",
                "bore"
            ],
        "ontunexpected":
            [
                "fear",
                "Fear",
                "surprise",
                "Surprise",
                "startle",
                "jumped",
                "startled",
                "jump",
                "scare",
                "scared",
                "fright",
                "frightened",
                "terror",
                "terrorized",
                "terrorizing",
                "frightening",
                "panic",
                "panicked",
                "panicking",
                "alarm",
                "alarmed",
                "anxious",
                "anxiety",
                "feared",
                "jumped"
            ],
        "ontperception":
            [
                "control",
                "Control",
                "inability",
                "unable",
                "can't",
                "cant",
                "Can't",
                "Cant",
                "powerless",
                "Powerless",
                "lack"
            ],
        "ontaffirm":
            [
                "yes",
                "yea",
                "Yea",
                "yeah",
                "yep",
                "mhm",
                "mmhmm",
                "mmhm",
                "mhmm",
                "okay",
                "ok",
                "sure",
                "alright",
                "i know",
                "sure",
                "noted",
                "agree",
                "great",
                "good",
                "understood",
                "understand",
                "proceed",
                "yup"
            ],
        "ontnegate":
            [
                "no",
                "nah",
                "nope",
                "No",
                "NO",
                "Nah",
                "NAH",
                "Nope",
                "NOPE",
                "na",
                "Na",
                "nah",
                "not at all",
                "disagree"
            ],
        "ontbecause":
            [
                "because",
                "since",
                "thus",
                "hence"
            ],
        ########## confrontation branch ontologies ##############
        "ontconfrontation":
            [
                "argument",
                "fight",
                "dispute",
                "disagreement",
                "physical",
                "yelling",
                "yelled",
                "yell",
                "name-calling",
                "screaming",
                "scream",
                "confront",
                "confronted",
                "confrontation"
            ],
        ### anger ontologies ###
        "ontanger":
            [
                "ontcontrol",
                "ontinability",
                "ontinevitable",
                "ontavoidable",
                "onttried",
                "ontfriend"
            ],
        "ontcontrol":
            [
                "control",
                "controlling",
                "controlled",
                "inflexible"
            ],
        "ontinevitable":
            [
                "inevitable"
            ],
        "ontavoidable":
            [
                "avoidable",
                "avoid",
                "ran from",
                "avoided"
            ],
        "onttried":
            [
                "tried",
                "try",
                "trying"
            ],
        "ontfriend":
            [
                "friend",
                "friends"
            ],
        "ontshorttime":
            [
                "yesterday",
                "today",
                "day",
                "days",
                "week",
                "recent",
                "recently"
            ]
    }
}
knowledge = KnowledgeBase()
knowledge.load_json(ontology)
df = DialogueFlow(State.START, initial_speaker=DialogueFlow.Speaker.SYSTEM, kb=knowledge)

df.add_system_transition(State.START, State.PROMPT, '"Hi, how are you feeling today?"')

# The first user response feeling
df.add_user_transition(State.PROMPT, State.First_feeling_positive, '[$positive=#ONT(ontpositive)]')
df.add_user_transition(State.PROMPT, State.First_feeling_negative, '[$negative=#ONT(ontnegative)]')
####### Move to anger branch ##########################
df.add_user_transition(State.PROMPT, State.ANGER1, '[$confrontation=#ONT(ontangry)]')
####### Move to confrontation branch ##########################
df.add_user_transition(State.PROMPT, State.confrontation_answer,
                       '[$confrontation=#ONT(ontconfrontation)]')

# Moves to corona branch
df.set_error_successor(State.PROMPT, State.corona_prompt)

# Feeling Positive
df.add_system_transition(State.First_feeling_positive, State.First_positive_prompt,
                         '"That\'s great, anything interesting?"')

### small conversation branch for a positive response
df.add_user_transition(State.First_positive_prompt,State.First_positive_answer,'[$thing=#POS(verb)]')
df.set_error_successor(State.First_positive_prompt,State.First_positive_end)

df.add_system_transition(State.First_positive_answer,State.First_positive_reply,'"Were with anyone when you were"$thing"?"')
df.add_system_transition(State.First_positive_end,State.First_positive_ending,'"Cool, have a good day!"')

df.add_user_transition(State.First_positive_reply,State.First_positive_alone,"#ONT(ontnegate)")
df.set_error_successor(State.First_positive_reply,State.First_positive_end2)
df.add_system_transition(State.First_positive_end2,State.First_positive_ending2,'"Right on!"')

df.set_error_successor(State.First_positive_ending,error_successor=State.First_positive_ending)
df.set_error_successor(State.First_positive_ending2,error_successor=State.First_positive_ending2)


# Feeling Negative

df.add_system_transition(State.First_feeling_negative, State.First_negative_prompt,
                         '[!"What\'s been making you feel"$negative"?"]')

####### Move to confrontation branch ##########################
df.add_user_transition(State.First_negative_prompt, State.confrontation_answer,
                       '[$confrontation=#ONT(ontconfrontation)]')

####### Move to anger branch ##########################
df.add_user_transition(State.First_negative_prompt, State.ANGER1, '[$confrontation=#ONT(ontangry)]')

#Angela transitions
df.add_user_transition(State.First_negative_prompt, State.corona_prompt, '[$conju=#ONT(ontcorona)]')
df.add_user_transition(State.First_negative_prompt, State.school_prompt, "[$response=#ONT(ontschool)]")
df.add_user_transition(State.First_negative_prompt, State.family_prompt, "[$response=#ONT(ontfamily)]")
df.add_user_transition(State.First_negative_prompt, State.work_prompt, "[$response=#ONT(ontwork)]")
# df.add_user_transition(State.First_negative_prompt, State.eating_prompt, "[$response=#ONT(onteating)]")

#Error state foes to corona
df.set_error_successor(State.First_negative_prompt, State.corona_prompt)


#################################################

### ANGER BRANCH ###

df.add_system_transition(State.ANGER1, State.QUESTION1,'"Is there a person/activity that comes to mind that may cause you anger? "')
df.add_system_transition(State.ANGER2, State.QUESTION2,'"Do you think getting angry was or was not inevitable? "')

# U4 POSSIBLE BRANCHES DEPENDING ON USER RESPONSE

df.add_user_transition(State.QUESTION1, State.PERSON, "[$person=#ONT(ontfamily,ontfriend)]")
df.add_user_transition(State.QUESTION1, State.ACTIVITY,'[$activity=#POS(verb)]')
df.set_error_successor(State.QUESTION1, State.ANGER2)

df.add_user_transition(State.QUESTION2, State.INEVITABLE,"[$inevitable=#ONT(ontinevitable,ontaffirm)]")
df.add_user_transition(State.QUESTION2, State.AVOIDABLE,"[$avoidable=#ONT(ontavoidable,ontnegate)]")
# changed from generic error state
df.set_error_successor(State.QUESTION2, State.INEVDESCRIP)

# S5 TRANSITIONS
df.add_system_transition(State.PERSON, State.IDENTIFYPERSON, '[!"Thank you for telling me about your hard time dealing with "$person". \n Have you tried or resolving this issue directly with "$person"? \n Please feel free to tell me exactly how you went about fixing this relationship if you have already tried."]')
df.set_error_successor(State.IDENTIFYPERSON,State.confrontation_cause_self)

df.add_system_transition(State.ACTIVITY, State.IDENTIFYACTIVITY, '[!"Thank you for telling me about your difficult time engaging with that " $activity ". \n Have you tried talking to your friends or family about this " $activity"? \n Let me know explicitly whether you spoke to either your friends or family."]')
df.set_error_successor(State.IDENTIFYACTIVITY,State.family_self_pressure_y)

df.add_system_transition(State.INEVITABLE, State.INEVDESCRIP,'"Would you say that your anger partly stems from lack of control over your situation?"')
df.add_user_transition(State.INEVDESCRIP,State.confrontation_treatment_relaxedbreathing,"#ONT(ontaffirm)")
df.set_error_successor(State.INEVDESCRIP,State.confrontation_treatment_journaling)

df.add_system_transition(State.AVOIDABLE, State.AVOIDDESCRIP,'"Did you feel more inability or control over trying to avoid the situation"')
df.set_error_successor(State.AVOIDDESCRIP,State.confrontation_treatment_journaling)

# 4 possible responses
# it identifies a person
# they talk about an an activity
# there is a lack of control (yes/no) mindfulness/journaling
# they could have / could not have avoided situation


### END OF ANGER BRANCH ###


# angela's stuff
####################################################################################

#Club activities
df.add_system_transition(State.school_prompt, State.club_prompt,
                         '"Oh man, I feel that. I\'ve been there too. Are you in any clubs by chance?"')
df.add_user_transition(State.club_prompt, State.club_answer, "[$club=#ONT(ontclubs)]")
df.set_error_successor(State.club_prompt, State.club_enjoy_n)

df.add_system_transition(State.club_answer,State.club_enjoy,'"Are you enjoying the "$club" that you\'re in?"')
df.add_user_transition(State.club_enjoy,State.club_enjoy_y,"#ONT(ontaffirm)")
df.set_error_successor(State.club_enjoy,State.club_enjoy_n)

df.add_system_transition(State.club_enjoy_y,State.EXIT,'"That\'s nice!"')

df.add_system_transition(State.club_enjoy_n, State.EXIT,
                         '"There are plenty of clubs around, I think you should find a club that you enjoy."')

#add further depth if necessary

#family Branch

df.add_system_transition(State.family_prompt, State.family_answer,
                         '"That\'s tough, do you feel like your family places pressure on you?"')
df.add_user_transition(State.family_answer, State.family_self, "#ONT(ontnegate)")
df.set_error_successor(State.family_answer, State.family_talk)

df.add_system_transition(State.family_talk, State.family_talk_answer, '"Have you talked to them about this stuff?"')
df.add_user_transition(State.family_talk_answer, State.family_talk_end, "#ONT(onaffirm)")
df.set_error_successor(State.family_talk_answer, State.family_talk_suggestion)

#havent talked with family
df.add_system_transition(State.family_talk_suggestion, State.EXIT,
                         '"I feel like you should talk to them. Start with something small, and work your way though. '
                         'Take your time, and if it gets heated, it means you\'re on the right track."')
#already talked with family
df.add_system_transition(State.family_talk_end, State.EXIT, '"Way to go!"')

#pressure on self?
df.add_system_transition(State.family_self, State.family_self_pressure,
                         '"Do you place pressure on yourself?"') #->activities
df.add_user_transition(State.family_self_pressure, State.family_talk_end, "#ONT(ontnegate)")
df.set_error_successor(State.family_self_pressure, State.family_self_pressure_y)

df.add_system_transition(State.family_self_pressure_y, State.family_self_pressure_college,
                         '"It\'s not good to pressure yourself too much. Are you in college by any chance?"')
df.add_user_transition(State.family_self_pressure_college, State.school_prompt, "#ONT(ontaffirm)")
df.set_error_successor(State.family_self_pressure_college, State.family_self_pressure_job)

df.add_system_transition(State.family_self_pressure_job, State.family_self_pressure_job_answer,
                         '"Do you have a job?"')
df.add_user_transition(State.family_self_pressure_job_answer, State.work_prompt, "#ONT(ontaffirm)")
df.set_error_successor(State.family_self_pressure_job_answer, State.A111)




# job branch
df.add_system_transition(State.work_prompt, State.work_answer, '"Where do you work?"')
df.set_error_successor(State.work_answer, State.work_enjoy)

df.add_system_transition(State.work_enjoy, State.work_enjoy_yn, '"That\'s cool! Do you enjoy your job?"')
df.add_user_transition(State.work_enjoy_yn, State.work_enjoy_y, "#ONT(ontaffirm)")
df.set_error_successor(State.work_enjoy_yn, State.work_enjoy_n)

df.add_system_transition(State.work_enjoy_y, State.EXIT,
                         '"I\'m glad you enjoy it!"')

df.add_system_transition(State.work_enjoy_n, State.work_stress_y, "Is it stressful?")
df.add_user_transition(State.work_stress_y, State.work_stress_not, "#ONT(ontnegate)")
#recommends mindfulness
df.set_error_successor(State.work_stress_y, State.confrontation_treatment_relaxedbreathing)

df.add_system_transition(State.work_stress_not, State.EXIT, '"It\'s awesome that you found a job that isn\'t stressful. More power to ya!"')


# eating
# df.add_system_transition(State.eating_prompt, State.eating_answer, '"Uh oh, have you been eating too much or too little?"')
# df.add_user_transition(State.eating_answer, State.eating_toomuch, "#ONT(ontnegate)")
# df.add_user_transition(State.eating_answer, State.eating_toolittle, "#ONT(ontnegate)")
# df.add_user_transition(State.eating_answer, State.eating_ambiguous)
#
# df.add_system_transition(State.eating_ambiguous, State.EXIT,
#                          '"Eating regularly and healthily is a very important part of life. Please stay healthy by eating well."')
#
#
#
# df.add_system_transition(State.U4E1, State.P4E1A,
#                          '"Haha, weight gain is common in college students. Do you think it actually harms you, though?"')
#
# df.add_system_transition(State.U4E1A2, State.P4E1A2A,
#                          '"You may eat excessively because you are stressed. Has anything been stressing you out recently?"')
#
# df.add_system_transition(State.U4E1A1, State.P4E1A2B,
#                          '"Haha, I think you\'re doing just fine. Your body is just growing, as it should be. "')
#
# df.add_system_transition(State.U4E2, State.P4E2A,
#                          '"Oh no, that\'s a problem! You need to eat. Are you on a meal plan?"')
#
# df.add_system_transition(State.U4E2A1, State.P4E2A1A,
#                          '" I think you need to make more of an effort to go to dining halls. They have very healthy options. Can you try that?"')
#
# df.add_system_transition(State.U4E2A1A2, State.P4C2B1A2A2A,
#                          '"I think this inability to take action holds you back. Why don\'t you brace yourself to take action and then we can talk again next time?"')
#
# df.add_system_transition(State.U4E2A2, State.P4E2A2A,
#                          '"Then you need to start grocery shopping for yourself. Is money a problem?"')
#
# df.add_system_transition(State.U4E2A2A2, State.P4E2A2A2A,
#                          '"You should talk to your career center about finding a job. You need to eat. Do you think you can look for a job?"')
#
# df.add_system_transition(State.U4E2A2A1, State.P4E2A2A1A, '"Good, then you should go grocery shopping more often."')




########### Confrontation Branch (Yuewu) ################################
df.add_system_transition(State.confrontation_answer, State.confrontation_cause_prompt,
                         '"How did the"$confrontation"start?"')
df.set_error_successor(State.confrontation_answer, State.confrontation_cause_self)
# -> argument branchag

df.add_system_transition(State.confrontation_cause_error, State.confrontation_noCatch_self_prompt,
                         '"Do you feel like it had something to do with what you did?"')
df.add_user_transition(State.confrontation_noCatch_self_prompt, State.confrontation_cause_self, "#ONT(ontaffirm)")
df.set_error_successor(State.confrontation_noCatch_self_prompt, State.confrontation_cause_self)

##### argument branch
df.add_user_transition(State.confrontation_cause_prompt, State.confrontation_cause_self, '[{I,i}]')
df.add_system_transition(State.confrontation_cause_self, State.confrontation_usual_prompt,
                         '"Is this something that has happened before?"')
# -> usual

df.add_user_transition(State.confrontation_cause_prompt, State.confrontation_cause_other, '[$person=#POS(propn)]')
df.add_system_transition(State.confrontation_cause_other, State.confrontation_intentional_yn,
                         '"Do you think it was intentional?"')
# -> argument motive

df.set_error_successor(State.confrontation_cause_prompt, State.confrontation_cause_self)
# -> usual


##### argument motive
df.add_user_transition(State.confrontation_intentional_yn, State.confrontation_intentional_answer, "#ONT(ontaffirm)")
# -> exposure
df.set_error_successor(State.confrontation_intentional_yn, State.confrontation_intentional_answer)
# -> advice

df.add_system_transition(State.confrontation_intentional_answer, State.confrontation_intentional_motive_prompt,
                         '"Why do you think they did that?"')
df.add_user_transition(State.confrontation_intentional_motive_prompt, State.confrontation_intentional_motive_answer,
                       '[{because,Because} $reason=/.*/]')
df.set_error_successor(State.confrontation_intentional_motive_prompt, State.confrontation_cause_self)
# -> usual

df.add_system_transition(State.confrontation_intentional_motive_answer, State.confrontation_intentional_motive_yn,
                         '"Do you think it\'s good to argue because"$reason"?"')
df.add_user_transition(State.confrontation_intentional_motive_yn, State.confrontation_exposure_prompt,
                       "#ONT(ontaffirm)")
# -> usual

df.set_error_successor(State.confrontation_intentional_motive_yn,State.confrontation_treatment_journaling)
# -> advice


##### usual
df.add_user_transition(State.confrontation_usual_prompt, State.confrontation_usual_yn, "#ONT(ontaffirm)")
df.add_system_transition(State.confrontation_usual_yn, State.confrontation_usual_when,
                         '"When was the last time this has happened?"')

df.add_user_transition(State.confrontation_usual_when, State.confrontation_usual_when1, "#ONT(ontshorttime)")
df.add_user_transition(State.confrontation_usual_when, State.confrontation_advice_yn, '[never]')
df.set_error_successor(State.confrontation_usual_when, State.confrontation_usual_when_answer)


df.add_system_transition(State.confrontation_usual_when1,State.confrontation_usual_when_answer1,
                         '"So, it\s fairly recent, then?"')
df.add_user_transition(State.confrontation_usual_when_answer1, State.confrontation_usual_when2, "#ONT(ontaffirm)")
df.set_error_successor(State.confrontation_usual_when_answer1,State.confrontation_usual_when_answer)

df.add_system_transition(State.confrontation_usual_when2,State.confrontation_usual_when_answer2,
                         '"Ah, gotcha. Any chance of reconciliation?"')
df.add_user_transition(State.confrontation_usual_when_answer2, State.confrontation_usual_when3, "#ONT(ontaffirm)")
df.set_error_successor(State.confrontation_usual_when_answer2, State.confrontation_advice_calmer_answer)

df.add_system_transition(State.confrontation_usual_when3,State.confrontation_usual_when_answer3,
                         '"That\'s great to hear. People have their"$confrontation"s, but it\'s always good to make up afterwards."')
df.set_error_successor(State.confrontation_usual_when_answer3, State.ENDwGREET)


# df.add_user_transition(State.confrontation_usual_when,State.confrontation_usual_when_answer,"$time=#NER(date)")
# -> exposure (because no time catch)
df.add_system_transition(State.confrontation_usual_when_answer, State.confrontation_usual_when_yn,
                         '"Have you had a"$confrontation"?"often?"')

df.add_user_transition(State.confrontation_usual_when_yn, State.confrontation_advice_yn, "#ONT(ontaffirm)")
# -> advice
df.set_error_successor(State.confrontation_usual_when_yn, State.confrontation_exposure_end)
# -> exposure

##### advice
df.add_system_transition(State.confrontation_advice_yn, State.confrontation_advice_yn_answer,
                         '"Could I offer you some advice?"')
df.add_user_transition(State.confrontation_advice_yn_answer, State.confrontation_advice_calmer_yn, "#ONT(ontaffirm)")
df.set_error_successor(State.confrontation_advice_yn_answer, State.ENDwGREET)
# -> END
df.add_system_transition(State.confrontation_advice_calmer_yn, State.confrontation_advice_calmer_answer,
                         '"Okay, do you think a calmer attitude would have mitigated the"$confrontation"?"')
df.set_error_successor(State.confrontation_advice_calmer_answer, State.confrontation_treatment_relaxedbreathing)


##### exposure
df.add_system_transition(State.confrontation_exposure_prompt, State.confrontation_exposure_answer,
                         '"Why do you spend time with them?"')
df.add_user_transition(State.confrontation_exposure_answer, State.confrontation_exposure_why,
                       '[{because,Because} $reason=/.*/]')
df.set_error_successor(State.confrontation_exposure_answer, State.confrontation_exposure_why)

df.add_system_transition(State.confrontation_exposure_why, State.confrontation_exposure_yn,
                         '"Do you think you\'ll talk with them again soon?"')

df.add_user_transition(State.confrontation_exposure_yn, State.confrontation_treatment_relaxedbreathing, "#ONT(ontaffirm)") ### Relaxed breathing
df.add_user_transition(State.confrontation_exposure_yn, State.confrontation_exposure_end, "#ONT(ontnegate)")
# -> advice
df.set_error_successor(State.confrontation_exposure_yn, State.confrontation_exposure_end)

df.add_system_transition(State.confrontation_exposure_end, State.END,
                         '"I think it\'s best to spend some time cooling off after a"$confrontation"."')

##### Treatment branch
### Relaxed breathing
df.add_system_transition(State.confrontation_treatment_relaxedbreathing,State.confrontation_treatment_relaxedbreathing_response,
                         '"Based on your responses, I would recommend an exercise in mindfulness. Is that something you\'d be interested in? "')
df.add_user_transition(State.confrontation_treatment_relaxedbreathing_response,State.confrontation_treatment_relaxedbreathing2,"#ONT(ontaffirm)")
df.set_error_successor(State.confrontation_treatment_relaxedbreathing_response,State.ENDwGREET)
df.add_system_transition(State.confrontation_treatment_relaxedbreathing2,State.confrontation_treatment_relaxedbreathing_response2,
                         '"Mindfulness is the practice of taking a different perspective on various things, often in combination with breathing exercises and meditation. '
                         'Things that mindfulness teaches are: Paying close attention to what is going on around you. Participating without being self-conscious, '
                         'Taking a non-judgmental stance, Focusing on the moment without distraction from other ideas or events, '
                         'and Doing what works rather than second-guessing yourself."')
### Journaling
df.add_system_transition(State.confrontation_treatment_journaling,State.confrontation_treatment_relaxedbreathing_response,
                         '"Based on your responses, I would recommend is journaling. Is that something you\'d be interested in? "')
df.add_user_transition(State.confrontation_treatment_journaling_response,State.confrontation_treatment_journaling2,"#ONT(ontaffirm)")
df.set_error_successor(State.confrontation_treatment_journaling_response,State.ENDwGREET)
df.add_system_transition(State.confrontation_treatment_journaling2,State.confrontation_treatment_journaling_response2,
                         '"Journaling is the practice of writing for therapeutic purposes. Often done with specific exercises, '
                         'journaling is helpful in identifying and processing stressful or difficult events in a persons life."')
# -> END

# ENDwGREET
df.add_system_transition(State.ENDwGREET, State.EXIT, '"Alright, have a good day!"')

#############ANGELA
df.add_system_transition(State.corona_prompt, State.S2, '"Haha, the world is pretty crazy now isn\'t it? Are you in the US?"')
df.add_user_transition(State.S2, State.U7, "#ONT(ontaffirm)")
df.add_user_transition(State.S2, State.U8, "#ONT(ontnegate)")
df.add_system_transition(State.U7, State.S1, '"Which state are you in right now?"')
df.add_user_transition(State.S1, State.U1, "#ONT(ontnewjersey)")
df.add_user_transition(State.S1, State.U2, "#ONT(ontnewyork)")
df.add_user_transition(State.S1, State.U3, "#ONT(ontcalifornia)")
df.add_user_transition(State.S1, State.U4, "#ONT(ontmichigan)")
df.add_user_transition(State.S1, State.U5, "#ONT(ontbadstate)")
df.add_user_transition(State.S1, State.U6, "#ONT(ontokaystate)")
df.set_error_successor(State.S1,State.U8)
df.set_error_successor(State.S2,State.U8)
##### Error handle

#####

df.add_system_transition(State.U6, State.S3, '"Oh, I heard that corona not too bad there! How are you doing with social distancing?"')
df.add_system_transition(State.U5, State.S4, '"Yikes, I hear corona is spreading very quickly there. How are you doing with social distancing?"')
df.add_system_transition(State.U1, State.S5, '"Yikes, NJ is not a good place to be right now. How are you doing with social distancing?"')
df.add_system_transition(State.U2, State.S6, '"Yikes, NYC is very scary right now. How are you doing with social distancing?"')
df.add_system_transition(State.U3, State.S7, '"Not as bad as New York, but it seems to be spreading in California as well. How are you doing with social distancing?"')
df.add_system_transition(State.U4, State.S8, '"Yeah, I\'m personally surprised Michigan is up there with NY and NJ in coronavirus cases! How are you doing with social distancing?"')
df.add_system_transition(State.U8, State.S9, '"Well, how are you doing with social distancing?"')
df.add_user_transition(State.S3, State.U9, "[$checkin=#ONT(ontpositive,ontneutral)]")
df.add_user_transition(State.S3, State.U10, "[$checkin=#ONT(ontnegative)]")
df.add_user_transition(State.S4, State.U9, "[$checkin=#ONT(ontpositive,ontneutral)]")
df.add_user_transition(State.S4, State.U10, "[$checkin=#ONT(ontnegative)]")
df.add_user_transition(State.S8, State.U9, "[$checkin=#ONT(ontpositive,ontneutral)]")
df.add_user_transition(State.S8, State.U10, "[$checkin=#ONT(ontnegative)]")
df.add_user_transition(State.S7, State.U9, "[$checkin=#ONT(ontpositive,ontneutral)]")
df.add_user_transition(State.S7, State.U10, "[$checkin=#ONT(ontnegative)]")
df.add_user_transition(State.S6, State.U9, "[$checkin=#ONT(ontpositive,ontneutral)]")
df.add_user_transition(State.S6, State.U10, "[$checkin=#ONT(ontnegative)]")
df.add_user_transition(State.S5, State.U9, "[$checkin=#ONT(ontpositive,ontneutral)]")
df.add_user_transition(State.S5, State.U10, "[$checkin=#ONT(ontnegative)]")
df.add_user_transition(State.S9, State.U9, "[$checkin=#ONT(ontpositive,ontneutral)]")
df.add_user_transition(State.S9, State.U10, "[$checkin=#ONT(ontnegative)]")

#S3 - S9
df.set_error_successor(State.S3,State.U16)
df.set_error_successor(State.S4,State.U16)
df.set_error_successor(State.S5,State.U16)
df.set_error_successor(State.S6,State.U16)
df.set_error_successor(State.S7,State.U16)
df.set_error_successor(State.S8,State.U16)
df.set_error_successor(State.S9,State.U16)



df.add_system_transition(State.U9, State.S10, '"Well I\'m glad you\'re not suffering! What do you spend your free time doing?"')
df.add_system_transition(State.U10, State.S11, '"Oh no! I\'m sorry that the current events have affected your mental health. What have you been doing to keep busy?"')
df.add_user_transition(State.S10, State.U12, "[$checkin=#ONT(ontstillbusy)]")
df.add_user_transition(State.S10, State.U13, "[$checkin=#ONT(ontgoodactivities)]")
df.add_user_transition(State.S10, State.U14, "[$checkin=#ONT(ontbadactivities)]")
df.add_user_transition(State.S10, State.U15, "[$checkin=#ONT(ontwasteoftime)]")
df.set_error_successor(State.S10,State.U16)

# We're skipping back to therapy section S17 / S18 (comments can be deleted)
# error_state_activity
# therapy_lead_in
# therapy_lead_in_response
# df.set_error_successor(State.S10,State.error_state_activity)
# df.add_system_transition(State.error_state_activity,State.therapy_lead_in_response, '"How are you feeling right now?"')
# df.add_user_transition()

#States S11
df.add_user_transition(State.S11, State.U12, "[$checkin=#ONT(ontstillbusy)]")
df.add_user_transition(State.S11, State.U13, "[$checkin=#ONT(ontgoodactivities)]")
df.add_user_transition(State.S11, State.U14, "[$checkin=#ONT(ontbadactivities)]")
df.add_user_transition(State.S11, State.U15, "[$checkin=#ONT(ontwasteoftime)]")
df.set_error_successor(State.S11,State.U16)

#States S12
df.add_system_transition(State.U12, State.S12, '"Well, it\'s good that you\'re still busy but make sure you make time for yourself! Do you do any activities to relax?"')
df.add_user_transition(State.S12, State.U13, "[$checkin=#ONT(ontgoodactivities)]")
df.add_user_transition(State.S12, State.U15, "[$checkin=#ONT(ontwasteoftime)]")
df.add_user_transition(State.S12, State.U16, "[$checkin=#ONT(ontaffirm)]")
df.add_user_transition(State.S12, State.U17, "[$checkin=#ONT(ontnegate)]")
df.set_error_successor(State.S12,State.U16)

#States S13
df.add_system_transition(State.U16, State.S13, '"Well, what do you do to relax?"')
df.add_user_transition(State.S13, State.U13, "[$checkin=#ONT(ontgoodactivities)]")
df.add_user_transition(State.S13, State.U14, "[$checkin=#ONT(ontbadactivities)]")
df.add_user_transition(State.S13, State.U15, "[$checkin=#ONT(ontwasteoftime)]")
df.set_error_successor(State.S13,State.U30)

#States S14
df.add_system_transition(State.U17, State.S14, '"That\'s not good! I know that life feels like it\'s at a standstill right now, but you should still use your time wisely. Do you have any ideas for activities you could do?"')
df.add_user_transition(State.S14, State.U13, "[$checkin=#ONT(ontgoodactivities)]")
df.add_user_transition(State.S14, State.U14, "[$checkin=#ONT(ontbadactivities)]")
df.add_user_transition(State.S14, State.U15, "[$checkin=#ONT(ontwasteoftime)]")
df.add_user_transition(State.S14, State.U18, "[$checkin=#ONT(ontnegate)]")
df.set_error_successor(State.S14,State.U19)

#States U15
df.add_system_transition(State.U13, State.EXIT, '"That\'s a great way to spend your time! If you keep doing that, I think you\'ll be okay once this all passes. I would also suggest reminding yourself of everything you have to be grateful for."')
df.add_system_transition(State.U14, State.S18, '[!"Do you think"$checkin"can be part of a healthy life?"]')
df.set_error_successor(State.S18,State.U15)
df.add_system_transition(State.U15, State.EXIT, '"That\'s not the best way to spend your time, but I get that things are a little crazy right now. At least you\'re relaxed. "')
df.add_system_transition(State.U19, State.EXIT, '"Thanks for talking to me today! Hope we can talk again sometime."')


##S17 Therapy Section
##States used: U30, U31, S30
df.add_system_transition(State.U30, State.EXIT, '"Great to hear that and I think it\'s time to conclude our session. Thanks for talking to me today! Hope we can talk again sometime."')

#S18 Therapy section
df.add_user_transition(State.S18, State.U15, "[$affirm_healthy=#ONT(ontaffirm)]")
df.add_user_transition(State.S18,State.confrontation_treatment_relaxedbreathing, "[$negate_healthy=#ONT(ontnegate)]")
df.set_error_successor(State.S18,State.U15)


df.set_error_successor(State.EXIT,error_successor=State.EXIT)

if __name__ == '__main__':
    df.run(debugging=False)