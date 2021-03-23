init 5 python:
    addEvent(
        Event(
            persistent._mas_mood_database,
            "mas_mood_cold",
            prompt="...cold",
            category=[store.mas_moods.TYPE_GOOD],
            unlocked=True
        ),
        eventdb=store.mas_moods.mood_db
    )

label mas_mood_cold:
    m 1eka "[player]..."
    m 3eka "If you're feeling cold, why not go get a blanket?"
    m 1ekbsa"But if I was with you, I'd hold you so you'd be warm~"
    m 1gsbsa "I could probably just make sure it's always cold in your house...{nw}"
    $ _history_list.pop()
    m 1hksdlb "Pretend that you didn't see that..."
    return
