% Facts: Fruit and its colour

fruit(apple, red).
fruit(banana, yellow).
fruit(orange, orange).
fruit(grapes, green).
fruit(mango, yellow).
fruit(guava, green).
fruit(strawberry, red).

% Query to find fruits and colours

find_fruit :-
    fruit(Fruit, Colour),
    write('Fruit: '),
    write(Fruit),
    write(' Colour: '),
    write(Colour),
    nl,
    fail.

find_fruit.
