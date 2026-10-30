
% BACKWARD CHAINING PROGRAM

% Initial Facts
fact(has_fever).
fact(has_cough).

% Rules
rule(flu) :-
    fact(has_fever),
    fact(has_cough).

rule(needs_rest) :-
    rule(flu).

rule(consult_doctor) :-
    fact(has_fever),
    fact(has_cough).

% Backward Chaining
backward(Goal) :-
    fact(Goal),
    write('Fact Found: '),
    write(Goal),
    nl.

backward(Goal) :-
    rule(Goal),
    write('Rule Verified: '),
    write(Goal),
    nl.

% Display all initial facts
display :-
    fact(X),
    write(X),
    nl,
    fail.

display.
