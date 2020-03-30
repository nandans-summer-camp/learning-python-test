##########################
# Scoreboard
#
# In this part we will pretend
# we have an imaginary arcade
# game and we need to keep track
# of users and their scores on
# each level.
#
# You will create:
# 1. A class "User" with some methods.
# 2. Some separate functions that
#    use the User class.
#
##########################


#
# 1)
# Create a class called "User"
#
# The class should be instantiated
# with one attribute: "name"
# which is a string.
#
#
#
# 2)
# Add methods "add_score" and
# "get_scores" to the User class.
#
# "add_score" should store the user's
# score for a given level. The choice
# of how to store it is up to you,
# but each user can have multiple
# scores for each level.
#
# "add_score" should have parameters:
# 1. level (str)
# 2. score (int)
# and should return nothing.
#
# "get_scores" should have one parameter:
# 1. level (str)
# and should return a list of integers
# representing the scores the user
# has achieved for that level
#
#
#
# 3)
# Modify the "add_score" method
# so that it throws an error if the
# "score" it is given is not an integer
# or is negative.
#
#
#
# 4)
# Create a "top_score" method
# that has one parameter: "level"
# and returns the user's top score
# for that level.
#
# If the user has no score for that
# level, the method should return None


#
# 5)
# Now create a separate function
# called "top_player" that has two
# parameters:
# 1. a list of User objects
# 2. a level (str)
#
# And returns a tuple with the following
# form: (str, int) where the values
# represent: (player_name, score)


#
# 6)
# Now modify the function "top_player"
# so that it returns None if given a level
# that no player has played


#
# 7)
# Create a separate function
# called "best_scores".
#
# This function should have one
# parameter: a list of User objects
# and should return a list of tuples
# of the following form:
# (str, str, int)
# where the values represent:
# (level, player_name, score)
#
# The list should be sorted with
# the top score coming first
# and should be truncated to the
# top 3 scores.
#
# HINT: use the builtin "sorted"
# function to sort a list and
# look how to use key-functions:
# https://docs.python.org/3/howto/sorting.html
