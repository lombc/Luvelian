# Act One

label cursed_knight:

"You pick up the wanted poster for the Cursed Knight, reward-1000 gold coins."

"Description: A Cursed Knight has taken residence in a nearby abandoned castle and has been killing anyone who gets close."

"A bounty has been placed for his life."

"You accept the bounty and head in the direction of the abandoned castle."

# Put background of a forest here
scene forest_bg with dissolve
stop music fadeout 1.0
play music "forest_theme.mp3"

"You trek through the forest for a couple hours before hearing the sounds of a voice yelling for help."

sc "Please help! I\’m trapped in a spider web!"

"You see a woman trapped in a web struggling to break free from a large spider web between two trees."

menu:
    "Do you help the stranger break free or continue on your path?"

    "Help the stranger":
        jump help_stranger

    "Continue on your path":
        jump dont_help_stranger


label help_stranger:

    "Just as the stranger is freed from the web your vision blacks out for a moment as you're quickly wrapped into the web by the stranger."

    scene forest_bg with vpunch

    "The stranger reveals their true identity, you see a large half woman/half spider."    

    show hr_p_webbed:
        zoom 0.40
        xzoom -1.0
        xalign 0.1
        yalign 0.75
    with dissolve

    show ar_p_unimp:
        zoom 0.48
        xalign 1.0
        yalign 0.65
    with dissolve

    hr "How dare you! Release me! Do you know who I am?! I\’m the chosen hero!"

    scene forest_bg

    show hr_p_webbed:
        zoom 0.40
        xzoom -1.0
        xalign 0.1
        yalign 0.85

    show ar_p_talk:
        zoom 0.48
        xalign 1.0
        yalign 0.65

    ar "What kind of “chosen hero” gets caught in a simple trap like this?"

    ar "I\’d expect this from a common traveling merchant, but how stupid are you?"

    scene forest_bg

    show hr_p_webbed:
        zoom 0.40
        xzoom -1.0
        xalign 0.1
        yalign 0.65

    show ar_p_unimp:
        zoom 0.48
        xalign 1.0
        yalign 0.75

    hr "*Sigh* You\’re not going to free me are you?"

    scene forest_bg

    show hr_p_webbed:
        zoom 0.40
        xzoom -1.0
        xalign 0.1
        yalign 0.85

    show ar_p_talk:
        zoom 0.48
        xalign 1.0
        yalign 0.65

    ar "Nope." 

    scene forest_bg

    show hr_p_webbed:
        zoom 0.40
        xzoom -1.0
        xalign 0.1
        yalign 0.65

    show ar_p_unimp:
        zoom 0.48
        xalign 1.0
        yalign 0.75

    hr "Then what are you going to do to me? Eat me?"

    scene forest_bg

    show hr_p_webbed:
        zoom 0.40
        xzoom -1.0
        xalign 0.1
        yalign 0.85

    show ar_p_talk:
        zoom 0.48
        xalign 1.0
        yalign 0.65

    ar "I was considering it but I don\’t think you\’d be very tasty. “Heros” are kind of gamey, you know with all the good deeds and being annoying in general."

    ar "No, I think I\’ll just kill you."

    scene forest_bg

    show hr_p_webbed:
        zoom 0.40
        xzoom -1.0
        xalign 0.1
        yalign 0.65

    show ar_p_unimp:
        zoom 0.48
        xalign 1.0
        yalign 0.75

    hr "You know, if you kill me I\’m going to haunt you with my heroic soul."

    scene forest_bg

    show hr_p_webbed:
        zoom 0.40
        xzoom -1.0
        xalign 0.1
        yalign 0.85

    show ar_p_talk:
        zoom 0.48
        xalign 1.0
        yalign 0.65

    ar "What?"

    scene forest_bg

    show hr_p_webbed:
        zoom 0.40
        xzoom -1.0
        xalign 0.1
        yalign 0.65

    show ar_p_unimp:
        zoom 0.48
        xalign 1.0
        yalign 0.75

    hr "Oh? You don\’t know?"

    scene forest_bg

    show hr_p_webbed:
        zoom 0.40
        xzoom -1.0
        xalign 0.1
        yalign 0.85

    show ar_p_laugh:
        zoom 0.48
        xalign 1.0
        yalign 0.65

    ar "Know what? That you’re lying to delay your death?"

    scene forest_bg

    show hr_p_webbed:
        zoom 0.40
        xzoom -1.0
        xalign 0.1
        yalign 0.65

    show ar_p_unimp:
        zoom 0.48
        xalign 1.0
        yalign 0.75

    hr "No. If you kill me my heroic soul will haunt you for the rest of your life. I\’ll hide all your left shoes and I\’ll bore you to death with my extensive knowledge of fine poetry."

    scene forest_bg

    show hr_p_webbed:
        zoom 0.40
        xzoom -1.0
        xalign 0.1
        yalign 0.85

    show ar_p_laugh:
        zoom 0.48
        xalign 1.0
        yalign 0.65

    ar "*Bursts out in laughter*"

    ar "I can\’t believe you\’re the chosen hero. You\’re an idiot Haha."

    scene forest_bg

    show hr_p_webbed:
        zoom 0.40
        xzoom -1.0
        xalign 0.1
        yalign 0.65

    show ar_p_blush:
        zoom 0.48
        xalign 1.0
        yalign 0.75

    hr "I try."

    scene forest_bg

    show hr_p_webbed:
        zoom 0.40
        xzoom -1.0
        xalign 0.1
        yalign 0.85

    show ar_p_laugh:
        zoom 0.48
        xalign 1.0
        yalign 0.65

    ar "Well the joke is on you because for one, I don\’t wear shoes, I\’m half spider, and two, I happen to love fine poetry. Specifically the dark and depressing kind."

    ar "Why are you even this far in the woods anyways?"

    scene forest_bg

    show hr_p_webbed:
        zoom 0.40
        xzoom -1.0
        xalign 0.1
        yalign 0.65

    show ar_p_blush:
        zoom 0.48
        xalign 1.0
        yalign 0.75

    hr "There\’s a Cursed Knight killing innocent people nearby the previously abandoned castle."

    scene forest_bg

    show hr_p_webbed:
        zoom 0.40
        xzoom -1.0
        xalign 0.1
        yalign 0.85

    show ar_p_talk:
        zoom 0.48
        xalign 1.0
        yalign 0.65

    ar "Oh, that castle was never abandoned."

    scene forest_bg

    show hr_p_webbed:
        zoom 0.40
        xzoom -1.0
        xalign 0.1
        yalign 0.65

    show ar_p_unimp:
        zoom 0.48
        xalign 1.0
        yalign 0.75

    hr "What do you mean?"

    scene forest_bg

    show hr_p_webbed:
        zoom 0.40
        xzoom -1.0
        xalign 0.1
        yalign 0.85

    show ar_p_talk:
        zoom 0.48
        xalign 1.0
        yalign 0.65

    ar "What is your name hero?"

    scene forest_bg

    show hr_p_webbed:
        zoom 0.40
        xzoom -1.0
        xalign 0.1
        yalign 0.65

    show ar_p_unimp:
        zoom 0.48
        xalign 1.0
        yalign 0.75

    hr "My name is [hr]."

    scene forest_bg

    show hr_p_webbed:
        zoom 0.40
        xzoom -1.0
        xalign 0.1
        yalign 0.85

    show ar_p_talk:
        zoom 0.48
        xalign 1.0
        yalign 0.65

    ar "Well [hr], the names Arachne, and you\’ve entertained me so I\’ll help you out."

    scene forest_bg

    show hr_p_webbed:
        zoom 0.40
        xzoom -1.0
        xalign 0.1
        yalign 0.65

    show ar_p_unimp:
        zoom 0.48
        xalign 1.0
        yalign 0.75

    hr "By freeing me?"

    scene forest_bg

    show hr_p_webbed:
        zoom 0.40
        xzoom -1.0
        xalign 0.1
        yalign 0.85

    show ar_p_laugh:
        zoom 0.48
        xalign 1.0
        yalign 0.65

    ar "No."

    ar "Take this locket with you. It may prove helpful to you."

    "*Arachne places the locket in the web trap*"

    scene forest_bg

    show hr_p_webbed:
        zoom 0.40
        xzoom -1.0
        xalign 0.1
        yalign 0.65

    show ar_p_unimp:
        zoom 0.48
        xalign 1.0
        yalign 0.75

    hr "Wait, what is that for?"

    scene forest_bg

    show hr_p_webbed:
        zoom 0.40
        xzoom -1.0
        xalign 0.1
        yalign 0.85

    show ar_p_talk:
        zoom 0.48
        xalign 1.0
        yalign 0.65

    ar "Farewell [hr], the chosen hero, hopefully we\’ll see each other again and you can enlighten with this fine poetry that you claim to write."

    scene forest_bg

    show hr_p_webbed:
        zoom 0.40
        xzoom -1.0
        xalign 0.1
        yalign 0.85

    show ar_p_wink:
        zoom 0.48
        xalign 1.0
        yalign 0.65

    "*Arachne disappears into the forest*"

    scene forest_bg

    show hr_p_webbed:
        zoom 0.40
        xalign 0.5
        yalign 0.85
    with dissolve

    hr "Well shit, that was weird."

    scene forest_bg with hpunch

    show hr_p:
        zoom 0.40
        xalign 0.5
        yalign 0.60
    with dissolve

    "[hr] struggled for half an hour before finally freeing themselves from Arachne's web picking up the locket on the way out"

    scene forest_bg
    with dissolve

    "After a few hours of traveling you notice something odd on your path."

    show deer_dead:
        zoom 0.30
        xalign 0.5
        yalign 0.80
    with dissolve

    "The corpse of a dead deer comes into view. Perhaps if you got here sooner then the deer's life could be saved."

    "The gaze of the forest is upon you and seems to blow the winds of disappointment."

    scene forest_bg
    with dissolve

    "You continue on your path to the abandoned castle."

    jump act_two_b1

    scene forest_bg
    with dissolve

    label dont_help_stranger:

    "You hear the stranger begging for help as you pass by ignoring their pleas."

    "You then continue on your path."

    show deer_wounded:
        zoom 0.30
        xalign 0.5
        yalign 0.80
    with dissolve

    "After some time passes you see a wounded deer on the side of your path. The deer seems to have a wounded limb and is losing a lot of blood."

    "The deer will die if you do not give aid. "

    menu:
        "Do you take time to bandage the deer?"

        "Yes":
            jump help_deer
        "No":
            jump dead_deer

    label help_deer:

    scene forest_bg
    with dissolve

    show deer_healed:
        zoom 0.30
        xalign 0.5
        yalign 0.80
    with dissolve

    $ deer_help = 1

    "You take the time to bandage the deers wound and give it some water from your canteen."

    "The deer takes a moment to get to its feet but gives you some licks as it rushes off into the forest."

    scene forest_bg
    with dissolve

    "You continue on your journey."

    # Create jump label to act where you approach reaper > no locket > not know cursed knight's name
    jump act_two_b2

    label dead_deer:

    $ deer_help = 2

    scene forest_bg
    with dissolve

    show deer_dead:
        zoom 0.30
        xalign 0.5
        yalign 0.80
    with dissolve

    "You avoid the deer and choose to ration your own resources for the journey ahead."

    "You continue on your journey."
            
    jump act_two_b3