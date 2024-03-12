label act_two_b2_p2:
    if know == 1:
        jump dont_know_name
    else:
        jump know_name

    label dont_know_name:

        play music "corridor.mp3"

        scene corridor
        with dissolve

        "{i}You enter a vast ruined corridor upon opening the castle doors.{/i}"
        "{i}In the distance, you spot a man in armor on the ground, back against the corridor wall with his head down.{/i}"

        show hr_p_fight:
            zoom 0.40
            xzoom -1.0
            xalign 0.1
            yalign 0.75
        with dissolve

        show ck_p:
            zoom 0.35
            xalign 0.85
            yalign 0.90
        with dissolve

        "{i}He appears to be in pain, and his armor is emitting a mysterious purple aura.{/i}"
        "{i}You slowly approach the man.{/i}"

        menu:
            "You call out to him."
            
            "Cursed Knight?":
                jump know_ck

                label know_ck:

                    scene corridor

                    show hr_p:
                        zoom 0.40
                        xzoom -1.0
                        xalign 0.1
                        yalign 0.75

                    show ck_p:
                        zoom 0.35
                        xalign 0.85
                        yalign 0.60

                    ck "Cursed Knight?"
                    ck "...A fitting name I suppose. My body is decaying as we speak."
                    lg "The name is Ludwig. Would rather you not call me the former, despite its verity."
                    "{i}As Ludwig grimaces, you inspect his damaged and veiny skin, flushed with an unnatural purple tone.{/i}"
                    lg "This affliction will be my demise…"

                    scene corridor

                    show hr_p:
                        zoom 0.40
                        xzoom -1.0
                        xalign 0.1
                        yalign 0.45

                    show ck_p:
                        zoom 0.35
                        xalign 0.85
                        yalign 0.90

                    hr "What is affecting you?"

                    scene corridor

                    show hr_p:
                        zoom 0.40
                        xzoom -1.0
                        xalign 0.1
                        yalign 0.75

                    show ck_p:
                        zoom 0.35
                        xalign 0.85
                        yalign 0.60

                    lg "A curse was cast upon me when I put on this set of armor. Spoils of war taken from one of my enemies during a quest. I\’m sure a hero such as yourself would understand."
                    lg "Ever since then, the armor has been taking over my mind and body. Forcing me to act upon truly evil deeds. Such deeds that no man should forgive. It’s becoming more and more frequent."
                    lg "I can feel myself slipping away. I fear that soon I will completely lose control of myself to its unholy madness.” "
                    lg "...Not all hope is lost. I learned that an altar located on the mountainside nearby holds a relic that can cure my affliction. However, the pain came back, stronger than ever before, forcing me to take refuge in this very castle."
                    lg "Will you help me, hero?"
                    
                    menu:
                        "Of course, just rest here. I will retrieve this relic for you.":
                            jump retrieve_relic
                        "I'm sorry. My duty as a hero is to put an end to your crimes.":
                            jump kill_ludwig