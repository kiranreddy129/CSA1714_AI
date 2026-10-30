
% Student-Teacher-Subject Code Database

student_teacher('Kiran', 'Ramesh', 'CS101').
student_teacher('Rahul', 'Suresh', 'CS102').
student_teacher('Arun', 'Kumar', 'CS103').
student_teacher('Priya', 'Ramesh', 'CS104').
student_teacher('Vijay', 'Suresh', 'CS105').

% Display all records
display :-
    student_teacher(Student, Teacher, SubCode),
    write('Student: '), write(Student),
    write('  Teacher: '), write(Teacher),
    write('  Subject Code: '), write(SubCode),
    nl,
    fail.

display.
