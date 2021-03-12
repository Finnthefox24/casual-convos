init 5 python:
    addEvent(
        Event(
            persistent._mas_compliments_database,
            eventlabel="mas_compliment_cool",
            prompt="You're cool",
            unlocked=True
        ),
        code="CMP"
    )


label mas_compliment_cool:
    $ mas_gainAffection(5,bypass=True)
    m 1tta "I'm cool, huh?"
    m 1dsa "Sorry, [player]..."
    m 1hub "But I'm not as cool as you are!"

    return
