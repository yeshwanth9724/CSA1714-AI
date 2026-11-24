% Minimum marks required in each subject
eligible(Math, Physics, CS) :-
    Math >= 50,
    Physics >= 50,
    CS >= 50.
not_eligible(Math, Physics, CS) :-
    \+ eligible(Math, Physics, CS).
% Queries
% ?- eligible(80, 75, 85).
% ?- eligible(40, 35, 45).
