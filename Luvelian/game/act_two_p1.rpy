label act_two_p1:

scene evil_castle
with dissolve

stop music fadeout 1.0
play music "wind_theme.mp3"

"Leaving the forest, you finally come across the Abandoned Castle."

"As you approach the gates of the castle, you notice a hooded figure leaning on the gate."

"Deciding not to cause any trouble, you ignore the individual and reach towards the gate"

scene evil_castle
with dissolve

show hr_p:
    zoom 0.40
    xzoom -1.0
    xalign 0.1
    yalign 0.75
with dissolve

show reaper:
    zoom 0.35
    xalign 1.0
    yalign 0.90
with dissolve

play sound "metal_clank.mp3"

"The hooded figure hits the gate with his scythe just inches away from your hand."

stop sound fadeout 1.0

show hr_p:
    zoom 0.40
    xzoom -1.0
    xalign 0.1
    yalign 0.75

show reaper:
    zoom 0.35
    xalign 1.0
    yalign 0.60

uc "What business brings you here?"

menu:
    "I’m looking for the Cursed Knight who resides here.":
        jump dodge_reaper
    "None of yours if you value your life.":
        jump fight_reaper

label dodge_reaper:
    uc "The Cursed Knight? I presume you are here for the bounty placed upon his head. If that is so, you truly do not value your life, traveler."

    uc "I too have \"business\" with a wanted individual."

    uc "Half-spider. Half-woman."

    scene evil_castle

    show hr_p:
        zoom 0.40
        xzoom -1.0
        xalign 0.1
        yalign 0.75

    show reaper:
        zoom 0.35
        xalign 1.0
        yalign 0.90

    "The figure slowly runs his finger along the edge of his scythe."

    scene evil_castle

    show hr_p:
        zoom 0.40
        xzoom -1.0
        xalign 0.1
        yalign 0.75

    show reaper:
        zoom 0.35
        xalign 1.0
        yalign 0.60

    uc "Do you happen to have met her?"

    scene evil_castle

    show hr_p:
        zoom 0.40
        xzoom -1.0
        xalign 0.1
        yalign 0.75

    show reaper:
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

        show hr_p:
            zoom 0.40
            xzoom -1.0
            xalign 0.1
            yalign 0.75

        show reaper:
            zoom 0.35
            xalign 1.0
            yalign 0.60

        uc "You side with that wench?"

        "In an instant, the figure shoves you to the ground with his scythe. He brings his weapon back, looking to attack you as you lie helplessly on the ground."

        scene evil_castle
        with hpunch

        play sound "fall.mp3" noloop

        show hr_p:
            zoom 0.40
            xzoom -1.0
            xalign 0.1
            yalign 0.75

        show reaper:
            zoom 0.35
            xalign 1.0
            yalign 0.60

        uc "There are two things that are guaranteed in life."

        uc "Death…"

        uc "and most certainly…"

        "Mid-swing, the figure stops and seems to notice something on the ground near you. The locket given to you by Arachne."

        scene evil_castle

        show hr_p:
            zoom 0.40
            xzoom -1.0
            xalign 0.1
            yalign 0.75

        show reaper:
            zoom 0.35
            xalign 1.0
            yalign 0.90

        scene evil_castle

        show hr_p:
            zoom 0.40
            xzoom -1.0
            xalign 0.1
            yalign 0.75

        show reaper:
            zoom 0.35
            xalign 1.0
            yalign 0.60

        uc "Snuggles!"

        scene evil_castle

        show hr_p:
            zoom 0.40
            xzoom -1.0
            xalign 0.1
            yalign 0.60

        show reaper:
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

        show reaper:
            zoom 0.35
            xalign 1.0
            yalign 0.90

        "The figure drops his scythe and rushes over to pick up the locket you dropped."

        scene evil_castle

        show hr_p:
            zoom 0.40
            xzoom -1.0
            xalign 0.1
            yalign 0.75

        show reaper:
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

        show reaper:
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

        show reaper:
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

        show reaper:
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

        show reaper:
            zoom 0.35
            xalign 1.0
            yalign 0.60

        rp "The \"Cursed Knight\" you seek."


        play sound "door_creak.mp3"

        scene evil_castle

        show hr_p:
            zoom 0.40
            xzoom -1.0
            xalign 0.1
            yalign 0.75

        show reaper:
            zoom 0.35
            xalign 1.0
            yalign 0.90

        "Reaper opens the gate for you and motions for you to pass through."

        scene evil_castle

        show hr_p:
            zoom 0.40
            xzoom -1.0
            xalign 0.1
            yalign 0.75

        show reaper:
            zoom 0.35
            xalign 1.0
            yalign 0.60

        rp "Until we meet again, hero."

        scene evil_castle
        with dissolve

        play sound "woosh.mp3" noloop

        "Suddenly, Reaper disappears into a thick black mist."

        "You decide to pass through the gate and enter the Abandoned Castle."

        jump act_two_p2 

    label not_met_arachne:
        uc "I can tell when someone is lying to me."
       
        "In an instant, the figure shoves you to the ground with his scythe. He brings his weapon back, looking to attack you as you lie helplessly on the ground."

        scene evil_castle
        with hpunch

        play sound "fall.mp3" noloop

        show hr_p:
            zoom 0.40
            xzoom -1.0
            xalign 0.1
            yalign 0.75

        show reaper:
            zoom 0.35
            xalign 1.0
            yalign 0.60

        uc "There are two things that are guaranteed in life."

        uc "Death…"

        uc "and most certainly…"

        "Mid-swing, the figure stops and seems to notice something on the ground near you. The locket given to you by Arachne."

        scene evil_castle

        show hr_p:
            zoom 0.40
            xzoom -1.0
            xalign 0.1
            yalign 0.75

        show reaper:
            zoom 0.35
            xalign 1.0
            yalign 0.90

        scene evil_castle

        show hr_p:
            zoom 0.40
            xzoom -1.0
            xalign 0.1
            yalign 0.75

        show reaper:
            zoom 0.35
            xalign 1.0
            yalign 0.60

        uc "Snuggles!"

        scene evil_castle

        show hr_p:
            zoom 0.40
            xzoom -1.0
            xalign 0.1
            yalign 0.60

        show reaper:
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

        show reaper:
            zoom 0.35
            xalign 1.0
            yalign 0.90

        "The figure drops his scythe and rushes over to pick up the locket you dropped."

        scene evil_castle

        show hr_p:
            zoom 0.40
            xzoom -1.0
            xalign 0.1
            yalign 0.75

        show reaper:
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

        show reaper:
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

        show reaper:
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

        show reaper:
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

        show reaper:
            zoom 0.35
            xalign 1.0
            yalign 0.60

        rp "The \"Cursed Knight\" you seek."


        play sound "door_creak.mp3"

        scene evil_castle

        show hr_p:
            zoom 0.40
            xzoom -1.0
            xalign 0.1
            yalign 0.75

        show reaper:
            zoom 0.35
            xalign 1.0
            yalign 0.90

        "Reaper opens the gate for you and motions for you to pass through."

        scene evil_castle

        show hr_p:
            zoom 0.40
            xzoom -1.0
            xalign 0.1
            yalign 0.75

        show reaper:
            zoom 0.35
            xalign 1.0
            yalign 0.60

        rp "Until we meet again, hero."

        scene evil_castle
        with dissolve

        play sound "woosh.mp3" noloop

        "Suddenly, Reaper disappears into a thick black mist."

        "You decide to pass through the gate and enter the Abandoned Castle."

        jump act_two_p2

label fight_reaper:
    uc "Hah! The naivety of mortals is never dull."

    "In an instant, the figure shoves you to the ground with his scythe. He brings his weapon back, looking to attack you as you lie helplessly on the ground."

    scene evil_castle
    with hpunch

    play sound "fall.mp3" noloop

    show hr_p:
        zoom 0.40
        xzoom -1.0
        xalign 0.1
        yalign 0.75

    show reaper:
        zoom 0.35
        xalign 1.0
        yalign 0.60

    uc "There are two things that are guaranteed in life."

    uc "Death…"

    uc "and most certainly…"

    "Mid-swing, the figure stops and seems to notice something on the ground near you. The locket given to you by Arachne."

    scene evil_castle

    show hr_p:
        zoom 0.40
        xzoom -1.0
        xalign 0.1
        yalign 0.75

    show reaper:
        zoom 0.35
        xalign 1.0
        yalign 0.90

    scene evil_castle

    show hr_p:
        zoom 0.40
        xzoom -1.0
        xalign 0.1
        yalign 0.75

    show reaper:
        zoom 0.35
        xalign 1.0
        yalign 0.60

    uc "Snuggles!"

    scene evil_castle

    show hr_p:
        zoom 0.40
        xzoom -1.0
        xalign 0.1
        yalign 0.60

    show reaper:
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

    show reaper:
        zoom 0.35
        xalign 1.0
        yalign 0.90

    "The figure drops his scythe and rushes over to pick up the locket you dropped."

    scene evil_castle

    show hr_p:
        zoom 0.40
        xzoom -1.0
        xalign 0.1
        yalign 0.75

    show reaper:
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

    show reaper:
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

    show reaper:
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

    show reaper:
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

    show reaper:
        zoom 0.35
        xalign 1.0
        yalign 0.60

    rp "The \"Cursed Knight\" you seek. And whatever business you have with him, I could care less."

    "Reaper turns his head towards the castle with a longing glance for a moment."

    rp "…He\'s long gone anyways. He won\'t be much of a threat to you, so no need to tread with caution."

    play sound "door_creak.mp3"

    scene evil_castle

    show hr_p:
        zoom 0.40
        xzoom -1.0
        xalign 0.1
        yalign 0.75

    show reaper:
        zoom 0.35
        xalign 1.0
        yalign 0.90

    "Reaper opens the gate for you and motions for you to pass through."

    scene evil_castle

    show hr_p:
        zoom 0.40
        xzoom -1.0
        xalign 0.1
        yalign 0.75

    show reaper:
        zoom 0.35
        xalign 1.0
        yalign 0.60

    rp "Until we meet again, hero."

    scene evil_castle
    with dissolve

    play sound "woosh.mp3" noloop

    "Suddenly, Reaper disappears into a thick black mist."

    "You decide to pass through the gate and enter the Abandoned Castle."

    jump act_two_p2