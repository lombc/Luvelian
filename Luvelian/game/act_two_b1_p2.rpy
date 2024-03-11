label act_two_b1_p2:

    play music "corridor.mp3"

    scene corridor
    with dissolve

    "You enter a vast ruined corridor upon opening the castle doors."

    "In the distance, you spot a man in armor on the ground, back against the corridor wall with his head down."

    show hr_p:
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

    "You slowly approach the man."

    menu:
        "Ludwig?":
            jump know_name
        "Cursed Knight?":
            jump dont_know_name

            label know_name:
                
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

                lg "Ludwig? How do you know my name?"

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

                hr "A man who called himself Reaper."

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

                lg "That decaying pile of bones? You must have shown great character to get that information from him."

                lg "But who am I to speak? My body is decaying as we speak."

                scene corridor

                show hr_p:
                    zoom 0.40
                    xzoom -1.0
                    xalign 0.1
                    yalign 0.75

                show ck_p:
                    zoom 0.35
                    xalign 0.85
                    yalign 0.90

                "As Ludwig grimaces, you inspect his damaged and veiny skin, flushed with an unnatural purple tone."

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

                lg "Ever since then, the armor has been taking over my mind and body. Forcing me to act upon truly evil deeds. Such deeds that no man should forgive. It\’s becoming more and more frequent."

                lg "I can feel myself slipping away. I fear that soon I will completely lose control of myself to its unholy madness."

                lg "...Not all hope is lost. I learned that an altar located on the mountainside nearby holds a relic that can cure my affliction. However, the pain came back, stronger than ever before, forcing me to take refuge in this very castle."

                lg "Will you help me, hero?"

                scene corridor

                show hr_p:
                    zoom 0.40
                    xzoom -1.0
                    xalign 0.1
                    yalign 0.75

                show ck_p:
                    zoom 0.35
                    xalign 0.85
                    yalign 0.90

                menu:
                    "Of course, just rest here. I will retrieve this relic for you.":
                        jump retrieve_relic
                    "I'm sorry. My duty as a hero is to put an end to your crimes.":
                        jump kill_ludwig

                        label retrieve_relic:
                            
                            "Ludwig smiles at you."

                            lg "Thank you, hero. The altar is close by, just a few miles north at the top of the mountain."

                            lg "May I ask… what is your name, hero?"

                            menu:
                                "They call me [hr], but you can call me anytime :)":
                                    jump flirt_ludwig
                                "[hr]. I should get going, before your condition gets worse.":
                                    jump not_flirt

                                    label flirt_ludwig:

                                        "Ludwig is taken aback by your comment and blushes."
                                        
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

                                        lg "I see. It is my pleasure to be acquainted with you."

                                        lg "My curse…I sense that it is nearing its completion. If you come back with the relic and I am in an uncontrollable state…do what you must [hr]."

                                        lg "And besides..."

                                        lg "If that happens, I am glad to have met such a kind and attractive hero in my final moments before I lose consciousness."

                                        "You immediately blush and don\’t know what to say."

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

                                        hr "I…I understand. I\’ll…be back with the relic as soon as possible."

                                        scene corridor
                                        with dissolve

                                        "Embarrassed, you hurriedly leave Ludwig to rest as you head off to find the relic."

                                        jump end

                                    label not_flirt:

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

                                        lg "I see. It is my pleasure to be acquainted with you."

                                        lg "My curse…I sense that it is nearing its completion. If you come back with the relic and I am in an uncontrollable state…do what you must[hr]."

                                        "You nod, understanding the implication."

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

                                        hr "I understand. I\'ll be back with the relic as soon as possible."

                                        scene corridor
                                        with dissolve

                                        "You leave Ludwig to rest as you head off to find the relic."

                                        jump end

                        label kill_ludwig:

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

                            lg "..."

                            scene corridor
                            with dissolve

                            "Ludwig longingly stares into your eyes. You sense he accepts his end."

                            "You give Ludwig a solemn nod, and swiftly plunge your sword into his chest."

                            play sound "stab.mp3" noloop
                            scene corridor
                            with dissolve
                            with vpunch

                            "Ludwig recoils, and crumples to his side as you quickly pull the sword out from his body."

                            stop sound fadeout 2.0

                            "Ludwig faintly smiles as he lays. You sense his death is freeing for him."

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

                            lg "I don\’t blame you at all, hero. You are doing what you believe is right. I can finally be at peace."

                            "Ludwig passes away."

                            "You stand above his motionless body for a moment in silence, reflecting upon your decision. It certainly did not feel right."

                            stop music fadeout 1.0
                            play music "wind_theme.mp3"

                            scene evil_castle
                            with dissolve

                            "You proceed to carry him outside to hold a proper ceremony and give him a proper burial."

                            stop music fadeout 1.0
                            play music "main_menu.mp3"

                            scene main_menu_bg
                            with dissolve

                            "You solemnly travel back to the kingdom"

                            "After collecting your bounty, you hear songs and praises about your recent achievement."

                            "Claiming the rewards associated with Ludwig’s demise did not give you any ounce of fulfillment."

                            "The End."

                            jump end