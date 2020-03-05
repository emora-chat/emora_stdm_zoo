from emora_stdm import KnowledgeBase, DialogueFlow
from enum import Enum, auto
from emora_stdm import Macro

class State(Enum):
    S1 = auto()
    U1 = auto()
    S2a = auto()
    S2b = auto()
    U2a = auto()
    U2b = auto()
    S3a = auto()
    S3b = auto()
    S3c = auto()
    S3d = auto()
    U3a = auto()
    U3b = auto()
    S4a = auto()
    S4b = auto()
    S4c = auto()
    S4d = auto()
    S4e = auto()
    U4a = auto()
    U4b = auto()
    U4c = auto()
    S5a = auto()
    S5b = auto()
    S5c = auto()
    S5d = auto()
    U5a = auto()
    U5b = auto()
    S6a = auto()
    S6b = auto()
    S6c = auto()
    S6d = auto()
    S6e = auto()
    S6f = auto()
    U6a = auto()
    S7a = auto()
    S7b = auto()
    S7c = auto()
    U7a = auto()
    S8a = auto()
    S8b = auto()
    U8a = auto()
    S9a = auto()
    U9a = auto()
    S10a = auto()
    S10b = auto()
    S10c = auto()
    U10a = auto()
    S11a = auto()
    S11b = auto()
    S11c = auto()
    S11d = auto()
    U11a = auto()
    U11b = auto()
    U11c = auto()
    END = auto()
    ERR1 = auto()
    ERR2 = auto()
    ERR3 = auto()
    ERR4 = auto()
    ERR5 = auto()
    ERR6 = auto()
    ERR7 = auto()
    ERR8 = auto()
    ERR9 = auto()
    ERR10 = auto()
    ERR11 = auto()
    ERR12 = auto()


exp_con = {'more car': 'I agree. Since more people will be able to access to cars, there will be more people and more cars on the road.',
           'more people': 'I agree. Since more people will be able to access to cars, there will be more people and more cars on the road.',
           'increase car': 'I agree. Since more people will be able to access to cars, there will be more people and more cars on the road.',
           'insecur': 'Actually autonomous cars are much more secure than human-driven car, so this should not be a concern',
           'not secur': 'Actually autonomous cars are much more secure than human-driven car, so this should not be a concern',
           'danger': 'Actually autonomous cars are much more secure than human-driven car, so this should not be a concern',
           'hack': 'I agree. Like all computer systems, there is always a risk of the computer being hacked or crashing due to some reason.',
           'crash': 'I agree. Like all computer systems, there is always a risk of the computer being hacked or crashing due to some reason.',
           'job': 'I agree. Autonomous cars will replace a large amount of jobs such as drivers of any kind.',
           'expensive': 'I agree. Just like any new technology that has taken years to develop and make, the cost of autonomous cars is likely to be astronomical at first.',
           'price': 'I agree. Just like any new technology that has taken years to develop and make, the cost of autonomous cars is likely to be astronomical at first.',
           'like': 'Absolutely. There must be some people who sincerely love driving, the fully integration of autonomous cars in our transportation system will definitely disappoint them.',
           'regulation': 'I agree. There is no comprehensive regulation currently available for autonomous vehicles now.',
           'act': 'I agree. There is no comprehensive regulation currently available for autonomous vehicles now.',
           'law': 'I agree. There is no comprehensive regulation currently available for autonomous vehicles now.',
           'moral': 'I agree. Since computer programs only make optimal decisions, it is debatable for how the programs should be written to tell the machine how to make decision when a passenger walks out of the road when the car drives very fast.'}

exp_pro = {'secur': 'For sure! 90% of car accidents are due to human errors such as speeding and drink driving. Thus autonomous cars would be much more secure as human errors can all be eradicated.',
           'safe':'For sure! 90% of car accidents are due to human errors such as speeding and drink driving. Thus autonomous cars would be much more secure as human errors can all be eradicated.',
           'accident': 'For sure! 90% of car accidents are due to human errors such as speeding and drink driving. Thus autonomous cars would be much more secure as human errors can all be eradicated.',
           'disab': 'For sure! With fully automated cars, people who are not allowed or not able to drive in the past can now access to vehicles',
           'traffic': 'For sure! Since autonomous cars can sense and communicate with each other, bumper to bumper traffic jams will not happen anymore. Speed limit will go up since it is less likely for cars to crash.',
           'environment': 'For sure! Since autonomous cars will travel at consistent speeds and distances from one another, there will be a reduced need for braking and re-accelerating, which largely reduced the amount of emissions from cars.',
           'free': 'For sure! There definitely are some people who do not like driving or wish to spend their time in car more efficiently, then autonomous car for sure solves their problem.',
           'attention': 'For sure! People can spend their time in the car freely since they do not need to focus on driving anymore.'}

exp_field = {'farm': 'increase efficiency',
             'agriculture': 'increase efficiency',
             'irrigat': 'increase efficiency',
             'deliver': 'save human labor cost',
             'tractor': 'increase efficiency',
             'taxi': 'save human labor cost',
             'mining': 'avoid human injures caused by mining accidents',
             'drill': 'avoid human injures caused by drilling accidents',
             'industrial': 'increase efficiency and save human labor cost',
             'forklift': 'increase efficiency and save human labor cost',
             'test': 'be safer',
             'experiment': 'be safer'}

comp_char_dict = {'gm': 'is working on superhuman sensors',
                  'general motor': 'is working on superhuman sensors',
                  'generalmotor': 'is working on superhuman sensors',
                  'cruise': 'is working on superhuman sensors',
                  'argo ai': 'is improving the safety of driverless vehicles',
                  'argoai': 'is improving the safety of driverless vehicles',
                  'zoox': 'is trying to complete automation in complex environments',
                  'tesla':'is the most famous autonomous vehicle company',
                  'ford': 'will have a fully autonomous vehicle in operation by 2021',
                  'aptiv': 'is working on commercializing autonomous vehicles',
                  'toyota': 'is working on commercializing autonomous vehicles',
                  'intel': 'is the leading supplier of software that supports autonomous driving',
                  'volkswagen': 'has a Level 5, fully autonomous vehicle, Sedric',
                  'bosch': 'focus on communication between car and passenger',
                  'nissan':'plans to build commercially viable autonomous vehicles on the road by 2020',
                  'nvidia':'provides autonomous driving software and hardware',
                  'amazon':'provides tons of services to support the development of autonomous driving',
                  'nuro':'designs autonomous vehicles specialized in delivery'}



class elabCon(Macro):
    def run(self, ngrams, vars, args):
        if 'con' in vars:
            vars['expcon'] = ""
            for key in exp_con:
                if key in vars['con']:
                    vars['expcon'] = exp_con[key]
        return ""

class elabPro(Macro):
    def run(self, ngrams, vars, args):
        if 'pro' in vars:
            vars['exppro'] = ""
            for key in exp_pro:
                if key in vars['pro']:
                    vars['exppro'] = exp_pro[key]
        return ""

class EXPLfield(Macro):
    def run(self, ngrams, vars, args):
        if 'field' in vars:
            vars['expfield'] = ""
            for key in exp_field:
                if key in vars['field']:
                    vars['expfield'] = exp_field[key]
        return ""

class YEAR(Macro):
    def run(self, ngrams, vars, args):
        curr_year = 2020
        d, s = 0, ""
        if 'year' in vars:
            d = int(vars['year']) - curr_year
            s = str(d) + " years from now"
            vars['n'] = 'test'
        elif 'duration' in vars:
            vars['new'] = 'new'
            d = curr_year + int(vars['duration'])
            s = "around " + str(d)
        return s


class company(Macro):
    def run(self, ngrams, vars, args):
        vars['lis'] = 'Waymo, General Motors, Tesla, Argo AI'
        return ''


class chooseComp(Macro):
    def run(self, ngrams, vars, args):
        google = ['waymo google alphabet']
        comps = ["ford", "tesla", "zoox"]
        result = ""
        if 'comp' in vars:
            if vars['comp'] not in google:
                for elem in comps:
                    if vars['comp'] in elem:
                        comps.remove(elem)
        for elem in comps: result += elem + ', '
        return result[:-2]

class COMPCHAR(Macro):
    def run(self, ngrams, vars, args):
        if 'notchosen' in vars:
            a = ""
            for key in comp_char_dict:
                if key in vars['notchosen']:
                    a = comp_char_dict[key]
        return a



df = DialogueFlow(State.S1, initial_speaker=DialogueFlow.Speaker.SYSTEM, macros={"elabCon": elabCon(), "elabPro": elabPro(), "EXPLfield": EXPLfield(), "YEAR": YEAR(), "company": company(), "choosecomp": chooseComp(), "COMPCHAR": COMPCHAR()})

pro = r"[$pro={secure,security,safe,safety, [{accident,accidents}, /reduce[sd]?|decrease[sd]?/], [{few,fewer,reduce,reduces,reduced}, {accident,accidents}], /disable[d]?|disability/, traffic,traffics, environment,environmental,free,attention,attentions}]"
con = "[$con={</more|increase[d]?|increasing|/, /car[s]?|people/>,hack,hacked,hacker,crash,crashed,crashing,moral,morality,immoral,immorality,ethic, expensive,price,job,jobs, /like[s]?\sdriving/, /regulate[s]?|regulation|law[s]?|act[s]?/,insecure,insecurity,danger,dangerous,not secure,not safe}]"
con1 = r'[{no, not really, nah}, [$con={danger, not safe}]]'
procon = "{[$pro={/economic[s]?|economy\s?(benefit[s]?)?/, /secure|security/, [/accident[s]?/, /reduce[d]?|decrease[sd]?|cut\sdown/], [/few|fewer/, /accident[s]?/], /disable[d]?|disability/, </traffic|traffics/, /quick|quicker|fast|faster|better|good|improve[d]?|solve[d]?/>, /environment|environmental/, free}], $con={</more|increase[d]?|increasing|/, /car[s]?|people/>, {hack,hacked,hacker,crash,crashed,crashing}, {moral,morality,immoral,immorality}, {expensive,price}, {job,jobs}, /like[s]?\sdriving/, /regulate[s]?|regulation|law[s]?|act[s]?/}]}"


df.add_system_transition(State.S1, State.U1, r'"Do you drive?"')

df.add_user_transition(State.U1, State.S2a, r'[{yes, yeah, yep, yea, ye, of course}]')
df.add_user_transition(State.U1, State.S2b, r'[{no, not really, nah}]')

df.add_system_transition(State.S2a, State.U2a, r'"Cool, what car do you have?"')
df.add_system_transition(State.S2b, State.U2b, r'"Do you plan to learn driving at some point in the future?"')

df.add_user_transition(State.U2a, State.S3a, r'#NOT(tesla)')
df.add_user_transition(State.U2a, State.S3b, r'[{tesla, tesla}]')
df.add_user_transition(State.U2b, State.S3c, r'[{yes, yeah, yep, yea, ye, of course, sure, why not}]')
df.add_user_transition(State.U2b, State.S3d, r'[{no, not really, nah, /don\'t/}]')


df.add_system_transition(State.S3a, State.U3a, r'"Have you ever felt too tired to drive that you would like the car to drive itself?"')
df.add_system_transition(State.S3b, State.U3b, r'"Awesome, what model do you have?"')
df.add_system_transition(State.S3c, State.U3a,
                         r'"That’s great! But sometimes you may feel too tired to drive, would you like to have the car to drive itself?"')
df.add_system_transition(State.S3d, State.U3a,
                         r'"Well, that’s totally reasonable. Maybe you don’t need to in the future! Would you like to have the car to drive itself?"')

df.add_user_transition(State.U3a, State.S4a, r'[{yes, yeah, yep, yea, ye, sure, y}]')
df.add_user_transition(State.U3a, State.S4b, r'[{no, not really, nah, n}]', score = 1)
df.add_user_transition(State.U3a, State.S4c, con, score = 2)
df.add_user_transition(State.U3b, State.S4d, r'[{models, model s, /model\s3/, /model3/, modelx, model x}]', score = 1)
df.add_user_transition(State.U3b, State.S4e, r'[{modely, model y}]')

df.add_system_transition(State.S4a, State.U4a, r'"Autonomous Vehicles allows the car to drive itself. Do you think it is a good idea to have them in our transportation system?"')
df.add_system_transition(State.S4b, State.U4b, r'"Why not?"')
df.add_system_transition(State.S4c, State.U4c, r'[!#elabCon$expcon However, do you think if there is any potential advantages of autonomous cars"?"]')
df.add_system_transition(State.S4d, State.U4a, r'"Cool! This model is capable of autonomous driving. Do you think it is a good idea to have them in our transportation system?"')
df.add_system_transition(State.S4e, State.U4a, r'"I do not know much about this model but I know that some Tesla vehicles are capable of autonomous driving. Do you think it is a good idea to have them in our transportation system?"')

df.add_user_transition(State.U4a, State.S5a, pro, score=2)
df.add_user_transition(State.U4a, State.S5b, con, score=2)
df.add_user_transition(State.U4a, State.S5d, r'[{yes, ye, yea, yeah, sure, i do, good, cool, great, awesome, of course, sure}]', score = 1)
df.add_user_transition(State.U4a, State.S4b, r'[{no, nop, not really, nah, n}]')

df.add_user_transition(State.U4b, State.S5b, con)

df.add_user_transition(State.U4c, State.S5c, pro)

df.add_system_transition(State.S5d, State.U4a, r'[!Could you elaborate more about why you think so"?"]')

df.add_system_transition(State.S5a, State.U5a, r'[!#elabPro$exppro However, do you think there is any potential risks of autonomous cars"?"]')
df.add_system_transition(State.S5b, State.U5b, r'[!#elabCon$expcon However, do you think there is any potential advantages of autonomous cars"?"]')
df.add_system_transition(State.S5c, State.U6a, r'[!#elabPro$exppro Even though there might be problems using this technology on human, is there any other field that you think we can apply this technique to"?"]')

df.add_user_transition(State.U5a, State.S6a, con, score=2)
df.add_user_transition(State.U5a, State.S6c, r'[{yes, ye, yea, yeah, sure, i do, of course, sure}]', score=1)
df.add_user_transition(State.U5a, State.S6f, r'[{no, n, not really, nop, nah}]')
df.add_system_transition(State.S6c, State.U5a, r'"Could you tell me more about what you think?"')
df.add_system_transition(State.S6f, State.U6a, r'"One downside is that autonomous cars will replace a large amount of jobs such as drivers of any kind. Do you know any field that we can apply this technique to?"')

df.add_user_transition(State.U5b, State.S6b, pro, score=2)
df.add_user_transition(State.U5b, State.S6e, r'[{no, n, not really, nop, nah}]')
df.add_user_transition(State.U5b, State.S6d, r'[{yes, ye, yea, yeah, sure, i do, of course, sure}]', score=1)
df.add_system_transition(State.S6d, State.U5b, r'"Could you tell me more about what you think?"')
df.add_system_transition(State.S6e, State.U6a, r'"One advantage is that autonomous cars are actually safer. 90% of car accidents are due to human errors such as speeding and drink driving. Do you know any field that we can apply this technique to?"')

# elaborate and ask field
df.add_system_transition(State.S6a, State.U6a, r'[!#elabCon$expcon Since it is such a great technique, is there any other field that you think we can apply this technique to"?"]')
df.add_system_transition(State.S6b, State.U6a, r'[!#elabPro$exppro Even though there might be problems using this technology on human, is there any other field that you think we can apply this technique to"?"]')


lis = "[$field={delivery, deliveries, taxi, taxis, farm, farming, agriculture, irrigator, irrigators, irrigate, irrigation, tractor, tractors, mining, drill, drilling, drillings, industrial, forklift, forklifts, test, tests, testing, experiment, experiments, experimenting}]"
df.add_user_transition(State.U6a, State.S7a, lis)
df.add_user_transition(State.U6a, State.S7b, r'#NOT(delivery, deliveries, taxi, taxis, farm, farming, agriculture, irrigator, irrigators, irrigation, tractor, tractors, mining, drill, drilling, drillings, industrial, forklift, forklifts, test, tests, testing, experiment, experiments, experimenting)')
df.add_user_transition(State.U6a, State.S7c, r'[{no, not really, nah, /don\'t/}]', score=2)

# if answer in our list of field, give explanation to the field and go to question #EXPLfield$expfield
df.add_system_transition(State.S7a, State.U7a, r'[!$field is a great way to apply the Autonomou driving technique"!" It can#EXPLfield$expfield"." Do you think autonomous cars will be widely employed by the majority of the world"?"]')
df.add_system_transition(State.S7b, State.U7a, r'"That is a good idea! Do you think autonomous cars will be widely employed by the majority of the world?"')
df.add_system_transition(State.S7c, State.U7a,
                         r'"One application is autonomous mining vehicles, which could reduce human injures caused by mining accidents. Do you think autonomous cars will be widely employed by the majority of the world?"')

df.add_user_transition(State.U7a, State.S8a, r'[{yes, yeah, yep, yea, ye}]')
df.add_user_transition(State.U7a, State.S8b, r'[{no, not really, nah, /don\'t/}]')

df.add_system_transition(State.S8a, State.U8a, r'"I think so too! When do you think it will happen?"')
df.add_system_transition(State.S8b, State.U9a, r'"Many other people hold the same opinion as you do. By the way, do you know any companies that are currently developing this technology?"')

df.add_user_transition(State.U8a, State.S9a, r'[{$year=/\d{4}/,[!/[in]?/, $duration=/\d{1,3}/, /year[s]?/]}]')
df.add_system_transition(State.S9a, State.U9a, r'[!That is #YEAR"." I think it will happen by "2050." By the way, do you know what companies are now developing this technology"?"]')


complist = "[$comp={waymo,google,alphabet,gmcruise,gm cruise,gm,cruise,generalmotors,general motors,argoai,argo ai,zoox,tesla,ford,aptiv,intel,mobileye,volkswagen,bosch,toyota,nissan,nvidia,amazon,nuro}]"
df.add_user_transition(State.U9a, State.S10a, complist)
df.add_user_transition(State.U9a, State.S10b, '[#NOT(waymo,google,alphabet,gmcruise,gm cruise,gm,cruise,generalmotors,general motors,argoai,argo ai,zoox,tesla,ford,aptiv,intel,mobileye,volkswagen,bosch,toyota,nissan,nvidia,amazon,nuro), $compnotinlist=#NER(ORG)]')
df.add_user_transition(State.U9a, State.S10c, r'[{no, not really, nah, /don\'t/}]', score=2)

df.add_system_transition(State.S10a, State.U10a, r'[!Definitely"!" #choosecomp are also working on Autonomous Vehicles"." Among all the companies that you know are developing autonomous vehicles"," which one do you think will contribute most to the popularization of this technology"?"]')
df.add_system_transition(State.S10b, State.U10a, r'[!Oh I did not know $compnotinlist is also working on Autonomous Vehicles"." But I know #company$lis are doing this"." Among all the companies that you know are developing autonomous vehicles"," which one do you think will contribute most to the popularization of this technology"?"]')
df.add_system_transition(State.S10c, State.U10a, r'[!That is okay"." I know that #company$lis are doing this"." Among all the companies that you know are developing autonomous vehicles"," which one do you think will contribute most to the popularization of this technology"?"]')

df.add_user_transition(State.U10a, State.S11a, r'[$chosen={waymo, google, alphabet}]')
df.add_user_transition(State.U10a, State.S11b, r'[$notchosen={gmcruise,gm cruise,gm,cruise,generalmotors,general motor,general motors,argoai,argo ai,zoox,tesla,ford,aptiv,intel,mobileye,volkswagen,bosch,toyota,nissan,nvidia,amazon,nuro}]', score = 2)
df.add_user_transition(State.U10a, State.S11c, r'[$userchosen=#NER(ORG)]', score = 1)

df.add_system_transition(State.S11a, State.U11a,
                         r'[!I also think $chosen is the pioneer in Autonomous Vehicles since it has an experienced self driving system that lets its autonomous cars learn from the world"’"s longest and toughest driving test including millions of miles on public roads and billions of miles in simulation.]')
df.add_system_transition(State.S11b, State.U11b,
                         r'[!I know $notchosen is #COMPCHAR"." However I think Waymo"/"Google is the most successful firm in this field because it has an experienced self driving system that lets its autonomous cars learn from the world"’"s longest and toughest driving test including millions of miles on public roads and billions of miles in simulation.]')
df.add_system_transition(State.S11c, State.U11c,
                         r'[!I am not very familiar with $userchosen"," could you tell me more about it"?"]')

df.add_user_transition(State.U11a, State.END, "/.*/")
df.add_user_transition(State.U11b, State.END, "/.*/")
df.add_user_transition(State.U11c, State.END, "/.*/")

df.set_error_successor(State.U1, error_successor=State.ERR1)
df.add_system_transition(State.ERR1, State.U3a, r'"I do not understand. But would you like to have cars to drive themselves and take you to the destination?"')
df.set_error_successor(State.U2a, error_successor=State.ERR2)
df.add_system_transition(State.ERR2, State.U3a, r'"I do not understand. But would you like to have cars to drive themselves and take you to the destination?"')
df.set_error_successor(State.U2b, error_successor=State.ERR3)
df.add_system_transition(State.ERR3, State.U3a, r'"I do not understand. But would you like to have cars to drive themselves and take you to the destination?"')
df.set_error_successor(State.U3a, error_successor=State.S4a)
df.set_error_successor(State.U3b, error_successor=State.S4e)
df.set_error_successor(State.U4a, error_successor=State.ERR4)
df.add_system_transition(State.ERR4, State.U6a, r'"I think it is a good way to significantly reduce the amount of car accidents as it is much more safe than human driven cars. Is there any other fields that you think we can apply this technique to?"')
df.set_error_successor(State.U4b, error_successor=State.ERR5)
df.add_system_transition(State.ERR5, State.U5b, r'"I agree. However, do you think there is any potential advantages of autonomous cars?"')
df.set_error_successor(State.U4c, error_successor=State.ERR6)
df.add_system_transition(State.ERR6, State.U6a, r'"I think so too. Even though there might be problems using this technology on human, is there any other field that you think we can apply this technique to?"')
df.set_error_successor(State.U5a, error_successor=State.ERR7)
df.add_system_transition(State.ERR7, State.U6a, r'"For sure! One downside is that autonomous cars will replace a large amount of jobs such as drivers of any kind. Do you know any field that we can apply this technique to?"')
df.set_error_successor(State.U5b, error_successor=State.ERR8)
df.add_system_transition(State.ERR8, State.U6a, r'"For sure! One advantage is that autonomous cars are actually safer. 90% of car accidents are due to human errors such as speeding and drink driving. Do you know any field that we can apply this technique to?"')
df.set_error_successor(State.U7a, error_successor=State.ERR9)
df.add_system_transition(State.ERR9, State.U9a, r'"I think it will eventually happen but might still take a while. By the way, do you know what companies are now developing this technology?"')
df.set_error_successor(State.U8a, error_successor=State.ERR10)
df.add_system_transition(State.ERR10, State.U9a, r'"I do not understand. But I think it will happen by "2050." By the way, do you know what companies are now developing this technology?"')
df.set_error_successor(State.U10a, error_successor=State.ERR11)
df.add_system_transition(State.ERR11, State.U10a, r'"It is not a company, choose a company that you think is the most promising in the world of autonomous car."')
df.set_error_successor(State.U9a, error_successor=State.ERR12)
df.add_system_transition(State.ERR12, State.U10a, r'[!That is okay"." I know that #company$lis are doing this"." Among all the companies that you know are developing autonomous vehicles"," which one do you think will contribute most to the popularization of this technology"?"]')


df.add_system_transition(State.END, State.U1, '"Lets start again. Do you drive?"')

df.run(debugging=False)