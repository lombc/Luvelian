label act_three_b3:  
    play music "wind_theme_2.mp3"

    scene nature
    with dissolve

    "{i}You spend hours of searching and continuously deliberating what you are going to do next.{/i}"
    "{i}Eventually, you spot the altar where the Relief Rune is strictly stored.{/i}"

    scene altar
    with dissolve    

    "{i}As you were gazing in awe of the Relief Rune, you can not help but feel conflicted about what will happen with either the decisions that you have to make.{/i}"
    "{i}Will you take the Relief Rune?"

    menu:
        "Take the Relief Rune":
            jump take_rune_2
        "Leave the Relief Rune":
            jump dont_take_rune

            label take_rune_2:
                "{i}You spend minutes investigating the altar to see if there are any contraptions that might hinder them from taking the Relief Rune.{/i}"
                "{i}To their surprise, there were no traps or tricks that they had to be careful about.{/i}"
                "{i}You then proceeded to take the Relief Rune and left the altar.{/i}"

                play sound "clink.mp3"
                
                "{i}After struggling from pulling the Relief Rune from its placements, you successfully took the Relief Rune.{/i}"

                show hr_p:
                    zoom 0.40
                    xalign 0.5
                    yalign 0.60
                with dissolve

                hr "{i}*Phew*{/i} Whoever built this altar sure did not care that much about the stone it kept or the devastating effects it can cause if the stone were to be dislodged from its storage."

                scene altar
                with dissolve  

                "{i}Feeling relieved for a while, a frightening sound can be heard by the mountainside where the altar was located.{/i}"

                play sound "landslide.mp3"

                scene flood
                with dissolve

                "{i}You then stare in horror as you see a huge flood flow from the mountainside and onto the Cendria ravaging the homes and taking the lives of people that inhabit it.{/i}"

                stop sound fadeout 2.0
                play sound "panic.mp3"

                scene nature
                with dissolve

                stop sound fadeout 2.0

                "{i}To escape the madness, you quickly traverse the landscape to get back to the Abandoned Castle.{/i}"

                show hr_p:
                    zoom 0.40
                    xalign 0.5
                    yalign 0.60
                with dissolve

                hr "What have I done?"

                "{i}On your way back to the Abandoned Castle, you can not help but feel immense guilt over the taking of the Relief Rune.{/i}"

                scene evil_castle
                with dissolve

                show hr_p:
                    zoom 0.40
                    xalign 0.5
                    yalign 0.60
                with dissolve                
                
                hr "I did what I have to do, it was either that flood or Ludwig taking that town and causing mayhem.{/i}"

                scene corridor
                with dissolve

                "{i}Continuously traveling, you finally made it back to the Abandoned Castle.{/i}"

                show hr_p:
                    zoom 0.40
                    xalign 0.5
                    yalign 0.60
                with dissolve

                hr "Ludwig! I have come back with the Relief Rune in hand!!"

                scene corridor
                with dissolve

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

                "{i}Ludwig quickly comes down to the Main Hall to gree you.{/i}"
                "{i}When Ludwig runs to you, he accidentally falls into your arm...{/i}"
                "{i}...which results in the Relief Rune slipping out of your hand.{/i}"
                "{i}The rune then falls on the ground and is cracked.{/i}"

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

                hr "Okay, let's place this rune on you. Surely it should work just fin-"

                scene corridor
                with hpunch

                show hr_p:
                    zoom 0.40
                    xzoom -1.0
                    xalign 0.1
                    yalign 0.75

                show ck_p:
                    zoom 0.35
                    xalign 0.85
                    yalign 0.90

                "{i}After placing the Relief Rune on Ludwig's chest, the dark aura that enveloped him slowly disappears.{/i}"
                "{i}Then suddenly...{/i}"

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

                lg "Uhhhhhh...."
                lg "AHHHHHHHHHHH!!!!!"

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

                "{i}A dark hole suddenly emanates from Ludwig's armor which swallows him whole.{/i}"

                scene corridor
                with dissolve

                show hr_p:
                    zoom 0.40
                    xzoom -1.0
                    xalign 0.1
                    yalign 0.75
                with dissolve

                "You then stare in horror at what just happened.{/i}"

                scene corridor

                show hr_p:
                    zoom 0.40
                    xzoom -1.0
                    xalign 0.1
                    yalign 0.75                                                                

                hr "What."
                hr "The."
                hr "HELL!!!!!!"
                hr "That was not supposed to happen!!"

                scene corridor
                with dissolve

                "{i}Without any explanation, you spend the next few minutes deliberating on what just happened.{/i}"

                "{i}You then proceed to head out of the castle, unable to accept how everything turned out.{/i}"

                "{i}The town of Cendria ravaged.{/i}"

                "{i}And Ludwig gone.{/i}"

                "{i}You then hear mercenaries march by looking for you.{/i}"

                jump end