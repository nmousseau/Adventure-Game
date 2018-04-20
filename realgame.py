import random

def die():
    return random.randint(1,6)

print("Welcome to Game")
print("Type quit at any time to quit")
print("Type go to continue")
start = 'go'
replay = 'play again'
something = 'yes'
McDonalds = 'McDonalds'
Leavitt = 'Leavitt Park'
Fratellos = 'Fratellos'
Fight = 'Fight'
Punch = 'Punch'
Hit = 'Hit'
Shoot = 'Shoot'
Ejaculate = 'Ejaculate'
Garage = 'Parking Garage'
Aromas = 'Aroma Joes'
Wash = 'Car Wash'
Tressel = 'Tressel'
Belknap = 'Belknap Mill'
Library = 'Library'
Chase = 'Chase'
Track = 'Track'
Skate = 'Skate Escape'
belknap = 'Belknap Mall'
Wow = 'Wow Trail'
Orthodontist = 'Orthodontist'
Home = 'Home'
Theatre = 'Colonial Theatre'
Pine = 'Pine Street'
Eddie = 'Eddies House'
Braces = 'Braces'
Police = 'Police'
Make = 'Make'
Watch = 'Watch'
Phill = 'Phill Reed'
Walmart = 'Walmart'
Sals = 'Sals'
game = True

y = 50

while game:
    ans = input("Type \n")
    if ans == "quit":
        game = False
        
    if start in ans:
        print('Welcome Phill Reed. You have been given the task to defeat the evil Phill Reed without losing all 50 health. Type McDonalds to start your journey.')
    if replay in ans:
        print('Welcome Phill Reed. Type McDonalds to start your journey.')
        y = 50
    if McDonalds in ans:
        print('You decide to go to McDonalds. While boolin wit the homies at McDonalds, the LHS valedictorian from 2016 kicks you out for not buying anything. Pissed off, your homies decide to leave after squirting mayonnaise on his face. Are you going to Fratellos or Leavitt Park?')
    if Leavitt in ans:
        print('You decide to go with your homies to Leavitt Park. When you get there, you realize your friend has given you a slight erection and you are forced to masturbate violently. You try to contain the cum in your hand, but some gets on your friends shirt. He is super mad, and threatens to beat you up. You call for a truce, but accidentally shake his hand with yours which is filled with hot cum. After both of you swallow cum, you need to clean up. Are you going to the car wash or the tressel?')
    if Fratellos in ans:
        print('You and your homies get to Fratellos. After ordering a platter of coleslaw, a Wild Evan Fields attacks you. You are forced to fight back. Type fight')
    if Fight in ans:

        x = die()
        if x > 5:
            print("The Wild Evan Fields hasn't showered and hits you with a stink bomb! You lose 5 health.")
            y = (y - 5)
            print("Health =", y)
            print("Are you going to the Parking Garage or Aroma Joes?")
        else:
            print("You hit the Wild Evan Fields! He is disabled, and you escape. Are you going to the Parking Garage or Aroma Joes?")
            print("Health =", y)

    if Garage in ans:
        print('You decide to go to the Parking Garage. You see a lamborghini, and decide to take a piss on your friend. Your friend pushes you off the top floor of the parking garage you land in Phill Reeds hands while he caresses your cock. Type quit to quit or play again to play again')
    if Aromas in ans:
        print('You decide to order a coffee for you and your homies to share. It tastes good. One of your homies gets a call from Phill Reed saying come to the library. But, you would rather go to the Library to read books about the Wild Phill Reed. Are you gonna go to the Belknap Mill or the Library?')
    if Wash in ans:
        print('You head to the Car Wash to clean off. One of your friends gets soap in his eye and goes blind. He wanders out into the street where a passing car stops, grabs him and drives off. But that friend has autism, so do you want to go after him really or would you rather go to the Track? Chase or Track?')
    if Tressel in ans:
        print('All of you head to the Tressel to wash off. You jump in one by one, then get out and push the car into the lake to clean it off. Unfortunately, you cant retrieve it and are forced to leave on foot. But, as you try to leave a crazy Sister ODonnell jumps you. You are forced to fight back! Type Punch.')
    if Punch in ans:

        x = die()
        if x > 5:
            print("The Wild Sister O'Donnell hits you with some gang signs and breaks your arm! You lose 5 health.")
            y = (y - 5)
            print("Health =", y)
            print("Are you going to Skate Escape or the Belknap Mall?")
        else:
            print("You hit the Wild Sister O'Donnell! With your huge blow, she is sent back to California. Are you going to Skate Escape or the Belknap Mall?")
            print("Health =", y)
            
    if Belknap in ans:
        print('You all go to the party at the Belknap Mill. One of your friends snorts cocaine, but turns out it was actually dog shit. He starts dying, so you have to get him some help. But before you can, a Wild Chris pulls out an AR-15. You are forced to fight back. Type shoot to shoot')
    if Shoot in ans:
        
        x = die()
        if x > 4:
            print("The Wild Chris blows a full round into your foot. You lose 10 health.")
            y = (y - 10)
            print("Health =", y)
            print("Do you want to go to the homeless shelter on the Wow Trail or bring him to the Orthodontist?")
        else:
            print("You tricked Chris and he killed himself. Are you going to the homeless shelter on the Wow Trail or bring him to the Orthodontist?")
            print("Health =", y)
                  
    if Library in ans:
        print('You get to the Library to try and check out Phill Reeds Greatest Moments Off Camera. But, you open the book and a 9 inch dildo comes out. It shoots cum at you. Type Ejaculate to Fight.')
    if Ejaculate in ans:

        x = die()
        if x > 3:
            print("The 9 inch dildo creampies your face. You lose 15 health.")
            y = (y - 15)
            print("Health =", y)
            print("Do you want to go to the Car Wash or the Tressel to wash off?")
        else:
            print("You tricked Chris and he killed himself. Are you going to the homeless shelter on the Wow Trail or bring him to the Orthodontist?")
            print("Health =", y)
        
    if Chase in ans:
        print('You chase after your friend at 10mph. The car takes lots of turns, and stops at the high school. You watch from a distance. Out of the car steps Phill Reed. You run up to him as he is raping your blind friend. He asks if you want to join and you say yes. Type quit to quit or play again to play again')
    if Track in ans:
        print('You leave your autistic and now blind friend behind in the car. You instead go to the Track to run some laps. You get extremely tired after 27 laps. Your friends want to go home, but you would rather go to the Colonial Theatre. Are you going Home or to the Colonial Theatre?')
    if Skate in ans:
        print('You and your homies go to Skate Escape. When you get there, you realize it burned down. Out of depression and sexual longing, you all kill yourselves. Type quit to quit or play again to play again')
    if belknap in ans:
        print('You go to the Belknap Mall with your homies to pump shit up. While lactating, a Wild Sam Bastis emerges fully clad in condoms. You are forced to fight back! Type hit')
    if Hit in ans:

        x = die()
        if x > 4:
            print("The Wild Sam Bastis shoves a condom down your throat and disappears. You lose 10 health.")
            y = (y - 10)
            print("Health =", y)
            print("Your friends want to go to the coke house on Pine Street, but you would rather go to Eddies House. Are you going Pine Street or Eddies House?")
        else:
            print("You pulled out your own dick and shoved it down the Wild Sam Bastis' throat. Your friends want to go to the coke house on Pine Street, but you would rather go to Eddies House. Are you going Pine Street or Eddies House?")
            print("Health =", y)

    if Wow in ans:
        print('You bring your friend who snorted dog shit to the Wow Trail to be treated by Joey T. Joey T diagnoses him as paralysed and you leave him with Joey T. Then you kill yourself. Type quit to quit or play again to play again')
    if Orthodontist in ans:
        print('You bring your friend to the Orthodontist to get the dog shit out of his nose. You can stay and get braces or go to the Fuck 12 Station. Braces or Station?')
    if Home in ans:
        print('You and your pussy friends go home and when you get home you die in your sleep from swallowing a wild alligator. Type quit to quit or play again to play again')
    if Theatre in ans:
        print('You go to the Colonial Theatre to watch a movie with your homies. You had a cool plan to sneak in without tickets, but you get there and realize the Colonial Theatre has been closed for 20 years. You can go watch a porno or make a porno. Watch or Make?')
    if Pine in ans:
        print('You go the Pine Street to become a gangster at a coke house. You become a blood and your friend becomes a crip. All of the gang members in Laconia make you fight to the death. And you lose. Type quit to quit or play again to play again')
    if Eddie in ans:
        print('You go to Eddies House where you get eaten by Raymond. Type quit to quit or play again to play again')
    if Braces in ans:
        print('Type quit to quit or play again to play again')
    if Police in ans:
        print('You go to the Fuck 12 Station, where you scream Fuck 12 with your phone held in the air. The police mistake your phone for a gun and shoot your black friend. You are then arrested for promoting gang affiliation. In jail you are raped by Caleb Hounsell and Dirty Dirty ODonnell. Type quit to quit or play again to play again')
    if Make in ans:
        print('You and your homies Make an ass eating porno. You make millions of dollars and live at Pornhub studios in Manchester, New Hampshire. You win the game. Type quit to quit or play again to play again')
    if Watch in ans:
        print('You and your homies Watch a porno in 144p and it turns out it was gay, not straight. You and your homies have an orgy, then realize you forgot to say no homo. Type quit to quit or play again to play again')
    if something in ans:
        print('found')
        
"""
i = 0
j = 0


    while i < 5:
        print("NEW ROW")
        while j < 5:
            print("x")
            j += 1
        j = 0
        i += 1
"""
#

