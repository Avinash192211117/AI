fact(color(apple, red)).
fact(color(banana, yellow)).
fact(color(grape, purple)).
fact(taste(apple, sweetfact(taste(banana, sweet)).
fact(taste(grape, sour)).

rule(eat(X), [color(X, C), taste(X, T)], [likes(X, [C, T])]).

forward_chain :-
    rule(Head, Body, Conclusion),
    loop(Body, Conclusion),
    fail.
forward_chain.

loop([], _).
loop([Fact|Body], Conclusion) :-
    fact(Fact),
    call(Conclusion),
    delete(Body, Fact, NewBody),
    loop(NewBody, Conclusion).

delete([], _, []).
delete([X|T], X, T1) :-
    delete(T, X, T1).
delete([X|T], Y, [X|T1]) :-
    delete(T, Y, T1).

query(Query) :-
    fact(Query),
    !,
    write(Query),
    write(' is '),
    write(value(Query)).
query(Query) :-
    write(Query),
    write(' is unknown.'),
    nl.

display_facts :-
    fact(Fact),
    write(Fact),
    nl,
    fail.

display_rules :-
    rule(Head, Body, Conclusion),
    write('Rule: '),
    write(Head),
    write(' :- '),
    write(Body),
    write(' => '),
    write(Conclusion),
    nl,
    fail.

display_unknown_queries :-
    query(Query),
       write(Query),
    write(' is unknown.'),
    nl,
    fail.

main :-
    write('Known Facts:'),
    nl,
    display_facts,
    write('Rules:'),
    nl,
    display_rules,
    forward_chain,
    write('Unknown Queries:'),
    nl,
    display_unknown_queries,
    write('Do you want to add a new fact? (y/n) '),
    read(Answer),
    (   Answer = y
    ->
        add_fact,
        main
    ;
        true
    ).

add_fact :-
    write('Enter the fact (e.g., color(apple, red)) '),
    read(Fact),
    \+ fact(Fact),
    assertz(Fact),
    write('Updated Known Facts:'),
    nl,
    display_facts.
main :-
    write('Known Facts:'),
    nl,
    display_facts,
    write('Rules:'),
    nl,
    display_rules,
    forward_chain,




















