
% Planets Database

planet(mercury, 57900000).
planet(venus, 108200000).
planet(earth, 149600000).
planet(mars, 227900000).
planet(jupiter, 778600000).
planet(saturn, 1433500000).
planet(uranus, 2872500000).
planet(neptune, 4495100000).

% Display all planets
display :-
    planet(Name, Distance),
    write('Planet: '), write(Name),
    write('  Distance from Sun: '),
    write(Distance),
    write(' km'),
    nl,
    fail.

display.
