
% Animal facts

mammal(dog).
mammal(cat).
mammal(cow).
mammal(elephant).

bird(parrot).
bird(eagle).
bird(penguin).

reptile(snake).
reptile(crocodile).
reptile(lizard).

aquatic_animal(shark).
aquatic_animal(whale).
aquatic_animal(dolphin).
aquatic_animal(fish).

% Classification rules

classify(X, mammal) :-
    mammal(X).

classify(X, bird) :-
    bird(X).

classify(X, reptile) :-
    reptile(X).

classify(X, aquatic_animal) :-
    aquatic_animal(X).

% Display classification

show_classification(X) :-
    classify(X, Category),
    write(X),
    write(' belongs to '),
    write(Category).
