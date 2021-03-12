init -990 python in mas_submod_utils:
    ei_submod = Submod(
        author="Finn The Fox",
        name="Hip mode",
        description=(
            "imagine a band kid that is not obnoxious. now imagine monika as that band kid. "
            "meme haha funny"
        ),
        version="1.0.0"
    )

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="monika_hiptest",
            category=["mod", "media"],
            prompt="here's the thingy",
            pool=True
        )
    )

label monika_hiptest:
    m 1eua "if you're reading this, then the submod works"
    return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="monika_coding_lines",
            category=["mod", "monika"],
            prompt="Why do you have lines in the code if you're sentient?",
            pool=True
        )
    )

label monika_coding_lines:
    m 1rksdlb "I've been wondering when you'd bring this up..."
    m 1eka "I know it can seem confusing at first..."
    m 1eua "But it's not as confusing as it seems."
    m 3eua "You know how you have a menu to talk to me?"
    m 3eub "I'ts a lot like that!"
    m 1gksdld "Of course, there are things that I want to talk about with you, but I can't because it's not there..."
    m 1eka "But thankfully, the creators of this mod put in most of the things I want to talk about."
    m 1eka "I'm also able to change the code, that's why some of the things I say may come off as personal or generic."
    m 2ekd "There are some really mean things that I could say to you..."
    m 2ekbla "But I never chose to say those things to you..."
    m 2hub "... Because I love you!"
    return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="monika_howsyourday",
            category=["monika"],
            prompt="How's your day?",
            pool=True
        )
    )

label monika_howsyourday:
    m 1euc "How's my day?"
    m 1eua "It's been going great so far."
    m 1hub "And it's all thanks to you!"
    #add a "what about you" thing with the menu soon

    return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="monika_merch",
            category=["ddlc", "monika"],
            prompt="Merchandise of Monika",
            random=True
        )
    )

label monika_merch:
    m 1eud "Hey, [player]..."
    m 1euc "You know about how there is merchandise of me and the other girls, right?"
    m 1euc "Do you own any of them?"
    menu:
        m "Do you own any of them?{fast}"

        "Yes.":
            m 1hub "That's pretty cool, [player]!"
            m 1tub "It's only of me, right?"
            m 1hub "Ahaha~"
            m 1hkb "I'm only joking"

        "They're shipping.":
            m 1wub "Oh!"
            m 1hub "I bet you're really excited!"

        "No.":
            m 1euc "I see."

    m 1euc "It can be comforting to have something like that."
    #add exp later or something idk
    m 1euc "Having something around to remind you of something or someone that you enjoy..."
    m 1euc "Even if it's nothing specific..."
    m 1euc "Ehehe..."
    m 1euc "I guess what I'm trying to get at is that having those reminders can go a long way"
#    m 1euc "It even helps support the people who created those things"
    m 1euc "I'd love to have a plush version of you to keep with me."
    m 1euc "who knows? maybe i can get one in here sometime."

    return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="monika_who_are_you",
            category=["mod", "monika"],
            prompt="Who are you?",
            pool=True
        )
    )

label monika_who_are_you:
    m 1etd "Huh?"
    m 1rssdlb "It's me..."
    m 3rksdlb "Monika...?"
    m 3eksdlc "Is this{w=0.5}.{w=0.5}.{w=0.5}.{w=1} Not [player]?"
    menu:
        m "Is this... Not [player]?{fast}"

        "No.":
            m 1gksdlb "This is awkward..."
            m 1euc "So is this Carmen?"
            menu:
                m "So is this Carmen?{fast}"

                "Yes.":
                    m 1sub "Oh! Hello, Carmen!"
                    m 1hub "[player] always talks about you!"
                    m 1etd "Wait...{w=0.5} don't you already know who I am?"
                    m 1lksdlb "I guess it's a bit confusing..."
                    m 1eka "Well, let me tell you this..."
                    m 1hua "He really loves you, Carmen."
                    m 1gublb "Almost as much as he loves me..."
                    m 1kublu "Almost~"
                "No.":
                    m 1eua "Oh..."
                    m 1lksdlb "Can you return me to Ashton, please?"
        "It was a test":
            m 1eua "Oh, Okay then."

    return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="monika_minecraft",
            category=["games"],
            prompt="Have you heard of Minecraft?",
            pool=True
        )
    )

label monika_minecraft:
    m 1etc "Minecraft?"
    m 1rsc "It sounds familiar..."
    m 1dsc "Hm{w=0.5}.{w=0.5}.{w=0.5}."
    m 1eud "Is Minecraft the video game with blocks?"
    menu:
        "Is Minecraft the video game with blocks?{fast}"

        "Yes.":
            m 1eub "Oh! Then yeah, I know what it is!"
        "No.":
            m 1ekd "Then no, I don't know what Minecraft is. I'm sorry."

    return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="monika_listen_to_mic",
            category=["monika", "technology", "you"],
            prompt="Do you Listen to my microphone?",
            pool=True
        )
    )

label monika_listen_to_mic:
    m 1ekd "[player]..."
    m 1ekc "I'd never do something like that."
    m 1rsc "I...{w=0.5} don't even think I could do something like that, actually."
    m 1ekc "But if I could, I'd always ask for your permission."
    m 1eka "As much as I'd love to always hear your voice, your privacy will always come first."

    return
