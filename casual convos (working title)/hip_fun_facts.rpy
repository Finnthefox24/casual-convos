init 5 python:
    addEvent(
        Event(
            persistent._mas_fun_facts_database,
            eventlabel="mas_fun_fact_your_reality",
        ),
        code="FFF"
    )

label mas_fun_fact_your_reality:
    m 1eua "Did you know that 'Your Reality' is in C Major?"
    m 3eua "That means only the white keys are used on the Piano"
    m 1eua "Some Popular songs that use this key are 'Let It Be', 'While My Guitar Gently Weeps',"
    m 1eua "'Bad Romance', 'Piano Man', and 'Hallelujah'!"
    m 3eua "C Major is a really good key to start with if you're a beginner."
    m 1hua "That's why my song is C Major!"
    #Call the end
    call mas_fun_facts_end
    return

init 5 python:
    addEvent(
        Event(
            persistent._mas_fun_facts_database,
            eventlabel="mas_fun_fact_slayer",
        ),
        code="FFF"
    )

label mas_fun_fact_slayer:
    m 1eub "Did you know that the vocalist and bassist for the thrash metal band Slayer, Tom Araya, is a catholic?"
    m 3eua "Pretty unexpected, right?"
    m 1eua "I guess it goes to show that people on stage aren't always the same offstage."
    call mas_fun_facts_end
    return
