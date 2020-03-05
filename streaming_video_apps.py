from emora_stdm import KnowledgeBase, DialogueFlow, Macro
from enum import Enum

# idk push

class State(Enum):
    S0 = 0
    S1 = 1
    U1a = 2
    U1b = 3
    U1c = 4
    U1d = 5
    U1e = 16
    U1f = 17
    S2a = 6
    S2b = 7
    S2d = 8
    S3b = 10
    U2aa = 22
    S3a = 26
    S3e = 18
    S3f = 19
    U3ba = 11
    U3bb = 12
    U3bc = 13
    U3be = 15
    U3aa = 24
    U3ab = 25
    S4a = 27
    S4b = 28
    S4c = 20
    S4d = 21
    U4ca = 32
    U4cb = 150
    U4cc = 151
    U4cd = 152
    U4ce = 153
    S5b = 33
    U5ba = 34
    U5bb = 39
    U5bc = 41
    S6a = 35
    S6ab = 63
    S6c = 42
    U6ab = 37
    U6ac = 38
    S7bb = 43
    U7ba = 36
    S8b = 45
    U8bc = 44
    U8ba = 46
    U8bb = 47
    S9a = 50
    U9ab = 48
    S10a = 60
    U10aa = 49
    U10ab = 61
    S11b = 62
    U11a = 65
    U11b = 66
    ERR1 = 99
    ERR2 = 100
    ERR3 = 101
    ERR4 = 102
    ERR5 = 103
    ERR6 = 40
    ERR7 = 110
    ERR8 = 104
    ERR9= 105
    END1 = 23
    END2 = 29
    END3 = 30
    END4 = 64
    ENDF = 999


d_shows = {
    'bobs burgers': [
        'i love watching bob’s burgers. i am very excited for the feature film, that is scheduled to release in july 2020.',
        'comedy'],
    'adventure time': [
        ' adventure time is a really fun show, i love the creativity in the characters, like finn and jake, and scenery',
        'comedy'],
    'futurama': ['futurama is so funny, my favorite character is turanga leela.', 'comedy'],
    'rick and morty': [
        'rick and morty is so clever, i am constantly amazed by the creative plots the writers come up with to explore new worlds. my favorite is pickle rick.',
        'comedy'],
    'daria': ['i enjoy daria’s monotone and sarcastic sense of humor.', 'comedy'],
    'veronica mars': [
        'veronica mars is a really fun show. I heard that hulu is creating a new season with kristen bell to be released on hulu july 2019',
        'comedy'],
    '30 rock': ['i really love 30 rock, especially the development of liz lemon and jack donaghy’s relationship.',
                'comedy'],
    'community': [
        'looking back on community is so much fun, especially when considering what alison brie and donald glover have gone on to do.',
        'comedy'],
    'seinfeld': [
        'seinfeld is a hilarious american sitcom. I heard netflix acquired the global streaming rights recently, and therefore it will be switching video streaming services.',
        'comedy'],
    'party down': [
        'I have watched the first few episodes of party down. It was really fun to see jane lynch before glee and adam scott before parks and recreation.',
        'comedy'],
    'shrill': ['i really like aidy bryant on snl and therefore was incredible excited to hear about shrill.', 'comedy'],
    'brooklyn nine-nine': ['brooklyn nine-nine is so funny,  amy santiago is my favorite character.', 'comedy'],
    'the office': ['my favorite part of the office was watching jim and pam develop as a couple.', 'comedy'],
    'atlanta': [
        'watching atlanta continuously reminds me about the talent of donald glover, i cant wait to see what he does next.',
        'comedy'],
    '11.22.63': ['the show 11.22.63 was thrilling to watch, i especially enjoyed james franco’s performance.', 'drama'],
    'elementary': ['i enjoyed elementary, although i couldnt help comparing it  to the bbc sherlock series.', 'drama'],
    'killing eve': [
        'killing eve has been an incredibly successful show, which is a testament to the talent of phoebe waller-bridge as a writer',
        'drama'],
    'the good wife': ['she may have been called the good wife, but she was okay at best.', 'drama'],
    'er': [
        'i think er is a thrilling medical drama. it is very impressive that it won the peoples choice award for favorite television dramatic series every year from 1995 to 2002.',
        'drama'],
    'friday night lights': [
        'i am not a huge football fan, but i really enjoyed watching the team on friday night lights.', 'drama'],
    'the handmaid tale': ['the handmaid’s tale kept me on the edge of my seat, it was really intriguing to watch.',
                          'drama'],
    'castle rock': ['it is really cool that they were able to create a stephan kind multiverse in castle rock.',
                    'thriller'],
    'lost': ['i got really confused by the ending of lost.', 'thriller'],
    'twin peaks': ['twin peaks definitely kept me on the edge of my seat, im so glad it got a reboot in 2017.',
                   'thriller'],
    'agents of sheild': ['i love how agents of shield tied into the overall mcu', 'action'],
    'marvel runaways': ['it was really cool to see the mcu  as interpreted from a teen perspective in marvel runaways.',
                        'action'],
    'i, tonya': ['watching margot robbie in i, tonya gave me an entirely new perception of the nancy kerrigan scandal.',
                 'comedy'],
    'when harry met sally': [
        'my favorite scene from when harry met sally is definitely the one in the dinner, when the old lady chimes in.',
        'comedy'],
    'heathers': ['while i love the movie for heathers, the musical will always be my favorite version', 'comedy'],
    'sorry to bother you': [
        'the style of sorry to bother you was mesmerizing, i love the visual comedy that they created.', 'comedy'],
    'booksmart': ['i really enjoyed booksmart because it is a rare movie about genuine female friendship', 'comedy'],
    'ingrid goes west': ['i enjoy watching anything with aubrey plaza, she is one of my favorite comedians.', 'comedy'],
    'almost famous': ['almost famous is such a lovely coming of age movie, i loved the performance of kate hudson.',
                      'comedy'],
    'true grit': ['true grit is one of my favorite movies from the coen brothers.', 'drama'],
    'free solo': ['free solo freaked me out as a movie, i was so worried that alex honnold would fall.', 'drama'],
    'vice': ['i loved watching amy adams perform in vice, she is one of my favorite actresses.', 'drama'],
    'blood diamond': ['blood diamond was an okay movie, but definitely not my favorite leonardo dicaprio performance.',
                      'drama'],
    'if beale street could talk': [
        'if beal street could talk was a visually stunning film, and kept me thinking for days after.', 'drama'],
    'eyes wide shut': [
        'this film is is one of my favorites from stanley kubrick, although it was definitely confusing to watch.',
        'drama'],
    'mother': ['mother was a very creepy movie, but i really enjoyed the performance of jennifer lawrence.',
               'thriller'],
    'quiet place': ['i really enjoyed the creative use of soundscape in a quiet place to create a creepy environment.',
                    'thriller'],
    'annihilation': [
        'annihilation was a very entertaining film, i found the way they described the shimmer dimension intriguing.',
        'thriller'],
    'honeymoon': [
        'i really enjoyed watching rose leslie after seeing her in game of thrones, however the movie was very creepy.',
        'thriller'],
    'mission impossible': [
        'the mission impossible franchise is amazing, i can never get the theme song out of my head. ', 'action'],
    'bumblebee': ['bumblebee was my favorite installment of the transformers franchise.', 'action'],
    'santa clarita diet': [
        'i loved santa clarita diet and its sitcom approach to the zombie genre,especially as shown by the relationship of shiela and joel.',
        'comedy'],
    'queer eye': [
        'watching queer eye is so uplifting, my favorite parts are definetly when antony teaches them how to cook.',
        'comedy'],
    'big mouth': [
        'watching big mouth definitely makes me appreciate the friendship that nick kroll and john mulaney share.',
        'comedy'],
    'atypical': [
        'i appreciated watching atypical as it is a clear attempt to normalize special needs children by allowing people a reference within pop culture.',
        'comedy'],
    'one day at a time': ['i love one day at a time, especially the performance of rita moreno.', 'comedy'],
    'grace and frankie': [
        'watching grace and frankie was so entertaining,  i truly enjoyed the performances of lily tomlin and jane fonda.',
        'comedy'],
    'the ranch': [
        'the show ranch was very heartwarming and a great performance from ashton kutcher, it was wonderful to watch colts relationship with his father develop.',
        'comedy'],
    'dead to me': [
        'i have heard good things about dead to me, especially the tasteful blend of comedy while dealing with the serious issues of mourning.',
        'comedy'],
    'bojack horseman': ['I am so sad that bojack horseman ended but i really enjoyed the final season.', 'comedy'],
    'sex education': [
        'all i could think about when watching sex educaiton was that asa butterfeilds eyes are bluer than the sky.',
        'comedy'],
    'lucifer': ['the premise of lucifer is so interesting, it was a fun interpretation of how the devil would behave.',
                'drama'],
    'orange is the new black': [
        'although i loved watching orange is the new black, piper was my least favorite character, i prefer hearing about the other women',
        'drama'],
    '13 reasons why': [
        'i know that the series 13 reasons why ended up being very controversial for its depiction of mental health.',
        'drama'],
    'mind hunter': [
        'i love watching jonothan groff in his serious roll on the mind hunter, as previously he was so associated with musical theater.',
        'drama'],
    'designated survivor': [
        'designated survivor was an intriguing take on the classic political drama, as it focuses on someone who stumbles into power.',
        'drama'],
    'the witcher': ['henry cavill is a god amongst men.', 'drama'],
    'breaking bad': ['they did a great job in breaking bad of making walt a villain by the end.', 'drama'],
    'riverdale': [
        'i loved the first few seasons of  riverdale, but the plot got a bit too convoluted for me by the end.',
        'drama'],
    'stranger things': [
        'i loved how the relationship between joe keery and the kids developed in the second season of stranger things.',
        'thriller'],
    'chilling adventures of sabrina': [
        'i thought it was a fun way to reimagine the world of sabrina the teenage witch, setting apart from both the animated series and the  90s show.',
        'thriller'],
    'black mirror': [
        'watching black mirror always makes me think about my relationship with technology, the conversation we are having right now could be good fuel for another episode.',
        'thriller'],
    'you': [
        ' the show you freaked me out so much, as the performance of penn badgley made me question how well people really know their significant others.',
        'thriller'],
    'ozark': [
        'its crazy that jason bateman directs four episodes, while acting in them, for the first season of ozark.',
        'thriller'],
    'the umbrella academy': [
        ' i loved watching the umbrella academy! klaus was definitely my favorite character, i cant wait to watch him again in season 2.',
        'action'],
    'jessica jones': [
        'i really enjoyed the first season of jessica jones, i thought david tennent made for a truly compelling villain.',
        'action'],
    'sherlock': [
        'i can never figure out how to spell the name of the lead actor from sherlock, i believe it is bennyboy cucumber.',
        'action'],
    'miss americana': [
        'watching miss americana gave me an entirely new perspective from taylor swift, as it truly highlights the journey she has gone on as an artist.',
        'drama'],
    'to all the boys ive loved before': [
        'watching to all the boys i loved before was so much fun, i fell hard for peter kavinsky. I cant wait to watch the sequel.',
        'comedy'],
    'step brothers': ['will ferrell and john c reilly make for a hilarious duo in step brothers.', 'comedy'],
    'monty python and the holy grail': [
        'monty python and the holy grail is a classic comedy, i love informing my friends that their father smelt of elderberries.',
        'comedy'],
    'always be my maybe': [
        'funnily enough my favorite part of always be my maybe was the song about punching keaunu reeves that played during the credits.',
        'comedy'],
    'the perfect date': [
        'it was fun to see noah centineo take the lead in the perfect date after his success in to all the boys ive loved before.',
        'comedy'],
    'the notebook': [
        'the notebook is a classic of the romantic genre, somehow making a romantic exchange out of the desire of the lead to become a bird.',
        'drama'],
    'the irishman': [
        'the fact that netflix could get a big name hollywood director, like martin scorsese, to make a movie for them, like the irishman, says a lot about the rise of streaming services.',
        'drama'],
    'a silent voice': [
        'it was wonderful to see character growth as portrayed in the silent voice, although i am not sold  on the trope of the bully becoming the boyfriend.',
        'drama'],
    'roma': ['i loved the shooting style of roma, the black and white visuals built upon the story they were telling.',
             'drama'],
    'frances ha': [
        'watching the performance of greta gerwig performance in frances ha was absolutely beautiful, and predicts the kinds of complex characters she will write in little women and lady bird.',
        'drama'],
    'marriage story': [
        'adam driver and scarlett johansson both gave such honest performances in the marriage story, which made the film incredibly compelling to watch.',
        'drama'],
    'el camino': [
        'watching el camina was really nostalgic, as i could enjoy the characters from breaking bad one final time.',
        'thriller'],
    'zodiac': ['watching zodiac was truly freaky, but my favorite david fincher movie is probably se7en.', 'thriller'],
    'bird box': [
        'bird box became such a huge cultural phenomenon, it was definitely fun to see sandra bullock in such a different role.',
        'thriller'],
    'indiana jones': [
        ' i love the indiana jones franchise. it is great that it always feels like harrison ford is making it up as he goes along.',
        'action'],
    'spiderman': [
        'i love the spiderman franchise, my favorite depiction is miles morales, but i will always enjoy tom holland’s version.',
        'action'],
    'inglourious basterds': [
        'my favorite part of inglourious bastards is how they build tension in the first scene with the  nazi inspection, and the people hidden beneath the floorboards.',
        'action'],
    'black panther': ['black panther has one of the most well developed villains, killmonger,  in all of the MCU.',
                      'action'],
    'the dark knight': ['the performance of heath ledger in the dark knight will always be legendary.', 'action'],
    'parks and rec': [
        'parks and recreation is made incredible by the wonderful cast, that creates lovable and well rounded characters. Watching the relationship between leslie and ben develop is my favorite part.',
        'comedy'],
    'fleabag': [
        'watching fleabag created such a wonderfully unique comedic experience, the second season with the hot priest is my favorite.',
        'comedy'],
    'the marvelous mrs maisel': [
        'the combination of watching midge come into her own as comedian, as well as an independent women living in the 1950s is part of what makes the marvelous mrs maisel so special.',
        'comedy'],
    'psych': [
        'watching psych is so much fun as sean is such a compelling character. i will never fully understand why it is so associated with pineapples.',
        'comedy'],
    'curb your enthusiasm': [
        'it is really cool that the entire curb your enthusiasm show is improvised, with only an outline written for each episode.',
        'comedy'],
    'veep': [
        'when watching veep it was incredibly compelling to watch how they developed the characters in line with the changing political climate of the real world.',
        'comedy'],
    'the americans': [
        'watching the americans is made so much better by knowing that the leading couple keri russell and matthew rhys are a couple in real life as well.',
        'drama'],
    'modern love': [
        'watching each short film from modern love created little windows into several diverse depictions of love. The one with anne hathaway was my favorite.',
        'drama'],
    'orphan black': [
        'when watching orphan black i cannot help but be baffled that tatiana maslany is able to so convincingly play all of the clones at once.',
        'drama'],
    'the sopranos': ['watching the sopranos is incredible throughout, however the ending always gives me the chills.',
                     'drama'],
    'downton abbey': [
        ' i am excited to watch the downton abby movie, based off the show, as i can never get enough of the witty one liners from maggie smith.',
        'drama'],
    'band of brothers': [
        'the band of brothers mini series was a powerful depiction of wold war two. this was not a surprise as it was made by the same talented people involved in saving private ryan.',
        'drama'],
    'the wire': [
        'i have heard that the wire is considered to be one of the greatest tv shows of all time, which makes sense considering the incredible writing when depicting a crime ridden baltimore.',
        'drama'],
    'big love': [
        ' watching big love was an interesting dramatization of morman life, exploring the ramifications of a poligomous lifestyle.',
        'drama'],
    'true blood': [
        'the true blood franchise definitely built upon the growing vampire phenomenon from the twilight series and vampire diaries.',
        'drama'],
    'american horror story': [
        'american horror story is made a significantly better series because it switches location every season, allowing the shocks to be fresh. my favorite season is the murder house.',
        'thriller'],
    'hannibal': [
        ' the movie silence of the lambs was absolutely superb, and i am so glad they got to explore the story of such an iconic character in hannibal.',
        'thriller'],
    'mr robot': ['in my opinion the show mr robot was made incredible by the performance of rami malek.', 'thriller'],
    'banshee': [
        'i have heard banshee is a really fun over the top show, which is made incredible by the talented lead actors.',
        'thriller'],
    'jack ryan': [
        'when watching jack ryan i initially was thrown off by john krasinski in an action roll, as i was used to him as jim from the office.',
        'action'],
    'star trek': ['star trek is an incredible franchise, spock will always be my favorite character.', 'action'],
    'teen wolf': ['i love teen wolf, my favorite part was all of the snarky remarks made by styles.', 'action'],
    'legally blonde': [
        ' i love the legally blonde movie, but my favorite version will always be watching christian borle in the broadway musical.',
        'comedy'],  # start genres here
    'spy who dumped me': [
        'i found the spy who dumped me incredibly funny, as i love anything that kate mckinnon is involved.', 'comedy'],
    'clue': ['clue is an incredibly funny movie with so many comedic legends such as madeline kahn and tim curry.',
             'comedy'],
    'late night': [' i enjoyed late night, i have been a big fan of mindy kaling since her time on the office. ',
                   'comedy'],
    'eighth grade': [
        ' i enjoyed watching eighth grade as it was wonderful to see bo burnham successfully make the jump from stand up comedian to director.',
        'drama'],
    'lady bird ': ['watching lady bird made me cry multiple times, the story of mother daughter love is timeless.',
                   'drama'],
    'farwell': [
        'the farewell was an incredibly sincere movie. I loved the performance from awkwafina, and am really happy she won the golden globe.',
        'drama'],
    'the last black man in san francisco': [
        'the last black man in san francisco was a compelling movie, i enjoyed the performance from jimmie fails.',
        'drama'],
    'aeronauts': ['the aeronauts was a wonderful movie, the cgi used to create the sky environments were stunning.',
                  'drama'],
    'florida project': [
        'i loved watching the florida project as it was such a human story watching halley trying to be a decent parent.',
        'drama'],
    'hereditary': [
        'hereditary was an incredibly well done horror movie, i shiver every time i remember the scene with the daughter and the light pole.',
        'thriller'],
    'silence of the lambs': [
        'he silence of the lambs is an incredible movie, watching the escape of hannibal lecter was absolutely terrifying.',
        'thriller'],
    'cabin in the woods': [
        'when watching cabin in the woods i was surprised at how funny a film it was for a horror movie and the meta nature of the premise was incredibly entertaining.',
        'thriller'],
    'midsommar': ['it was incredible how effectively midsommar could scare me while being set in broad daylight.',
                  'thriller'],
    'phineas and ferb': [
        'the theme song of phineas and ferb never quite let me forget how many days there were in summer vacation.',
        'comedy'],
    'simpsons': ['my favorite character from the simpsons is bart.', 'comedy'],
    'zack and cody': ['it was really cool watching dylan and cole sprouse grow up on zack and cody.', 'comedy'],
    'gravity falls': [
        'watching gravity falls always felt disproportionately dark, but i loved going on adventures with mabel and dipper.',
        'comedy'],
    'hannah montana': ['hannah montana is incredibly fun, but it always makes me think about how miley cyrus is now. ',
                       'comedy'],
    'x men': [
        'i love the x men franchise.  My favorite character is rogue, because i think the compromising nature of her power makes her an intriguing character.',
        'action'],
    'agent carter': ['agent carter was a fun show, building off of my love for captain america.', 'action'],
    'mandalorian': ['baby yoda is so cute.', 'action'],
    'clone wars': ['i enjoyed the close wars tv show as it expanded the star wars universe.', 'action'],
    'hercules': [
        'although hercules is a wholly inaccurate depiction of mythology, i loved the music and found hades to be absolutely hilarious.',
        'comedy'],
    'the little mermaid': ['ariel from the little mermaid is one of the best disney princesses.', 'comedy'],
    'aladdin': ['i love robin williams in the original version of aladdin.', 'comedy'],
    'coco': [
        'the song remember me from coco is absolutely gorgeous, and was used at such powerful moments within the film.',
        'comedy'],
    'newsies': [
        'watching newsies is made so much fun because you get to watch a mini christian bale sing and dance before his batman days.',
        'comedy'],
    'frozen': [
        'when frozen came out it was huge phenomenon, it felt like i could never truly escape hearing someone sing let it go.',
        'comedy'],
    'a goofy movie': [
        'a goofy movie is always much better than i think it will be, the relationship between goofy and max is developed so beautifully, even making me cry at points.',
        'comedy'],
    '10 things i hate about you': [
        'my favorite scene in 10 things i hate about you is when patrick performs for kat on the bleachers to get a date.',
        'comedy'],
    'lady and the tramp': [
        'i have always wanted to recreate the scene from lady and the tramp where they are eating spaghetti.',
        'comedy'],
    'snow white': ['i love the depiction of the evil queen in snow white.', 'comedy'],
    'zootopia': [
        'i enjoyed zootopia a lot, it provided a great way to talk about important issues in a child friendly context.',
        'comedy'],
    'mulan': ['lets get down to business.', 'comedy'],
    'inside out': ['inside out was an wonderful pixar movie, all of the emotions were perfectly cast.', 'comedy'],
    'finest hours': ['the finest hours is a wonderful movie, i enjoyed the performance from chris pine.', 'drama'],
    'star wars': [' i love the star wars franchise, the music from john williams is iconic.', 'action'],
    'thor': ['i love the portrayal of thor from chris hemsworth, especially in the third film.', 'action'],
    'avengers': ['my favorite avenger is captain america, he has the glutes of america.', 'action'],
    'iron man': [
        'tony stark is a really fun superhero. even without the suit he is still a genius, billionaire, playboy philanthropist.',
        'action'],
    'guardians of the galaxy': ['i loved the way the incorporated classic 80s music in the guardians of the galaxy.',
                                'action'],
}

d_rec = {
    'hulu': {
        'show': {
            'comedy': 'community',
            'drama': 'the handmaid tale',
            'thriller': 'twin peaks',
            'action': 'agents of sheild',
        },
        'movie': {
            'comedy': 'i, tonya',
            'drama': 'if beale street could talk',
            'thriller': 'quiet place',
            'action': 'mission impossible'
        }
    },
    'amazon prime': {
        'show': {
            'comedy': 'fleabag',
            'drama': 'the americans',
            'thriller': 'hannibal',
            'action': 'jack ryan',
        },
        'movie': {
            'comedy': 'legally blonde',
            'drama': 'lady bird',
            'thriller': 'silence of the lambs',
            'action': 'mission impossible'
        },
    },
    'netflix': {
        'show': {
            'comedy': 'sex education',
            'drama': 'mind hunter',
            'thriller': 'black mirror',
            'action': 'jessica jones',
        },
        'movie': {
            'comedy': 'monty python and the holy grail',
            'drama': 'the irishman',
            'thriller': 'zodiac',
            'action': 'the dark knight'
        }
    },
    'disney plus': {
        'show': {
            'comedy': 'phineas and ferb',
            'action': 'mandalorian',
        },
        'movie': {
            'comedy': 'zootopia',
            'drama': 'finest hours',
            'action': 'guardians of the galaxy'
        }
    }
}


class SPECIFIC(Macro):
    def run(self, ngrams, vars, args) -> str:
        if 'curVid' in vars:
            s = vars['curVid']
            x = d_shows.get(s)[0]
            y = d_shows.get(s)[1]
        vars['genre'] = d_shows.get(s)[1]
        if s:
            return x + ' is ' + y + ' your favorite genre?'


class TVorMovie(Macro):
    def run(self, ngrams, vars, args) -> str:
        tv_list = ["tv", "tv show", "tv shows", "television", "television shows", "series", "show", "shows"]
        movie_list = ["movie", 'movies', "film", "films", "feature film", "feature films", "feature"]
        if 'mediaType' in vars:
            if vars['mediaType'] in tv_list:
                return "show"
            if vars['mediaType'] in movie_list:
                return "movie"
            else:
                return vars['mediaType']
        return ''


class REC(Macro):
    def run(self, ngrams, vars, args) -> str:
        mt = vars['mediaType']
        st = vars['stream']
        gen = vars['genre']
        if not 'curVid' in vars:
            vars['curVid'] = ""

        tv_list = ["tv", "tv show", "tv shows", "television", "television shows", "series", "show", "shows"]
        movie_list = ["movie", 'movies', "film", "films", "feature film", "feature films", "feature"]

        if vars['mediaType'] in movie_list:
            mt = 'movie'
        if vars['mediaType'] in tv_list:
            mt = 'show'

        prime_list = ["prime", "amazon"]
        dp_list = ["plus", "disney", "dp"]

        if vars['stream'] in dp_list:
            st = 'disney plus'
        if vars['stream'] in prime_list:
            st = 'amazon prime'

        comedy_list = ["funny", "silly", "absurd"]
        drama_list = ["sad", "heartbreaking", "thought provoking"]
        action_list = ["fighting", "fight", "battle", "spy", "superhero"]
        thriller_list = ["creepy", "spooky", "scary", "exhilarating", "horror"]

        if gen in comedy_list:
            gen = 'comedy'
        if gen in drama_list:
            gen = 'drama'
        if gen in action_list:
            gen = 'action'
        if gen in thriller_list:
            gen = 'thriller'

        if (st == 'disney plus') and (gen == 'drama') and (mt == 'show'):
            return "hmm i was trying to give you a recommendation but I don't know any dramas on disney plus. " \
                   "you should give mandalorian a try - i love baby yoda. what do you think?"

        elif (st == 'disney plus') and (gen == 'thriller') and (vars['curVid'] != 'mandalorian'):
            return "hmm i was trying to give you a recommendation but I don't know any thrillers on disney plus. " \
                   "you should give mandalorian a try - i love baby yoda. what do you think?"

        elif (st == 'disney plus') and (gen == 'thriller') and (vars['curVid'] == 'mandalorian'):
            return "hmm i was trying to give you a recommendation but I don't know any thrillers on disney plus. " \
                   "it might not be your cup of tea but phineas and ferb can be thrilling at times. will you give it a try?"

        else:
            rec = d_rec[st][mt][gen]
            if vars['curVid'] == rec:
                return "hmm I was trying to give you a recommendation but " + vars['curVid'] + \
                       " is exactly what I was thinking of. I'll be sure to have a recommendation for you next time"
            else:
                return "you should watch " + rec + ". it's a " + gen +" "+ mt + " on " + st + " that i think you'll enjoy. will you give" \
                                                                                " it a shot? "


ontology = {
    "ontology": {
        "negative": [
            "no",
            "nope",
            "dont",
            "do not",
            "not really",
            "nah",
            "it is",
            "definitely not",
            "haven't",
            "not recently",
            "never",
            "none"
        ],
        "positive": [
            "yes",
            "yeah",
            "i do",
            "sure"
            "it is not",
            "it isnt",
            "yep",
            "yup",
            "sure",
            "of course",
            "definitely"
        ],
        "conjunction": [
            "and",
            "both"
        ],
        "multiple": [
            "a lot",
            "a few",
            "a couple",
            "many",
            "some"
        ],
        "watch": [
            "spectate",
            "partake",
            "enjoy",
            "view",
            "indulge"
        ],
        "streamServices": [
            "hulu",
            "amazon prime",
            "netflix",
            "disney plus",
            "plus"
        ],
        "amazon prime": [
            "prime",
            "amazon"
        ],
        "disney plus": [
            "plus",
            "disney",
            "dp"
        ],
        "netflix": [

        ],
        "hulu": [

        ],
        "cheap": [
            "cheap",
            "low price",
            "good value",
            "do not pay a lot",
            "only pay",
            "good price",
            "good deal",
            "value"
        ],
        "howTowatch": [
            "rentLibs",
            "ownTvPirate"
        ],
        "variety": [
            "option",
            "choice",
            "multitude",
            "plenty",
            "a lot",
            "many"
        ],
        "rentLibs": [
            "rent",
            "library",
            "libs",
            "loan"
        ],
        "ownTvPirate": [
            "online",
            "pirate",
            "own",
            "my tv"
        ],
        "tv show": [
            "tv",
            "tv shows",
            "television",
            "television shows",
            "series",
            "shows"
        ],
        "movie": [
            "movie",
            'movies',
            "film",
            "films",
            "feature film",
            "feature films",
            "feature"
        ],
        "specVids": [
            'bobs burgers',
            'adventure time',
            'futurama',
            'rick and morty',
            'daria',
            'veronica mars',
            '30 rock',
            'community',
            'seinfeld',
            'party down',
            'shrill',
            'brooklyn nine-nine',
            'the office',
            'atlanta',
            '11.22.63',
            'elementary',
            'killing eve',
            'the good wife',
            'er',
            'friday night lights',
            'the handmaid tale',
            'castle rock',
            'lost',
            'twin peaks',
            'agents of sheild',
             'marvel runaways',
            'i, tonya',
            'when harry met sally',
            'heathers',
            'sorry to bother you',
            'booksmart',
            'ingrid goes west',
            'almost famous',
            'true grit',
            'free solo',
            'vice',
            'blood diamond',
            'if street could talk',
            'eyes wide shut',
            'mother',
            'quiet place',
            'annihilation',
            'honeymoon',
            'mission impossible',
            'bumblebee',
            'santa clarita diet',
            'queer eye',
            'big mouth',
            'atypical',
            'one day at a time',
            'grace and frankie',
            'the ranch',
            'dead to me',
            'bojack horseman',
            'sex education',
            'lucifer',
            'orange is the new black',
            '13 reasons why',
            'mind hunter',
            'designated survivor',
            'the witcher',
            'breaking bad',
            'riverdale',
            'stranger things',
            'chilling adventures of sabrina',
            'black mirror',
            'you',
            'ozark',
            'the umbrella academy',
            'jessica jones',
            'sherlock',
            'miss americana',
            'to all the boys ive loved before',
            'step brothers',
            'monty python and the holy grail',
            'always be my maybe',
            'the perfect date',
            'the notebook',
            'the irishman',
            'a silent voice',
            'roma',
            'frances ha',
            'marriage story',
            'el camino',
            'zodiac',
            'bird box',
            'indiana jones',
            'spiderman',
            'inglourious basterds',
            'black panther',
            'the dark knight',
            'parks and rec',
            'fleabag',
            'the marvelous mrs maisel',
            'psych',
            'curb your enthusiasm',
            'veep',
            'the americans',
            'modern love',
            'orphan black',
            'the sopranos',
            'downton abbey',
            'band of brothers',
            'the wire',
            'big love',
            'true blood',
            'american horror story',
            'hannibal',
            'mr robot',
            'banshee',
            'jack ryan',
            'star trek',
            'teen wolf',
            'legally blonde',
            'spy who dumped me',
            'clue',
            'late night',
            'eighth grade',
            'lady bird ',
            'farwell',
            'the last black man in san francisco',
            'aeronauts',
            'florida project',
            'hereditary',
            'silence of the lambs',
            'cabin in the woods',
            'midsommar',
            'phineas and ferb',
            'simpsons',
            'zack and cody',
            'gravity falls',
            'hannah montana',
            'x men',
            'agent carter',
            'mandalorian',
            'clone wars',
            'hercules',
            'the little mermaid',
            'aladdin',
            'coco',
            'newsies',
            'frozen',
            'a goofy movie',
            '10 things i hate about you',
            'lady and the tramp',
            'snow white',
            'zootopia',
            'mulan',
            'inside out',
            'finest hours',
            'star wars',
            'thor',
            'avengers',
            'iron man',
            'guardians of the galaxy'
        ],
        "genre": [
            "comedy",
            "action",
            "thriller",
            "drama"
        ],
        "comedy": [
            "funny",
            "silly",
            "absurd"
        ],
        "drama": [
            "sad",
            "heartbreaking",
            "thought provoking"
        ],
        "action": [
            "fighting",
            "fight",
            "battle",
            "spy",
            "superhero"
        ],
        "thriller": [
            "creepy",
            "spooky",
            "scary",
            "exhilarating",
            "horror",
        ]
    }
}

knowledge = KnowledgeBase()
knowledge.load_json(ontology)
df = DialogueFlow(State.S0, initial_speaker=DialogueFlow.Speaker.SYSTEM, kb=knowledge,
                  macros={"SPECIFIC": SPECIFIC(), "TVorMovie": TVorMovie(), "REC": REC()})

#  NaTex
netflix_prime = r"[!-{[#ONT(hulu)], [#ONT(disney plus)], " \
                r"[#ONT(negative)]}, {[$stream=#ONT(netflix)], [$stream=#ONT(amazon prime)]}]"
hulu = r"[!-{[#ONT(amazon prime)], [#ONT(disney plus)], [#ONT(netflix)], [#ONT(negative)]}, [$stream=#ONT(hulu)]]"
dplus = r"[!-{[#ONT(amazon prime)], [#ONT(hulu)], [#ONT(netflix)], [#ONT(negative)]}, [$stream=#ONT(disney plus)]]"

affirm = r"[!-[#ONT(negative)],[#ONT(positive)]]"
deny = r"[!-[#ONT(positive)],[#ONT(negative)]]"

pirate_own = r"[!-[#ONT(rentLibs)], [#ONT(ownTvPirate)]]"
rent = r"[!-[#ONT(ownTVPirate)], [#ONT(rentLibs)]]"

cheap = r"[!-[#ONT(variety)], [#ONT(cheap)]]"
variety = r"[!-[#ONT(cheap)], [#ONT(variety)]]"

tv_movie = r"[!-[#ONT(conjunction)], {[$mediaType=#ONT(tv show)], [$mediaType=#ONT(movie)]}]"

# End State
df.add_system_transition(State.ENDF, State.ENDF, 'Conversation Ended')
df.set_error_successor(State.ENDF, error_successor=State.ENDF)

# Turn 0
df.add_system_transition(State.S0, State.S1, '"Do you use any movie streaming services?"')
df.add_user_transition(State.S1, State.U1a,
                       '[!-{[#ONT(streamServices)], [#ONT(multiple)], [#ONT(negative)]}, [#ONT(positive)]]')
df.add_user_transition(State.S1, State.U1b, netflix_prime)
df.add_user_transition(State.S1, State.U1c,
                       '[!-{[#ONT(streamServices)], [#ONT(negative)]}, <[#ONT(multiple)], #ONT(positive)>]')
df.add_user_transition(State.S1, State.U1e, hulu)
df.add_user_transition(State.S1, State.U1f, dplus)
df.add_user_transition(State.S1, State.U1d,
                       "[!-{[#ONT(watch)], [#ONT(positive)], [#ONT(streamServices)]} [#ONT(negative)]]")
df.add_user_transition(State.S1, State.END1,
                       "[!-{[#ONT(streamServices)],[#ONT(positive)]}, [#ONT(negative)], [#ONT(watch)]]")

# # Error Handling
df.set_error_successor(State.S1, error_successor=State.ERR1)
df.add_system_transition(State.ERR1, State.S1, '"i didnt catch that. which of netflix, '
                                               'hulu, amazon prime, and disney plus do you use the most?"')
df.set_error_successor(State.ERR1, error_successor=State.ERR1)

# "No" branch
df.add_system_transition(State.U1d, State.S2a, '"do you watch movie or tv shows frequently?"')
df.add_user_transition(State.S2a, State.END1, "[!-{[#ONT(howTowatch)], [#ONT(positive)]}, [#ONT(negative)]]")
df.add_system_transition(State.END1, State.END1, '"thats too bad. it was nice to talk to you"')
df.set_error_successor(State.END1, error_successor=State.ENDF)

df.add_user_transition(State.S2a, State.U2aa, "[!-{[#ONT(howTowatch)], [#ONT(negative)]}, [#ONT(positive)]]")
df.add_user_transition(State.S2a, State.U3aa, pirate_own)
df.add_user_transition(State.S2a, State.U3ab, rent)
df.set_error_successor(State.S2a, error_successor=State.ERR3)
df.add_system_transition(State.ERR3, State.S2a, '"i didnt catch that. do you watch a lot of television?"')
df.set_error_successor(State.ERR3, error_successor=State.ERR3)

df.add_system_transition(State.U2aa, State.S3a, '"how do you watch tv and movies?"')
df.add_user_transition(State.S3a, State.U3aa, pirate_own)
df.add_user_transition(State.S3a, State.U3ab, rent)
df.set_error_successor(State.S3a, error_successor=State.ERR4)
df.add_system_transition(State.ERR4, State.S4b, '"do you find how you currently watch to be convenient?"')

df.add_system_transition(State.U3ab, State.S4b, '"that sounds like it could be a hassle.'
                                                ' is it convenient to watch that way?"')
df.add_user_transition(State.S4b, State.END2, affirm)
df.add_user_transition(State.S4b, State.END3, deny)
df.set_error_successor(State.S4b, error_successor=State.ERR8)
df.add_system_transition(State.ERR8, State.S4b, '"if you had to decide, would you say yes or no"')

df.set_error_successor(State.END2, error_successor=State.ENDF)
df.add_system_transition(State.END2, State.END2, '"im glad you have a way to watch. good bye!"')

df.add_system_transition(State.U3aa, State.S4a, '"when i do that i can never find the shows i want. '
                                                'do you have enough options?"')
df.add_user_transition(State.S4a, State.END2, affirm)
df.add_user_transition(State.S4a, State.END3, deny)
df.set_error_successor(State.S4a, error_successor=State.ERR9)
df.add_system_transition(State.ERR9, State.S4a, '"if you had to decide, would you say yes or no"')

df.set_error_successor(State.END3, error_successor=State.END3)
df.add_system_transition(State.END3, State.END3, '"you should consider getting a streaming service! good bye!"')

# Yes Branch
# # Variety section
df.add_system_transition(State.U1c, State.S2b, '"wow, you have more than one service! which one is your favorite?"')
df.add_user_transition(State.S2b, State.U1b, netflix_prime)
df.add_user_transition(State.S2b, State.U1e, hulu)
df.add_user_transition(State.S2b, State.U1f, dplus)
df.set_error_successor(State.S2b, error_successor=State.ERR1)

df.add_system_transition(State.U1a, State.S2d, '"thats awesome. which streaming service do you use most regularly?"')
df.add_user_transition(State.S2d, State.U1b, netflix_prime)
df.add_user_transition(State.S2d, State.U1e, hulu)
df.add_user_transition(State.S2d, State.U1f, dplus)
df.set_error_successor(State.S2d, error_successor=State.ERR1)

df.add_system_transition(State.U1b, State.S3b, 'what do you like about $stream"?"')
df.add_system_transition(State.U1e, State.S3e, 'what do you like about $stream"?"')
df.add_system_transition(State.U1f, State.S3f, 'what do you like about $stream"?"')

# # # Have hulu - what do you like?
df.add_user_transition(State.S3e, State.U3ba, cheap)
df.add_user_transition(State.S3e, State.U3be, variety)
df.set_error_successor(State.S3e, error_successor=State.ERR2)

# # # have disney plus-what do you like?
df.add_user_transition(State.S3f, State.U3bb, cheap)
df.add_user_transition(State.S3f, State.U3bc, variety)
df.set_error_successor(State.S3f, error_successor=State.ERR2)

# # # else- what do you like
df.add_user_transition(State.S3b, State.U3bb, cheap)
df.add_user_transition(State.S3b, State.U3be, variety)
df.set_error_successor(State.S3b, error_successor=State.ERR2)

df.add_system_transition(State.ERR2, State.S5b,
                         'there are lots of things to enjoy about streaming services. do you watch more movies or tv shows on $stream"?"')
# # # from CHEAP options
df.add_system_transition(State.U3ba, State.S4c, '"i have heard hulu is a really great deal, especially '
                                                'when paired with spotify. do you like it?"')
df.add_system_transition(State.U3bb, State.S4d,
                         'i have heard hulu is a really great deal, especially when paired with spotify. would you be interested in switching from $stream to hulu"?"')

# # # from VARIETY options
df.add_system_transition(State.U3bc, State.S4c, '"i have heard disney plus has wonderful variety, as disney owns fox,'
                                                ' marvel, lucas films and abc. do you like it?"')
df.add_system_transition(State.U3be, State.S4d,
                         'i have heard disney plus has wonderful variety, as disney owns fox, marvel, lucas films and abc. would you be interested in switching from $stream to disney plus"?"')

# # # Transition to TV/Movie Discussion
df.add_user_transition(State.S4c, State.U4ca, affirm)
df.add_user_transition(State.S4c, State.U4cb, deny)
df.add_user_transition(State.S4d, State.U4cc, affirm)
df.add_user_transition(State.S4d, State.U4cd, deny)
df.set_error_successor(State.S4c, error_successor=State.U4ce)
df.set_error_successor(State.S4d, error_successor=State.U4ce)

# # TV or Movies?
df.add_system_transition(State.U4ca, State.S5b,
                         'im glad you like it. do you tend to watch more tv shows or movies on $stream"?"')
df.add_system_transition(State.U4cb, State.S5b,
                         'awww, maybe consider switching from $stream in the future. for now, do you tend to watch more tv shows or movies on $stream"?"')
df.add_system_transition(State.U4cc, State.S5b,
                         'we should talk again once you switch. for now, do you tend to watch more tv shows or movies on $stream"?"')
df.add_system_transition(State.U4cd, State.S5b,
                         'fair enough. do you tend to watch more tv shows or movies on $stream"?"')
df.add_system_transition(State.U4ce, State.S5b,
                         'cool"!" so anyway, do you tend to watch more tv shows or movies on $stream"?"')

df.add_user_transition(State.S5b, State.U5ba, tv_movie)
df.set_error_successor(State.S5b, error_successor=State.ERR6)

df.add_system_transition(State.ERR6, State.S5b, '"but if you had to pick only tv or movies for the rest of your life, '
                                                'which would you pick?"')
df.add_user_transition(State.ERR6, State.U5ba, tv_movie)
df.set_error_successor(State.ERR6, error_successor=State.ERR6)

# # THE HARD PART
df.add_system_transition(State.U5ba, State.S6a, 'whats your favorite #TVorMovie on $stream"?"')
df.add_user_transition(State.S6a, State.U7ba, '[$curVid=#ONT(specVids)]')
df.add_user_transition(State.S6a, State.U6ab, '[!-[#ONT(specVids)],[#ONT(negative)]]')
df.set_error_successor(State.S6a, error_successor=State.ERR7)

df.add_system_transition(State.U7ba, State.S9a, r'[!#SPECIFIC]')
df.add_system_transition(State.U6ab, State.S6a,
                         'im sorry you dont have a favorite. do you have a #TVorMovie youve liked on $stream"?"')
df.add_system_transition(State.ERR7, State.S8b, 'i havent heard of that #TVorMovie can you tell me about it')


df.add_user_transition(State.S8b, State.U8ba, "[$genre=#ONT(genre)]")
df.set_error_successor(State.S8b, error_successor=State.U8bb)
df.add_system_transition(State.U8ba, State.S9a,
                         'i really enjoy $mediaType like that, thanks for the recommendation"!" is $genre your favorite genre"?"')
df.add_system_transition(State.U8bb, State.S10a,
                         'i will have to look into that #TVorMovie"!" what is your favorite genre"?"')


df.add_user_transition(State.S9a, State.U10aa, affirm)
df.add_user_transition(State.S9a, State.U9ab, deny)
df.set_error_successor(State.S9a, error_successor=State.U9ab)

df.add_system_transition(State.U9ab, State.S10a, 'whats your favorite genre"?"')

df.add_user_transition(State.S10a, State.U10aa, "[$genre=#ONT(genre)]")
df.set_error_successor(State.S10a, error_successor=State.U10ab)
df.add_system_transition(State.U10ab, State.S10a, 'do you tend to like thriller, drama, comedy or action"?"')


df.add_system_transition(State.U10aa, State.S11b, r'[!#REC]')
df.add_user_transition(State.S11b, State.U11a, affirm)
df.add_user_transition(State.S11b, State.U11b, deny)
df.set_error_successor(State.S11b, error_successor=State.END4)

df.add_system_transition(State.U11a, State.ENDF, "im glad you plan on watching, lets talk about it next time")
df.add_system_transition(State.U11b, State.ENDF, "thats too bad. ill try to give you a better recommendation next time")
df.add_system_transition(State.END4, State.ENDF, "i had a lot of fun talking to you, lets speak again soon")


df.run(debugging=False)