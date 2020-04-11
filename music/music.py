import json
from enum import Enum, auto
from typing import Dict, Any, List

from emora_stdm import KnowledgeBase, DialogueFlow, Macro, Ngrams
from spotify_query import requester

# TODO: Update the State enum as needed
class State(Enum):
    START = auto()
    RES = auto()
    RES2 = auto()
    RES_ERROR = auto()
    RES_ERROR2 = auto()
    NO = auto()
    NO_ANS = auto()
    MUSIC_GOOD = auto()
    MUSIC_OPINION = auto()
    AGREE = auto()
    DISAGREE = auto()
    NEUT = auto()
    YES = auto()
    VERB = auto()
    VERBRES = auto()
    TIMERES = auto()
    VERB2 = auto()
    ACT_ERROR = auto()
    ACT_ERROR2 = auto()
    SERVICE = auto()
    STREAM = auto()
    OTHERSTREAM2 = auto()
    STREAM_ERROR = auto()
    STREAM_ERROR2 = auto()
    CDS = auto()
    VINYLS = auto()
    OTHERMED = auto()
    SERV_ERROR = auto()
    SERV_ERROR2 = auto()
    SERVICE2 = auto()
    ADJ = auto()
    POSITIVE = auto()
    NEGATIVE = auto()
    ADJ_ERROR = auto()
    ADJ2 = auto()
    ADJ_ERROR2 = auto()
    ARTIST = auto()
    PANDORA = auto()
    APPLE = auto()
    AMAZON = auto()
    YOUTUBE = auto()
    SPOTIFY = auto()
    OTHERSTREAM = auto()
    DISCOUNT = auto()
    PLAYLIST = auto()
    CONVENIENCE = auto()
    SELECTION = auto()
    SHOWS = auto()
    DOWNLOAD = auto()
    DISCOVERY = auto()
    END = auto()
    TERMINAL = auto()
    ERR = auto()
    ARTIST_ERROR = auto()
    NOUNRES = auto()
    PLACERES = auto()

sp_requester = requester()

class ARTIST_GENRE(Macro):

    def run(self, ngrams: Ngrams, vars: Dict[str, Any], args: List[Any]):
        if 'fav_artist' in vars:
            fav_artist_name = vars['fav_artist']
            vars['artist_genre'] = sp_requester.get_artist_genres(fav_artist_name)[0]
            # returns the first genre in the artists' genre list
            return vars['artist_genre']

class ARTIST_QUALITIES(Macro):

    def run(self, ngrams: Ngrams, vars: Dict[str, Any], args: List[Any]):
        if 'fav_artist' in vars:
            fav_artist_name = vars['fav_artist']
            query_first_result = requester.search_for_artist(fav_artist_name)[0]
            artist_id = query_first_result['id']
            artist_features = requester.get_artist_avg_features(artist_id)
            # these next two lines are for testing. Remove once macro is up and running
            for key, val in artist_features:
                print(""+key+""+val)

            # TODO: build a way to turn artist feature metrics into qualitative descriptives

# TODO: create the ontology as needed
ontology = json.loads(open('ontology.json').read())

knowledge = KnowledgeBase()
knowledge.load_json(ontology)
df = DialogueFlow(State.START, initial_speaker=DialogueFlow.Speaker.SYSTEM, kb=knowledge,
                  macros={"ARTIST_QUALITIES": ARTIST_QUALITIES(),
                          "ARTIST_GENRE": ARTIST_GENRE()})

df.add_system_transition(State.START, State.RES, '"Do you listen to music?"')

df.add_user_transition(State.RES, State.YES, '[#ONT(yes)]')
df.add_user_transition(State.RES, State.NO, '[#ONT(no)]')


# Error
df.set_error_successor(State.RES, State.RES_ERROR)
df.add_system_transition(State.RES_ERROR, State.RES2, '"Sorry, I didn\'t catch that. Do you listen to music?"')
df.add_user_transition(State.RES2, State.YES, '[#ONT(yes)]')
df.add_user_transition(State.RES2, State.NO, '[#ONT(no)]')
df.set_error_successor(State.RES2, State.RES_ERROR2)
df.add_system_transition(State.RES_ERROR2, State.ERR, '"Sorry, I still didn\'t catch that. Let\'s start over."')


#USER DOESNT LISTEN TO MUSIC
df.add_system_transition(State.NO, State.NO_ANS, '"That\'s a shame. Why do you not listen to music?"')

df.add_user_transition(State.NO_ANS, State.YES, '[{-not,-dont}, like, music]')
df.set_error_successor(State.NO_ANS, State.MUSIC_GOOD)

df.add_system_transition(State.MUSIC_GOOD, State.MUSIC_OPINION, "Scientists have actually found many benefits to listening "
                                                        "to music. Research shows music makes you happier, "
                                                        "it enhances workout performance and lowers stress. "
                                                        '"Have you heard about the benefits of music before?"')

df.add_user_transition(State.MUSIC_OPINION, State.AGREE, '[#ONT(yes)]')
df.add_user_transition(State.MUSIC_OPINION, State.DISAGREE, '[#ONT(no)]')
df.set_error_successor(State.MUSIC_OPINION, State.NEUT) # error handling

df.add_system_transition(State.AGREE, State.TERMINAL, '"Great! I hope this convinced you to listen to more music"')
df.add_system_transition(State.DISAGREE, State.TERMINAL, '"That\'s a shame, you should read up on it."')
df.add_system_transition(State.NEUT, State.TERMINAL, '"You should read up on it.')



#USER LISTENS TO MUSIC
df.add_system_transition(State.YES, State.VERB, '"When do you listen to music?"')

df.add_user_transition(State.VERB, State.VERBRES, '[-listen, $activity={#POS(verb), $activity=#POS(VBG)}]')
df.add_user_transition(State.VERB, State.TIMERES, '[$time=#NER(time)]')
df.add_user_transition(State.VERB, State.PLACERES, '[$place={in the}]')

# Error
df.set_error_successor(State.VERB, State.ACT_ERROR)
df.add_system_transition(State.ACT_ERROR, State.VERB2, '"Sorry, I didn\'t catch that. When do you listen to music?"')
df.add_user_transition(State.VERB2, State.VERBRES, '[-listen, $activity={#POS(verb), $activity=#POS(VBG)}]')
df.add_user_transition(State.VERB2, State.TIMERES, '[$time=#NER(time)]')
df.add_user_transition(State.VERB2, State.PLACERES, '[$place={in the}]')
df.set_error_successor(State.VERB2, State.ACT_ERROR2)
df.add_system_transition(State.ACT_ERROR2, State.ERR, '"Sorry, I still didn\'t catch that. Let\'s start over."')



df.add_system_transition(State.VERBRES, State.SERVICE,
                         '[!"During" $activity "is a great time to listen to music! What do you use to listen to music? "]')
df.add_system_transition(State.TIMERES, State.SERVICE,
                         '[!$time "is a great time to listen to music! What do you use to listen to music?"]')
df.add_system_transition(State.PLACERES, State.SERVICE,
                         '"That\'s a great place to listen to music! I personally listen to music in the car. What do you use to listen to music?"')


df.add_user_transition(State.SERVICE, State.CDS, '[-vinyl, $medium=#ONT(mediums)]')
df.add_user_transition(State.SERVICE, State.VINYLS, '[$medium=vinyl]')
df.add_user_transition(State.SERVICE, State.OTHERMED, '[$medium=#ONT(othermediums)]')

#Error
df.set_error_successor(State.SERVICE, State.SERV_ERROR)
df.add_system_transition(State.SERV_ERROR, State.SERVICE2, '"Sorry, I didn\'t catch that. What do you use to listen to music?"')
df.add_user_transition(State.SERVICE2, State.CDS, '[-vinyl, $medium=#ONT(mediums)]')
df.add_user_transition(State.SERVICE2, State.VINYLS, '[$medium=vinyl]')
df.add_user_transition(State.SERVICE2, State.OTHERMED, '[$medium=#ONT(othermediums)]')
df.add_user_transition(State.SERVICE2, State.PANDORA, '[{pandora, pandora radio}]')
df.add_user_transition(State.SERVICE2, State.APPLE, '[{apple, iphone, siri}]')
df.add_user_transition(State.SERVICE2, State.AMAZON, '[{amazon, amazonplus, amazonpremium}]')
df.add_user_transition(State.SERVICE2, State.YOUTUBE, '[{YouTube, youtube}]')
df.add_user_transition(State.SERVICE2, State.SPOTIFY, '[{spotify, spotify music}]')
df.set_error_successor(State.SERVICE2, State.SERV_ERROR2)
df.add_system_transition(State.SERV_ERROR2, State.ERR, '"Sorry, I still didn\'t catch that. Let\'s start over."')


df.add_user_transition(State.SERVICE, State.PANDORA, '[{pandora, pandora radio}]')
df.add_system_transition(State.PANDORA, State.OTHERSTREAM,
                         '"Pandora is great for discovering new music, and the free version allows you unlimited skips but has ads! Why do you like pandora?"')
df.add_user_transition(State.SERVICE, State.APPLE, '[{apple, iphone, siri}]')
df.add_system_transition(State.APPLE, State.OTHERSTREAM,
                         '"Apple music is well integrated with Siri! Why do you like apple music?"')
df.add_user_transition(State.SERVICE, State.AMAZON, '[{amazon, amazonplus, amazonpremium}]')
df.add_system_transition(State.AMAZON, State.OTHERSTREAM,
                         '"Amazon music is well integrated with alexa! why do you like Amazon music?"')
df.add_user_transition(State.SERVICE, State.YOUTUBE, '[{YouTube, youtube}]')
df.add_system_transition(State.YOUTUBE, State.OTHERSTREAM,
                         '"You can watch thousands of music videos on youtube, all for free! Why do you like youtube?"')
df.add_user_transition(State.SERVICE, State.SPOTIFY, '[{spotify, spotify music}]')
df. add_system_transition(State.SPOTIFY, State.OTHERSTREAM, '"Spotify has really cool insights about your listening habits! Why do you like spotify?"')


discount = r"[#ONT(discount)]"
df.add_user_transition(State.OTHERSTREAM, State.DISCOUNT, discount)
df.add_system_transition(State.DISCOUNT, State.ADJ, '"You\'re right. It\'s pretty affordable and there might be discounts if you\'re a student. How do you think music streaming has impacted the music industry?"')

playlists = r"[#ONT(playlists)]"
df.add_user_transition(State.OTHERSTREAM, State.PLAYLIST, playlists)
df.add_system_transition(State.PLAYLIST, State.ADJ, '"It\'s cool to create and share playlists! How do you think music streaming has impacted the music industry?"')

convenient = r"[#ONT(convenience)]"
df.add_user_transition(State.OTHERSTREAM, State.CONVENIENCE, convenient)
df.add_system_transition(State.CONVENIENCE, State.ADJ, '"You\'re right. its a convenient service. How do you think music streaming has impacted the music industry?"')

selection = r"[#ONT(selection)]"
df.add_user_transition(State.OTHERSTREAM, State.SELECTION, selection)
df.add_system_transition(State.SELECTION, State.ADJ, '"There are thousands of songs on there! How do you think music streaming has impacted the music industry?"')

shows = r"[#ONT(shows)]"
df.add_user_transition(State.OTHERSTREAM, State.SHOWS, shows)
df.add_system_transition(State.SHOWS, State.ADJ, '"I love when streaming services come with perks like that! How do you think music streaming has impacted the music industry?"')

downloading = r"[#ONT(offline)]"
df.add_user_transition(State.OTHERSTREAM, State.DOWNLOAD, downloading)
df.add_system_transition(State.DOWNLOAD, State.ADJ, '"Downloading music is especially convenient for long plane rides. How do you think music streaming has impacted the music industry?"')

discovery = r"[#ONT(discovery)]"
df.add_user_transition(State.OTHERSTREAM, State.DISCOVERY, discovery)
df.add_system_transition(State.DISCOVERY, State.ADJ, '"I like finding new music too! How do you think music streaming has impacted the music industry?"')

#Error
df.set_error_successor(State.OTHERSTREAM, State.STREAM_ERROR)
df.add_system_transition(State.STREAM_ERROR, State.OTHERSTREAM2, '"Sorry, I didn\'t catch that. What do you like about your streaming service?"')
df.add_user_transition(State.OTHERSTREAM2, State.DISCOUNT, discount)
df.add_user_transition(State.OTHERSTREAM2, State.PLAYLIST, playlists)
df.add_user_transition(State.OTHERSTREAM2, State.CONVENIENCE, convenient)
df.add_user_transition(State.OTHERSTREAM2, State.SELECTION, selection)
df.add_user_transition(State.OTHERSTREAM2, State.SHOWS, shows)
df.add_user_transition(State.OTHERSTREAM2, State.DOWNLOAD, downloading)
df.add_user_transition(State.OTHERSTREAM2, State.DISCOVERY, discovery)
df.set_error_successor(State.OTHERSTREAM2, State.STREAM_ERROR2)
df.add_system_transition(State.STREAM_ERROR2, State.ERR, '"Sorry, I still didn\'t catch that. Let\'s start over."')


df.add_system_transition(State.CDS, State.ADJ,
                         '[!$medium "s are dead. How do you think music streaming services have impacted the music industry?"]')

df.add_system_transition(State.VINYLS, State.ADJ,
                         '"Vinyls are great. I exclusively listen to vinyls because I think the music quality is much better. How do you think music streaming services have impacted the music industry?"')

df.add_system_transition(State.OTHERMED, State.ADJ, '"oh you use" $medium "? I prefer the sound quality of vinyls. How do you think music streaming services have impacted the music industry?"')


df.add_user_transition(State.ADJ, State.POSITIVE, '[#ONT(positive_response)]')
df.add_user_transition(State.ADJ, State.NEGATIVE, '[#ONT(negative_response)]')

# Error
df.set_error_successor(State.ADJ, State.ADJ_ERROR)
df.add_system_transition(State.ADJ_ERROR, State.ADJ2, '"Sorry, I didn\'t catch that. How do you think music streaming services have impacted the music industry?"')
df.add_user_transition(State.ADJ2, State.POSITIVE, '[#ONT(positive_response)]')
df.add_user_transition(State.ADJ2, State.NEGATIVE, '[#ONT(negative_response)]')
df.set_error_successor(State.ADJ2, State.ADJ_ERROR2)
df.add_system_transition(State.ADJ_ERROR2, State.ERR, '"Sorry, I still didn\'t catch that. Let\'s start over."')


df.add_system_transition(State.POSITIVE, State.ARTIST,
                         '"Yes sometimes it can be good, but Spotify has caused artists to create albums with more songs but theyre shorter songs, since artists are paid by song. Who\'s your favorite artist?"')
df.add_system_transition(State.NEGATIVE, State.ARTIST,
                         '"I agree, streaming services like Spotify only give artists a small percent of the profit. Who\'s your favorite artist?"')
df.add_user_transition(State.ARTIST, State.END, '[$fav_artist=#NER(person)]')


df.add_system_transition(State.END, State.TERMINAL,
                         '[!$fav_artist "is a great" #ARTIST_GENRE "artist!"]')


df.set_error_successor(State.ARTIST, State.ARTIST_ERROR)
df.add_system_transition(State.ARTIST_ERROR, State.TERMINAL, '"Hmm, I\'ve never heard of them. Guess I\'ll go listen to their music now!"')


df.add_user_transition(State.ERR, State.START, '/.*/')

if __name__ == '__main__':
    #df.precache_transitions()
    df.run(debugging=False)
