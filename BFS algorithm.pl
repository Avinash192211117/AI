edge(a, b, 10).
edge(a, c, 1).
edge(b, d, 5).
edge(c, d, 2).
edge(c, e, 7).
edge(d, e, 6).

heuristic(a, 0).
heuristic(b, 3).
heuristic(c, 4).
heuristic(d, 2).
heuristic(e, 0).

best_first_search(Start, Goal, Path) :-
    frontier([[Start, [Start], 0]]),
    explored([]),
    loop.

loop :-
    frontier([[Node, Path, Cost]|_]),
    (   Node = Goal
    ->
        Path
    ;

        findall([Neighbor, [Node|Path], Cost1+Cost],
                (   edge(Node, Neighbor, Cost1),
                    \+ member(Neighbor, Path),
                    Neighbor \= Node
                ),
                Neighbors),
        sort(Neighbors, SortedNeighbors),
        append(SortedNeighbors, FrontierRest),
        frontier(FrontierRest),
        \+ member(Node, Explored),
        explored([Node|Explored]),
        loop
    ).

frontier([]).
frontier([[_, Path, _]|T]) :-
    frontier(T).

member(X, [X|_]).
member(X, [_|T]) :-
    member(X, T).

sort([], []).
sort([X], [X]).
sort([X,Y|T], [X|Sorted]) :-
    X =< Y,
    sort([Y|T], Sorted).
sort([X,Y|T], [Y|Sorted]) :-
    X > Y,
    sort([X|T], Sorted).













































