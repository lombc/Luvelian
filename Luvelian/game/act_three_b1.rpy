label act_three_b1:
    
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
            jump take_rune
        "Leave the Relief Rune":
            jump dont_take_rune

            label take_rune:
                "{i}You spend minutes investigating the altar to see if there are any contraptions that might hinder them from taking the Relief Rune.{/i}"
                "{i}To their surprise, there were no traps or tricks that they had to be careful about.{/i}"
                "{i}You then proceeded to take the Relief Rune and left the altar.{/i}"

                play sound "clink.mp3"
                
                "{/i}After struggling from pulling the Relief Rune from its placements, you successfully took the Relief Rune.{/i}"

                show hr_p:
                    zoom 0.40
                    xalign 0.5
                    yalign 0.60
                with dissolve

                hr "{i}*Phew*{/i} Whoever built this altar sure did not care that much about the stone it kept or the devastating effects it can cause if the stone were to be dislodged from its storage."

                scene altar
                with dissolve  

                "{/i}Feeling relieved for a while, a frightening sound can be heard by the mountainside where the altar was located.{/i}"

                play sound "landslide.mp3"

                scene flood
                with dissolve

                "{/i}You then stare in horror as you see a huge flood flow from the mountainside and onto the Cendria ravaging the homes and taking the lives of people that inhabit it.{/i}"

                stop sound fadeout 2.0
                play sound "panic.mp3"

                scene nature
                with dissolve

                stop sound fadeout 2.0

                "{/i}To escape the madness, you quickly traverse the landscape to get back to the Abandoned Castle.{/i}"

                show hr_p:
                    zoom 0.40
                    xalign 0.5
                    yalign 0.60
                with dissolve

                hr "What have I done?"

                "{/i}On your way back to the Abandoned Castle, you can not help but feel immense guilt over the taking of the Relief Rune.{/i}"

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

                "{i}Ludwig then struggles to walk down to the Main Hall to greet you.{/i}"

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

                "{i}He then falls into your arms, fighting away at the curse that is slowly consuming him.{/i}"

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

                "{i}You then place the Relief Rune on Ludwig\’s chest, and the curse that was consuming him slowly fades away.{/i}"

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

                show hr_p_flat:
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

                show hr_p_kawaii:
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

                "{i}Upon leaving the Abandoned Castle, *you hear a slight cry from a distance or was it just their imagination?{/i}"                

                jump end

            label dont_take_rune:

                scene altar
                with dissolve   

                "{i}You spend minutes investigating the altar to see if there are any contraptions that might hinder them from taking the Relief Rune.{/i}"
                "{i}To their surprise, there were no traps or tricks that they had to be careful about.{/i}"
                "{i}After catching a glance of the town of Cendria, you ponder and decide to not take the rune.{/i}"
            
                show hr_p:
                    zoom 0.40
                    xalign 0.5
                    yalign 0.60
                with dissolve    

                hr "I can not do it. I can not."
                hr "Risking the lives of Cendria\’s people should not be the after-effect of me saving Ludwig."
                hr "I might be able to find some other way to save him."

                scene altar
                with dissolve

                "{i}After gazing much more at the Relief Rune, *Insert name here* travels back to the Abandoned Castle.{/i}"

                scene evil_castle
                with dissolve

                "{i}When they reach the castle, they immediately run up to where Ludwig was resting.{/i}"

                scene corridor
                with dissolve

                show hr_p:
                    zoom 0.40
                    xzoom -1.0
                    xalign 0.1
                    yalign 0.75

                show ck_p:
                    zoom 0.35
                    xalign 0.85
                    yalign 0.90

                "{i}Ludwig then struggles to walk down to the Main Hall to greet you.{/i}"

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

                hr "Ludwig, I apologize but I have not been able to take the Relief Rune."
                hr "There must be some other way that we can relieve you off of that cursed armor."

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

                lg "I wish I knew any other way. This armor’s curse is slowly getting more and more harder to contain."
                lg "I would not be able to control what happens next when the curse completely consumes me."

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

                hr "I\’m really sorry, if there was enough time."
                hr "I could figure out a way to save you!"

                scene corridor

                show hr_p_fight:
                    zoom 0.40
                    xzoom -1.0
                    xalign 0.1
                    yalign 0.75

                show ck_p:
                    zoom 0.35
                    xalign 0.85
                    yalign 0.90

                "{i}After a few seconds, the cursed armor slowly consumes Ludwig and the dark aura that enveloped him became more prominent.{/i}"
                "{i}They then get into it.{/i}"
                
                scene corridor with hpunch
                play sound "swords.mp3"

                "{i}Few minutes into the heated battle, you keep slashing away but Ludwig\’s armor just keeps on toughening up with the expense of it further corrupting Ludwig.{/i}"

                scene corridor with vpunch
                play sound "swords.mp3"

                scene corridor
                with dissolve

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

                hr "Is there really no other way?!"

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

                lg "AGGGGGGGHHHHHHH!!!!!"

                scene corridor
                with dissolve

                "{i}You continue exchanging slashes with Ludwig, until you find an opening and stab him.{/i}"

                play sound "stab.mp3"

                scene corridor
                with dissolve

                show hr_p:
                    zoom 0.40
                    xzoom -1.0
                    xalign 0.1
                    yalign 0.65
                with dissolve

                show ck_p:
                    zoom 0.35
                    xalign 0.85
                    yalign 0.90
                with dissolve

                "{i}Ludwig drops into your arms, slowly dying.{/i}"

                play sound "fall.mp3"

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

                "{i}Why did it have to come to this?!{/i}"

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

                lg "We both know there were no other options."
                lg "You did the best you could."
                lg "I thank you for trying."

                scene corridor
                with dissolve

                "{i}Ludwig passes away in your arms.{/i}"

                hr "WHY??!!!!!"

                show hr_p:
                    zoom 0.40
                    xalign 0.5
                    yalign 0.60
                with dissolve

                "{i}You caress Ludwig, then proceed to carry him outside to hold a proper ceremony and give him a proper burial.{/i}"

                scene corridor
                with dissolve

                play music "main_menu.mp3"

                scene main_menu_bg
                with dissolve

                "{i}You solemnly travel back to the kingdom.{/i}"

                "{i}After collecting your bounty, you hear songs and praises about your recent achievement.{/i}"

                "{i}Claiming the rewards associated with Ludwig’s demise did not give you any ounce of fulfillment.{/i}"

                "{i}The End."

                jump end    






