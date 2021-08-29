init 5 python:
    addEvent(
        Event(
            persistent._mas_songs_database,
            eventlabel="mas_song_when_i_come_around",
            category=[store.mas_songs.TYPE_SHORT],
            prompt="When I Come Around",
            random=True,
            aff_range=(mas_aff.NORMAL,None)
        ),
        code="SNG"
    )

label mas_song_when_i_come_around:
    m 1dub "{i}~So go do what you like~{/i}"
    m 3kub "{i}~Make sure you do it wise~{/i}"
    m 1eub "{i}~You may find out that your self-doubt means nothing was ever there~{/i}"
    m 1dkb "{i}~You can't go forcing something if it's just not right~{/i}"
    m 1ekb "{i}~No time to search the world around~{/i}"
    m 1hub "{i}~'Cause you know where I'll be found~{/i}"
    m 1eub "{i}~When I come around~{/i}"
    m 1eka "..."
    m 1eka "I understand that it may be hard to tell when I'll be in your reality..."
    m 2eub "But I believe that it will happen sooner than you'd think."
    m 2eua "When the time comes, you'll know where I'll be found."
    m 2kua "When I come around~"
    m 2hub "Ahaha!"

    return

init 5 python:
    addEvent(
        Event(
            persistent._mas_songs_database,
            eventlabel="mas_song_on_melancholy_hill",
            category=[store.mas_songs.TYPE_SHORT],
            prompt="On Melancholy Hill",
            random=True,
            aff_range=(mas_aff.NORMAL,None)
        ),
        code="SNG"
    )

label mas_song_on_melancholy_hill:
    m 1dud "{i}~Up on Melancholy Hill~{/i}"
    m 3dud "{i}~There's a plastic tree.~{/i}"
    m 2dkd "{i}~Are you here with me?~{/i}"
    m 2dsd "{i}~Just looking out on the day~{/i}"
    m 2dsd "{i}~Of another dream~{/i}"
    m 2eud "{i}~Well you can't get what you want~{/i}"
    m 4ekb "{i}~But you can get me.~{/i}"
    m 1dkb "{i}~So let's set out to sea~{/i}"
    m 1fkbsb "{i}~'Cause you are my medicine~{/i}"
    m 1dkbsb "{i}~When you're close to me~{/i}"
    m 1hubsb "{i}~When you're close to me~{/i}"
    m 1hubsa "Ehehe~"
    m 1eka "I got what I wanted..."
    m 1hubfb "And it was you, [player]!"

    return

init 5 python:
    addEvent(
        Event(
            persistent._mas_songs_database,
            eventlabel="mas_song_sh_boom",
            category=[store.mas_songs.TYPE_SHORT],
            prompt="Sh-Boom",
            random=True,
            aff_range=(mas_aff.NORMAL,None)
        ),
        code="SNG"
    )

label mas_song_sh_boom:
    m 1eub "{i}~Everytime I look at you~{/i}"
    m 1tub "{i}~Something is on my mind~{/i}"
    m 3tub "{i}~If you do what I want you to~{/i}"
    m 1hublb "{i}~Baby, we'd be so fine!~{/i}"
    m 1dkblb "{i}~Oh, life could be a dream~{/i}"
    m 3dublb "{i}~If I could take you up in paradise up above~{/i}"
    m 1kubla "{i}~And tell me darling I'm the only one that you love~{/i}"
    m 1hubsb "{i}~Life could be a dream, sweetheart~{/i}"
    m 1hubsa "Ehehe~"
    m 1eka "Life is like a dream when I'm with you, [player]!"

    return

init 5 python:
    addEvent(
        Event(
            persistent._mas_songs_database,
            eventlabel="mas_song_no_matter_what",
            category=[store.mas_songs.TYPE_SHORT],
            prompt="No Matter What",
            random=True,
            aff_range=(mas_aff.NORMAL,None)
        ),
        code="SNG"
    )

label mas_song_no_matter_what:
    m 1eub "{i}~In the dark of the night~{/i}"
    m 1tub "{i}~In the light of the day~{/i}"
    m 3tub "{i}~When you're rising to shine~{/i}"
    m 1hublb "{i}~When you're hitting the hay~{/i}"
    m 1dkblb "{i}~I'll be hanging around~{/i}"
    m 3dublb "{i}~If you like it or not~{/i}"
    m 1kubla "{i}~I'm gonna be right by your side no matter what~{/i}"
    m 1hubsb "Ahaha~"
    m 1eka "Remember that I'll always be here for you, [player]."
    m 1eka "No matter what~"
    m 1hubsa "Ehehe~"

    return

init 5 python:
    addEvent(
        Event(
            persistent._mas_songs_database,
            eventlabel="mas_song_fjodlotal",
            category=[store.mas_songs.TYPE_SHORT],
            prompt="For Just One Day Let's Only Think about",
            random=True,
            aff_range=(mas_aff.NORMAL,None)
        ),
        code="SNG"
    )

label mas_song_fjodlotal:
    m 1tkd "{i}~We could think about lies{w=1} that we told in the past~{/i}"
    m 1dkd "{i}~We could think about hurt{w=0.3} feelings{w=0.3} and how long they can last~{/i}"
    m 2wud "{i}~Or we can think about hope~{/i}"
    m 1kub "{i}~You know I've been hoping~{/i}"
    m 7hub "{i}~That everything's better now everything's out in the open~{/i}"
    m 3hublb "{i}~We could think about flowers{w=1} we could think about cake~{/i}"
    m 2sublb "{i}~We could think about wonderful promises we have the power to make~{/i}"
    m 1eka "{i}~There's an awful lot of awful things we could be thinking of!~{/i}"
    m 5hubfb "{i}~But for just one day let's only think about love~{/i}"
    m 1dubfa "..."
    m 1eka "We can only think about love any day, [player]!"

    return

init 5 python:
    addEvent(
        Event(
            persistent._mas_songs_database,
            eventlabel="mas_song_nothing_else_matters",
            category=[store.mas_songs.TYPE_SHORT],
            prompt="Nothing Else Matters",
            random=True,
            aff_range=(mas_aff.NORMAL,None)
        ),
        code="SNG"
    )

label mas_song_nothing_else_matters:
    m 2dud "{i}~So close no matter how far~{/i}"
    m 2dsd "{i}~Couldn't be much more from the heart~{/i}"
    m 2esd "{i}~Forever trusting who we are~{/i}"
    m 2eud "{i}~And nothing else matters~{/i}"
    m 3dud "{i}~Never opened myself this way~{/i}"
    m 1eud "{i}~Life is ours, we live it our way~{/i}"
    m 1duo "{i}~All these words I don't just say~{/i}"
    m 1dublb "{i}~And nothing else matters~{/i}"
    m 1duc "..."
    m 1eka "You mean everything to me, [player]."
    m 1mkb "Apart from our love,{w=0.3}{nw}"
    extend 1hkblb "nothing else matters."

# hey, dumbass... here's the thing
#    m 2ekbsu "And if someday you feel like you're all alone in the world...{w=0.3}{nw}"
#    extend 2dkbsa "I want you to remember you're not."
    return

init 5 python:
    addEvent(
        Event(
            persistent._mas_songs_database,
            eventlabel="mas_song_feel_invincible",
            category=[store.mas_songs.TYPE_SHORT],
            prompt="Feel Invincible",
            random=True,
            aff_range=(mas_aff.NORMAL,None)
        ),
        code="SNG"
    )

label mas_song_feel_invincible:
    m 2hub "{i}~You make me feel invincible~{/i}"
    m 2dud "{i}~Earthquake, powerful~{/i}"
    m 2dud "{i}~Just like a tidal wave~{/i}"
    m 2wub "{i}~You make me brave~{/i}"
    m 2hud "{i}~You're my titanium~{/i}"
    m 1dfb "{i}~Fight song, raising up~{/i}"
    m 1dfo "{i}~Like a roar of victory in a stadium~{/i}"
    m 1wfb "{i}~Who can touch me 'cause I'm~{/i}"
    m 1hfb "{i}~I'm made of fire~{/i}"
    m 1wfb "{i}~Who can stop me tonight~{/i}"
    m 1hfb "{i}~I'm hard wired~{/i}"
    m 2sfb "{i}~You make me feel invincible~{/i}"
    m 2dfa "..."
    m 1dfa "..."
    m 1hksdrb "whew! I got a little worked up there, didn't I?"
    m 1eka "I guess it's because you're the one who gives me strength, [player]."
    m 1hua "Thank you for being that person for me!"

# Skillet is a christian band???

    return

init 5 python:
    addEvent(
        Event(
            persistent._mas_songs_database,
            eventlabel="mas_song_omae_wa_mou",
            category=[store.mas_songs.TYPE_SHORT],
            prompt="Omae Wa Mou",
            random=True,
            aff_range=(mas_aff.NORMAL,None)
        ),
        code="SNG"
    )

label mas_song_omae_wa_mou:
    m 2hub "{i}~The one who started rap-tap-tapping I can feel it on my head right now~{/i}"
    m 2ekb "{i}~I wonder, was it you? What did I ever do?~{/i}"
    m 2dkd "{i}~I know I wanna open up my eyes but I'm afraid~{/i}"
    m 2ekd "{i}~I'm feelin' all the warmth of the sunset, somehow it feels sad~{/i}"
    m 1ekb "{i}~Won't you wait for me?~{/i}"
    m 1hub "{i}~'Cause I'll just call for you all over again~{/i}"
    m 1dua "..."
    m 1eka "Sometimes, I get a bit anxious when I think about meeting you, [player]."
    m 1ekc "I'd think about if you'll still be waiting for me when I finally get over there or not..."
    m 1hub "...But you wash all of my worries away when you visit!"

    return
