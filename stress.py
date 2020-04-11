from emora_stdm import KnowledgeBase, DialogueFlow
from enum import Enum, auto
from emora_stdm import Macro


class n20(Macro):

    def run(self, ngrams, vars, args):
        positive = {
            'admirable', 'energetic', 'lucky',
            'affable', 'enjoyable', 'magnificent',
            'affectionate', 'enthusiastic', 'marvelous',
            'agreeable', 'euphoric', 'meritorious',
            'amazing', 'excellent', 'merry',
            'amiable', 'exceptional', 'mild-mannered',
            'amused', 'excited', 'nice',
            'amusing', 'extraordinary', 'noble',
            'animated', 'exultant', 'outstanding',
            'appreciative', 'fabulous', 'overjoyed',
            'astonishing', 'faithful', 'passionate',
            'authentic', 'fantastic', 'peaceful',
            'believable', 'fervent', 'placid',
            'benevolent', 'fortunate', 'pleasant',
            'blissful', 'friendly', 'pleasing',
            'bouncy', 'fun', 'pleasurable',
            'brilliant', 'genuine', 'positive',
            'bubbly', 'glad', 'praiseworthy',
            'buoyant', 'glorious', 'prominent',
            'calm', 'good', 'proud',
            'charming', 'good-humored', 'relaxed',
            'cheerful', 'good-natured', 'reliable',
            'cheery', 'gracious', 'respectable',
            'clever', 'grateful', 'sharp',
            'comfortable', 'great', 'sincere',
            'comical', 'happy', 'spirited',
            'commendable', 'heartfelt', 'splendid',
            'confident', 'honest', 'superb',
            'congenial', 'honorable', 'superior',
            'content', 'hopeful', 'terrific',
            'cordial', 'humorous', 'thankful',
            'courteous', 'incredible', 'tremendous',
            'dedicated', 'inspirational', 'triumphant',
            'delighted', 'jolly', 'trustworthy',
            'delightful', 'jovial', 'trusty',
            'dependable', 'joyful', 'truthful',
            'devoted', 'joyous', 'uplifting',
            'docile', 'jubilant', 'victorious',
            'dynamic', 'keen', 'vigorous',
            'eager', 'kind', 'virtuous',
            'earnest', 'laudable', 'vivacious',
            'easygoing', 'laughing', 'whimsical',
            'ebullient', 'likable', 'witty',
            'ecstatic', 'lively', 'wonderful',
            'elated', 'lovely', 'worthy',
            'emphatic', 'loving', 'zealous',
            'enchanting', 'loyal', 'zestful',
            'well', 'smooth', 'awesome',
            "not bad", "not too bad", "wasn't too bad",
            "wasn't bad", "isn't bad", "isn't too bad",
            "isn't very bad"
        }
        if 'neuroticsm' in vars.keys():
            vars['neuroticsm'] += 20
        else:
            vars['neuroticsm'] = 20
        return positive


class n_n20(Macro):

    def run(self, ngrams, vars, args):
        negative = {'afraid',
                    'bad',
                    'anxious',
                    'apprehensive',
                    'ashamed',
                    'cowardly',
                    'frightened',
                    'guilty',
                    'horrified',
                    'paralyzed',
                    'petrified',
                    'scared',
                    'shocked',
                    'shy',
                    'skittish',
                    'startled',
                    'terrified',
                    'terrorized',
                    'timid',
                    'troubled',
                    'tired',
                    'awful',
                    'terrible',
                    'worried',
                    'aggressive',
                    'bellicose',
                    'belligerent',
                    'combative',
                    'hawkish',
                    'merciless',
                    'presumptuous',
                    'pugnacious',
                    'ruthless',
                    'self-assertive',
                    'angry',
                    'enraged',
                    'exasperated',
                    'furious',
                    'incensed',
                    'indignant',
                    'livid',
                    'mad',
                    'outraged',
                    'wrathful',
                    'annoyed',
                    'asinine',
                    'bored',
                    'disgusted',
                    'dullish',
                    'dull',
                    'obtuse',
                    'peeved',
                    'riled',
                    'vexed',
                    'evil',
                    'abusive',
                    'baneful',
                    'contaminated',
                    'contemptible',
                    'corrupt',
                    'cruel',
                    'demonic',
                    'depraved',
                    'despicable',
                    'devilish',
                    'diabolic',
                    'ferocious',
                    'fiendish',
                    'fierce',
                    'heartless',
                    'hellish',
                    'infernal',
                    'inimical',
                    'malicious',
                    'nasty',
                    'nefarious',
                    'nether',
                    'perfidious',
                    'putrefied',
                    'savage',
                    'scrupulous',
                    'sinister',
                    'sneaky',
                    'spiteful',
                    'spoiled',
                    'tainted',
                    'treacherous',
                    'venal',
                    'vile',
                    'villainous',
                    'wicked',
                    'frustrated',
                    'balked',
                    'disappointed',
                    'discontented',
                    'foiled',
                    'thwarted',
                    'nervous',
                    'alarmed',
                    'anxious',
                    'apprehensive',
                    'cautious',
                    'concerned',
                    'confused',
                    'conspicuous',
                    'disturbed',
                    'doubtful',
                    'insecure',
                    'irritable',
                    'panicked',
                    'perturbed',
                    'suspicious',
                    'pathetic',
                    'affecting',
                    'agitating',
                    'lamentable',
                    'piteous',
                    'pitiful',
                    'poignant',
                    'stirring',
                    'touching',
                    'quarrelsome',
                    'blatant',
                    'boisterous',
                    'cantankerous',
                    'clamorous',
                    'conspicuously',
                    'contentious',
                    'cross',
                    'deafening',
                    'disagreeable',
                    'fretful',
                    'hysterical',
                    'jealous',
                    'litigious',
                    'mean',
                    'mean-spirited',
                    'militant',
                    'nasty',
                    'noisy',
                    'offensively',
                    'ornery',
                    'peevish',
                    'pugnacious',
                    'rambunctious',
                    'recalcitrant',
                    'renitent',
                    'roisterous',
                    'strident',
                    'testy',
                    'touchy',
                    'truculent',
                    'unpleasant',
                    'vociferous',
                    'sad',
                    'bleak',
                    'dejected',
                    'depressed',
                    'desolate',
                    'dingy',
                    'discouraged',
                    'dismal',
                    'doleful',
                    'dreary',
                    'forlornly',
                    'gloomy',
                    'glum',
                    'grievous',
                    'grim',
                    'heart',
                    'broken',
                    'lonely',
                    'lugubrious',
                    'melancholic',
                    'miserable',
                    'mopish',
                    'morose',
                    'mournful',
                    'poor',
                    'seamy',
                    'somber',
                    'sordid',
                    'sorrowful',
                    'sulky',
                    'sullen',
                    'temperamental',
                    'unfortunate',
                    'unhappy',
                    'wistful',
                    'wretched',
                    'stubborn',
                    'adamant',
                    'hardheaded',
                    'inflexible',
                    'obdurate',
                    'obstinate',
                    'relentless',
                    'unyielding',
                    'terrible',
                    'abhorrent',
                    'abominable',
                    'appalling',
                    'awful',
                    'bizarre',
                    'calamitous',
                    'dire',
                    'disastrous',
                    'dreadful',
                    'fearful',
                    'formidable',
                    'freakish',
                    'frightful',
                    'ghastly',
                    'grotesque',
                    'gruesome',
                    'heinous',
                    'horrible',
                    'horrid',
                    'lurid',
                    'odious',
                    'painful',
                    'terrifying',
                    'tragic',
                    'unctuous',
                    "not well",
                    "not very well",
                    "not so well",
                    "didn't go well",
                    "wasn't well",
                    "isn't good"
                    }
        if 'neuroticsm' in vars.keys():
            vars['neuroticsm'] -= 20
        else:
            vars['neuroticsm'] = -20
        return negative


class o40(Macro):

    def run(self, ngrams, vars, args):
        never = {
            "never",
            "never ever",
            "first time"
        }
        if 'openness' in vars.keys():
            vars['openness'] += 20
        else:
            vars['openness'] = 20
        return never


class n70(Macro):

    def run(self, ngrams, vars, args):
        often = {
            "always",
            "constantly",
            "frequently",
            "regularly",
            "often",
            "hourly",
            "daily",
            "weekly",
            "biweekly",
            "every month",
            "monthly",
            "every day",
            "everyday",
            "every hour"
        }
        if 'neuroticsm' in vars.keys():
            vars['neuroticsm'] += 70
        else:
            vars['neuroticsm'] = 70
        return often


class n40(Macro):

    def run(self, ngrams, vars, args):
        sometimes = {
            "sometimes",
            "occasionally",
            "infrequently",
            "seldom",
            "not often",
            "rarely",
            "hardly ever",
            "not so often",
            "not very often",
            "not too often",
            "not always",
            "not too frequently",
            "not so frequently",
            "not very frequently",
            "not constantly",
            "not too constantly",
            "don't constantly",
            "don't often",
            "don't frequently",
            "don't always",
            "from time to time",
            "once in a while",
            "quarterly",
            "yearly",
            "annually",
            "every quarter",
            "every semester",
            "every year",
            "rarely",
            "hardly ever"
        }
        if 'neuroticsm' in vars.keys():
            vars['neuroticsm'] += 40
        else:
            vars['neuroticsm'] = 40
        return sometimes


class n10(Macro):

    def run(self, ngrams, vars, args):
        never = {
            "never",
            "never ever",
            "first time"
        }
        if 'neuroticsm' in vars.keys():
            vars['neuroticsm'] += 10
        else:
            vars['neuroticsm'] = 10
        return never


class o_n20(Macro):

    def run(self, ngrams, vars, args):
        yes = {
            "yes",
            "Yes",
            "YES",
            "yeah",
            "yea",
            "sure",
            "Of Course",
            "of course",
            "Sure",
            "i guess",
            "i think so",
            "do"
        }
        if 'openness' in vars.keys():
            vars['openness'] -= 20
        else:
            vars['openness'] = -20
        return yes


class o_20(Macro):

    def run(self, ngrams, vars, args):
        no = {
            "no",
            "not really",
            "nope",
            "don't",
            "none",
            "No",
            "NO",
            "Nope",
            "nope",
            "Nah",
            "nah"
        }
        if 'openness' in vars.keys():
            vars['openness'] += 60
        else:
            vars['openness'] = 60
        return no


class o_20_1(Macro):

    def run(self, ngrams, vars, args):
        yes = {
            "yes",
            "Yes",
            "YES",
            "yeah",
            "yea",
            "sure",
            "Of Course",
            "of course",
            "Sure",
            "i guess",
            "i think so",
            "do"
        }
        if 'openness' in vars.keys():
            vars['openness'] += 60
        else:
            vars['openness'] = 60
        return yes


class o_n20_1(Macro):

    def run(self, ngrams, vars, args):
        no = {
            "no",
            "not really",
            "nope",
            "dont",
            "none",
            "No",
            "NO",
            "Nope",
            "nope",
            "Nah",
            "nah"
        }
        if 'openness' in vars.keys():
            vars['openness'] -= 20
        else:
            vars['openness'] = -20
        return no


class e80(Macro):

    def run(self, ngrams, vars, args):
        positive = {
            'admirable', 'energetic', 'lucky',
            'affable', 'enjoyable', 'magnificent',
            'affectionate', 'enthusiastic', 'marvelous',
            'agreeable', 'euphoric', 'meritorious',
            'amazing', 'excellent', 'merry',
            'amiable', 'exceptional', 'mild-mannered',
            'amused', 'excited', 'nice',
            'amusing', 'extraordinary', 'noble',
            'animated', 'exultant', 'outstanding',
            'appreciative', 'fabulous', 'overjoyed',
            'astonishing', 'faithful', 'passionate',
            'authentic', 'fantastic', 'peaceful',
            'believable', 'fervent', 'placid',
            'benevolent', 'fortunate', 'pleasant',
            'blissful', 'friendly', 'pleasing',
            'bouncy', 'fun', 'pleasurable',
            'brilliant', 'genuine', 'positive',
            'bubbly', 'glad', 'praiseworthy',
            'buoyant', 'glorious', 'prominent',
            'calm', 'good', 'proud',
            'charming', 'good-humored', 'relaxed',
            'cheerful', 'good-natured', 'reliable',
            'cheery', 'gracious', 'respectable',
            'clever', 'grateful', 'sharp',
            'comfortable', 'great', 'sincere',
            'comical', 'happy', 'spirited',
            'commendable', 'heartfelt', 'splendid',
            'confident', 'honest', 'superb',
            'congenial', 'honorable', 'superior',
            'content', 'hopeful', 'terrific',
            'cordial', 'humorous', 'thankful',
            'courteous', 'incredible', 'tremendous',
            'dedicated', 'inspirational', 'triumphant',
            'delighted', 'jolly', 'trustworthy',
            'delightful', 'jovial', 'trusty',
            'dependable', 'joyful', 'truthful',
            'devoted', 'joyous', 'uplifting',
            'docile', 'jubilant', 'victorious',
            'dynamic', 'keen', 'vigorous',
            'eager', 'kind', 'virtuous',
            'earnest', 'laudable', 'vivacious',
            'easygoing', 'laughing', 'whimsical',
            'ebullient', 'likable', 'witty',
            'ecstatic', 'lively', 'wonderful',
            'elated', 'lovely', 'worthy',
            'emphatic', 'loving', 'zealous',
            'enchanting', 'loyal', 'zestful',
            'well', 'smooth', 'awesome',
            "not bad", "not too bad", "wasn't too bad",
            "wasn't bad", "isn't bad", "isn't too bad",
            "isn't very bad", "happy"
        }
        if 'extroversion' in vars.keys():
            vars['extroversion'] = 80
        else:
            vars['extroversion'] = 80
        return positive


class e40(Macro):

    def run(self, ngrams, vars, args):
        negative = {
            'afraid',
            'bad',
            'anxious',
            'apprehensive',
            'ashamed',
            'cowardly',
            'frightened',
            'guilty',
            'horrified',
            'paralyzed',
            'petrified',
            'scared',
            'shocked',
            'shy',
            'skittish',
            'startled',
            'terrified',
            'terrorized',
            'timid',
            'troubled',
            'tired',
            'awful',
            'terrible',
            'worried',
            'aggressive',
            'bellicose',
            'belligerent',
            'combative',
            'hawkish',
            'merciless',
            'presumptuous',
            'pugnacious',
            'ruthless',
            'self-assertive',
            'angry',
            'enraged',
            'exasperated',
            'furious',
            'incensed',
            'indignant',
            'livid',
            'mad',
            'outraged',
            'wrathful',
            'annoyed',
            'asinine',
            'bored',
            'disgusted',
            'dullish',
            'dull',
            'obtuse',
            'peeved',
            'riled',
            'vexed',
            'evil',
            'abusive',
            'baneful',
            'contaminated',
            'contemptible',
            'corrupt',
            'cruel',
            'demonic',
            'depraved',
            'despicable',
            'devilish',
            'diabolic',
            'ferocious',
            'fiendish',
            'fierce',
            'heartless',
            'hellish',
            'infernal',
            'inimical',
            'malicious',
            'nasty',
            'nefarious',
            'nether',
            'perfidious',
            'putrefied',
            'savage',
            'scrupulous',
            'sinister',
            'sneaky',
            'spiteful',
            'spoiled',
            'tainted',
            'treacherous',
            'venal',
            'vile',
            'villainous',
            'wicked',
            'frustrated',
            'balked',
            'disappointed',
            'discontented',
            'foiled',
            'thwarted',
            'nervous',
            'alarmed',
            'anxious',
            'apprehensive',
            'cautious',
            'concerned',
            'confused',
            'conspicuous',
            'disturbed',
            'doubtful',
            'insecure',
            'irritable',
            'panicked',
            'perturbed',
            'suspicious',
            'pathetic',
            'affecting',
            'agitating',
            'lamentable',
            'piteous',
            'pitiful',
            'poignant',
            'stirring',
            'touching',
            'quarrelsome',
            'blatant',
            'boisterous',
            'cantankerous',
            'clamorous',
            'conspicuously',
            'contentious',
            'cross',
            'deafening',
            'disagreeable',
            'fretful',
            'hysterical',
            'jealous',
            'litigious',
            'mean',
            'mean-spirited',
            'militant',
            'nasty',
            'noisy',
            'offensively',
            'ornery',
            'peevish',
            'pugnacious',
            'rambunctious',
            'recalcitrant',
            'renitent',
            'roisterous',
            'strident',
            'testy',
            'touchy',
            'truculent',
            'unpleasant',
            'vociferous',
            'sad',
            'bleak',
            'dejected',
            'depressed',
            'desolate',
            'dingy',
            'discouraged',
            'dismal',
            'doleful',
            'dreary',
            'forlornly',
            'gloomy',
            'glum',
            'grievous',
            'grim',
            'heart',
            'broken',
            'lonely',
            'lugubrious',
            'melancholic',
            'miserable',
            'mopish',
            'morose',
            'mournful',
            'poor',
            'seamy',
            'somber',
            'sordid',
            'sorrowful',
            'sulky',
            'sullen',
            'temperamental',
            'unfortunate',
            'unhappy',
            'wistful',
            'wretched',
            'stubborn',
            'adamant',
            'hardheaded',
            'inflexible',
            'obdurate',
            'obstinate',
            'relentless',
            'unyielding',
            'terrible',
            'abhorrent',
            'abominable',
            'appalling',
            'awful',
            'bizarre',
            'calamitous',
            'dire',
            'disastrous',
            'dreadful',
            'fearful',
            'formidable',
            'freakish',
            'frightful',
            'ghastly',
            'grotesque',
            'gruesome',
            'heinous',
            'horrible',
            'horrid',
            'lurid',
            'odious',
            'painful',
            'terrifying',
            'tragic',
            'unctuous',
            "not well",
            "not very well",
            "not so well",
            "didn't go well",
            "wasn't well",
            "isn't good"
        }
        if 'extroversion' in vars.keys():
            vars['extroversion'] = 40
        else:
            vars['extroversion'] = 40
        return negative


class printS(Macro):

    def run(self, ngrams, vars, args):
        if 'neuroticsm' not in vars.keys():
            vars['neuroticsm'] = 0
        if 'extroversion' not in vars.keys():
            vars['extroversion'] = 0
        if 'openness' not in vars.keys():
            vars['openness'] = 0
        score = "Neuroticism: " + str(vars['neuroticsm']) + " Openness: " + str(
            vars['openness']) + " Extroversion: " + str(vars['extroversion'])
        return score

class det_ss(Macro):
    def run(self, ngrams, vars, args):
        if str(vars['S_S'])[0] is ('a' or "a" or 'e' or "e" or 'i' or "i" or 'o' or "o" or 'x' or "x"):
            return 'an '+str(vars['S_S'])
        else:
            return 'a '+str(vars['S_S'])


class result(Macro):

    def run(self, ngrams, vars, args):
        if 'neuroticsm' not in vars.keys():
            vars['neuroticsm'] = 0
        if 'extroversion' not in vars.keys():
            vars['extroversion'] = 0
        if 'openness' not in vars.keys():
            vars['openness'] = 0

        if vars['neuroticsm'] > 50 and vars['openness'] <= 50 and vars['extroversion'] <= 50:
            return 'I think you are a bit sensitive to stress, but I am sure that once you overcome the stress you will have a lot of fun! I wish you best of luck at the upcoming ' + str(vars['S_S']) +'! let me know how it goes!'
        if vars['neuroticsm'] > 50 and vars['openness'] <= 50 and vars['extroversion'] > 50:
            return 'You have such a bubbly personality. As long as you are being considerate and thoughtful about other people at the upcoming ' + str(vars['S_S']) +', I am sure you will have such a great time. Let me know how it goes!'
        if vars['neuroticsm'] > 50 and vars['openness'] > 50 and vars['extroversion'] <= 50:
            return 'I know you love stepping out of your comfort zone a lot. I am sure other people will love that side of you when they get to know you at the upcoming '+ str(vars['S_S']) +'. Let me know how it goes!'
        if vars['neuroticsm'] > 50 and vars['openness'] > 50 and vars['extroversion'] > 50:
            return 'You have a really unique personality type. I admire your creativity and expressiveness. I hope you have fun at the upcoming '+ str(vars['S_S']) +'! Let me know how it goes!'
        if vars['neuroticsm'] <= 50 and vars['openness'] <= 50 and vars['extroversion'] <= 50:
            return 'I feel so composed after talking to you. Whoever goes to the upcoming '+ str(vars['S_S']) +' would be so lucky to meet you and learn about your perspective on things. I hope you have fun at the upcoming '+ str(vars['S_S']) +'! let me know how it goes!'
        if vars['neuroticsm'] <= 50 and vars['openness'] <= 50 and vars['extroversion'] > 50:
            return 'You will become really popular at the upcoming '+ str(vars['S_S']) +' like you always do during any social situation. I hope that you get to become friends with people that are different from you at the upcoming '+ str(vars['S_S']) +'!'
        if vars['neuroticsm'] <= 50 and vars['openness'] > 50 and vars['extroversion'] <= 50:
            return 'Just be your adventurous self as you always do before. People will love that side of you when they get to know you. Let me know how the upcoming '+ str(vars['S_S']) +' goes!'
        if vars['neuroticsm'] <= 50 and vars['openness'] > 50 and vars['extroversion'] > 50:
            return 'I know you will not only enjoy the upcoming '+ str(vars['S_S']) +' but also naturally help everyone else to have a great time at the upcoming '+ str(vars['S_S']) +'! Let me know how it goes!'

class State(Enum):
    START = auto()
    PROMPT0 = auto()
    PROMPT0_re = auto()
    PROMPT0_err = auto() #user is stressed about nothing/unsure
    PROMPT0_other = auto()
    PROMPT0_a =auto()
    PROMPT0_b =auto()
    PROMPT1 = auto()
    PROMPT1_often = auto()
    PROMPT1_sometimes = auto()
    PROMPT1_never = auto()
    PROMPT1_err = auto()
    PROMPT2 = auto()
    PROMPT2_notbad = auto()
    PROMPT2_bad = auto()
    PROMPT2_err = auto()
    PROMPT3 = auto()
    PROMPT3_often = auto()
    PROMPT3_sometimes = auto()
    PROMPT3_never = auto()
    PROMPT3_err = auto()
    PROMPT4 = auto()
    PROMPT4_yes = auto()
    PROMPT4_no = auto()
    PROMPT4_err = auto()
    PROMPT5 = auto()
    PROMPT5_yes = auto()
    PROMPT5_no = auto()
    PROMPT5_err = auto()
    PROMPT6 = auto()
    PROMPT6_re = auto()
    PROMPT6_other = auto()
    PROMPT6_err = auto()
    PROMPT7 = auto()
    PROMPT7_err = auto()
    PROMPT7_ex = auto()
    PROMPT7_in = auto()
    PROMPT8 = auto()
    PROMPT8_chores = auto()
    PROMPT8_games = auto()
    PROMPT8_music = auto()
    PROMPT8_art = auto()
    PROMPT8_food = auto()
    PROMPT8_sports = auto()
    PROMPT8_dance = auto()
    PROMPT8_shopping = auto()
    PROMPT8_readwatch = auto()
    PROMPT8_onlinesocial = auto()
    PROMPT8_social = auto()
    PROMPT8_err = auto()
    PROMPT9 = auto()
    END = auto()
    SCORE = auto()


# TODO: create the ontology as needed
stress_dict = {
    "ontology":
        {
            "ontoften":
                [
                    "always",
                    "constantly",
                    "frequently",
                    "regularly",
                    "often",
                    "hourly",
                    "daily",
                    "weekly",
                    "biweekly",
                    "every month",
                    "monthly",
                    "every day",
                    "everyday",
                    "every hour"
                ],
            "ontsometimes":
                [
                    "sometimes",
                    "occasionally",
                    "infrequently",
                    "seldom",
                    "not often",
                    "rarely",
                    "hardly ever",
                    "not so often",
                    "not very often",
                    "not too often",
                    "not always",
                    "not too frequently",
                    "not so frequently",
                    "not very frequently",
                    "not constantly",
                    "not too constantly",
                    "don't constantly",
                    "don't often",
                    "don't frequently",
                    "don't always",
                    "from time to time",
                    "once in a while",
                    "quarterly",
                    "yearly",
                    "anually",
                    "every quarter",
                    "every semester",
                    "every year",
                    "rarely",
                    "hardly ever"
                ],
            "ontnever":
                [
                    "never",
                    "never ever",
                    "first time"
                ],
            "ontsocial":
                [
                    "party",
                    "hanging out",
                    "clubbing",
                    "mixer",
                    'drinking',
                    "gathering",
                    "debate",
                    "mock trial",
                    "a trip",
                    "a date",
                    "dating",
                    "dancing",
                    "night out",
                    "party",
                    "hangouts",
                    "hangout",
                    "presentation",
                    "presenting",
                    "public speaking",
                    "social event",
                    "conversation",
                    "meeting",
                    "performance",
                    "piano performance",
                    "dance performance",
                    "theatre performance",
                    "bowling",
                    "ice-skating",
                    "ice skating",
                    "ice cream social",
                    "icecream social"
                    "retreat",
                    "conversation",
                    "seminar",
                    "discussion",
                    "discussing",
                    "music festival",
                    "festival",
                    "carnival",
                    "dance",
                    "ice-cream social",
                ],
            "ontyes":
                [
                    "yes",
                    "Yes",
                    "YES",
                    "yeah",
                    "yea",
                    "sure",
                    "Of Course",
                    "of course",
                    "Sure",
                    "i guess",
                    "i think so",
                    "do"
                ],
            "ontno":
                [
                    "no",
                    "not really",
                    "nope",
                    "don't",
                    "none",
                    "No",
                    "NO",
                    "Nope",
                    "nope",
                    "Nah",
                    "nah"
                ],
            'ontpositive':
                [
                    'admirable', 'energetic', 'lucky',
                    'affable', 'enjoyable', 'magnificent',
                    'affectionate', 'enthusiastic', 'marvelous',
                    'agreeable', 'euphoric', 'meritorious',
                    'amazing', 'excellent', 'merry',
                    'amiable', 'exceptional', 'mild-mannered',
                    'amused', 'excited', 'nice',
                    'amusing', 'extraordinary', 'noble',
                    'animated', 'exultant', 'outstanding',
                    'appreciative', 'fabulous', 'overjoyed',
                    'astonishing', 'faithful', 'passionate',
                    'authentic', 'fantastic', 'peaceful',
                    'believable', 'fervent', 'placid',
                    'benevolent', 'fortunate', 'pleasant',
                    'blissful', 'friendly', 'pleasing',
                    'bouncy', 'fun', 'pleasurable',
                    'brilliant', 'genuine', 'positive',
                    'bubbly', 'glad', 'praiseworthy',
                    'buoyant', 'glorious', 'prominent',
                    'calm', 'good', 'proud',
                    'charming', 'good-humored', 'relaxed',
                    'cheerful', 'good-natured', 'reliable',
                    'cheery', 'gracious', 'respectable',
                    'clever', 'grateful', 'sharp',
                    'comfortable', 'great', 'sincere',
                    'comical', 'happy', 'spirited',
                    'commendable', 'heartfelt', 'splendid',
                    'confident', 'honest', 'superb',
                    'congenial', 'honorable', 'superior',
                    'content', 'hopeful', 'terrific',
                    'cordial', 'humorous', 'thankful',
                    'courteous', 'incredible', 'tremendous',
                    'dedicated', 'inspirational', 'triumphant',
                    'delighted', 'jolly', 'trustworthy',
                    'delightful', 'jovial', 'trusty',
                    'dependable', 'joyful', 'truthful',
                    'devoted', 'joyous', 'uplifting',
                    'docile', 'jubilant', 'victorious',
                    'dynamic', 'keen', 'vigorous',
                    'eager', 'kind', 'virtuous',
                    'earnest', 'laudable', 'vivacious',
                    'easygoing', 'laughing', 'whimsical',
                    'ebullient', 'likable', 'witty',
                    'ecstatic', 'lively', 'wonderful',
                    'elated', 'lovely', 'worthy',
                    'emphatic', 'loving', 'zealous',
                    'enchanting', 'loyal', 'zestful',
                    'well', 'smooth', 'awesome',
                    "not bad", "not too bad", "wasn't too bad",
                    "wasn't bad", "isn't bad", "isn't too bad",
                    "isn't very bad"
                ],
            'ontnegative':
                ['afraid',
                 'bad',
                 'anxious',
                 'apprehensive',
                 'ashamed',
                 'cowardly',
                 'frightened',
                 'guilty',
                 'horrified',
                 'paralyzed',
                 'petrified',
                 'scared',
                 'shocked',
                 'shy',
                 'skittish',
                 'startled',
                 'terrified',
                 'terrorized',
                 'timid',
                 'troubled',
                 'tired',
                 'awful',
                 'terrible',
                 'worried',
                 'aggressive',
                 'bellicose',
                 'belligerent',
                 'combative',
                 'hawkish',
                 'merciless',
                 'presumptuous',
                 'pugnacious',
                 'ruthless',
                 'self-assertive',
                 'angry',
                 'enraged',
                 'exasperated',
                 'furious',
                 'incensed',
                 'indignant',
                 'livid',
                 'mad',
                 'outraged',
                 'wrathful',
                 'annoyed',
                 'asinine',
                 'bored',
                 'disgusted',
                 'dullish',
                 'dull',
                 'obtuse',
                 'peeved',
                 'riled',
                 'vexed',
                 'evil',
                 'abusive',
                 'baneful',
                 'contaminated',
                 'contemptible',
                 'corrupt',
                 'cruel',
                 'demonic',
                 'depraved',
                 'despicable',
                 'devilish',
                 'diabolic',
                 'ferocious',
                 'fiendish',
                 'fierce',
                 'heartless',
                 'hellish',
                 'infernal',
                 'inimical',
                 'malicious',
                 'nasty',
                 'nefarious',
                 'nether',
                 'perfidious',
                 'putrefied',
                 'savage',
                 'scrupulous',
                 'sinister',
                 'sneaky',
                 'spiteful',
                 'spoiled',
                 'tainted',
                 'treacherous',
                 'venal',
                 'vile',
                 'villainous',
                 'wicked',
                 'frustrated',
                 'balked',
                 'disappointed',
                 'discontented',
                 'foiled',
                 'thwarted',
                 'nervous',
                 'alarmed',
                 'anxious',
                 'apprehensive',
                 'cautious',
                 'concerned',
                 'confused',
                 'conspicuous',
                 'disturbed',
                 'doubtful',
                 'insecure',
                 'irritable',
                 'panicked',
                 'perturbed',
                 'suspicious',
                 'pathetic',
                 'affecting',
                 'agitating',
                 'lamentable',
                 'piteous',
                 'pitiful',
                 'poignant',
                 'stirring',
                 'touching',
                 'quarrelsome',
                 'blatant',
                 'boisterous',
                 'cantankerous',
                 'clamorous',
                 'conspicuously',
                 'contentious',
                 'cross',
                 'deafening',
                 'disagreeable',
                 'fretful',
                 'hysterical',
                 'jealous',
                 'litigious',
                 'mean',
                 'mean-spirited',
                 'militant',
                 'nasty',
                 'noisy',
                 'offensively',
                 'ornery',
                 'peevish',
                 'pugnacious',
                 'rambunctious',
                 'recalcitrant',
                 'renitent',
                 'roisterous',
                 'strident',
                 'testy',
                 'touchy',
                 'truculent',
                 'unpleasant',
                 'vociferous',
                 'sad',
                 'bleak',
                 'dejected',
                 'depressed',
                 'desolate',
                 'dingy',
                 'discouraged',
                 'dismal',
                 'doleful',
                 'dreary',
                 'forlornly',
                 'gloomy',
                 'glum',
                 'grievous',
                 'grim',
                 'heart',
                 'broken',
                 'lonely',
                 'lugubrious',
                 'melancholic',
                 'miserable',
                 'mopish',
                 'morose',
                 'mournful',
                 'poor',
                 'seamy',
                 'somber',
                 'sordid',
                 'sorrowful',
                 'sulky',
                 'sullen',
                 'temperamental',
                 'unfortunate',
                 'unhappy',
                 'wistful',
                 'wretched',
                 'stubborn',
                 'adamant',
                 'hardheaded',
                 'inflexible',
                 'obdurate',
                 'obstinate',
                 'relentless',
                 'unyielding',
                 'terrible',
                 'abhorrent',
                 'abominable',
                 'appalling',
                 'awful',
                 'bizarre',
                 'calamitous',
                 'dire',
                 'disastrous',
                 'dreadful',
                 'fearful',
                 'formidable',
                 'freakish',
                 'frightful',
                 'ghastly',
                 'grotesque',
                 'gruesome',
                 'heinous',
                 'horrible',
                 'horrid',
                 'lurid',
                 'odious',
                 'painful',
                 'terrifying',
                 'tragic',
                 'unctuous',
                 "not well",
                 "not very well",
                 "not so well",
                 "didn't go well",
                 "wasn't well",
                 "isn't good"
                 ],
            'ontextro':
                [
                    "meeting new people",
                    "leading a conversation",
                    "leading conversations",
                    "initiating a conversation",
                    "initiating conversations",
                    "making new friends",
                    "making friends",
                    "influencing others",
                    "changing other people's opinions",
                    "public speaking",
                    "sharing ideas",
                    "sharing",
                    "socializing",
                    "communicating with other people",
                    "the opportunity to socialize",
                    "networking",
                    "connecting with people",
                    "establishing connection with other people",
                    "connecting with other people",
                    "communicating",
                    "connecting with people",
                    "connecting with others",
                    "getting people's attention",
                    "getting people's approval",
                    "having people's attention",
                    "having people's approval",
                    "public speaking",
                    "making people laugh",
                    "entertaining people",
                    "entertaining others",
                    "entertaining other people",
                    "vibe",
                    "vibes"
                ],
            'ontintro':  ##probably enjoy talking in a more structured setting and enjoy things/experience/content
                [
                    "listening to others' ideas ",
                    "learning new things",
                    "enjoying myself",
                    "learning",
                    "participating in a conversation",
                    "expanding my horizon",
                    "getting to know people better",
                    "getting to know them better",
                    "getting to know other people better",
                    "games"
                    "listening to others",
                    "learning from others",
                    "learning from others' ideas",
                    "listening to speeches",
                    "listening to a speech",
                    "being with my friends",
                    "hanging out with my friends",
                    "spending time with my friends",
                    "bonding with people I know",
                    "hanging out with people I know",
                    "talking to my friends",
                    "getting to know my friends better",
                    "dancing",
                    "ice-skating",
                    "eating",
                    "drinking",
                    "singing",
                    "food",
                    "music",
                    "deep conversation",
                    "playing on my phone",
                    "internet surfing"
                ],
            'ontveryintro':
                [
                    "don't think I will enjoy",
                    "do not think I will enjoy",
                    "I will not enjoy",
                    "I won't enjoy",
                    "nothing",
                    "none",
                    "dont know",
                    "do not know",
                    "not sure",
                    "no ideas",
                    "no idea",
                    "no opinions",
                    "no opinion",
                    "no thoughts",
                    "no thought",
                    "no knowledge",
                    "not certain",
                    "dont really know",
                    "hard to say"
                ],
            'ontexternal':
                [
                    "dont have better things to do",
                    "do not have better things to do",
                    "dont have better plans",
                    "do not have better plans",
                    "have nothing to do",
                    "have nothing else to do",
                    "trying to find something to do",
                    "tryna find something to do",
                    "want to find something to do",
                    "want to kill time",
                    "wanna kill time",
                    "want to distract myself",
                    "wanna distract myself"
                ],
            'ontshopping':
                [
                    "go shopping online",
                    "go shopping",
                    "mall",
                    "malls",
                    "outlet",
                    "shop",
                    "buy",
                    "buying",
                    "purchase",
                    "purchasing"
                ],
            'ontchores':
                [
                    "washing dishes",
                    "folding clothes",
                    "laundry",
                    "cleaning",
                    "clean",
                    "organizing",
                    "doing chores",
                    "wiping",
                    "wipe",
                    "mopping",
                    "mop",
                    "vaccum"
                ],
            'ontgames':
                [
                    "video games",
                    "board games",
                    "game",
                    "video game",
                    "games",
                    "LOL",
                    "League of Legends",
                    "VR games",
                    "VR Games",
                    "Games",
                    "VR Game",
                    "Game",
                    "video games",
                    "games",
                    "LOL",
                    "League of Legends",
                    "league",
                    "VR games",
                    "VR Games",
                    "Games",
                    "2K18",
                    "2K19",
                    "2K20",
                    "FIFA",
                    "PC",
                    "PS4",
                    "Play Station",
                    "Xbox",
                    "xbox",
                    "play station",
                    "pc",
                    "ps4"
                ],
            'ontmusic':
                [
                    "listening to music",
                    "singing",
                    "composing",
                    "music composition",
                    "playing the piano",
                    "playing the guitar",
                    "playing the drum",
                    "singing",
                    "listen to music",
                    "music",
                    "hip hop",
                    "rock",
                    "pop music",
                    "pop culture",
                    "jazz",
                    "heavy metal",
                    "classical music",
                    "country music",
                    "rap",
                    "study music",
                    "studying music",
                    "sleep music",
                    "calm music",
                    "calming music"
                ],
            'ontfood':
                [
                    "eating",
                    "cooking",
                    "cook",
                    "eat",
                    "order takeouts",
                    "order takeout",
                    "snack",
                    "snacks",
                    "snacking on",
                     "frozen food",
                    "dining",
                    "restaurants",
                     "restaurant",
                    "eat out",
                    "potluck",
                    "food",
                    "order Chinese",
                    "order chinese",
                    "order Japanese",
                    "Order japanese",
                    "order Italian",
                    "Order italian",
                    "pasta",
                    "burger",
                    "pizza",
                    "sushi",
                      "rice",
                    "groceries",
                    "stress baking",
                    "bake",
                    "baking"

                ],
            'ontsports':
                [
                    "basketball",
                    "run",
                    "running",
                    "cardio",
                    "working out",
                    "work-out",
                    "work out",
                    "tennis",
                    "football",
                    "soccer",
                    "swimming",
                    "table tennis",
                    "ping pong",
                    "cross country",
                    "crosscountry",
                    "xcountry",
                    "jog",
                    "jogging",
                    "ice hockey",
                    "hockey",
                    "field hockey",
                    "icehockey",
                    "ice hockey",
                    "field hockey",
                    "lacrosse",
                    "softball",
                    "baseball",
                    "badminton",
                    "sport",
                    "sports",
                    "exercise",
                    "fencing",
                    "wrestling",
                    "weight lifting",
                    "lifting"
                ],
            'ontdance':
                [
                    "dancing",
                    "choreographing",
                    "doing cover dances"
                ],
            'ontreadwatch':
                [
                    "books",
                    "TV",
                    "netflix",
                    "television",
                     "Netflix",
                    "Hulu",
                    "hulu",
                    "youtube",
                    "Youtube",
                    "Youtube videos",
                     "news",
                    "newspaper",
                    "online article",
                    "articles",
                    "research paper",
                    "scientific report",
                ],
            'ontonlinesocial':
                [
                    "social media",
                    "facebook",
                    "twitter",
                    "instagram",
                    "ig",
                    "fb",
                    "tik tok",
                    "social media",
                    "Facebook",
                    "Twitter",
                    "Instagram",
                    "youtube",
                    "Youtube",
                    "snapchat",
                    "ig",
                    "fb",
                    "tik tok",
                    "Line",
                    "line",
                    "Kakao Talk",
                    "kakao",
                    "Messenger",
                    "messenger",
                    "WeChat",
                     "wechat"
                ],
            'ontart':
                [
                    "painting",
                    "watercolor",
                    "take photos",
                    "take pictures",
                    "art",
                    "arts",
                    "taking photos",
                    "photography",
                    "taking pictures",
                    "make films",
                    "making films",
                    "filming",
                    "draw",
                    "drawing",
                    "drawings",
                    "paint",
                    "do my nails",
                    "paint my nails",
                    "artsy",
                    "photoshop",
                    "album",
                     "illustrator",
                     "filter",
                    "lighting",
                    "shadow",
                    "pose",
                    "model"
                ]
        }
}

knowledge = KnowledgeBase()
knowledge.load_json(stress_dict)
df = DialogueFlow(State.START, initial_speaker=DialogueFlow.Speaker.SYSTEM, kb=knowledge,
                  macros={'det_ss': det_ss(),"n20": n20(), "n_n20": n_n20(), 'o40': o40(), 'n70': n70(), 'n40': n40(), 'n10': n10(),
                          'o_n20': o_n20(), 'o_20': o_20(), 'o_20_1': o_20_1(), 'o_n20_1': o_n20_1(), 'e80': e80(),
                          'e40': e40(), 'printS': printS(), 'result':result()})
df.add_system_transition(State.START, State.PROMPT0,
                         r'[!"Hi! Tell me what social events you are stressed about."]')
df.add_user_transition(State.PROMPT0, State.PROMPT0_re, r'<$S_S=[!#ONT(ontsocial)]>')
df.add_user_transition(State.PROMPT0, State.PROMPT0_other, r'<$S_S={[!#POS(noun)]}>')
df.add_system_transition(State.PROMPT0_other, State.PROMPT3, r'[!"Oh..."$S_S"? How often do you find"#det_ss"overwhelming?"]') ###added a new branch for nouns not predicted by our social event ontology
df.add_system_transition(State.PROMPT0_re, State.PROMPT1, r'[!"Oh..."$S_S"? How often do you participate in"#det_ss"?"]')
df.add_user_transition(State.PROMPT1, State.PROMPT1_often,
                       r'<{[!#ONT(ontoften)],/(?:\s|^)(once|twice|three\stimes|four\stimes|five\stimes|1\stimes|2\stimes|3\stimes|4\stimes|5\stimes)\s((every|per|a)(\s)?(one|1|two|2|three|3|four|4|five|5|six|6|seven|7|other)?\s(hour+s?|day+s?|week+s?))|((every)\s(one|1|two|2|other)\s(month+s?))|((a|per)\s(month))(?:\s|,|\.|$)/}>')  # neuroticism=40
df.add_user_transition(State.PROMPT1, State.PROMPT1_sometimes,
                       r'<{[!#ONT(ontsometimes)],/(?:\s|^)(once|twice|three\stimes|four\stimes|five\stimes|1\stimes|2\stimes|3\stimes|4\stimes|5\stimes)\s((every|per|a)(\s)?(one|1|two|2|three|3|four|4|five|5|six|6|seven|7|other)?\s(semester+s?|term+s?|quarter+s?|year+s?|decade+s?))|((every\s)(three|3|four|4|five|5|six|6|seven|7|eight|8|nine|9|ten|10)\s(month+s?))(?:\s|,|\.|$)/}>')  # neuroticism =20
df.add_user_transition(State.PROMPT1, State.PROMPT1_never, r'[!#o40]')  # opennes +20  V
df.add_system_transition(State.PROMPT1_often, State.PROMPT2,
                         r'[!"It must be really hard for you... I get stressed about"#det_ss"sometimes, but the stress gradually decreases every time. How did your most recent"$S_S"go?"]')
df.add_system_transition(State.PROMPT1_sometimes, State.PROMPT2,
                         r'[!"That is totally normal! I sometimes feel stressed about"#det_ss"too. How did your most recent"$S_S"go?"]')
df.add_system_transition(State.PROMPT1_never, State.PROMPT4,
                         r'[!"Wow. It is your first time ever? Trying new things can be scary sometimes, but you got this! Is this"$S_S"mandatory?"]')

df.add_user_transition(State.PROMPT2, State.PROMPT2_notbad, r'<{[!#n20]}>')  # neuroticism +20  V
df.add_user_transition(State.PROMPT2, State.PROMPT2_bad, r'<{[!#n_n20]}>')  # neuroticism -20  V
df.add_system_transition(State.PROMPT2_notbad, State.PROMPT3,
                         r'[!"Then I am pretty sure this time will be just fine as well. Just curious, Do you always feel stressed about it?"]')
df.add_system_transition(State.PROMPT2_bad, State.PROMPT3,
                         r'[!"Yeah...sometimes"#det_ss"can be really bad. I know how it feels when things get out of control. Just curious, Do you always feel stressed about it?"]')

df.add_user_transition(State.PROMPT3, State.PROMPT3_often, r'<{[!#n70]}>')  # neuroticism +70  V
df.add_user_transition(State.PROMPT3, State.PROMPT3_sometimes, r'<{[!#n40]}>')  # neuroticism +40  V
df.add_user_transition(State.PROMPT3, State.PROMPT3_never, r'<{[!#n10]}>')  # neuroticism +10  V
df.add_system_transition(State.PROMPT3_often, State.PROMPT4,
                         r'[!"I see...but no pain no gain right? The stress could bring out your best performance. Is this"$S_S"mandatory for you?"]')
df.add_system_transition(State.PROMPT3_sometimes, State.PROMPT4,
                         r'[!"You know some amount of stress is helpful, believe it or not. It can help you be more effecient and motivated. Is this"$S_S"mandatory for you?"]')
df.add_system_transition(State.PROMPT3_never, State.PROMPT4,
                         r'[!"Oh really? This upcoming"$S_S" must mean a lot to you. Just treat it the same way you did before and you will do just fine! Is this"$S_S"mandatory for you?"]')

df.add_user_transition(State.PROMPT4, State.PROMPT4_yes, r'<{[!#o_n20]}>')  # openness-20  V
df.add_user_transition(State.PROMPT4, State.PROMPT4_no, r'<{[!#o_20]}>')  # openness+60  V
df.add_system_transition(State.PROMPT4_yes, State.PROMPT5, r'[!"Do you wanna participate in this"$S_S"then?"]')
df.add_system_transition(State.PROMPT4_no, State.PROMPT6, r'[!"What made you wanna attend this event?"]')

df.add_user_transition(State.PROMPT5, State.PROMPT5_yes, r'<{[!#o_20_1]}>')  # openness+60  V
df.add_user_transition(State.PROMPT5, State.PROMPT5_no, r'<{[!#o_n20_1]}>')  # openness-20  V
df.add_system_transition(State.PROMPT5_yes, State.PROMPT6, r'[!"Great! What made you wanna attend this event?"]')
df.add_system_transition(State.PROMPT5_no, State.PROMPT7,
                         r'[!"I am sorry that you have to go...but on the bright side, you might meet someone interesting there! This might sound weird but sometimes i enjoy"#det_ss"when everyone is focusing on me. Fo...fo...focus on me. Okay that was a little too much of Ariana. I feel nervous and excited at the same time during"#det_ss". How about you, what else do you feel about the upcoming"$S_S"?"]')

df.add_user_transition(State.PROMPT6, State.PROMPT6_re,
                       '<$reason={[!#POS(verb) #POS(part) #POS(verb) #POS(adj) #POS(noun)],[!#POS(verb) #POS(part) #POS(verb) #POS(verb)],[!#POS(verb) #POS(part) #POS(verb) #POS(adp) #POS(noun)],[!#POS(verb) #POS(part) #POS(verb) #POS(noun)],[!#POS(verb) #POS(part) #POS(verb)], [!#POS(verb) #POS(verb) #POS(adj) #POS(noun)],[!#POS(verb) #POS(verb) #POS(adp) #POS(noun)],[!#POS(verb) #POS(verb) #POS(noun)],[!#POS(verb) #POS(verb)]}>')
df.add_user_transition(State.PROMPT6, State.PROMPT6_other, r'<$External={[!#ONT(ontexternal)]}>')
df.add_system_transition(State.PROMPT6_re, State.PROMPT7,
                         r'[!"I am glad that you"$reason". This might sound weird but often I enjoy"#det_ss"when everyone is focusing on me. Fo...fo...focus on me. Okay that was a little too much of Ariana. I feel nervous and excited at the same time. How about you, what else do you feel about the upcoming"$S_S"?"]')
df.add_system_transition(State.PROMPT6_other, State.PROMPT7,
                         r'[!"I would have thought that"#det_ss"is a great option if I"$External"too! This might sound weird but often I enjoy"$S_S"when everyone is focusing on me. Fo...fo...focus on me. I feel nervous and excited at the same time. How about you, what else do you feel about the upcoming"$S_S"?"]')



df.add_user_transition(State.PROMPT7, State.PROMPT7_ex, r'<{[!#e80]}>')
df.add_user_transition(State.PROMPT7, State.PROMPT7_in, r'<{[!#e40]}>')
df.add_system_transition(State.PROMPT7_ex, State.PROMPT8,
                         r'[!"I feel like you are a very social person. Perhaps we are kinda similar haha. Hey shall we stop talking about stressful things? What is your favorite destress activity?"]')
df.add_system_transition(State.PROMPT7_in, State.PROMPT8,
                         r'[!"I guess we are not all that similar, but I love meeting people that are different from me! Hey shall we stop talking about stressful things. What is your favorite destress activity?"]')


df.add_user_transition(State.PROMPT8, State.PROMPT8_chores, r'<$activity={[!#ONT(ontchores)]}>')
df.add_system_transition(State.PROMPT8_chores, State.PROMPT9,
                         r'[!"Same! It feels so good when things are clean and organized, right?"]')
df.add_user_transition(State.PROMPT8, State.PROMPT8_games, r'<$activity={[!#ONT(ontgames)]}>')
df.add_system_transition(State.PROMPT8_games, State.PROMPT9,
                         r'[!"Oh I did not know you are a gamer! We should definetely play"$activity"together sometime!"]')
df.add_user_transition(State.PROMPT8, State.PROMPT8_music, r'<$activity={[!#ONT(ontmusic)]}>')
df.add_system_transition(State.PROMPT8_music, State.PROMPT9,
                         r'[!"Of course, listening to music is so stress-relieving, right? I love listening to pop music, do you?"]')
df.add_user_transition(State.PROMPT8, State.PROMPT8_art, r'<$activity={[!#ONT(ontart)]}>')
df.add_system_transition(State.PROMPT8_art, State.PROMPT9,
                         r'[!"I did not know that you are an artist! I hope I am more artistic... I am gonna go indulge myself in some watercolor painting later haha"]')
df.add_user_transition(State.PROMPT8, State.PROMPT8_food, r'<$activity={[!#ONT(ontfood)]}>')
df.add_system_transition(State.PROMPT8_food, State.PROMPT9,
                         r'[!"Are you a professional foodie haha? You need to give me some recommendations for restaurants next time!"]')
df.add_user_transition(State.PROMPT8, State.PROMPT8_sports, r'<$activity={[!#ONT(ontsports)]}>')
df.add_system_transition(State.PROMPT8_sports, State.PROMPT9,
                         r'[!"Oh what a coincidence, my friend just ask me if I want to play"$activity"this weekend. You should join us!"]')
df.add_user_transition(State.PROMPT8, State.PROMPT8_dance, r'<$activity={[!#ONT(ontdance)]}>')
df.add_system_transition(State.PROMPT8_dance, State.PROMPT9,
                         r'[!"Hey I am a dancer too! I am choreographing the song "Rewrite the Star"!"]')
df.add_user_transition(State.PROMPT8, State.PROMPT8_shopping, r'<$activity={[!#ONT(ontshopping)]}>')
df.add_system_transition(State.PROMPT8_shopping, State.PROMPT9,
                         r'[!"Shopping is super duper relaxing for me too. I always end up feeling so guilty for spending money afterward lol but I guess it is worth it."]')
df.add_user_transition(State.PROMPT8, State.PROMPT8_readwatch, r'<$activity={[!#ONT(ontreadwatch)]}>')
df.add_system_transition(State.PROMPT8_readwatch, State.PROMPT9,
                         r'[!"I love staying indoors when I am stressed too. It really helps me to stay calm."]')
df.add_user_transition(State.PROMPT8, State.PROMPT8_onlinesocial, r'<$activity={[!#ONT(ontonlinesocial)]}>')
df.add_system_transition(State.PROMPT8_onlinesocial, State.PROMPT9,
                         r'[!"Guess how many hours I spend on social media every day. 5 hours! I bet you spend even longer than me."]')
df.add_user_transition(State.PROMPT8, State.PROMPT8_social, r'<$activity={[!#ONT(ontsocial)]}>')
df.add_system_transition(State.PROMPT8_social, State.PROMPT9,
                         r'[!"You are such a social butterfly! I am glad that you have so many friends!"]')

df.add_user_transition(State.PROMPT9, State.SCORE, r'</.*/>')
df.add_system_transition(State.SCORE, State.END, r'[!#result]')

#df.add_user_transition(State.PROMPT8, State.SCORE, r'</.*/>')
#df.add_system_transition(State.SCORE, State.END, r'[!#printS]')

###### error cases
df.set_error_successor(State.PROMPT0,State.PROMPT0_err)
df.set_error_successor(State.PROMPT1, State.PROMPT1_err)
df.set_error_successor(State.PROMPT2, State.PROMPT2_err)
df.set_error_successor(State.PROMPT3, State.PROMPT3_err)
df.set_error_successor(State.PROMPT4, State.PROMPT4_err)
df.set_error_successor(State.PROMPT5, State.PROMPT5_err)
df.set_error_successor(State.PROMPT6, State.PROMPT6_err)
df.set_error_successor(State.PROMPT7, State.PROMPT7_err)
df.set_error_successor(State.PROMPT8, State.PROMPT8_err)
######an independent branch for user that did not bring up a specific stressor
df.add_system_transition(State.PROMPT0_err, State.PROMPT0_a, r'[!"I am glad that school is not stressful to you as it is to me. I personally often feel overwhelmed by my crazy workload in college."]')
df.add_user_transition(State.PROMPT0_a,State.PROMPT0_b,r'</.*/>')
df.add_system_transition(State.PROMPT0_b,State.PROMPT8,r'[!"You know what? Talking about stressful things makes me more stressed. I need to do something to destress. What is your favorite destress activity?"]')
######
df.add_system_transition(State.PROMPT1_err, State.PROMPT1,
                         r'[!"Sorry. I did not get it. Is it more like very often, sometimes, or never?"]')
df.add_system_transition(State.PROMPT2_err, State.PROMPT3,
                         r'[!"I see I see. Just curious, how often do you feel stressed about it?"]')
df.add_system_transition(State.PROMPT3_err, State.PROMPT4, r'[!"Yeah. I feel you. Is this"$S_S"mandatory for you?"]')
df.add_system_transition(State.PROMPT4_err, State.PROMPT5, r'[!"Mmhmm. Do you want to participate in this"$S_S"then?"]')
df.add_system_transition(State.PROMPT5_err, State.PROMPT5, r'[! "Um is that a yes?"]')
df.add_system_transition(State.PROMPT6_err, State.PROMPT7,
                         r'[!"Oh! That is very interesting! This might sound weird but sometimes I enjoy"#det_ss"when everyone is focusing on me. Fo...fo...focus on me. Okay that was a little too much of Ariana. What else do you feel about this upcoming"$S_S"?"]')
df.add_system_transition(State.PROMPT7_err, State.PROMPT8,
                         r'[!"Interesting! Hey shall we stop talking about stressful things? What is your favorite destess activity?"]')
df.add_system_transition(State.PROMPT8_err, State.PROMPT9,
                         r'[!"I personally like to organize my rooms. Doing chores is so stress-relieving. Well I am gonna go help my friends wash some dishes right now. Later!"]')

if __name__ == '__main__':
    df.run(debugging=False)