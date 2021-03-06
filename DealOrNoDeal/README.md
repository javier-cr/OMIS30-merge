# README & Release Documentation
## Deal or No Deal: A recreation of the gameplay of the hit TV gameshow.
### Created by Chris, Javi, Lily, and Tanner.
usernames: cmartin, jramirez, lrodgersmasamori, tsuard
#### Introduction
Thank you for taking the time to use our code! Our code runs a digital version of the popular game show "Deal or No Deal". 

#### Gameplay
The app will begin by asking for the user to choose a case of the 26 cases presented. Then, the user will be prompted to eliminate 6 of the remaining cases and will be told the value that was inside those cases. An offer will then be presented to the user by the banker and the user can either accept the offer and thereby end the game, or say 'no deal' and the game will continue. This pattern will continue (with the user eliminating one less case each round) until either the user chooses 'deal' or there is only one case remaining. If there is only one case left, the user can either keep the money in the case that they chose or they can take the money in the final remaining case. Afer this, the game ends.

#### Development
The authors spent a lot of time working on the dictionary for the briefcaces with values and creating code that would eliminate cases as they were chosen (popping). We especially learned a lot learning to separate out each operation of the game into different functions.

#### Technical Description
This game begins by creating two lists, one of briefcase numbers (1-26), and the other of briefcase dollar values ($0.01-$1,000,000.00). We use the random library to shuffle only the dollar values of the cases, then pair these two lists together as a key:value pair within a dictionary.

We create a dictionary to keep track of cases that have been opened, and individual variables to keep track of which case the user has chosen to claim as their own, as well as the dollar value of this case.

Each function of the game is broken up into a different function:\
\
*intro()* - prints a welcome message\
*pick_user_case()* - allows the user to set aside a case to be their own, to be opened at the conclusion of the game\
*pick_cases* (with integer *cases_this_round* passed into this function - allows user to open other cases\
*show_cases()* - shows the user all of the cases they have selected so far\
*offer()* -  calculates the offer the banker will give\
*decision* - allows the user to continue ('no deal') or end ('deal') the game\
*finalCase()* - called when the user must select 1 case at a time until no cases remain\
*finalDecision() - handles the user's final choice necessary to end the game\
*keep_going()* allows us to repeat functions so that the user selects 6 cases, then 5, 4, 3, 2, 1, 1, 1, 1, then 1 case\
\
These functions are called as necessary, while the *cases_this_round* integer is decremented throughout the game to achieve the behavior described within the *keep_going()* function.

#### Known Limitations
There is one thing to be careful of in the game. If you accidentally enter an invalid number or other invalid character while eliminating briefcases, you will be asked to enter a valid input, but if you have already chosen a briefcases to eliminate in that step, thos briefcases will remain eliminated, though you will still have to enter a brand new list of cases. This may sometimes result in an error ONLY if you make it to the final case. Otherwise, this should not be a problem unless multiple invalid inputs are entered.
