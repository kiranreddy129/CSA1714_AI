% Monkey and Banana Problem

% Initial state
initial(state(atdoor, onfloor, atwindow, hasnot)).

% Go
% Monkey and Banana Problem

% Initial state:
% state(MonkeyPosition, MonkeyStatus, BoxPosition, HasBanana)

initial(state(atdoor, onfloor, atwindow, no)).

% Goal state
goal(state(_, _, _, yes)).

% Move monkey towards the box
move(state(P, onfloor, B, H),
     state(B, onfloor, B, H)) :-
     P \= B.

% Push box to the middle
push(state(P, onfloor, P, H),
     state(middle, onfloor, middle, H)) :-
     P \= middle.

% Climb onto the box
climb(state(middle, onfloor, middle, H),
      state(middle, onbox, middle, H)).

% Grasp the banana
grasp(state(middle, onbox, middle, no),
      state(middle, onbox, middle, yes)).

% Solve the problem
solve(State, _) :-
    goal(State),
    write('Monkey got the banana!'), nl.

solve(State, Visited) :-
    (move(State, NewState);
     push(State, NewState);
     climb(State, NewState);
     grasp(State, NewState)),
    \+ member(NewState, Visited),
    write(NewState), nl,
    solve(NewState, [NewState|Visited]).

% Start execution
start :-
    initial(State),
    write('Initial State: '), write(State), nl,
    solve(State, [State]).
