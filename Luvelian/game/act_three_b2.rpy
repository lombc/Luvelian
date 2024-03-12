label act_three_b2:
    scene nature
    with dissolve

    "On the way to retrieve the Relief Rune, you catch a glimpse of something."
    
    show deer_healed:
        zoom 0.25
        xalign 0.5
        yalign 0.80
    with dissolve

    "It turns out to be the deer that they saved from its demise early on."
    "You noticed that the deer is urging you in another direction."

    menu:
        "Follow the deer.":
            jump follow_deer
        "Ignore the deer.":
            jump ignore_deer

            label follow_deer:
                show hr_p:
                    zoom 0.40
                    xzoom -1.0
                    xalign 0.1
                    yalign 0.75
                with dissolve

                show deer_healed:
                    zoom 0.35
                    xalign 1.0
                    yalign 0.60
                with dissolve

                hr "Hmmm, I wonder if there’s another deer wounded."
                hr "Hunters these days sure over-hunt, what a bummer."
                hr "Go ahead! I’ll follow you!"

                play sound "gallop.mp3"

                scene nature
                with dissolve

                "After minutes of following the deer, you immediately spot a cave from a nearby distance."
                
                scene cave
                with dissolve

                "You squint and notice that there's a stone glowing located in the middle of the altar."

                show hr_p:
                    zoom 0.40
                    xalign 0.5
                    yalign 0.60
                with dissolve

                hr "Woah, what is that?"

                scene cave
                with dissolve

                "You jog to the altar but as you were about to reach it, an entity comes from behind it." 

                show hr_p:
                    zoom 0.40
                    xzoom -1.0
                    xalign 0.1
                    yalign 0.75
                with dissolve

                show dr_p:
                    zoom 0.35
                    xalign 1.0
                    yalign 0.90
                with dissolve

                "...."

                scene cave

                show hr_p:
                    zoom 0.40
                    xzoom -1.0
                    xalign 0.1
                    yalign 0.75

                show dr_p:
                    zoom 0.35
                    xalign 1.0
                    yalign 0.60

                dr "Hold on there, friend."

                scene cave

                show hr_p:
                    zoom 0.40
                    xzoom -1.0
                    xalign 0.1
                    yalign 0.75

                show dr_p:
                    zoom 0.35
                    xalign 1.0
                    yalign 0.90

                "Caught off guard, you clutch the handle of your sword."

                scene cave

                show hr_p:
                    zoom 0.40
                    xzoom -1.0
                    xalign 0.1
                    yalign 0.45

                show dr_p:
                    zoom 0.35
                    xalign 0.85
                    yalign 0.90              

                hr "Who are you?"

                scene cave

                show hr_p:
                    zoom 0.40
                    xzoom -1.0
                    xalign 0.1
                    yalign 0.75

                show dr_p:
                    zoom 0.35
                    xalign 1.0
                    yalign 0.60

                dr "Slow your roll, there is no need for bloodshed."
                dr "I am the Dryad that watches this forest."
                dr "I have taken notice of your actions earlier, when you helped one of my people."


                scene cave

                show hr_p:
                    zoom 0.40
                    xzoom -1.0
                    xalign 0.1
                    yalign 0.75

                show dr_p:
                    zoom 0.35
                    xalign 1.0
                    yalign 0.90

                "Dryad glances at the deer."

                scene cave

                show hr_p:
                    zoom 0.40
                    xzoom -1.0
                    xalign 0.1
                    yalign 0.45

                show dr_p:
                    zoom 0.35
                    xalign 0.85
                    yalign 0.90             

                hr "I'm just doing what I can."

                scene cave

                show hr_p:
                    zoom 0.40
                    xzoom -1.0
                    xalign 0.1
                    yalign 0.75

                show dr_p:
                    zoom 0.35
                    xalign 1.0
                    yalign 0.60

                dr "And for that, I am grateful."
                dr "The deer noticed you again while you were traveling, so I urged it to bring you to me."
                
                scene cave

                show hr_p:
                    zoom 0.40
                    xzoom -1.0
                    xalign 0.1
                    yalign 0.45

                show dr_p:
                    zoom 0.35
                    xalign 0.85
                    yalign 0.90             

                hr "That is true. I am in search of the Relief Rune to aid a friend."

                scene cave

                show hr_p:
                    zoom 0.40
                    xzoom -1.0
                    xalign 0.1
                    yalign 0.75

                show dr_p:
                    zoom 0.35
                    xalign 1.0
                    yalign 0.60

                dr "Is that so?"
                dr "You do know what retrieving the Relief Rune will do to the town of Cendria, right?"
            
                scene cave

                show hr_p:
                    zoom 0.40
                    xzoom -1.0
                    xalign 0.1
                    yalign 0.45

                show dr_p:
                    zoom 0.35
                    xalign 0.85
                    yalign 0.90             

                hr "You\’re right."
                hr "I am a bit conflicted about that effect, but I do want to save a friend."


                scene cave

                show hr_p:
                    zoom 0.40
                    xzoom -1.0
                    xalign 0.1
                    yalign 0.75

                show dr_p:
                    zoom 0.35
                    xalign 1.0
                    yalign 0.60

                dr "If that\’s the case."
                dr "I allow you to retrieve the Forest Rune."
                dr "With my power, I can properly maintain this forest without the aid of it."
                dr "It can be useful in thwarting the effect of the Relief Rune’s retrieval on the town of Cendria."
                dr "Please accept this as a small token of appreciation for being a friend of the forest."

                scene cave

                show hr_p:
                    zoom 0.40
                    xzoom -1.0
                    xalign 0.1
                    yalign 0.45

                show dr_p:
                    zoom 0.35
                    xalign 0.85
                    yalign 0.90             

                hr "I am in greatly appreciative of your gesture."
                hr "Surely, I can return the favor?"


                scene cave

                show hr_p:
                    zoom 0.40
                    xzoom -1.0
                    xalign 0.1
                    yalign 0.75

                show dr_p:
                    zoom 0.35
                    xalign 1.0
                    yalign 0.60

                dr "No need. Helping this deer is enough for me to be also appreciative of you."
                dr "Make sure to continue doing great deeds, further down the road."

                scene cave

                show hr_p:
                    zoom 0.40
                    xzoom -1.0
                    xalign 0.1
                    yalign 0.45

                show dr_p:
                    zoom 0.35
                    xalign 0.85
                    yalign 0.90             

                hr "Thank you."

                scene cave
                with dissolve

                "You retrieve the Forest Rune and quickly travel to the altar by the town of Cendria."

                scene altar
                with dissolve

                "You spent minutes investigating the altar to see if there are any contraptions that might hinder you from taking the Relief Rune."
                "To your surprise, there were no traps or tricks that you had to be careful about."
                "You then proceeded to take the Relief Rune."

                play sound "clink.mp3"

                "You then quickly place the Forest Rune on the slot where the Relief Rune\’s previously located."                                      

                play sound  "clink.mp3"

                show hr_p:
                    zoom 0.40
                    xalign 0.5
                    yalign 0.60
                with dissolve

                hr "Wew, that was not so hard."

                "Feeling relieved for a while, a frightening sound can be heard by the mountainside where the altar was located."

                play sound "landslide.mp3"

                "Then the sound ceased."

                stop sound fadeout 1.0

                show hr_p:
                    zoom 0.40
                    xalign 0.5
                    yalign 0.60
                with dissolve

                hr "I really thought the rune would not work."
                hr "Way to play with my emotions there for a second."

                scene altar
                with dissolve

                "You then proceed to head back."

                scene corridor
                with dissolve

                "Continuously traveling, you finally got back to the Abandoned Castle."

                show hr_p:
                    zoom 0.40
                    xalign 0.5
                    yalign 0.60
                with dissolve

                hr "Ludwig! I have come back with the Relief Rune in hand!!"

                scene corridor
                with dissolve

                "Ludwig then struggles to walk down to the Main Hall to greet you."

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

                "He then falls into your arms, fighting away at the curse that is slowly consuming him."

                scene corridor

                show hr_p:
                    zoom 0.40
                    xzoom -1.0
                    xalign 0.1
                    yalign 0.45
                with dissolve

                show ck_p:
                    zoom 0.35
                    xalign 0.85
                    yalign 0.90
                with dissolve                

                hr "Here I\’m gonna place this Relief Rune on your chest, please hold on!"

                play sound "glowing.mp3"

                "You then place the Relief Rune on Ludwig\’s chest, and the curse that was consuming him slowly fades away."

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

                lg "It sure took you long enough."                

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

                hr "I hope the wait was not too painful."

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

                lg "It\’s okay, I only had to push and pull with myself because of the damn armor."

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

                hr "You managed to hold on until I came, you\’re fine."

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

                lg "Heh, I\’ve just had enough of this damn cage. Let\’s get out of here."

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

                hr "Sure thing ;)"

                scene evil_castle
                with dissolve

                "Upon leaving the Abandoned Castle, you proceeds to head back to the Kingdom to show Ludwig around."  

                scene main_menu_bg
                with dissolve

                "Helping him integrate back into society, after a long slumber."

                "Congratulations on getting the good ending! You have successfully saved Ludwig from the curse and managed to prevent catastrophe from befalling the Town of Cendria!"              

                jump end

            label ignore_deer:
                show hr_p:
                    zoom 0.40
                    xzoom -1.0
                    xalign 0.1
                    yalign 0.65
                with dissolve

                show deer_healed:
                    zoom 0.35
                    xalign 1.0
                    yalign 0.90
                with dissolve

                hr "You look similar to the deer I saved a while ago!"
                hr "Oh wait, you ARE the deer I saved a while ago!"
                hr  "I hope you\' feeling better, friend."
                
                scene nature
                with dissolve

                hr "I must get on my way."

                jump act_three_b1

                
