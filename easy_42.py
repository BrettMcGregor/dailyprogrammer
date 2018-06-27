# Write a program that prints out the lyrics for
# "Ninety-nine bottles of beer", "Old McDonald had
# a farm" or "12 days of Christmas".
#
# If you choose "Ninety-nine bottles of beer", you
# need to spell out the number, not just write the
# digits down. It's "Ninety-nine bottles of beer on
# the wall", not "99 bottles of beer"!
#
# For Old McDonald, you need to include at least 6
# animals: a cow, a chicken, a turkey, a kangaroo,
# a T-Rex and an animal of your choosing (Old McDonald
# has a weird farm). The cow goes "moo", the chicken
# goes "cluck", the turkey goes "gobble", the kangaroo
# goes "g'day mate" and the T-Rex goes "GAAAAARGH".
# You can have more animals if you like.
#
# Make your code shorter than the song it prints out!

animals = [('cow', 'moo'), ('horse', 'neigh'), ('kangaroo', "g'day"), ('dog', 'woof'), ('cat', 'meow'), ('hen', 'cluck')]
ei = "E-i-e-i-o!"
om = "Old McDonald"
verse_a = f"{om} had a farm,\n{ei}\nAnd on that farm he had a..."

for animal in animals:
    double = f"{animal[1]}-{animal[1]}"
    print(verse_a, animal[0]+"!")
    print(ei)
    print(f"With a {double} here and a {double} there,")
    print(f"Here a {animal[1]}, there a {animal[1]}, everywhere a {double},")
    print(f"{om} had a farm,")
    print(f"{ei}\n")
