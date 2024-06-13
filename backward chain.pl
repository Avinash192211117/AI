fact(color(apple, red)).
fact(color(banana, yellow)).
fact(color(grape, purple)).
fact(taste(apple, sweet)).
fact(taste(banana, sweet)).
fact(taste(grape, sour)).

rule(likes(X, [C, T]), [color(X, C), taste(X, T)]).

backward_chain(Query) :-
    fact(Query),
    !.
backward_chain(Query) :-
    rule(Query, Body),
    loop(Body),
    write(Query),
    write(' is '),
    write(value(Query)).

loop([]).
loop([Condition|Body]) :-
    fact(Condition),
    loop(Body),
    !.
loop([Condition|Body]) :-
    backward_chain(Condition),
    loop(Body),
    !.

main :-
    write('Enter the query (e.g., likes(apple)) '),
    read(Query),
    backward_chain(Query).
display_facts :-
    fact(Fact),
    write(Fact),
    nl,
    fail.
display_rules :-
    rule(Head, Body),
    write('Rule: '),
    write(Head),
    write(' :- '),
    write(Body),
    nl,
    fail.

main :-
    write('Known Facts:'),
    nl,
    display_facts,
    write('Rules:'),
    nl,
    display_rules,
    write('Enter the query (e.g., likes(apple)) '),
    read(Query),
    backward_chain(Query).












