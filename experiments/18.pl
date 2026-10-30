
% Database of Name and Date of Birth

person('Kiran', '15-08-2005').
person('Rahul', '10-03-2004').
person('Arun', '22-06-2005').
person('Priya', '12-12-2004').
person('Suresh', '05-01-2003').

% Query to display all records
display :-
    person(Name, DOB),
    write('Name: '), write(Name),
    write('  DOB: '), write(DOB),
    nl,
    fail.

display.
