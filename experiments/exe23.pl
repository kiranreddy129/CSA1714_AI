
% Bird Flying Program

% Birds that can fly
can_fly(parrot).
can_fly(eagle).
can_fly(pigeon).
can_fly(sparrow).
can_fly(crow).

% Birds that cannot fly
cannot_fly(ostrich).
cannot_fly(penguin).
cannot_fly(kiwi).

% Rule to check whether a bird can fly
check_bird(Bird) :-
    can_fly(Bird),
    write(Bird),
    write(' can fly.'), nl.

check_bird(Bird) :-
    cannot_fly(Bird),
    write(Bird),
    write(' cannot fly.'), nl.

% Unknown bird
check_bird(Bird) :-
    \+ can_fly(Bird),
    \+ cannot_fly(Bird),
    write('Information about '),
    write(Bird),
    write(' is not available.'), nl.
