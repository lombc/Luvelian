# Introduction

# Characters
define narrator = Character(None, italics=True)

# Hero
define hr = Character(color="#52be4f")
image hr_p = "hr.png"
image hr_p_webbed = "hr_webbed.png"

# Cursed Knight/Ludwig
define ck = Character("Cursed Knight", color="#9e063b")
define lg = Character("Ludwig", color="#9e063b")
image ck_p = "Cursed_Knight.png"

# Arachne
define ar = Character("Arachne", color="#aa22ff")
image ar_p = "Arachne_02.png"
image ar_p_blush = "Arachne_Blush.png"
image ar_p_laugh = "Arachne_Laughing.png"
image ar_p_talk = "Arachne_Talking.png"
image ar_p_wink = "Arachne_Winking.png"
image ar_p_unimp = "Arachne_Unimpressed.png"

# Dryad
define dr = Character("Dryad", color="#808000")
image dr_p = "dryad.png"
image dr_p_smile = "dryad_smile.png"

# Mysterious Stranger
define sc = Character("Mysterious Stranger", color="#ff000f")
define uc = Character("????", color="#adaec2")

# Deer
image deer_dead = "deer_dead.png"
image deer_wounded = "deer_wounded_01.png"
image deer_healed = "deer_bandage.png"

# Reaper
define rp = Character("Reaper", color="#adaec2")
image reaper = "Reaper_02.png"
image reaper_happy = "Reaper_Happy.png"
image reaper_laugh = "Reaper_Laugh.png"
image reaper_scary = "Reaper_Scary.png"
image reaper_surprised = "Reaper_Surprised.png"

# Extras
define gender = 0
define know = 0
define deer_help = 0
image bounty = "bounty_board.png"
image bounty_blur = im.Blur("bounty_board.png", 1.5)




label start:

    stop music fadeout 1.0

    play music "intro.mp3"
    scene black with dissolve

    label gender:
        '{i}What are your pronouns?{/i}'

        menu Choice:
            "He/Him":
                jump gender_male
            "She/Her":
                jump gender_female
            "They/Them":
                jump gender_neutral

        label gender_male:
            show hr_p:
                zoom 0.5
                xalign 0.5
                yalign 0.5
            with dissolve
            '{i}Are you male?{/i}'

            menu:
                "Yes":
                    $ gender = 1
                    jump name
                "No":
                    jump gender

        label gender_female:
            show hr_p:
                zoom 0.5
                xalign 0.5
                yalign 0.5
            with dissolve
            '{i}Are you female?{/i}'

            menu:
                "Yes":
                    $ gender = 2
                    jump name
                "No":
                    jump gender

        label gender_neutral:
            show hr_p:
                zoom 0.5
                xalign 0.5
                yalign 0.5
            with dissolve
            '{i}Are you neither?{/i}'

            menu:
                "Yes":
                    $ gender = 3
                    jump name
                "No":
                    jump gender

    label name:

    $ hr = renpy.input("What is your name?")
    $ hr = hr.strip()

    if hr == "":
        $ hr = "Dori"

   
    scene black with dissolve

    # Put background of Kingdom here
    scene main_menu_bg with dissolve

    "{i}[hr], you are the hero of a kingdom, who has proven yourself in battle and as a responsible pillar of justice. However, one thing weighs on your mind.{/i}"

    "{i}No amount of adventures, gold, or accolades can fill the void that is your singled lonely heart.{/i}"

    "{i}You\’ve decided to find love anywhere you can.{/i}"

    "{i}You still have a responsibility to keep the kingdom and its surroundings safe however.{/i}"

    # Put background of a bounty board here
    scene main_menu_bg with dissolve
    show bounty:
        zoom 0.25
        xalign 0.5
        yalign 1.0
    with dissolve

    "{i}You resort to the one thing you do best, which is checking the local bounty board for any jobs that need to be done.{/i}"

    "{i}Five Wanted posters are posted on the bounty board - Demon, Dryad, Cursed Knight, Arachne, Bandit Captain.{/i}"

    show bounty_blur:
        zoom 0.25
        xalign 0.5
        yalign 1.0

    menu:
        "Which one do you choose?"

        "Demon":
            jump wrong_villain
        "Dryad":
            jump wrong_villain
        "Cursed Knight":
            jump cursed_knight
        "Arachne":
            jump wrong_villain
        "Bandit Captain":
            jump wrong_villain


    label wrong_villain:

    scene chaos with dissolve
    stop music fadeout 1.0
    play music "encounter.mp3"
    "{i}This villain is too powerful for you to defeat. You are killed, the kingdom plunges into chaos, and its citizens experience demise. Game Over.{/i}"

    label end:

    return
