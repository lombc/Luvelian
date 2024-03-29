label act_two_b1:

scene evil_castle
with dissolve

stop music fadeout 1.0
play music "wind_theme.mp3"

"{i}Leaving the forest, you finally come across the Abandoned Castle.{/i}"

"{i}As you approach the gates of the castle, you notice a hooded figure leaning on the gate.{/i}"

"{i}Deciding not to cause any trouble, you ignore the individual and reach towards the gate.{/i}"

scene evil_castle
with dissolve

show hr_p_fight:
    zoom 0.40
    xzoom -1.0
    xalign 0.1
    yalign 0.75
with dissolve

show reaper_scary:
    zoom 0.35
    xalign 1.0
    yalign 0.90
with dissolve

play sound "metal_clank.mp3"

"{i}The hooded figure hits the gate with his scythe just inches away from your hand.{/i}"

stop sound fadeout 1.0

show hr_p_fight:
    zoom 0.40
    xzoom -1.0
    xalign 0.1
    yalign 0.75

show reaper_scary:
    zoom 0.35
    xalign 1.0
    yalign 0.60

uc "What business brings you here?"

menu:
    "I’m looking for the Cursed Knight who resides here.":
        jump meet_reaper
    "None of yours if you value your life.":
        jump argue_reaper

label meet_reaper:
    uc "The Cursed Knight? I presume you are here for the bounty placed upon his head. If that is so, you truly do not value your life, traveler."

    uc "I too have \"business\" with a wanted individual."

    uc "Half-spider. Half-woman."

    scene evil_castle

    show hr_p_fight:
        zoom 0.40
        xzoom -1.0
        xalign 0.1
        yalign 0.75

    show reaper_scary:
        zoom 0.35
        xalign 1.0
        yalign 0.90

    "{i}The figure slowly runs his finger along the edge of his scythe.{/i}"

    scene evil_castle

    show hr_p_fight:
        zoom 0.40
        xzoom -1.0
        xalign 0.1
        yalign 0.75

    show reaper_scary:
        zoom 0.35
        xalign 1.0
        yalign 0.60

    uc "Do you happen to have met her?"

    scene evil_castle

    show hr_p_fight:
        zoom 0.40
        xzoom -1.0
        xalign 0.1
        yalign 0.75

    show reaper_scary:
        zoom 0.35
        xalign 1.0
        yalign 0.90

    menu:
        "As a matter of fact, I just ran into her recently. Quite charming, really.":
            jump met_arachne
        "Doesn’t ring a bell. Sorry.":
            jump not_met_arachne
    
    label met_arachne:

        scene evil_castle

        show hr_p_fight:
            zoom 0.40
            xzoom -1.0
            xalign 0.1
            yalign 0.75

        show reaper_surprised:
            zoom 0.35
            xalign 1.0
            yalign 0.60

        uc "You side with that wench?"

        "{i}In an instant, the figure shoves you to the ground with his scythe. He brings his weapon back, looking to attack you as you lie helplessly on the ground.{/i}"

        scene evil_castle
        with hpunch

        play sound "fall.mp3" noloop

        show hr_p_fight:
            zoom 0.40
            xzoom -1.0
            xalign 0.1
            yalign 0.75

        show reaper_scary:
            zoom 0.35
            xalign 1.0
            yalign 0.60

        uc "There are two things that are guaranteed in life."

        uc "Death…"

        uc "and most certainly…"

        "{i}Mid-swing, the figure stops and seems to notice something on the ground near you. The locket given to you by Arachne.{/i}"

        scene evil_castle

        show hr_p_fight:
            zoom 0.40
            xzoom -1.0
            xalign 0.1
            yalign 0.75

        show reaper_surprised:
            zoom 0.35
            xalign 1.0
            yalign 0.90

        scene evil_castle

        show hr_p_surprised:
            zoom 0.40
            xzoom -1.0
            xalign 0.1
            yalign 0.75

        show reaper_happy:
            zoom 0.35
            xalign 1.0
            yalign 0.60

        uc "Snuggles!"

        scene evil_castle

        show hr_p_flat:
            zoom 0.40
            xzoom -1.0
            xalign 0.1
            yalign 0.60

        show reaper_happy:
            zoom 0.35
            xalign 1.0
            yalign 0.90 
 
        hr "Snuggles?"

        scene evil_castle

        show hr_p:
            zoom 0.40
            xzoom -1.0
            xalign 0.1
            yalign 0.75

        show reaper_happy:
            zoom 0.35
            xalign 1.0
            yalign 0.90

        "{i}The figure drops his scythe and rushes over to pick up the locket you dropped.{/i}"

        scene evil_castle

        show hr_p:
            zoom 0.40
            xzoom -1.0
            xalign 0.1
            yalign 0.75

        show reaper_laugh:
            zoom 0.35
            xalign 1.0
            yalign 0.60

        uc "The name of my long lost dog. This is the only photo I have of him."

        scene evil_castle

        show hr_p:
            zoom 0.40
            xzoom -1.0
            xalign 0.1
            yalign 0.60

        show reaper_happy:
            zoom 0.35
            xalign 1.0
            yalign 0.90

        hr "Well you can keep it. It belongs to you anyways."

        scene evil_castle

        show hr_p:
            zoom 0.40
            xzoom -1.0
            xalign 0.1
            yalign 0.75

        show reaper_happy:
            zoom 0.35
            xalign 1.0
            yalign 0.60

        uc "Naturally. That depraved brat stole it from me. It must have been quite the trouble to tear it from her wretched hands."

        uc "....and thank you. This locket means everything to me."

        uc "They call me Reaper."

        rp "..."

        rp "Ludwig is waiting for you."

        scene evil_castle

        show hr_p:
            zoom 0.40
            xzoom -1.0
            xalign 0.1
            yalign 0.60

        show reaper_happy:
            zoom 0.35
            xalign 1.0
            yalign 0.90

        hr "Who?"

        scene evil_castle

        show hr_p:
            zoom 0.40
            xzoom -1.0
            xalign 0.1
            yalign 0.75

        show reaper_laugh:
            zoom 0.35
            xalign 1.0
            yalign 0.60

        rp "The \"Cursed Knight\" you seek. And whatever business you have with him, I could care less."

        "{i}Reaper turns his head towards the castle with a longing glance for a moment.{/i}"

        rp "…He\'s long gone anyways. He won\'t be much of a threat to you, so no need to tread with caution."


        play sound "door_creak.mp3"

        scene evil_castle

        show hr_p:
            zoom 0.40
            xzoom -1.0
            xalign 0.1
            yalign 0.75

        show reaper_happy:
            zoom 0.35
            xalign 1.0
            yalign 0.90

        "{i}Reaper opens the gate for you and motions for you to pass through.{/i}"

        scene evil_castle

        show hr_p:
            zoom 0.40
            xzoom -1.0
            xalign 0.1
            yalign 0.75

        show reaper_happy:
            zoom 0.35
            xalign 1.0
            yalign 0.60

        rp "Until we meet again, hero."

        scene evil_castle
        with dissolve

        play sound "woosh.mp3" noloop

        "{i}Suddenly, Reaper disappears into a thick black mist.{/i}"

        "{i}You decide to pass through the gate and enter the Abandoned Castle.{/i}"

        jump act_two_b1_p2

    label not_met_arachne:

        show hr_p_fight:
            zoom 0.40
            xzoom -1.0
            xalign 0.1
            yalign 0.75

        show reaper_scary:
            zoom 0.35
            xalign 1.0
            yalign 0.60

        uc "I can tell when someone is lying to me."
        uc "In fact..."
        uc "You came from that forest {i}she{/i} resides in."

        "{i}In an instant, the figure shoves you to the ground with his scythe. He brings his weapon back, looking to attack you as you lie helplessly on the ground.{/i}"

        scene evil_castle
        with hpunch

        play sound "fall.mp3" noloop

        show hr_p_fight:
            zoom 0.40
            xzoom -1.0
            xalign 0.1
            yalign 0.75

        show reaper_scary:
            zoom 0.35
            xalign 1.0
            yalign 0.60

        uc "There are two things that are guaranteed in life."

        uc "Death…"

        uc "and most certainly…"

        "{i}Mid-swing, the figure stops and seems to notice something on the ground near you. The locket given to you by Arachne.{/i}"

        scene evil_castle

        show hr_p_fight:
            zoom 0.40
            xzoom -1.0
            xalign 0.1
            yalign 0.75

        show reaper_surprised:
            zoom 0.35
            xalign 1.0
            yalign 0.90

        scene evil_castle

        show hr_p_surprised:
            zoom 0.40
            xzoom -1.0
            xalign 0.1
            yalign 0.75

        show reaper_happy:
            zoom 0.35
            xalign 1.0
            yalign 0.60

        uc "Snuggles!"

        scene evil_castle

        show hr_p_surprised:
            zoom 0.40
            xzoom -1.0
            xalign 0.1
            yalign 0.60

        show reaper_happy:
            zoom 0.35
            xalign 1.0
            yalign 0.90 
 
        hr "Snuggles?"

        scene evil_castle

        show hr_p:
            zoom 0.40
            xzoom -1.0
            xalign 0.1
            yalign 0.75

        show reaper_happy:
            zoom 0.35
            xalign 1.0
            yalign 0.90

        "{i}The figure drops his scythe and rushes over to pick up the locket you dropped.{/i}"

        scene evil_castle

        show hr_p:
            zoom 0.40
            xzoom -1.0
            xalign 0.1
            yalign 0.75

        show reaper_happy:
            zoom 0.35
            xalign 1.0
            yalign 0.60

        uc "The name of my long lost dog. This is the only photo I have of him."

        scene evil_castle

        show hr_p:
            zoom 0.40
            xzoom -1.0
            xalign 0.1
            yalign 0.60

        show reaper_happy:
            zoom 0.35
            xalign 1.0
            yalign 0.90

        hr "Well you can keep it. It belongs to you anyways."

        scene evil_castle

        show hr_p:
            zoom 0.40
            xzoom -1.0
            xalign 0.1
            yalign 0.75

        show reaper_happy:
            zoom 0.35
            xalign 1.0
            yalign 0.60

        uc "Naturally. That depraved brat stole it from me. It must have been quite the trouble to tear it from her wretched hands."

        uc "And…thank you. This locket means everything to me."

        uc "They call me Reaper."

        rp "..."

        rp "Ludwig is waiting for you."

        scene evil_castle

        show hr_p:
            zoom 0.40
            xzoom -1.0
            xalign 0.1
            yalign 0.60

        show reaper_happy:
            zoom 0.35
            xalign 1.0
            yalign 0.90

        hr "Who?"

        scene evil_castle

        show hr_p:
            zoom 0.40
            xzoom -1.0
            xalign 0.1
            yalign 0.75

        show reaper_laugh:
            zoom 0.35
            xalign 1.0
            yalign 0.60

        rp "The \"Cursed Knight\" you seek. And whatever business you have with him, I could care less."

        "{i}Reaper turns his head towards the castle with a longing glance for a moment.{/i}"

        rp "…He\'s long gone anyways. He won\'t be much of a threat to you, so no need to tread with caution."


        play sound "door_creak.mp3"

        scene evil_castle

        show hr_p:
            zoom 0.40
            xzoom -1.0
            xalign 0.1
            yalign 0.75

        show reaper_happy:
            zoom 0.35
            xalign 1.0
            yalign 0.90

        "{i}Reaper opens the gate for you and motions for you to pass through.{/i}"

        scene evil_castle

        show hr_p:
            zoom 0.40
            xzoom -1.0
            xalign 0.1
            yalign 0.75

        show reaper_happy:
            zoom 0.35
            xalign 1.0
            yalign 0.60

        rp "Until we meet again, hero."

        scene evil_castle
        with dissolve

        play sound "woosh.mp3" noloop

        "{i}Suddenly, Reaper disappears into a thick black mist.{/i}"

        "{i}You decide to pass through the gate and enter the Abandoned Castle.{/i}"

        jump act_two_b1_p2

label argue_reaper:
    scene evil_castle

    show hr_p_fight:
        zoom 0.40
        xzoom -1.0
        xalign 0.1
        yalign 0.75

    show reaper_scary:
        zoom 0.35
        xalign 1.0
        yalign 0.60 

    uc "Hah! The naivety of mortals is never dull."

    scene evil_castle

    show hr_p_fight:
        zoom 0.40
        xzoom -1.0
        xalign 0.1
        yalign 0.75

    show reaper_scary:
        zoom 0.35
        xalign 1.0
        yalign 0.90

    "{i}In an instant, the figure shoves you to the ground with his scythe. He brings his weapon back, looking to attack you as you lie helplessly on the ground.{/i}"

    scene evil_castle
    with hpunch

    play sound "fall.mp3" noloop

    show hr_p_fight:
        zoom 0.40
        xzoom -1.0
        xalign 0.1
        yalign 0.75

    show reaper_scary:
        zoom 0.35
        xalign 1.0
        yalign 0.60

    uc "There are two things that are guaranteed in life."

    uc "Death…"

    uc "and most certainly…"

    "{i}Mid-swing, the figure stops and seems to notice something on the ground near you. The locket given to you by Arachne.{/i}"

    scene evil_castle

    show hr_p_fight:
        zoom 0.40
        xzoom -1.0
        xalign 0.1
        yalign 0.75

    show reaper_surprised:
        zoom 0.35
        xalign 1.0
        yalign 0.90

    scene evil_castle

    show hr_p_surprised:
        zoom 0.40
        xzoom -1.0
        xalign 0.1
        yalign 0.75

    show reaper_happy:
        zoom 0.35
        xalign 1.0
        yalign 0.60

    uc "Snuggles!"

    scene evil_castle

    show hr_p_surprised:
        zoom 0.40
        xzoom -1.0
        xalign 0.1
        yalign 0.60

    show reaper_happy:
        zoom 0.35
        xalign 1.0
        yalign 0.90 

    hr "Snuggles?"

    scene evil_castle

    show hr_p:
        zoom 0.40
        xzoom -1.0
        xalign 0.1
        yalign 0.75

    show reaper_happy:
        zoom 0.35
        xalign 1.0
        yalign 0.90

    "{i}The figure drops his scythe and rushes over to pick up the locket you dropped.{/i}"

    scene evil_castle

    show hr_p:
        zoom 0.40
        xzoom -1.0
        xalign 0.1
        yalign 0.75

    show reaper_happy:
        zoom 0.35
        xalign 1.0
        yalign 0.60

    uc "The name of my long lost dog. This is the only photo I have of him."

    scene evil_castle

    show hr_p:
        zoom 0.40
        xzoom -1.0
        xalign 0.1
        yalign 0.60

    show reaper_happy:
        zoom 0.35
        xalign 1.0
        yalign 0.90

    hr "Well you can keep it. It belongs to you anyways."

    scene evil_castle

    show hr_p:
        zoom 0.40
        xzoom -1.0
        xalign 0.1
        yalign 0.75

    show reaper_happy:
        zoom 0.35
        xalign 1.0
        yalign 0.60

    uc "Naturally. That depraved brat stole it from me. It must have been quite the trouble to tear it from her wretched hands."

    uc "And…thank you. This locket means everything to me."

    uc "They call me Reaper."

    rp "..."

    rp "Ludwig is waiting for you."

    scene evil_castle

    show hr_p:
        zoom 0.40
        xzoom -1.0
        xalign 0.1
        yalign 0.60

    show reaper_happy:
        zoom 0.35
        xalign 1.0
        yalign 0.90

    hr "Who?"

    scene evil_castle

    show hr_p:
        zoom 0.40
        xzoom -1.0
        xalign 0.1
        yalign 0.75

    show reaper_laugh:
        zoom 0.35
        xalign 1.0
        yalign 0.60

    rp "The \"Cursed Knight\" you seek. And whatever business you have with him, I could care less."

    "{i}Reaper turns his head towards the castle with a longing glance for a moment.{/i}"

    rp "…He\'s long gone anyways. He won\'t be much of a threat to you, so no need to tread with caution."


    play sound "door_creak.mp3"

    scene evil_castle

    show hr_p:
        zoom 0.40
        xzoom -1.0
        xalign 0.1
        yalign 0.75

    show reaper_happy:
        zoom 0.35
        xalign 1.0
        yalign 0.90

    "{i}Reaper opens the gate for you and motions for you to pass through.{/i}"

    scene evil_castle

    show hr_p:
        zoom 0.40
        xzoom -1.0
        xalign 0.1
        yalign 0.75

    show reaper_happyr:
        zoom 0.35
        xalign 1.0
        yalign 0.60

    rp "Until we meet again, hero."

    scene evil_castle
    with dissolve

    play sound "woosh.mp3" noloop

    "{i}Suddenly, Reaper disappears into a thick black mist.{/i}"

    "{i}You decide to pass through the gate and enter the Abandoned Castle.{/i}"

    jump act_two_b1_p2


