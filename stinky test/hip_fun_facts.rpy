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
    m 1eua "'Bad Romance', 'Piano Man', and 'Hallelujah'!" #finish later
    #Call the end
    call mas_fun_facts_end
    return
