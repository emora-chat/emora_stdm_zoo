
from emora_stdm import KnowledgeBase, DialogueFlow, NatexNLG, Macro
from enum import Enum, auto
import random


class State(Enum):
    # Start states
    START = auto()
    PROMPT = auto()

    # Generic states
    USES_STREAMING_SITE = auto()
    NOT_USES_STREAMING_SITE = auto()
    ASK_WHICH_STREAMING_SITE = auto()
    UNKNOWN_STREAMING_SITE = auto()
    PICK_GENERAL_STREAMING_SITE = auto()
    ASK_GENERAL_GENRES = auto()
    PICK_OTHER_MEDIA = auto()

    # When the user does not report using a streaming site
    ASK_GENERAL_MOVIES_OR_TV = auto()
    RESPOND_YES_TO_MOVIES_OR_TV = auto()
    RESPOND_NO_TO_MOVIES_OR_TV = auto()
    ASK_PREFER_MOVIES_OR_TV = auto()

    # YouTube states
    PICK_YOUTUBE = auto()
    PICK_YOUTUBE_CHANNEL = auto()
    KNOWN_YOUTUBE_CHANNEL = auto()
    NO_YOUTUBE_CHANNEL_PREF = auto()
    ASK_YOUTUBE_GENRE_PREF = auto()
    RECOMMEND_YOUTUBE_CHANNEL = auto()
    GIVE_YOUTUBE_SUBSCRIBERS = auto()
    ERR_YOUTUBE_CHANNEL_NOT_RECOGNIZED = auto()
    USER_KNOWS_YOUTUBE_CHANNEL = auto()
    USER_NOT_KNOWS_YOUTUBE_CHANNEL = auto()
    RESPOND_TO_YOUTUBE_RECOMMENDATION = auto()

    # Netflix states
    PICK_NETFLIX = auto()
    ASK_NETFLIX_GENRES = auto()
    PICK_NETFLIX_MOVIES = auto()
    PICK_NETFLIX_TV = auto()
    NO_NETFLIX_GENRE_PREF = auto()
    ASK_NETFLIX_MOVIE_GENRES = auto()
    ASK_NETFLIX_TV_GENRES = auto()
    PICK_NETFLIX_MOVIE_GENRE = auto()
    PICK_NETFLIX_TV_GENRE = auto()
    RECOMMEND_NETFLIX_MOVIE = auto()
    RECOMMEND_NETFLIX_TV = auto()
    RESPOND_YES_TO_NETFLIX_RECOMMENDATION = auto()
    ERR_NETFLIX_RECOMMENDATION_RESPONSE_NOT_RECOGNIZED = auto()

    # Ending and error states
    END = auto()
    ERR = auto()


############################################################
# Netflix dictionaries
############################################################

##############################
# Netflix Movies
##############################
netflix_movie_recs = {"western": ["Once Upon a Time in the West", "True Grit"],
                      "family": ["The Incredibles 2", "The Karate Kid", "Coraline"],
                      "drama": ["The Irishman", "Marriage Story", "The Notebook"],
                      "thriller": ["Bird Box", "El Camino: A Breaking Bad Movie", "A Fall From Grace"],
                      "action": ["The Dark Knight", "Black Panther", "American Assassin"],
                      "sci fi": ["The Matrix", "Solo: A Star Wars Story", "Inception"],
                      "film noir": ["Blade Runner", "Zodiac", "The Chord"],
                      "biography": ["Ai Weiwei: Never Sorry", "American Anarchist"],
                      "mystery": ["Accident", "Automata", "Black Rose"],
                      "war": ["Let There Be Light", "The Memphis Belle: A Story of a Flying Fortress",
                              "Prelude to War"],
                      "history": ["American Experience: The Island Murder"],
                      "fantasy": ["The Lord of the Rings: The Two Towers"],
                      "crime": ["1922", "21", "The 4th Company"],
                      "documentary": ["American Factory", "Miss Americana", "What the Health"],
                      "adventure": ["Avengers: Infinity War", "The Foreigner"],
                      "comedy": ["Bad Boys", "The Other Guys", "Step Brothers"],
                      "animation": ["Spider-Man: Into the Spider-Verse", "9"],
                      "horror": ["47 Metres Down", "The Babysitter", "In the Tall Grass"],
                      "sport": ["The Game Changers", "Nacho Libre", "The Waterboy"],
                      "musical": ["Chitty Chitty Bang Bang", "Purple Rain", "Willy Wonka & the Chocolate Factory"],
                      "romance": ["After", "Falling Inn Love"]
                      }

##############################
# Netflix TV Shows
##############################
netflix_tv_recs = {"thriller": ["Narcos", "Breaking Bad", "You"],
                   "crime": ["Killer Inside: The Mind of Aaron Hernandez", "The Pharmacist", "I AM A KILLER"],
                   "family": ["A Series of Unfortunate Events", "Scooby Doo!: Mystery Incorporated"],
                   "action": ["The Witcher", "Ragnarok", "The 100"],
                   "documentary": ["Greatest Events of WWII in Colour", "The Devil Next Door"],
                   "drama": ["Shameless", "Better Call Saul", "THE STRANGER"],
                   "animation": ["Pokemon: Indigo League", "Bojack Horseman", "Attack on Titan"],
                   "romance": ["Cable Girls", "Jane the Virgin", "Crazy Ex-Girlfriend", "Love is Blind"],
                   "sci fi": ["Black Mirror", "The 100", "Star Trek", "Sense8"],
                   "horror": ["Supernatural", "American Horror Story", "Stranger Things", "The Walking Dead",
                              "The Haunting of Hill House"],
                   "mystery": ["Evil Genius", "Twin Peaks", "Sherlock"],
                   "reality": ["The World's Most Extraordinary Homes", "Heavy Rescue: 401", "Billy on the Street"],
                   "comedy": ["The Office", "Master of None", "The Good Place"],
                   "talk show": ["The Break with Michelle Wolf", "Off Camera", "Chelsea"],
                   "musical": ["Glee"],
                   "fantasy": ["Jonathan Strange & Mr Norrell", "Blood & Treasures", "Penny Dreadful"]
                   }

############################################################
# YouTube dictionaries
############################################################

##############################
# YouTube Channels
# (Keys are channel names and
# values are tuples with the
# channel genre and subscriber
# count in millions)
##############################
all_youtube_channels = {'shane': ('comedy', 23.2), 'the tonight show starring jimmy fallon': ('comedy', 23.7),
                        'smosh': ('comedy', 25.1), 'luisito comunica': ('comedy', 29.5),
                        'whinderssonnunes': ('comedy', 38.4), 'cvs 3d rhymes & kids songs': ('education', 22.8),
                        'little baby bum - nursery rhymes & kids songs': ('education', 24.6),
                        'billion surprise toys - bst kids songs': ('education', 25.3),
                        'pinkfong! kids\' songs & stories': ('education', 29.5),
                        'chuchu tv nursery rhymes & kids songs': ('education', 31.6),
                        'cocomelon - nursery rhymes': ('education', 73.4), 'pewdiepie': ('entertainment', 103),
                        'boram tube vlog': ('entertainment', 23.3), 'colors tv': ('entertainment', 23),
                        'ryan\'s world': ('entertainment', 24), 'abs-cbn entertainment': ('entertainment', 25.1),
                        'toypudding tv': ('entertainment', 25.5), 'rezendeevil': ('entertainment', 26.2),
                        'luis fonsi': ('entertainment', 26.9), 'stacy toys': ('entertainment', 26),
                        'workpointofficial': ('entertainment', 27.5), 'sab tv': ('entertainment', 27.7),
                        'luccas neto - luccas toon': ('entertainment', 28.7), 'mrbeast': ('entertainment', 30.2),
                        'get movies': ('entertainment', 30.3), 'você sabia?': ('entertainment', 31.6),
                        'rihanna': ('entertainment', 33.7), 'felipe neto': ('entertainment', 36.2),
                        'theellenshow': ('entertainment', 36.5), 'juegagerman': ('entertainment', 38.2),
                        'holasoygerman.': ('entertainment', 40.4), 'zee tv': ('entertainment', 41),
                        'badabun': ('entertainment', 42.4), 'kids diana show': ('entertainment', 46.8),
                        'like nastya vlog': ('entertainment', 48.1), 'set india': ('entertainment', 65.2),
                        'selena gomez': ('film & animation', 24.7), 'goldmines telefilms': ('film & animation', 32.4),
                        'movieclips': ('film & animation', 33.8), 'ninja': ('gaming', 22.8),
                        'jacksepticeye': ('gaming', 23.3), 'vanossgaming': ('gaming', 24.9),
                        'markiplier': ('gaming', 25), 'vegetta777': ('gaming', 28.9),
                        'fernanfloo': ('gaming', 35), 'elrubiusomg': ('gaming', 37), 'yuya': ('howto & style', 24.2),
                        'bright side': ('howto & style', 33.4), '5-minute crafts': ('howto & style', 64.4),
                        't-series': ('music', 129), 'worldstarhiphop': ('music', 22.8), 'maluma': ('music', 22.9),
                        'j balvin': ('music', 23.6),
                        'looloo kids - nursery rhymes and children\'s songs': ('music', 24.2),
                        'nocopyrightsounds': ('music', 24.9), 'shawn mendes': ('music', 24.9),
                        'xxxtentacion': ('music', 24), 'bangtantv': ('music', 25.4),
                        'katyperryvevo': ('music', 25.7), 'eminemvevo': ('music', 25.8),
                        'tips official': ('music', 25.8), 'rihannavevo': ('music', 25.9),
                        'bruno mars': ('music', 26.5), 'billie eilish': ('music', 26.6),
                        'spinnin\' records': ('music', 26.6), 't-series bhakti sagar': ('music', 26.7),
                        'taylorswiftvevo': ('music', 26.9), 'ozuna': ('music', 27.3), 'gr6 explode': ('music', 27.8),
                        'shakira': ('music', 27.8), 'daddy yankee': ('music', 27.9),
                        'sonymusicindiavevo': ('music', 27.9), 'trap nation': ('music', 28.1),
                        'speed records': ('music', 28.3), 'yrf': ('music', 28), 'maroon 5': ('music', 29.6),
                        'el reino infantil': ('music', 30.4), 'one direction': ('music', 30.6),
                        'sony music india': ('music', 30.9), 'wave music': ('music', 31.6),
                        'big hit labels': ('music', 32.3), 'shemaroo filmi gaane': ('music', 32.4),
                        'alan walker': ('music', 32.5), 'justinbiebervevo': ('music', 32.9),
                        'blackpink': ('music', 33.2), 'katy perry': ('music', 36.2),
                        'taylor swift': ('music', 37.1), 'ariana grande': ('music', 39.8),
                        'eminemmusic': ('music', 41.1), 'ed sheeran': ('music', 43.6), 'marshmello': ('music', 43),
                        'zee music company': ('music', 50.4), 'justin bieber': ('music', 51.1),
                        'canal kondzilla': ('music', 55.6), 'dude perfect': ('sports', 49.2), 'wwe': ('sports', 54.8)
                        }

##############################
# YouTube Comedy Channels
##############################
youtube_comedy = {'shane', 'the tonight show starring jimmy fallon', 'smosh', 'luisito comunica', 'whinderssonnunes'}

##############################
# YouTube Education Channels
##############################
youtube_education = {'cvs 3d rhymes & kids songs', 'little baby bum - nursery rhymes & kids songs',
                     'billion surprise toys - bst kids songs', 'pinkfong! kids\' songs & stories',
                     'chuchu tv nursery rhymes & kids songs', 'cocomelon - nursery rhymes'}

##############################
# YouTube Entertainment
# Channels
##############################
youtube_entertainment = {'pewdiepie', 'boram tube vlog', 'colors tv', 'ryan\'s world', 'abs-cbn entertainment',
                         'toypudding tv', 'rezendeevil', 'luis fonsi', 'stacy toys', 'workpointofficial', 'sab tv',
                         'luccas neto - luccas toon', 'mrbeast', 'get movies', 'você sabia?', 'rihanna',
                         'felipe neto', 'theellenshow', 'juegagerman', 'holasoygerman.', 'zee tv', 'badabun',
                         'kids diana show', 'like nastya vlog', 'set india'}

##############################
# YouTube Film & Animation
# Channels
##############################
youtube_film_animation = {'selena gomez', 'goldmines telefilms', 'movieclips'}

##############################
# YouTube Gaming Channels
##############################
youtube_gaming = {'ninja', 'jacksepticeye', 'vanossgaming', 'markiplier', 'vegetta777', 'fernanfloo', 'elrubiusomg'}

##############################
# YouTube Howto & Style
# Channels
##############################
youtube_howto_style = {'yuya', 'bright side', '5-minute crafts'}

##############################
# YouTube Music Channels
##############################
youtube_music = {'t-series', 'worldstarhiphop', 'maluma', 'j balvin',
                 'looloo kids - nursery rhymes and children\'s songs', 'nocopyrightsounds', 'shawn mendes',
                 'xxxtentacion', 'bangtantv', 'katyperryvevo', 'eminemvevo', 'tips official', 'rihannavevo',
                 'bruno mars', 'billie eilish', 'spinnin\' records', 't-series bhakti sagar', 'taylorswiftvevo',
                 'ozuna', 'gr6 explode', 'shakira', 'daddy yankee', 'sonymusicindiavevo', 'trap nation',
                 'speed records', 'yrf', 'maroon 5', 'el reino infantil', 'one direction', 'sony music india',
                 'wave music', 'big hit labels', 'shemaroo filmi gaane', 'alan walker', 'justinbiebervevo',
                 'blackpink', 'katy perry', 'taylor swift', 'ariana grande', 'eminemmusic', 'ed sheeran',
                 'marshmello', 'zee music company', 'justin bieber', 'canal kondzilla'}

##############################
# YouTube Sports Channels
##############################
youtube_sports = {'dude perfect', 'wwe'}

youtube_genre_dicts = {'comedy': youtube_comedy, 'education': youtube_education,
                       'entertainment': youtube_entertainment, 'film & animation': youtube_film_animation,
                       'gaming': youtube_gaming, 'howto & style': youtube_howto_style, 'music': youtube_music,
                       'sports': youtube_sports}


############################################################
# Macros for handling Movie, show and
# YouTube channel recommendations
############################################################
class RandomShowGenreMacro(Macro):

    def __init__(self, show_genre_dict):
        self.show_genre_dict = show_genre_dict

    def run(self, ngrams, variables, args):
        return random.choice(self.show_genre_dict.get(args[0].lower()))


class YouTubeSubscribersMacro(Macro):

    def __init__(self, channel_dict):
        self.channel_dict = channel_dict

    def run(self, ngrams, variables, args):
        return str(self.channel_dict[args[0].lower()][1])


class YouTubeGenreMacro(Macro):

    def __init__(self, channel_dict):
        self.channel_dict = channel_dict

    def run(self, ngrams, variables, args):
        return self.channel_dict[args[0].lower()][0]


class YouTubeChannelRecommendFromChannelMacro(Macro):

    def __init__(self, channel_dict, genre_mapping_dict):
        self.channel_dict = channel_dict
        self.genre_mapping_dict = genre_mapping_dict

    def run(self, ngrams, variables, args):
        channel_to_lower = args[0].lower()
        channel_genre = self.channel_dict[channel_to_lower][0]
        genre_set = self.genre_mapping_dict[channel_genre]
        genre_set.remove(channel_to_lower)
        return random.choice(tuple(genre_set))


class YouTubeChannelRecommendFromGenreMacro(Macro):

    def __init__(self, genre_mapping_dict):
        self.genre_mapping_dict = genre_mapping_dict

    def run(self, ngrams, variables, args):
        channels_set = self.genre_mapping_dict[args[0].lower()]
        return random.choice(tuple(channels_set))


############################################################
# Ontology storing the lists of Netflix Genres,
# Youtube Genres and Youtube Channels
############################################################
ontology = {
    "ontology": {
        "ontYoutubeChannel":
            list(all_youtube_channels.keys()),
        "ontNetflixMovieGenres":
            list(netflix_movie_recs.keys()),
        "ontNetflixTVGenres":
            list(netflix_tv_recs.keys()),
        "ontYoutubeGenres":
            list(youtube_genre_dicts.keys())
    }
}

knowledge = KnowledgeBase()
knowledge.load_json(ontology)
df = DialogueFlow(State.START, initial_speaker=DialogueFlow.Speaker.SYSTEM, kb=knowledge)

df.add_system_transition(State.START, State.PROMPT, '"Do you use a streaming site?"')

yes_natex = r"{/(?i)/{yes, yeah, yep, correct, ye, indeed, of course, absolutely, i do}}"
no_natex = r"{/(?i)/{no, none, nothing, dont use, dont really use, never, nope, nah, i dont, i do not, i havent, " \
           r"i have not}}"
gen_natex = r"[/(?i)/$gen={hulu,hbo,hbogo,xfinity,twitch,amazon,amazon prime,showtime,abc,twitch}]"
youtube_natex = r"{/(?i)/youtube}"
netflix_natex = r"{/(?i)/netflix}"
movie_natex = r"{/(?i)/{movie, movies, film, films}}"
tv_natex = r"{/(?i)/{tv, television, tv series, television series, tv show, tv shows, television shows, television " \
           r"show}}"
no_preference_natex = r"{/(?i)/{no preference, i dont know, no favorite, none, i dont have one}}"

############################################################
# Generic error response
############################################################
df.add_system_transition(State.ERR, State.END, '"Sorry! I am not familiar with that."')

############################################################
# 1: First stage
# (ask user about preferred streaming services)
############################################################

##############################
# 1a: User picks
# streaming site
##############################
# *** USER CAN RESPOND EITHER YES/NO OR IMMEDIATELY PROVIDE THEIR PREFERENCE
df.add_user_transition(State.PROMPT, State.PICK_NETFLIX, netflix_natex)
df.add_user_transition(State.PROMPT, State.PICK_YOUTUBE, youtube_natex)
df.add_user_transition(State.PROMPT, State.PICK_GENERAL_STREAMING_SITE, gen_natex)
df.add_user_transition(State.PROMPT, State.USES_STREAMING_SITE, yes_natex)
df.add_user_transition(State.PROMPT, State.NOT_USES_STREAMING_SITE, no_natex)
df.set_error_successor(State.PROMPT, State.ERR)

df.add_system_transition(State.NOT_USES_STREAMING_SITE, State.ASK_GENERAL_MOVIES_OR_TV, '"Oh, well do you like '
                                                                                        'movies or TV?"')

##############################
# 1b: User answers whether
# they like movies or TV
##############################
# *** USER CAN RESPOND EITHER YES/NO OR IMMEDIATELY PROVIDE THEIR PREFERENCE
df.add_user_transition(State.ASK_GENERAL_MOVIES_OR_TV, State.PICK_NETFLIX_MOVIES, movie_natex)
df.add_user_transition(State.ASK_GENERAL_MOVIES_OR_TV, State.PICK_NETFLIX_TV, tv_natex)
df.add_user_transition(State.ASK_GENERAL_MOVIES_OR_TV, State.RESPOND_YES_TO_MOVIES_OR_TV, yes_natex)
df.add_user_transition(State.ASK_GENERAL_MOVIES_OR_TV, State.RESPOND_NO_TO_MOVIES_OR_TV, no_natex)
df.set_error_successor(State.ASK_GENERAL_MOVIES_OR_TV, State.ERR)

df.add_system_transition(State.RESPOND_YES_TO_MOVIES_OR_TV, State.ASK_PREFER_MOVIES_OR_TV, '"Nice! Which one do you '
                                                                                           'prefer?"')
df.add_system_transition(State.RESPOND_NO_TO_MOVIES_OR_TV, State.END, '"Oh, you should consider watching some!"')

##############################
# 1c: User picks movies or TV
# (cuts to 2a)
##############################
df.add_user_transition(State.ASK_PREFER_MOVIES_OR_TV, State.PICK_NETFLIX_MOVIES, movie_natex)
df.add_user_transition(State.ASK_PREFER_MOVIES_OR_TV, State.PICK_NETFLIX_TV, tv_natex)
df.set_error_successor(State.ASK_PREFER_MOVIES_OR_TV, State.ERR)

df.add_system_transition(State.USES_STREAMING_SITE, State.ASK_WHICH_STREAMING_SITE,
                         '"Which streaming site do you use most often?"')

############################################################
# 2: General streaming branch (funnels to Netflix)
############################################################
df.add_user_transition(State.ASK_WHICH_STREAMING_SITE, State.PICK_GENERAL_STREAMING_SITE, gen_natex)

df.add_system_transition(State.PICK_GENERAL_STREAMING_SITE, State.ASK_GENERAL_GENRES, '[! $gen "is not as popular as '
                                                                                      'Youtube or Netflix. Do you watch'
                                                                                      ' movies, tv shows, or something'
                                                                                      ' else on it?"]')

##############################
# 2a: User picks Netflix
# movies or Netflix TV
##############################
df.add_user_transition(State.ASK_GENERAL_GENRES, State.PICK_NETFLIX_MOVIES, movie_natex)
df.add_user_transition(State.ASK_GENERAL_GENRES, State.PICK_NETFLIX_TV, tv_natex)
df.set_error_successor(State.ASK_GENERAL_GENRES, State.PICK_OTHER_MEDIA)

df.add_system_transition(State.PICK_OTHER_MEDIA, State.END, '"I see. Sorry, but I only have information on movies, '
                                                            'tv shows and YouTube channels."')

############################################################
# Netflix branch
############################################################
df.add_user_transition(State.ASK_WHICH_STREAMING_SITE, State.PICK_NETFLIX, netflix_natex)

df.add_system_transition(State.PICK_NETFLIX, State.ASK_NETFLIX_GENRES, '"Netflix is awesome! '
                                                                       'Do you prefer movies or television series?"')

df.add_user_transition(State.ASK_NETFLIX_GENRES, State.PICK_NETFLIX_MOVIES, movie_natex)
df.add_user_transition(State.ASK_NETFLIX_GENRES, State.PICK_NETFLIX_TV, tv_natex)
df.add_user_transition(State.ASK_NETFLIX_GENRES, State.NO_NETFLIX_GENRE_PREF, no_preference_natex)
df.set_error_successor(State.ASK_NETFLIX_GENRES, State.ERR)

df.add_system_transition(State.PICK_NETFLIX_MOVIES, State.ASK_NETFLIX_MOVIE_GENRES, '"Nice! What is your favorite '
                                                                                    'genre of movies?"')
df.add_system_transition(State.PICK_NETFLIX_TV, State.ASK_NETFLIX_TV_GENRES, '"Nice! What is your favorite '
                                                                             'television series genre?"')

df.add_system_transition(State.NO_NETFLIX_GENRE_PREF, State.END, '"Don\'t worry. It\'s a hard decision"')

netflix_movie_genre_natex = r"[/(?i)/$netflix_movie_genre=#ONT(ontNetflixMovieGenres)]"
netflix_tv_genre_natex = r"[/(?i)/$netflix_tv_genre=#ONT(ontNetflixTVGenres)]"
df.add_user_transition(State.ASK_NETFLIX_MOVIE_GENRES, State.PICK_NETFLIX_MOVIE_GENRE, netflix_movie_genre_natex)
df.set_error_successor(State.ASK_NETFLIX_MOVIE_GENRES, State.ERR)
df.add_user_transition(State.ASK_NETFLIX_TV_GENRES, State.PICK_NETFLIX_TV_GENRE, netflix_tv_genre_natex)
df.set_error_successor(State.ASK_NETFLIX_TV_GENRES, State.ERR)

df.add_system_transition(State.PICK_NETFLIX_MOVIE_GENRE, State.RECOMMEND_NETFLIX_MOVIE,
                         NatexNLG('[! "If you like" $netflix_movie_genre "then maybe you will like"'
                                  ' #Macro($netflix_movie_genre) ". You can find it on Netflix. Have you seen it?"]',
                                  macros={'Macro': RandomShowGenreMacro(netflix_movie_recs)}))
df.add_system_transition(State.PICK_NETFLIX_TV_GENRE, State.RECOMMEND_NETFLIX_TV,
                         NatexNLG('[! "If you like" $netflix_tv_genre "then maybe you will like"'
                                  ' #Macro($netflix_tv_genre) ". You can find it on Netflix. Have you seen it?"]',
                                  macros={'Macro': RandomShowGenreMacro(netflix_tv_recs)}))

df.add_user_transition(State.RECOMMEND_NETFLIX_MOVIE, State.RESPOND_YES_TO_NETFLIX_RECOMMENDATION, yes_natex)
df.set_error_successor(State.RECOMMEND_NETFLIX_MOVIE, State.ERR_NETFLIX_RECOMMENDATION_RESPONSE_NOT_RECOGNIZED)
df.add_user_transition(State.RECOMMEND_NETFLIX_TV, State.RESPOND_YES_TO_NETFLIX_RECOMMENDATION, yes_natex)
df.set_error_successor(State.RECOMMEND_NETFLIX_TV, State.ERR_NETFLIX_RECOMMENDATION_RESPONSE_NOT_RECOGNIZED)

df.add_system_transition(State.RESPOND_YES_TO_NETFLIX_RECOMMENDATION, State.END, '"You have great taste!"')

df.add_system_transition(State.ERR_NETFLIX_RECOMMENDATION_RESPONSE_NOT_RECOGNIZED,
                         State.END, '"You should put it at the top of your list!"')

############################################################
# 3: YouTube branch
############################################################
df.add_user_transition(State.ASK_WHICH_STREAMING_SITE, State.PICK_YOUTUBE, youtube_natex)
df.add_system_transition(State.PICK_YOUTUBE, State.PICK_YOUTUBE_CHANNEL, '"YouTube is one of my favorites! '
                                                                         'What is your favorite channel?"')

channel_natex = r"[/(?i)/$channel=#ONT(ontYoutubeChannel)]"

##############################
# 3a: User picks picks
# favorite YouTube channel
##############################
df.add_user_transition(State.PICK_YOUTUBE_CHANNEL, State.KNOWN_YOUTUBE_CHANNEL, channel_natex)
df.add_user_transition(State.PICK_YOUTUBE_CHANNEL, State.NO_YOUTUBE_CHANNEL_PREF, no_preference_natex)
df.set_error_successor(State.PICK_YOUTUBE_CHANNEL, State.ERR_YOUTUBE_CHANNEL_NOT_RECOGNIZED)

df.add_system_transition(State.KNOWN_YOUTUBE_CHANNEL, State.GIVE_YOUTUBE_SUBSCRIBERS,
                         NatexNLG('[! $channel "is a good one! It has" #Macro1($channel) "million subscribers. '
                                  'Its genre is" #Macro2($channel) ". Have you checked out" #Macro3($channel) "? '
                                  'It is another" #Macro2($channel) "channel."]',
                                  macros={'Macro1': YouTubeSubscribersMacro(all_youtube_channels),
                                          'Macro2': YouTubeGenreMacro(all_youtube_channels),
                                          'Macro3': YouTubeChannelRecommendFromChannelMacro(all_youtube_channels,
                                                                                            youtube_genre_dicts)}))

##############################
# 3b: User is asked if they
# know a youtube channel
# recommended by the system
##############################
df.add_user_transition(State.GIVE_YOUTUBE_SUBSCRIBERS, State.USER_KNOWS_YOUTUBE_CHANNEL, yes_natex)
df.add_user_transition(State.GIVE_YOUTUBE_SUBSCRIBERS, State.USER_NOT_KNOWS_YOUTUBE_CHANNEL, no_natex)
df.set_error_successor(State.GIVE_YOUTUBE_SUBSCRIBERS, State.ERR)

df.add_system_transition(State.USER_KNOWS_YOUTUBE_CHANNEL, State.END, '"You have great taste!"')
df.add_system_transition(State.USER_NOT_KNOWS_YOUTUBE_CHANNEL, State.END, '"You should check it out!"')

df.add_system_transition(State.NO_YOUTUBE_CHANNEL_PREF, State.ASK_YOUTUBE_GENRE_PREF,
                         '"Well, what kind of content do you prefer? Maybe I can give you some suggestions."')

df.add_system_transition(State.ERR_YOUTUBE_CHANNEL_NOT_RECOGNIZED, State.ASK_YOUTUBE_GENRE_PREF,
                         '"I have never heard of that channel before. What type of videos do they make?"')

##############################
# 3c: User is asked about
# their favorite genre of
# YouTube videos
##############################
youtube_topic_natex = r"[/(?i)/$topic=#ONT(ontYoutubeGenres)]"
df.add_user_transition(State.ASK_YOUTUBE_GENRE_PREF, State.RECOMMEND_YOUTUBE_CHANNEL, youtube_topic_natex)
df.set_error_successor(State.ASK_YOUTUBE_GENRE_PREF, State.ERR)

df.add_system_transition(State.RECOMMEND_YOUTUBE_CHANNEL, State.RESPOND_TO_YOUTUBE_RECOMMENDATION,
                         NatexNLG('"You might like " #Macro1($topic) ". They make" $topic "videos too. Have you seen '
                                  'that channel?"',
                                  macros={'Macro1': YouTubeChannelRecommendFromGenreMacro(youtube_genre_dicts)}))

df.add_user_transition(State.RESPOND_TO_YOUTUBE_RECOMMENDATION, State.USER_KNOWS_YOUTUBE_CHANNEL, yes_natex)
df.add_user_transition(State.RESPOND_TO_YOUTUBE_RECOMMENDATION, State.USER_NOT_KNOWS_YOUTUBE_CHANNEL, no_natex)
df.set_error_successor(State.RESPOND_TO_YOUTUBE_RECOMMENDATION, State.ERR)

############################################################
# 4: If the user enters an unknown streaming site
############################################################
df.set_error_successor(State.ASK_WHICH_STREAMING_SITE, State.UNKNOWN_STREAMING_SITE)
df.add_system_transition(State.UNKNOWN_STREAMING_SITE, State.ASK_GENERAL_GENRES, '"Hmm. I do not know that one. Do '
                                                                                 'you watch movies, TV, or something '
                                                                                 'else on it?"')

df.add_system_transition(State.END, State.END, '"Streaming sites are cool. I am glad we could talk about them! '
                                               'Goodbye!"')

df.set_error_successor(State.ERR, error_successor=State.END)
df.set_error_successor(State.END, error_successor=State.END)

df.run(debugging=False)
