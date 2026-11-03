bird(sparrow).
bird(parrot).
bird(penguin).
bird(ostrich).
bird(eagle).

can_fly(sparrow).
can_fly(parrot).
can_fly(eagle).

cannot_fly(penguin).
cannot_fly(ostrich).

check_fly(X) :-
    can_fly(X),
    write(X),
    write(' can fly.').

check_fly(X) :-
    cannot_fly(X),
    write(X),
    write(' cannot fly.').

check_fly(X) :-
    bird(X),
    \+ can_fly(X),
    \+ cannot_fly(X),
    write('Flying ability is unknown.').
