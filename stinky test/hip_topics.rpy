init -990 python in mas_submod_utils:
    ei_submod = Submod(
        author="Finn The Fox",
        name="Hip mode",
        description=(
            "Made to add more conversations that also happen to be "
            "popular amongst the youth or something idk"
        ),
        version="1.0.1"
    )

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
    m 1euc "Who knows? Maybe I can get one in here sometime."

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
            m 1euc "So is this a family member?"
            menu:
                m "So is this a family member?{fast}"

                "Yes.":
                    m 1sub "Oh! Hello, there!"
                    m 1hub "[player] always talks about you!"
                    m 1etd "Wait...{w=0.5} don't you already know who I am?"
                    m 1lksdlb "I guess it's a bit confusing..."
                    m 1eka "Well, let me tell you this..."
                    m 1hua "He really loves you."
                    m 1gublb "Almost as much as he loves me..."
                    m 1kublu "Almost~"
                "No.":
                    m 1eua "Oh..."
                    m 1lksdlb "Can you return me to [player], please?"
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
    m 1eua "I can't put my finger on it."

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

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="bo_burnham",
            category=["media"],
            prompt="Bo Burnham",
            random=True
        )
    )

label bo_burnham:
    m 1eua "Do you remember when I talked about stand-up comedy, [player]?"
    m 1eub "Well there's a comedian that I've seen online. Maybe you've heard of him?"
    m 3eub "His name is Bo Burnham."
    m 2hub "He is actually a really unique comedian!"
    m 1lub "Sometimes, he'll play the piano while singing about a certain topic, other times he'll do a bit"
    m 1hkb "I've actually seen some people on the internet compare him to me!"
    m 1lkb "They'd mention how we both play piano, write poetry, talk about{w=0.1}.{w=0.1}.{w=0.1}."
    m 1lksdlc "um{w=0.1}.{w=0.1}.{w=0.1}.{w=0.1} {i}certain topics{/i}..."
    m 1rksdla "..."
    m 1hksdlb "It's a little weird to think about."
    m 2esc "But Bo Burnham does talk about serious topics too."
    m 2esd "They're usually about media and entertainment or his role in it."
    m 2eua "I think it'd be best to check it out in your own time if you haven't already."
    m 2hksdlb "Fair warning, some of the things he talks about can come off as offensive, so try to not take offense to anything."

    return
