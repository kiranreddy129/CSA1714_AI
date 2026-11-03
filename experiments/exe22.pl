
% Towers of Hanoi Program

% Base Case
hanoi(1, Source, Destination, _) :-
    write('Move disk from '),
    write(Source),
    write(' to '),
    write(Destination),
    nl.

% Recursive Case
hanoi(N, Source, Destination, Auxiliary) :-
    N > 1,
    M is N - 1,
    hanoi(M, Source, Auxiliary, Destination),
    write('Move disk from '),
    write(Source),
    write(' to '),
    write(Destination),
    nl,
    hanoi(M, Auxiliary, Destination, Source).
