#Adding in true and false statements
small = False
green = False

#pea statement
if small and green:
    print('pea')
    
#cherry statement
elif small and not green:
    print('cherry')
    
#watermelon statememnt
elif not small and green:
    print('watermelon')
    
#pumpkin statement
elif not small and not green:
    print('pumpkin')