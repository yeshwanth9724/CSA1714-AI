disease(diabetes).
disease(blood_pressure).
disease(obesity).

food(diabetes, vegetables).
food(diabetes, oats).
food(diabetes, whole_grains).

food(blood_pressure, fruits).
food(blood_pressure, low_salt_food).
food(blood_pressure, vegetables).

food(obesity, salads).
food(obesity, fruits).
food(obesity, low_calorie_food).

suggest(Disease) :-
    food(Disease, Food),
    write('Suggested food: '),
    write(Food), nl,
    fail.

suggest(_).
