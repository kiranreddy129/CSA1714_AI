
% Best First Search Algorithm

% Graph connections
edge(a,b).
edge(a,c).
edge(b,d).
edge(b,e).
edge(c,f).
edge(c,g).

% Heuristic values
h(a,6).
h(b,4).
h(c,5).
h(d,3).
h(e,2).
h(f,1).
h(g,0).

% Main predicate
bestfirst(Start,Goal) :-
    search([Start],Goal,[]).

% Goal checking
search([Goal|_],Goal,_) :-
    write('Goal Found: '),
    write(Goal), nl.

% Search process
search([Current|Rest],Goal,Visited) :-
    findall(Node,
        (edge(Current,Node),
         \+ member(Node,Visited),
         \+ member(Node,[Current|Rest])),
        Children),
    append(Rest,Children,OpenList),
    sort_nodes(OpenList,Sorted),
    search(Sorted,Goal,[Current|Visited]).

% Empty list condition
search([],_,_) :-
    write('Goal Not Found'), nl,
    fail.

% Sort according to heuristic values
sort_nodes(List,Sorted) :-
    findall(H-Node,
        (member(Node,List),h(Node,H)),
        Pairs),
    keysort(Pairs,SortedPairs),
    extract_nodes(SortedPairs,Sorted).

% Extract nodes
extract_nodes([],[]).
extract_nodes([_-Node|T],[Node|R]) :-
    extract_nodes(T,R).
