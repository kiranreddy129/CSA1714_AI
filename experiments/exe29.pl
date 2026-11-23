% Disease diagnosis rules
disease(cold) :-
    symptom(runny_nose),
    symptom(sneezing).

disease(flu) :-
    symptom(fever),
    symptom(body_pain),
    symptom(cough).

disease(malaria) :-
    symptom(fever),
    symptom(chills),
    symptom(sweating).

disease(allergy) :-
    symptom(sneezing),
    symptom(itchy_eyes).

% Main predicate
:- initialization(main).

main :-
    write('Enter symptoms one by one.'), nl,
    write('Available symptoms: fever, cough, body_pain, chills, sweating, runny_nose, sneezing, itchy_eyes'), nl,
    write('Enter symptom (or stop to finish): '),
    read(S),
    collect_symptoms(S),
    diagnose.

collect_symptoms(stop).
collect_symptoms(S) :-
    S \= stop,
    assertz(symptom(S)),
    write('Enter next symptom (or stop): '),
    read(Next),
    collect_symptoms(Next).

diagnose :-
    disease(D),
    write('Possible disease: '), write(D), nl,
    fail.
diagnose :-
    write('Diagnosis completed.'), nl.
