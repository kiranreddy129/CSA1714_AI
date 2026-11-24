
% Initial fact

studies(ravi).

% Rules

gains_knowledge(X) :-
    studies(X).

passes_examination(X) :-
    gains_knowledge(X).

% Forward chaining query

forward_chaining(X) :-
    studies(X),
    gains_knowledge(X),
    passes_examination(X).
