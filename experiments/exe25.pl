
% Diet Suggestion Based on Disease

% Disease facts
disease(diabetes).
disease(high_bp).
disease(obesity).
disease(anemia).

% Diet facts
diet(diabetes, low_sugar_high_fibre).
diet(high_bp, low_salt_balanced).
diet(obesity, balanced_food).
diet(anemia, iron_rich_food).

% Diet descriptions
description(low_sugar_high_fibre, 'Low sugar and high fibre foods').
description(low_salt_balanced, 'Low salt and balanced foods').
description(balanced_food, 'Fruits and vegetables with balanced meals').
description(iron_rich_food, 'Iron-rich foods such as spinach and beans').

% Suggestion rule
suggest_diet(Disease, Diet) :-
    disease(Disease),
    diet(Disease, Code),
    description(Code, Diet).

% Unknown disease rule
suggest_diet(Disease, 'Disease not found') :-
    \+ disease(Disease).
