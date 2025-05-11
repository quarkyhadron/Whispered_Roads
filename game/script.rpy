# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

# The game starts here.

label start:
    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    # These display lines of dialogue.
    """
    {i}The room creaks when I shift my weight —{w=0.6} a slow,{w=0.5} drawn out
    groan from the floorboards beneath me, like the house itself is reluctant
    to let me go.{/i}
    """

    """
    {i}Dust rises from the cracks with every step, catching the golden light
    and hanging there,{w=0.7} suspended like tiny memories.{/i}
    """

    char_reid "The floor's louder than I remember.{w} Probably always was."
    char_reid "...Should've swept in there before packing. Or,{w=0.5} I don't
    know...{w=0.7} ever."

    char_reid "{i}I press a hand to the floor to steady myself —{w=0.5} another
    low creak answers me.{/i}"

    char_reid "Guess I'm leaving it just as messy as I lived it."

    """
    {i}The room smells like fabric softener clinging to old flannel,{w=0.5}
    books closed too long,{w=0.5} and the faint scent of earth from a dying
    potted plant on the windowsill.{/i}
    """
    
    """
    {i}The walls are papered in personality —{w=0.5} a faded corkboard with
    movie tickets,{w=0.5} a scuffed dresser draped in mismatched socks, and a
    cracked mug half-full of old pencils.{/i}
    """

    """
    {i}From down the hallway,{w=0.5} I hear the fridge hum, my dad cough once,
    and the soft patter of my mom pacing.{/i}
    """

    """
    {i}Somewhere deeper in the house, I hear my little brother’s
    voice—{w=0.5}probably arguing with his game console again.{/i}
    """

    """
    Test modification
    """
    # This ends the game.
    return
