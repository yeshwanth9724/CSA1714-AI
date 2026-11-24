% Medical Diagnostic System

symptom(john, fever).
symptom(john, cough).
symptom(john, headache).

symptom(raj, fever).
symptom(raj, cold).
symptom(raj, sneezing).

symptom(susan, chills).
symptom(susan, fever).
symptom(susan, body_ache).

disease(X, flu) :-
    symptom(X, fever),
    symptom(X, cough),
    symptom(X, headache).

disease(X, common_cold) :-
    symptom(X, cold),
    symptom(X, sneezing),
    symptom(X, fever).

disease(X, viral_infection) :-
    symptom(X, chills),
    symptom(X, fever),
    symptom(X, body_ache).

diagnosis(Patient, Disease) :-
    disease(Patient, Disease).
