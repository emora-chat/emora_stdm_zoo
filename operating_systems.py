from emora_stdm import KnowledgeBase, DialogueFlow
from enum import Enum
import re
from types import SimpleNamespace
from typing import List, Pattern

class State(Enum):
    START = 0
    NAME_Q = 1
    NAME_R = 2
    COM_Q = 3
    COM_NO = 4
    COM_YES = 5
    TYPE_Q = 6
    TYPE_DESK = 7
    TYPE_LAP = 8
    DESK_Q = 9
    LAP_Q = 10
    HOME_YES = 11
    ALSO_LAP_Q = 12
    HOME_NO = 13
    HOME_OTHER = 14

    # endings
    END_1_GENERIC = 50
    END_1_WORK_SCHOOL = 49
    END_1_HOME_LAP = 48
    # errors
    DESK_Q_ERR = 97
    LOCATION_UNKNOWN = 98
    COM_Q_ERR = 99
    LAP_Q_ERROR = 96
    TYPE_ERROR = 95

    # part 2
    PART_2_START = 101

    # part 2 types of computer
    PART_2_MAC = 102
    PART_2_WINDOWS = 103
    PART_2_CHROME = 104
    PART_2_OTHER = 105

    # part 2 information
    MAC_INFO = 110
    WINDOWS_INFO = 111
    CHROME_INFO = 112
    OTHER_INFO = 113

    # part 2 other operating system
    OTHER_Y = 120
    OTHER_N = 121

    # part 2 what other OS
    OTHER_WHAT = 130

    # part 2 end
    PART_2_END_TRY = 160
    MAC_INFO_END = 161
    WINDOWS_INFO_END = 162
    CHROME_INFO_END = 163

    # part 2 second set of OS
    PART_2_MAC_2 = 150
    PART_2_WINDOWS_2 = 151
    PART_2_CHROME_2 = 152

    # errors part 2
    PART_2_ERROR_1 = 199

    PART_2_ERROR_MAC = 198
    PART_2_ERROR_WINDOWS = 197
    PART_2_ERROR_CHROME = 196
    PART_2_ERROR_OTHER = 196

    PART_2_ERROR_3 = 195

    # part 3 start
    INTER_Y = 201
    INTER_N = 202

    # part 3 Y/N Integrate
    WHY_Y = 211
    WHY_N = 212

    # part 3 phones
    PART_3_IPHONE = 221
    PART_3_ANDROID = 222
    PART_3_OTHER = 223

    # part 3 OS
    PART_3_OS = 231
    PART_3_Y = 232
    PART_3_N = 233

    # part 3 hear more
    HEAR_MORE = 251
    HEAR_MORE_Y = 252
    HEAR_MORE_N = 253

    # part 3 errors
    PART_3_ERROR_TRY = 299
    PART_3_ERROR_MAC = 298
    PART_3_ERROR_WINDOWS = 297
    PART_3_ERROR_CHROME = 296
    WHY_Y_ERROR = 295
    WHY_N_ERROR = 294
    PART_3_OS_ERROR = 293
    TRAP_ERROR = 292
    HEAR_MORE_ERROR = 291

    # part 3 end
    END = 241
    TRAP = 242

# ontology
ontology = {
    "ontology": {
        "non_home_locations":
            [
                "work",
                "office",
                "lab",
                "class",
                "lecture",
                "meeting",
                "travel",
                "school"
            ]
        }
}
# start
knowledge = KnowledgeBase()
knowledge.load_json(ontology)
df = DialogueFlow(State.START, initial_speaker=DialogueFlow.Speaker.SYSTEM, kb=knowledge)

# desktop or laptop
df.add_system_transition(State.START,State.NAME_Q,'"hello, I am Emily, a virtual chatbot, what is your name? (Please simply type your name.)"')
df.add_user_transition(State.NAME_Q,State.NAME_R,'[$name=/.*/]')
df.add_system_transition(State.NAME_R, State.COM_Q, '[!"Hi"$name", do you have a computer?"]')
df.add_user_transition(State.COM_Q,State.COM_NO,'[{No,no,not,nah,Nah,N,n}]')
df.add_system_transition(State.COM_NO,State.COM_Q,'"Well, you should get a computer.'
                                                  '\n   Here are some websites where you can buy a comptuer:'
                                                  '\n   www.bestbuy.com'
                                                  '\n   www.apple.com'
                                                  '\n   www.microsoft.com'
                                                  '\nS: Do you have a computer now?"')
df.add_user_transition(State.COM_Q,State.COM_YES,'[{Yes,Yeah,yes,yeah,sure,of course,Of course,I do,i do}]')

df.add_system_transition(State.COM_YES,State.TYPE_Q,'"Do you have a desktop? Or do you only have a laptop?"')
df.add_user_transition(State.TYPE_Q,State.TYPE_DESK,'[desktop]')
df.add_user_transition(State.TYPE_Q,State.TYPE_LAP,'[laptop]')

df.add_system_transition(State.TYPE_DESK,State.DESK_Q,'"Oh, do you use the desktop mostly at home, then?"')
df.add_user_transition(State.DESK_Q,State.HOME_YES,'[{Yes,Yeah,yes,yeah,sure,of course,Of course,I do,i do,home,HOME,Home}]')
df.add_user_transition(State.DESK_Q,State.HOME_NO,'[{No,no,not,nah,Nah,N,n}]')
df.add_user_transition(State.DESK_Q,State.HOME_OTHER,'[$location=#ONT(non_home_locations)]')

df.add_system_transition(State.HOME_YES,State.ALSO_LAP_Q,'"That makes sense. Do you also have a laptop?"')
df.add_user_transition(State.ALSO_LAP_Q,State.TYPE_LAP,'[{Yes,Yeah,yes,yeah,sure,of course,Of course,I do,i do}]')
df.add_user_transition(State.ALSO_LAP_Q,State.END_1_GENERIC,'[{No,no,not,nah,Nah,N,n}]')

df.add_system_transition(State.HOME_NO,State.ALSO_LAP_Q,'"That is a strange choice. Do you also have a laptop?"')
df.add_system_transition(State.HOME_OTHER,State.ALSO_LAP_Q,'[!"It is strange to bring a desktop to"$location"... Do you also have a laptop?"]')

df.add_system_transition(State.TYPE_LAP,State.LAP_Q,'"I guess you use a laptop more than at home, right? Do you use it at school or at work?"')
df.add_user_transition(State.LAP_Q,State.END_1_WORK_SCHOOL,'[$location=#ONT(non_home_locations)]')
df.add_user_transition(State.LAP_Q,State.END_1_HOME_LAP,'[/(only)?(just)?(.{2})?home/]')


# errors
df.set_error_successor(State.COM_Q, State.COM_Q_ERR)
df.set_error_successor(State.TYPE_Q,State.TYPE_ERROR)
df.set_error_successor(State.DESK_Q,State.DESK_Q_ERR)
df.set_error_successor(State.LAP_Q,State.LOCATION_UNKNOWN)
df.set_error_successor(State.ALSO_LAP_Q,State.LAP_Q_ERROR)

df.add_system_transition(State.LAP_Q_ERROR, State.ALSO_LAP_Q, '"I did not understand that...\nS: Do you also have a laptop?"')
df.add_system_transition(State.TYPE_ERROR, State.TYPE_Q,'"I did not understand that...\nS: Do you have a desktop or a laptop?"')

df.add_system_transition(State.COM_Q_ERR,State.COM_Q,'"Let us try this again...do you have a computer?"')
df.add_system_transition(State.LOCATION_UNKNOWN,State.LAP_Q,'"I do not know that one. Try a different location."')
df.add_system_transition(State.DESK_Q_ERR,State.DESK_Q,'"Let us try this again...do you use the desktop mostly at home?"')

# part 1 endings
df.add_system_transition(State.END_1_GENERIC,State.PART_2_START,'"I see. \nS: Do you have a macbook, a windows computer, a chromebook or other computers?"')
df.add_system_transition(State.END_1_HOME_LAP,State.PART_2_START, '"That is a strange choice. You could have got a desktop instead and saved some money. \nS: Do you have a macbook, a windows computer, a chromebook or other computers?"')
df.add_system_transition(State.END_1_WORK_SCHOOL,State.PART_2_START, '"That makes sense. It is easier to bring a laptop than a desktop to"$location". \nS: Do you have a macbook, a windows computer, a chromebook or other computers?"')


# part 2 starts
# turn 1
df.add_user_transition(State.PART_2_START, State.PART_2_WINDOWS, '[$system_a={windows,WINDOWS,Windows,Microsoft,microsoft,MICROSOFT,win,WIN,Win,"WIN10","win10","Win10"}]')
df.add_user_transition(State.PART_2_START, State.PART_2_MAC, '[$system_a={mac,Mac,MAC,macbook,Macbook,Apple,apple,Macos,MacOS,MACOS,MACos,mbp,MBP,mba,MBA,imac,IMAC,iMac,Imac}]')

df.add_system_transition(State.PART_2_MAC,State.MAC_INFO, '"The family of Macintosh operating systems were developed by Apple Inc. in 1984.'
                                                          '\n   MacOS is based on the Unix operating system and on technologies developed between 1985 and 1997 at NeXT.'
                                                          '\n   Prior to the introduction of Mac OS X, Apple experimented with several other concepts, releasing different products designed to bring the Macintosh interface or applications to Unix-like systems or vice versa, A/UX, MAE, and MkLinux.'
                                                          '\n   See more information at https://en.wikipedia.org/wiki/MacOS'
                                                          '\nS: Have you ever used other operating systems other than MacOS?"')



df.add_system_transition(State.PART_2_WINDOWS,State.WINDOWS_INFO, '"Microsoft Windows, commonly referred to as Windows, is a group of several proprietary graphical operating system families.'
                                                                  '\n   Microsoft introduced an operating environment named Windows on November 20, 1985, as a graphical operating system shell for MS-DOS.'
                                                                  '\n   As of October 2018, the most recent version of Windows for PCs, tablets, smartphones and embedded devices is Windows 10.'
                                                                  '\n   See more information at https://en.wikipedia.org/wiki/MicrosoftWindows'
                                                                  '\nS: Have you ever used other operating systems other than Windows?"' )

df.add_user_transition(State.PART_2_START, State.PART_2_CHROME, '[$system_a={chrome,CHROME,Chrome,chromebook,Chromebook,CHROMEBOOK,google,Google,GOOGLE}]')

df.add_system_transition(State.PART_2_CHROME,State.CHROME_INFO, '"Chrome OS is a Linux kernel-based operating system designed by Google. It is derived from the free software Chromium OS and uses the Google Chrome web browser as its principal user interface.'
                                                          '\n   Google announced the project in July 2009, conceiving it as an operating system in which both applications and user data reside in the cloud'
                                                          '\n   Chrome OS is only available pre-installed on hardware from Google manufacturing partners, but there are unofficial methods that allow it to be installed in other equipment.'
                                                          '\n   See more information at https://en.wikipedia.org/wiki/ChromeOS'
                                                          '\nS: Have you ever used other operating systems other than ChromeOS?"' )

df.add_user_transition(State.PART_2_START, State.PART_2_OTHER, '[{Other,other,OTHER,No,Nah,nah,nope,Nope,NO}]')

# turn 2
df.add_system_transition(State.PART_2_OTHER,State.OTHER_INFO, '"Have you ever used any other operating systems?"')

df.add_user_transition(State.MAC_INFO, State.OTHER_Y, '[{Y,y,Yes,Yeah,yes,yeah,sure,of course,Of course,I do,i do,right}]')
df.add_user_transition(State.WINDOWS_INFO, State.OTHER_Y, '[{Y,y,Yes,Yeah,yes,yeah,sure,of course,Of course,I do,i do,right}]')
df.add_user_transition(State.CHROME_INFO, State.OTHER_Y, '[{Y,y,Yes,Yeah,yes,yeah,sure,of course,Of course,I do,i do,right}]')
df.add_user_transition(State.OTHER_INFO, State.OTHER_Y, '[{Y,y,Yes,Yeah,yes,yeah,sure,of course,Of course,I do,i do,right}]')

df.add_user_transition(State.MAC_INFO, State.OTHER_N, '[{No,no,not,nah,Nah,N,n}]')
df.add_user_transition(State.WINDOWS_INFO, State.OTHER_N, '[{No,no,not,nah,Nah,N,n}]')
df.add_user_transition(State.CHROME_INFO, State.OTHER_N, '[{No,no,not,nah,Nah,N,n}]')
df.add_user_transition(State.OTHER_INFO, State.OTHER_N, '[{No,no,not,nah,Nah,N,n}]')

df.add_system_transition(State.OTHER_Y,State.OTHER_WHAT, '"what other operating systems have you used?"')

df.add_user_transition(State.OTHER_WHAT, State.PART_2_MAC_2, '[$system_b={mac,Mac,MAC,macbook,Macbook,Apple,apple,Macos,MacOS,MACOS,MACos,mbp,MBP,mba,MBA,imac,IMAC,iMac,Imac}]')
df.add_user_transition(State.OTHER_WHAT, State.PART_2_WINDOWS_2, '[$system_b={windows,WINDOWS,Windows,Microsoft,microsoft,MICROSOFT,win,WIN,Win,"WIN10","win10","Win10"}]')
df.add_user_transition(State.OTHER_WHAT, State.PART_2_CHROME_2, '[$system_b={chrome,CHROME,Chrome,chromebook,Chromebook,CHROMEBOOK,google,Google,GOOGLE}]')

df.add_system_transition(State.OTHER_N,State.PART_2_END_TRY, '"Well, you should definitely try other operating systems and see which one suits you the best!'
                                                             '\nS: Do you think it is important for computers to integrate well with other mobile devices?"')

df.add_system_transition(State.PART_2_MAC_2,State.MAC_INFO_END, '"The family of Macintosh operating systems were developed by Apple Inc. in 1984.'
                                                          '\n   MacOS is based on the Unix operating system and on technologies developed between 1985 and 1997 at NeXT.'
                                                          '\n   Prior to the introduction of Mac OS X, Apple experimented with several other concepts, releasing different products designed to bring the Macintosh interface or applications to Unix-like systems or vice versa, A/UX, MAE, and MkLinux.'
                                                          '\n   See more information at https://en.wikipedia.org/wiki/MacOS'
                                                          '\n\nS: Do you think it is important for computers to integrate well with other mobile devices?"')
df.add_system_transition(State.PART_2_WINDOWS_2,State.WINDOWS_INFO_END, '"Microsoft Windows, commonly referred to as Windows, is a group of several proprietary graphical operating system families, all of which are developed and marketed by Microsoft.'
                                                          '\n   Microsoft introduced an operating environment named Windows on November 20, 1985, as a graphical operating system shell for MS-DOS.'
                                                          '\n   As of October 2018, the most recent version of Windows for PCs, tablets, smartphones and embedded devices is Windows 10.'
                                                          '\n   See more information at https://en.wikipedia.org/wiki/MicrosoftWindows'
                                                          '\n\nS: Do you think it is important for computers to integrate well with other mobile devices?"')
df.add_system_transition(State.PART_2_CHROME_2,State.CHROME_INFO_END, '"Chrome OS is a Linux kernel-based operating system designed by Google. It is derived from the free software Chromium OS and uses the Google Chrome web browser as its principal user interface.'
                                                          '\n   Google announced the project in July 2009, conceiving it as an operating system in which both applications and user data reside in the cloud'
                                                          '\n   Chrome OS is only available pre-installed on hardware from Google manufacturing partners, but there are unofficial methods that allow it to be installed in other equipment.'
                                                          '\n   See more information at https://en.wikipedia.org/wiki/ChromeOS'
                                                          '\n\nS: Do you think it is important for computers to integrate well with other mobile devices?"')

# errors part 2
df.set_error_successor(State.PART_2_START, State.PART_2_ERROR_1)
df.add_system_transition(State.PART_2_ERROR_1, State.PART_2_START, '"I did not understand that... \nS: Do you have a macbook, a windows computer, a chromebook or other computers?"')

df.set_error_successor(State.MAC_INFO, State.PART_2_ERROR_MAC)
df.set_error_successor(State.WINDOWS_INFO, State.PART_2_ERROR_WINDOWS)
df.set_error_successor(State.CHROME_INFO, State.PART_2_ERROR_CHROME)
df.set_error_successor(State.OTHER_INFO, State.PART_2_ERROR_OTHER)

df.add_system_transition(State.PART_2_ERROR_MAC, State.MAC_INFO, '"I did not understand that...\n   Please enter yes or no\nS: Have you ever used another operating system other than MacOS?"')
df.add_system_transition(State.PART_2_ERROR_WINDOWS, State.WINDOWS_INFO, '"I did not understand that...\n   Please enter yes or no\nS: Have you ever used another operating system other than Windows?"')
df.add_system_transition(State.PART_2_ERROR_CHROME, State.CHROME_INFO, '"I did not understand that...\n   Please enter yes or no\nS: Have you ever used another operating system other than ChromeOS?"')
df.add_system_transition(State.PART_2_ERROR_OTHER, State.OTHER_INFO, '"I did not understand that...\n   Please enter yes or no\nS: Have you ever used another operating system?"')

df.set_error_successor(State.OTHER_WHAT,State.PART_2_ERROR_3)
df.add_system_transition(State.PART_2_ERROR_3, State.OTHER_WHAT,'"I did not under stand that...\n   Please enter an operating system\nS: What other operating systems have you used?"')

# Part 3 - Integrate with mobile devices
df.add_user_transition(State.PART_2_END_TRY, State.INTER_Y,'[{Y,y,Yes,Yeah,yes,yeah,sure,of course,Of course,I do,i do,right}]')
df.add_user_transition(State.MAC_INFO_END, State.INTER_Y,'[{Y,y,Yes,Yeah,yes,yeah,sure,of course,Of course,I do,i do,right}]')
df.add_user_transition(State.WINDOWS_INFO_END, State.INTER_Y,'[{Y,y,Yes,Yeah,yes,yeah,sure,of course,Of course,I do,i do,right}]')
df.add_user_transition(State.CHROME_INFO_END, State.INTER_Y,'[{Y,y,Yes,Yeah,yes,yeah,sure,of course,Of course,I do,i do,right}]')

df.add_user_transition(State.PART_2_END_TRY, State.INTER_N,'[{No,no,not,nah,Nah,N,n}]')
df.add_user_transition(State.MAC_INFO_END, State.INTER_N,'[{No,no,not,nah,Nah,N,n}]')
df.add_user_transition(State.WINDOWS_INFO_END, State.INTER_N,'[{No,no,not,nah,Nah,N,n}]')
df.add_user_transition(State.CHROME_INFO_END, State.INTER_N,'[{No,no,not,nah,Nah,N,n}]')

# Part 3 - Why integrate with mobile devices
df.add_system_transition(State.INTER_Y, State.WHY_Y, '"Well Yeah! I believe it is important for computers to integrate well with mobile devices too!\nS: What kind of mobile phone do you have?"')
df.add_system_transition(State.INTER_N, State.WHY_N, '"Well, I believe it is important for computers to integrate well with mobile devices.\n   Wait until I show you the importance of having a good ecosystem of technology.\nS: What kind of mobile phone do you have?"')

# Part 3 - Phone type
df.add_user_transition(State.WHY_Y, State.PART_3_IPHONE,'[{Iphone,IPHONE,iphone,ios,IOS}]')
df.add_user_transition(State.WHY_Y, State.PART_3_ANDROID,'[{Android,ANDROID,android,google,GOOGLE,Google,PIXEL,Pixel,pixel,samsung,SAMSUNG,Samsung,sony,Sony,SONY}]')
df.add_user_transition(State.WHY_Y, State.PART_3_OTHER,'[{Other,other,OTHER,No,Nah,nah,nope,Nope,NO}]')

df.add_user_transition(State.WHY_N, State.PART_3_IPHONE,'[{Iphone,IPHONE,iphone,ios,IOS}]')
df.add_user_transition(State.WHY_N, State.PART_3_ANDROID,'[{Android,ANDROID,android,google,GOOGLE,Google,PIXEL,Pixel,pixel,samsung,SAMSUNG,Samsung,sony,Sony,SONY}]')
df.add_user_transition(State.WHY_N, State.PART_3_OTHER,'[{Other,other,OTHER,No,Nah,nah,nope,Nope,NO}]')

# Part 3 - OS Integration with mobile devices
df.add_system_transition(State.PART_3_IPHONE, State.PART_3_OS, '"You said that you have used"$system_a"OS before, right?"')
df.add_system_transition(State.PART_3_ANDROID,State.PART_3_OS, '"You said that you have used"$system_a"OS before, right?"')
df.add_system_transition(State.PART_3_OTHER,State.PART_3_OS, '"You said that you have used"$system_a"OS before, right?"')

df.add_user_transition(State.PART_3_OS, State.PART_3_Y, '[{Y,y,Yes,Yeah,yes,yeah,sure,of course,Of course,I do,i do,right}]')
df.add_user_transition(State.PART_3_OS, State.PART_3_N, '[{No,no,not,nah,Nah,N,n}]')

# END
df.add_system_transition(State.PART_3_Y,State.HEAR_MORE, '"That is what I thought!\n   Let me tell you something about integration with the computer OS at the end of this conversation\n'
                                                   '   A mobile operating system (or mobile OS) is an operating system for mobile phones, tablets, smartwatches, 2-in-1 PCs\n'
                                                   '   Mobile devices with mobile communications abilities contain two mobile operating systems – \n'
                                                   '   - the main user-facing software platform is supplemented by a second low-level proprietary real-time operating system which operates the radio and other hardware.\n'
                                                   '   It is typically believed that iphones (IOS) integrate better with MacOS while Android integrate better with windows OS\n'
                                                   'Do you want to hear more about mobile devices and computer OS?"')

df.add_system_transition(State.PART_3_N,State.HEAR_MORE, '"That is strange. I definitely heard you say that you have used"$system_a"OS before.\n   Anyway, let me tell you something about integration with the computer OS at the end of this conversation\n'
                                                   '   A mobile operating system (or mobile OS) is an operating system for mobile phones, tablets, smartwatches, 2-in-1 PCs\n'
                                                   '   Mobile devices with mobile communications abilities contain two mobile operating systems – \n'
                                                   '   - the main user-facing software platform is supplemented by a second low-level proprietary real-time operating system which operates the radio and other hardware.\n'
                                                   '   It is typically believed that iphones (IOS) integrate better with MacOS while Android integrate better with windows OS\n'
                                                   'Do you want to hear more about mobile operating systems?"')

df.add_user_transition(State.HEAR_MORE,State.HEAR_MORE_Y,'[{Y,y,Yes,Yeah,yes,yeah,sure,of course,Of course,I do,i do,right}]')
df.add_user_transition(State.HEAR_MORE,State.HEAR_MORE_N,'[{No,no,not,nah,Nah,N,n}]')

df.add_system_transition(State.HEAR_MORE_Y, State.TRAP, '"There are a lot of mobile operating systems in the market right now.\n'
                                                        '   IOS and Android are the two biggest ones, there used to be Blackberry OS, Windows Phone and Symbian but those are discontinued now\n\n'
                                                        '   Android (based on the modified Linux kernel) is a mobile operating system developed by Google.\n '
                                                        '   The base system is open-source, but most of it is not copyleft, and the apps and drivers which provide the functionality are increasingly becoming closed-source.\n'
                                                        '   Besides having the largest installed base worldwide on smartphones, it is also the most popular operating system for general purpose computers\n\n'
                                                        '   iOS (formerly iPhone OS) is a mobile operating system created and developed by Apple Inc. exclusively for its hardware.\n'
                                                        '   It is the operating system that presently powers many of the company mobile devices, including the iPhone, and iPod Touch;\n'
                                                        '   it also powered the iPad prior to the introduction of iPadOS in 2019. It is the second most popular mobile operating system globally after Android.\n'
                                                        '   The iOS user interface is based upon direct manipulation, using multi-touch gestures.\n'
                                                        '   Interface control elements consist of sliders, switches, and buttons.\n'
                                                        '   Interaction with the OS includes gestures such as swipe, tap, pinch, and reverse pinch\n\n'
                                                        'S: It was very nice talking to you. Again, my name is Emily, the virtual chatbot! Goodbye"$name"!!"')
df.add_system_transition(State.HEAR_MORE_N, State.TRAP, '"It was very nice talking to you. Again, my name is Emily, the virtual chatbot! Goodbye"$name"!!"')

df.add_user_transition(State.TRAP,State.TRAP,'[{somethingthatpeoplewillnevertypesothattherewillnotbeanybugs}]')

# Part 3 - Errors
df.set_error_successor(State.PART_2_END_TRY, State.PART_3_ERROR_TRY)
df.set_error_successor(State.MAC_INFO_END, State.PART_3_ERROR_MAC)
df.set_error_successor(State.WINDOWS_INFO_END, State.PART_3_ERROR_WINDOWS)
df.set_error_successor(State.CHROME_INFO_END, State.PART_3_ERROR_CHROME)

df.add_system_transition(State.PART_3_ERROR_TRY, State.PART_2_END_TRY, '"I did not understand that...\nS: Do you think it is important for computers to integrate well with other mobile devices?"')
df.add_system_transition(State.PART_3_ERROR_MAC, State.MAC_INFO_END, '"I did not understand that...\nS: Do you think it is important for computers to integrate well with other mobile devices?"')
df.add_system_transition(State.PART_3_ERROR_WINDOWS, State.WINDOWS_INFO_END, '"I did not understand that...\nS: Do you think it is important for computers to integrate well with other mobile devices?"')
df.add_system_transition(State.PART_3_ERROR_CHROME, State.CHROME_INFO_END, '"I did not understand that...\nS: Do you think it is important for computers to integrate well with other mobile devices?"')

df.set_error_successor(State.WHY_Y,State.WHY_Y_ERROR)
df.set_error_successor(State.WHY_N,State.WHY_N_ERROR)

df.add_system_transition(State.WHY_Y_ERROR, State.WHY_Y, '"I did not understand that...\nS: What kind of mobile phone do you have?"')
df.add_system_transition(State.WHY_N_ERROR, State.WHY_N, '"I did not understand that...\nS: What kind of mobile phone do you have?"')

df.set_error_successor(State.PART_3_OS,State.PART_3_OS_ERROR)
df.add_system_transition(State.PART_3_OS_ERROR,State.PART_3_OS, '"I did not understand that...\nS: You said that you have used"$system_a"OS before, right?"')

df.set_error_successor(State.HEAR_MORE,State.HEAR_MORE_ERROR)
df.add_system_transition(State.HEAR_MORE_ERROR, State.HEAR_MORE, '"I did not understand that...\nS: Do you want to hear more about mobile operating systems?"')

df.set_error_successor(State.TRAP,State.TRAP_ERROR)
df.add_system_transition(State.TRAP_ERROR,State.TRAP, '"Goodbye!!!"')

df.run(debugging=False)