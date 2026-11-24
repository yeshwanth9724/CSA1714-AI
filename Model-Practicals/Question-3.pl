% Book facts
book(python, yes).
book(java, no).
book(ai, yes).
book(prolog, yes).
% Author facts
author(python, guido).
author(java, james).
author(ai, russell).
author(prolog, cloc).
% Availability rule
available(Book) :-
    book(Book, yes).
not_available(Book) :-
    book(Book, no).

% Queries
% ?- author(python, X).
% ?- available(java).
