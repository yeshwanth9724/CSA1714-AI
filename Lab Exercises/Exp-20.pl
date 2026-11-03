:- dynamic known/1.

known(sunny).
known(warm).

rule(go_outside) :-
    known(sunny),
    known(warm).

rule(play_cricket) :-
    known(go_outside).

rule(enjoy_day) :-
    known(play_cricket).

derive(X) :-
    known(X), !.

derive(X) :-
    rule(X),
    assertz(known(X)).

forward :-
    derive(go_outside),
    derive(play_cricket),
    derive(enjoy_day).
