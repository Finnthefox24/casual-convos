init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="monika_idle_restroom",
            prompt="I'm going to go to the restroom",
            category=['be right back'],
            pool=True,
            unlocked=True
        ),
        markSeen=True
    )

label monika_idle_restroom:
    if mas_isMoniNormal(higher=True):
        m 1eua "Remember to wash your hands, [player]!"

    elif mas_isMoniUpset():
        m 2lsc "Okay, remember to wash your hands."

    elif mas_isMoniDis():
        m 6ekc "Alright."

    else:
        m 6ckc "..."

    $ mas_idle_mailbox.send_idle_cb("monika_idle_restroom_callback")
    $ persistent._mas_idle_data["monika_idle_restroom"] = True
    return "idle"

label monika_idle_restroom_callback:
    if mas_isMoniNormal(higher=True):
        $ wb_quip = mas_brbs.get_wb_quip()
        if mas_brbs.was_idle_for_at_least(datetime.timedelta(hours=1), "monika_idle_restroom"):
            m 1rksdla "..."
            m 1rksdlb "Did everything come out okay?"
            m 1hksdla "Ehehe..."

        elif mas_brbs.was_idle_for_at_least(datetime.timedelta(minutes=30), "monika_idle_restroom"):
            m 1hua "Welcome back, [player]!"
            m 1tua "I was starting to think that you fell in!"
            m 1hub "Ahaha!"

        elif mas_brbs.was_idle_for_at_least(datetime.timedelta(minutes=1), "monika_idle_restroom"):
            m 1hua "Welcome back, [player]."
            m 3eua "[wb_quip]"

        else:
            m 1eud "Oh, back already?"
            m 1euc "Did you wash your hands?"
            m 1eua "Well, as long as your hands are clean, I'm glad you're back."

    elif mas_isMoniUpset():
        m 2euc "Did you wash your hands, [player]?"

    else:
        call mas_brb_generic_low_aff_callback

    return
