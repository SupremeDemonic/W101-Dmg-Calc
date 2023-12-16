import time

gear = 250  # Make sure to change gear damage!!!!

gear = gear / 100 + 1
criticial = 2
peirce = 30
resist = 45
damage = 0
total_dmg = 0

# Toggles
blade = False
aura = False
trap = False
enemy_resist = False
attack = False

# Choose Attack
print('What is the name of the spell you want to use?')
spell_name = input()
print("How much damage does it do?")
damage = int(input())

# Determining what input from the user will do
while attack == False:
    time.sleep(.5)
    usrchoice = input('What happened this round?\n      Choose a Number\n           1 [Blade]   2 [Aura]   3 [Enchantment]   4 [Trap]   5 [Enemy Resist]   6 [Attack]  7 [Custom Damage]\n').title()
    
    if usrchoice == '1':
        usrchoice = 'Blade'
    elif usrchoice == '2':
        usrchoice = 'Aura'
    elif usrchoice == '3':
        usrchoice = 'Enchantment'
    elif usrchoice == '4':
        usrchoice = 'Trap'
    elif usrchoice == '5':
        usrchoice = 'Enemy Resist'
    elif usrchoice == '6':
        usrchoice = 'Attack'
    elif usrchoice == '7':
        usrchoice = 'Custom Damage'

# The choice of the user will create different events
    if usrchoice == 'Blade':
        bladedmg = int(input('How much damage does the blade give?    ')) /100 + 1
        print('Noted!')
        blade = True
        time.sleep(.5)

    elif usrchoice == 'Aura' and aura == False:
        auradmg = int(input('How much damage does the aura give you?\n')) /100 + 1
        print('Noted!')
        aura = True
        time.sleep(.5)

    elif usrchoice == 'Aura' and aura == True:
        print('You already have an aura equipped')

    elif usrchoice == 'Enchantment':
        enchdmg = int(input('How much was the enchantment?\n'))
        total_dmg += enchdmg
        print('Noted!')
        time.sleep(.5)

    elif usrchoice == 'Trap':
        trapdmg = int(input('What is the damage for the trap?\n')) /100 + 1
        print('Noted!')
        trap = True
        time.sleep(.5)

    elif usrchoice == 'Enemy Resist':
        eresist = int(input('How much resist did the enemy put on?\n')) /100
        print('Noted!')
        enemy_resist = True
        time.sleep(.5)

    elif usrchoice == 'Attack':
        finattck = input('Did you attack?  Y or N\n').upper()
        if finattck == 'Y':
            attack = True
            break
        elif finattck == 'N':
            print('Lets add more stuff!')
    
    elif usrchoice == 'Custom Damage':
        damage = int(input('What would you like to change the damage to?\n'))
        print('Noted!')
        time.sleep(.5)        



# Calculating the base damage that will be done from Stats w/ criticals and spell enchantments
total_dmg = damage + total_dmg
total_dmg = total_dmg * gear
total_dmg = total_dmg * criticial



# Calculating Damage done by blades, auras, traps, resistance, and etc.
if blade == True and aura == True and trap == True and enemy_resist == True:           #All
    final_dmg = total_dmg * bladedmg * auradmg * trapdmg / eresist
    print(f'Your {spell_name} will do an estimated {final_dmg}')

elif blade == False and aura == False and trap == False and enemy_resist == False:     #None
    final_dmg = total_dmg
    print(f'Your {spell_name} will do an estimated {final_dmg}')

elif blade == True and aura == True and trap == True and enemy_resist == False:        #blade aura trap
    final_dmg = total_dmg * bladedmg * auradmg * trapdmg
    print(f'Your {spell_name} will do an estimated {final_dmg}')

elif blade == True and aura == True and trap == False and enemy_resist == False:       #Blade and Aura
    final_dmg = total_dmg * bladedmg * auradmg
    print(f'Your {spell_name} will do an estimated {final_dmg}')

elif blade == False and aura == True and trap == True and enemy_resist == False:       #Aura trap
    final_dmg = total_dmg * auradmg * trapdmg
    print(f'Your {spell_name} will do an estimated {final_dmg}')

elif blade == True and aura == False and trap == True and enemy_resist == False:       #Blade and trap
    final_dmg = total_dmg * bladedmg * trapdmg
    print(f'Your {spell_name} will do an estimated {final_dmg}')

elif blade == True and aura == False and trap == True and enemy_resist == True:        #Blade trap resist
    final_dmg = total_dmg * bladedmg * trapdmg / eresist
    print(f'Your {spell_name} will do an estimated {final_dmg}')

elif blade == False and aura == True and trap == True and enemy_resist == True:        #aura trap resist
    final_dmg = total_dmg * auradmg * trapdmg / eresist
    print(f'Your {spell_name} will do an estimated {final_dmg}')

elif blade == False and aura == False and trap == True and enemy_resist == True:       #trap resist
    final_dmg = total_dmg * trapdmg / eresist
    print(f'Your {spell_name} will do an estimated {final_dmg}')

elif blade == True and aura == False and trap == False and enemy_resist == True:       #blade resist
    final_dmg = total_dmg * bladedmg / eresist
    print(f'Your {spell_name} will do an estimated {final_dmg}')

elif blade == False and aura == True and trap == False and enemy_resist == True:       #aura resist
    final_dmg = total_dmg * auradmg / eresist
    print(f'Your {spell_name} will do an estimated {final_dmg}')

elif blade == False and aura == True and trap == False and enemy_resist == False:      #aura
    final_dmg = total_dmg * auradmg
    print(f'Your {spell_name} will do an estimated {final_dmg}')

elif blade == False and aura == False and trap == True and enemy_resist == False:      #trap
    final_dmg = total_dmg * trapdmg
    print(f'Your {spell_name} will do an estimated {final_dmg}')

elif blade == True and aura == False and trap == False and enemy_resist == False:      #blade
    final_dmg = total_dmg * bladedmg
    print(f'Your {spell_name} will do an estimated {final_dmg}')

elif blade == False and aura == False and trap == False and enemy_resist == True:      #resist
    final_dmg = total_dmg / eresist
    print(f'Your {spell_name} will do an estimated {final_dmg}')

else: print('Something is not working...')




# Save attacks to dictionary
with open('Wizard101 Spells History.txt', 'a') as f:
    f.write(spell_name + ', ' + str(damage) + '\n')
    f.write(f'Total Damage dealt by {spell_name} was {final_dmg}\n')