# Can't-stop
This code produces a simple table which can improve your decision making in Can't Stop game (https://boardgamearena.com/).

We get a median of number of rolls before fail for every 3-line combination. So as a result, we should know how many times roll dices and which 3-line combinations are the best. But there is much more nuances to consider later.

Next step should involve calculating expected value of rolls especially around the median number threshold to examine if next roll is EV+ and we should continue or EV- and we should stop. In reality, this is a complicated matter in which lane position, game state, and opponents' tendencies (looseness or tightness) must be taken into account.

I am not even sure if I need that. Right now I use these median values as a rule of thumb and correct them using my knowledge and experience.

//The code is quite old, not very optimal, and with almost no docstrings, but I don't see any point in polishing it right know ;)
