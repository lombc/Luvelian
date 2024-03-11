label act_two_b3:

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
        "I\’m looking for the Cursed Knight who resides here.":
            jump avoid_reaper_b3
        "None of yours if you value your life.":
            jump kill_reaper

            label avoid_reaper_b3:

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

                uc "The Cursed Knight? I presume you are here for the bounty placed upon his head. If that is so, you truly do not value your life, traveler."
                uc "I too have “business” with a wanted individual."
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
                "You are reminded of the deer you left alone to die. You feel guilty. You begin to be lost in thought."

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

                "You come back to your senses and notice the figure waiting for a response from you."

                menu:
                    ".........Uhhh, I'm sorry but what did you say?":
                        jump ignore_reaper
                    ".....":
                        jump ignore_reaper

                        label ignore_reaper:
                            "The figure glares at you angrily."

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
                            
                            uc "I do not like being ignored."
                            uc "And in fact..."

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

                            "{i}In an instant, the figure shoves you to the ground with his scythe{/i}."

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

                            uc "You came from that forest that that wench reside in."
                            uc "YOU must side with that wench then?"
                            
                            scene evil_castle with hpunch

                            show hr_p:
                                zoom 0.40
                                xzoom -1.0
                                xalign 0.1
                                yalign 0.75

                            show reaper:
                                zoom 0.35
                                xalign 1.0
                                yalign 0.60 

                            uc "Death comes for us all, hero."

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

                            "He brings his weapon back, looking to attack you as you lie helplessly on the ground."

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

                            uc "Let me allow you to meet him early."

                            scene evil_castle with vpunch

                            show hr_p:
                                zoom 0.40
                                xzoom -1.0
                                xalign 0.1
                                yalign 0.75

                            show reaper:
                                zoom 0.35
                                xalign 1.0
                                yalign 0.90

                            "Acting fast, you kick the figure\’s leg as he starts to swing, causing him to lose balance"

                            scene evil_castle with hpunch

                            show hr_p:
                                zoom 0.40
                                xzoom -1.0
                                xalign 0.1
                                yalign 0.75

                            show reaper:
                                zoom 0.35
                                xalign 1.0
                                yalign 0.90
                            
                            "In an instant, you unleash a swift uppercut to the figure\’s jaw, sending him spiraling to the ground."

                            scene evil_castle with vpunch

                            show hr_p:
                                zoom 0.40
                                xzoom -1.0
                                xalign 0.1
                                yalign 0.75

                            show reaper:
                                zoom 0.35
                                xalign 1.0
                                yalign 0.60

                            uc "Bah! I don\’t have time for this!"

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

                            "The figure slam his fist into the ground and reaches his hand out to you."

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

                            uc "My scythe. Give it back."

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

                            hr "Or what?"

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

                            "The figure glares at you menacingly."

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

                            uc "I\’ll give you some insight on the man you seek in there for starters."

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

                            "Tilting your head, you contemplate his offer for a moment. Can you really trust this individual?"
                            "You ultimately decide to give him back his scythe. He clearly is no match for you anyhow. You give him your hand as you help him up and give him back his scythe."

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

                            rp "Much appreciated. They call me Reaper. I respect the hustle, but next time not so hard, yeah? My bones don\’t heal well at my age."

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

                            "The figure dusts himself off and straightens his cloak."

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

                            rp "At this point, I don\'t care what you do with that Cursed Knight."

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

                            "Reaper turns his head towards the castle with a longing glance for a moment."

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

                            rp "…He\’s long gone anyways. He won\’t be much of a threat to you, so no need to tread with caution."

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

                            hr "Is that all?"

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

                            rp "What, you want a backstory or something?"
                            rp "Besides..."

                            play sound "bones.mp3"

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

                            "Reaper tilts his head side to side, omitting several sounds of bones cracking."

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

                            rp "You disrespect me and almost break my jaw, mind you. Now then…"

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

                            "Reaper opens the gate for you and steps aside."
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
                                yalign 0.60

                            rp "I have my own matters to attend to. That wench I spoke of earlier took something of great importance from me."
                            rp "Until we meet again, hero."

                            scene evil_castle
                            with dissolve

                            play sound "woosh.mp3" noloop

                            "Suddenly, Reaper disappears into a thick black mist."
                            "You decide to pass through the gate and enter the Abandoned Castle."

                            jump act_two_b1_p2

