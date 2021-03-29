init 5 python:
    addEvent(
        Event(
            persistent._mas_windowreacts_database,
            eventlabel="mas_wrs_lmms",
            category=['LMMS'],
            rules={
                "notif-group": "Window Reactions",
                "skip alert": None,
                "keep_idle_exp": None
            },
            show_in_idle=True
        ),
        code="WRS"
    )

label mas_wrs_lmms:
    $ wrs_success = display_notif(
        m_name,
        [
            "Are you writing me a love song, [player]?",
            "I'd love to listen to whatever\nyou make, [player]!",
            "I can't wait to hear what you make!"
        ],
        'Window Reactions'
    )

    #Unlock again if we failed
    if not wrs_success:
        $ mas_unlockFailedWRS('mas_wrs_lmms')
    return

init 5 python:
    addEvent(
        Event(
            persistent._mas_windowreacts_database,
            eventlabel="mas_wrs_spotify",
            category=['Spotify'],
            rules={
                "notif-group": "Window Reactions",
                "skip alert": None,
                "keep_idle_exp": None
            },
            show_in_idle=True
        ),
        code="WRS"
    )

label mas_wrs_spotify:
    $ wrs_success = display_notif(
        m_name,
        [
            "Find anything new, [player]?",
            "Need reccomendations, [player]?",
            "I hope you have good taste!\nAhaha!"
        ],
        'Window Reactions'
    )

    #Unlock again if we failed
    if not wrs_success:
        $ mas_unlockFailedWRS('mas_wrs_spotify')
    return

init 5 python:
    addEvent(
        Event(
            persistent._mas_windowreacts_database,
            eventlabel="mas_wrs_discord",
            category=['Discord'],
            rules={
                "notif-group": "Window Reactions",
                "skip alert": None,
                "keep_idle_exp": None
            },
            show_in_idle=True
        ),
        code="WRS"
    )

label mas_wrs_discord:
    $ wrs_success = display_notif(
        m_name,
        [
            "Talking to your friends, [player]?",
            "I hope everyone is being nice to each other.",
            "I hope you don't mind if I take a look\nat your direct messages, [player]~"
        ],
        'Window Reactions'
    )

    #Unlock again if we failed
    if not wrs_success:
        $ mas_unlockFailedWRS('mas_wrs_discord')
    return
