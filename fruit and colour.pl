fruit_color(apple, red).
fruit_color(apple, green).
fruit_color(apple, yellow).
fruit_color(banana, yellow).
fruit_color(orange, orange).
fruit_color(lemon, yellow).

query_fruit_color(Fruit, Color) :-
    fruit_color(Fruit, Color).
