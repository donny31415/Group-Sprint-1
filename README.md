# Group-Sprint-1
Project Group: Don, Dylan, Luke, Pietro

## Project question here ##

Goal:
- build and implement classification models that accurately predicts the outcome of a shot during a football match
- analyse areas in which PL teams under/overperform in finishing using heat maps from the “best” model

Plan:
- find a dataset for all us to use
- clean and process dataset
- split dataset into training, validation and testing
- implement your assigned model on the data, starting from a simple version then progressively adding more features
- validate each version of your model and chose the best version to compare with rest of group
- collectively test all of our models on the same testing set
- evaluate our models’ performance using proper scoring. i.e. Brier, log-loss & ROC
- choose the best model out of the 4 and create xG heat maps for each PL football team for one whole season

## References ##

### Logistic baseline model (Don’s stuff) ###
- Null,core and full logistic model: https://github.com/alexgasconn/xG-Regression-Model/ 
- Heat maps: https://soccermatics.readthedocs.io/en/latest/gallery/lesson2/plot_xGModelFit.html#plotting-shot-location
- Implementing model walk-through: https://www.sportmonks.com/blogs/modeling-expected-goals-xg-from-match-event-data/
