from emora_stdm import KnowledgeBase, DialogueFlow
from enum import Enum, auto
from emora_stdm import Macro

class State(Enum):
    S1 = auto()
    U1 = auto()
    S2a = auto()
    S2b = auto()
    S2c = auto()
    S2d = auto()
    S2e = auto()
    S2f = auto()
    S2g = auto()
    U2a = auto()
    S3a = auto()
    U3a = auto()
    CONSULT = auto()
    FINANCE = auto()
    TECH = auto()
    DK = auto()
    SAME = auto()
    U4a = auto()
    U4b = auto()
    U4c = auto()
    S5 = auto()
    S5b = auto()
    U5 = auto()
    U5b = auto()
    S6a = auto()
    S6b = auto()
    S6c = auto()
    U6 = auto()
    ERR1 = auto()
    ERR2 = auto()
    ERR3 = auto()
    ERR4 = auto()
    ERR5 = auto()
    END = auto()


#industry-position
ind_pos = {"ontology": {"ontindustry":["ontconsulting","ontfinance","onttechnology"],
                        "ontconsulting":["business analyst", "associate consultant", "consultant"],
                        "ontfinance":["investment banking","sales and trading","quantitative analyst","wealth management","asset management","corporate banking","capital markets"],
                        "onttechnology":["software engineer","software developer","swe","sde","data analyst","full stack developer","uiux","ui","ux","ios app developer","android app developer","web developer","back end","front end","program manager","project manager","product manager","pm"]
                        }
          }

#industry-company
ind_comp = {"ontology": {"ontind":["ontconsultin","ontfinanc","onttechnolog"],
                         "ontconsultin":["mckinsey","bain","bcg","boston consulting group","deloitte","pwc","kpmg","at kearny","atkearny","accenture","ernest and young","ey","grant thorton","gt"],
                         "ontfinanc":["goldman saches","goldman","gs","jp morgan","jpm","morgan stanley","ms","bank of america","boa","wells fargo","citi","citigroup","citibank","td bank","capital one","deutsche bank","db","barclays","ubs","credit suisse","cs","merrill lynch","baml"],
                         "onttechnolog":["microsoft","apple","google","amazon","ibm","intel","facebook","oracle","linkedin","paypal","samsung","alphabet","huawei","dell","hp","cisco"]
                        }
           }

#dictionaries for response
pos_skill = {"business analyst": "demonstrated aptitude for analytics, the ability to work collaboratively in a team environment, and communication skills",
             "associate consultant": "demonstrated aptitude for analytics, the ability to work collaboratively in a team environment, and communication skills",
             "consultant": "demonstrated aptitude for analytics, the ability to work collaboratively in a team environment, and communication skills",
             "investment banking": "the ability to work in a fast-paced environment, knowledge of deal structuring and closing principals, and impeccable analytical skills",
             "ib": "the ability to work in a fast-paced environment, knowledge of deal structuring and closing principals, and impeccable research, quantitative and analytical skills",
             "sales and trading": "the proficiency in modeling, superior written and verbal skills, and the ability to work well in a fast-paced, team oriented environment",
             "quantitative": "the ability to identify and manage complex issues, strong multi-tasking skills, and large scale data querying and analysis skills",
             "wealth management": "ability to quickly analyze information and creatively reach solutions, understanding of the various businesses and products within the wealth management space",
             "corporate": "knowledge in accounting and finance, as well as fundamental understanding of valuation theory, methodologies, and applications",
             "capital market": "knolwdge in Fixed Income products and strong credit, financial analysis and modeling skills",
             "software": "the ability to develop software in Java, Ruby on Rails, C++ or other programming languages and experience with test-driven development",
             "data analyst": "strong knowledge of SQL, strong analytical skills, and the ability to collect, organize, analyze, and disseminate significant amounts of information",
             "full stack": "experience working across the full technical stack and knowledge of both frontend and backend",
             "uiux": "knowledge of wireframe tools such as Wireframe.cc and InVision as well as up-to-date knowledge of design software like Adobe Illustrator and Photoshop",
             "ui":"knowledge of wireframe tools such as Wireframe.cc and InVision as well as up-to-date knowledge of design software like Adobe Illustrator and Photoshop",
             "ux":"proficiency in visual design programs such as Adobe Photoshop and professional written and interpersonal skills",
             "ios": "proficiency in Objective-C, Swift, and Cocoa Touch, experience with iOS frameworks, and experience with design patterns such as MVC, Singleton",
             "android": "strong knowledge of Android SDK, Knowledge of the open-source Android ecosystem, and familiarity with RESTful APIs to connect Android applications to backend services",
             "web": "knowledge pf HTML, CSS, JavaScript, jQuery, and ReactJS, as well as experience in developing web applications supporting traditional web or mobile user interfaces",
             "back end": "fluency of Java, PHP, or Python, strong understanding of the web development cycle, and strong problem solving skills",
             "front end": "HTML, CSS, JavaScript and jQuery",
             "pm": "software Development coding experience, leadership skills, and managing multiple projects simultaneously",
             "program manager": "software Development coding experience, leadership skills, and managing multiple projects simultaneously",
             "project manager": "software Development coding experience, leadership skills, and managing multiple projects simultaneously",
             "product manager": "software Development coding experience, leadership skills, and managing multiple projects simultaneously"
            }

# city-industry dictionary
place_ind = {
        "new york": "finance and consulting",
        "ny": "finance and consulting",
        "la": "technology",
        "los angeles": "technology",
        "chicago": "technology and finance",
        "dallas": "technology and finance",
        "washington dc": "technology",
        "dc": "technology",
        "west": "technology",
        "east": "finance",
        "bay": "technology",
        "san francisco": "technology, finance and consulting",
        "sf": "technology, finance and consulting",
        "houston": "technology",
        "boston": "technology and consulting",
        "bos": "technology and consulting",
        "atl": "technology and finance",
        "atlanta": "technology and finance",
        "seattle": "technology",
        "sea": "technology",
        "san jose": "technology"
        }

#industry-company
industry_company={
    "finance": "Goldman Sachs, JP Morgan and CitiBank",
    "consulting": "McKinsey, Bain and Boston Consulting Group",
    "tech": "Facebook, LinkedIn, Apple and Google",
    "it": "Facebook, LinkedIn, Apple and Google"
    }

class placeInd(Macro):
    def run(self, ngrams, vars, args):
        if 'loc' in vars:
            for key, value in place_ind.items():
                if key in vars['loc']:
                    return value

class indComp(Macro):
    def run(self, ngrams, vars, args):
        if 'industry' in vars:
            for key, value in industry_company.items():
                if key in vars['industry']:
                    return value

class posSkill(Macro):
    def run(self, ngrams, vars, args):
        if 'pos' in vars:
            for key, value in pos_skill.items():
                if key in vars['pos']:
                    return value

knowledge = KnowledgeBase()
knowledge.load_json(ind_pos)
knowledge.load_json(ind_comp)
df = DialogueFlow(State.S1, initial_speaker=DialogueFlow.Speaker.SYSTEM, kb=knowledge, macros={"placeInd": placeInd(),"indComp":indComp(),"posSkill":posSkill()})

df.add_system_transition(State.S1, State.U1, '"Where do you want to work?"')
df.add_user_transition(State.U1, State.S2a, '[$loc={new york,ny,la,los angeles,chicago,dallas,washington dc,dc,west,east,bay,san francisco,sf,houston,boston,bos,atl,atlanta,seattle,sea,san jose}]', score=1)
df.add_user_transition(State.U1, State.S2b, '[$loc={new york,ny,la,los angeles,chicago,dallas,washington dc,dc,west,east,bay,san francisco,sf,houston,boston,bos,atl,atlanta,seattle,sea,san jose}]')
df.add_user_transition(State.U1, State.S2c, '[$comp=#ONT(ontfinanc)]', score = 2)
df.add_user_transition(State.U1, State.S2d, '[$comp=#ONT(ontconsultin)]', score = 2)
df.add_user_transition(State.U1, State.S2e, '[$comp=#ONT(onttechnolog)]', score = 2)
df.add_user_transition(State.U1, State.S2f, '[$comp=#NER(org)]', score = 1)
df.add_user_transition(State.U1, State.S2g, '[{dont know,do not know,unsure,[not,{sure,certain,considered,consider,thought}],hard to say,no idea,uncertain,[!no {opinion,opinions,idea,ideas,thought,thoughts,knowledge}]}]')
df.set_error_successor(State.U1, error_successor=State.ERR1)

df.add_system_transition(State.S2a, State.U2a, '[!Sure"." $loc is a great place to work"!" There are a lot of #placeInd companies there"." What industry are you interested in"?"]')
df.add_system_transition(State.S2b, State.U2a, '[!I also think $loc is a great place to work"!" There are a lot of #placeInd companies there"." What industry are you interested in"?"]')
df.add_system_transition(State.S2g, State.U2a, '"Oh it is fine that you have not decide where to work at. Do you have an industry that you are interested in?"')
df.add_system_transition(State.S2c, State.U3a, '[!$comp is a great bank"." What position in $comp are you interested in"?"]')
df.add_system_transition(State.S2d, State.U3a, '[!$comp is a great consulting firm"." What position in $comp are you interested in"?"]')
df.add_system_transition(State.S2e, State.U3a, '[!$comp is a great technology company"." What position in $comp are you interested in"?"]')
df.add_system_transition(State.S2f, State.U3a, '[!$comp is a great company to work for"." What position in $comp are you interested in"?"]')
df.add_system_transition(State.ERR1, State.U2a, '"I am not familiar with that place. What industry do you want to work in?"')

df.add_user_transition(State.U2a, State.S3a, '[$industry={consulting,finance,tech,technology,it}]')
df.set_error_successor(State.U2a, error_successor=State.ERR2)
df.add_system_transition(State.S3a, State.U1, '[!$industry is a very promising industry to work in"." I know #indComp are famous in the $industry industry"." What company in $industry do you want to work for"?"]')
df.add_system_transition(State.ERR2, State.U3a, '"Umm...I am not very familiar with this industry. What kind of position would you like to work at?"')

df.add_user_transition(State.U3a, State.CONSULT, '[$pos=#ONT(ontconsulting)]')
df.add_user_transition(State.U3a, State.FINANCE, '[$pos=#ONT(ontfinance)]')
df.add_user_transition(State.U3a, State.TECH, '[$pos=#ONT(onttechnology)]')
df.add_user_transition(State.U3a, State.DK, '[{dont know,do not know,unsure,[not,{sure,certain,considered,consider,thought}],hard to say,no idea,uncertain,[!no {opinion,opinions,idea,ideas,thought,thoughts,knowledge}]}]')
df.set_error_successor(State.U3a, error_successor=State.ERR3)
df.add_user_transition(State.U3a, State.SAME, '[{same,similar}]')

df.add_system_transition(State.CONSULT, State.U4a, '[!Many consulting companies are hiring great $pos"." Why do you want to become a $pos "?"]')
df.add_system_transition(State.FINANCE, State.U4a, '[!Many banks are looking for great $pos analysts"." Why do you want to do $pos "?"]')
df.add_system_transition(State.TECH, State.U4a, '[!Many technology firms are looking for great $pos"." Why do you want to do $pos "?"]')
df.add_system_transition(State.SAME, State.U4a, '[!Many firms are looking for great $pos"."Why do you want to become a $pos"?"]')
df.add_system_transition(State.ERR3, State.U4c, '"Well...I do not know much about this position, but I will look it up later. Why are you interested in this position?"')
df.add_system_transition(State.DK, State.U4b, '"Thats fine. It took me a long time to figure out what I really want to do either. I actually know a lot about different jobs now, such as business analyst, investment banking analyst, business consultant, software engineer, data analyst, wed developer, product manager… Which one are you interested in? I can tell you what I know about it."')

df.add_user_transition(State.U4a, State.S5, '[$why_posadj=#POS(adj)]')
df.set_error_successor(State.U4a, error_successor=State.ERR4)
df.add_user_transition(State.U4c, State.S5b, "/.*/")
df.add_user_transition(State.U4b, State.S6b, '[$pos={/.*/}]')

df.add_system_transition(State.S5, State.U5, '[!"Yeah for sure, it is" $why_posadj ". What kind of skills do you think that employees value for this position?"]')
df.add_system_transition(State.ERR4, State.U5, '"You have interesting insights. What kind of skills do you think that employees value for this position?"')
df.add_system_transition(State.S5b, State.U5b, '"Sounds interesting! I wish I could learn more about it. What kind of skills do you think that employees value for this position?"')

df.add_system_transition(State.S6b, State.END, '[!You know what"," crucial skills for a $pos are":" #posSkill Do you feel that you are ready for this job"?" We can always talk about this anytime.]')

df.add_user_transition(State.U5, State.S6a, "/.*/")
df.add_user_transition(State.U5b, State.S6c, "/.*/")
df.add_system_transition(State.S6a, State.U6, '[!Absolutely"." For a $pos "," #posSkill are very important. You should try to build these skillset in order to get a job"." Is any other place you wanna work at"?"]')
df.add_system_transition(State.S6c, State.U6, '"Wow sounds cool! Good luck! Is anywhere else you wanna work at?"')

df.add_user_transition(State.U6, State.S1, "[{yes, yeah, yea, ye, do}]")
df.add_user_transition(State.U6, State.END, "[{no, nope, nah, not, dont}]")
df.add_user_transition(State.U6, State.S2a, '[$loc={new york,ny,la,los angeles,chicago,dallas,washington dc,dc,west,east,bay,san francisco,sf,houston,boston,bos,atl,atlanta,seattle,sea,san jose}]')

df.run(debugging=False)
