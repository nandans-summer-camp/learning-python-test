#
# 1)
# Create a function called "dictionary_maker"
# that has one parameter: a list of 2-tuples.
# It should return the same data in the form
# of a dictionary, where the first element
# of every tuple is the key and the second
# element is the value.
#
# For example, if given: [('foo', 1), ('bar', 3)]
# it should return {'foo': 1, 'bar': 3}
#
# NOTE: Don't use any built-in functions!



############################################
############################################
#
# You are given data from a website that
# has people's CVs. The data comes
# as a list of dictionaries and each
# dictionary looks like this:
#
# { 'user': 'foo', 'jobs': ['bar', 'baz', 'qux']}
#
# we will refer to this as a "CV".
#
############################################
############################################



#
# 2)
# Create a function called "has_experience_as"
# that has two parameters:
# 1. A list of CV's.
# 2. A string (job_title)
#
# The function should return a list of strings
# representing the usernames of every user that
# has worked as job_title.



#
# 3)
# Create a function called "job_counts"
# that has one parameter: list of CV's
# and returns a dictionary where the
# keys are the job titles and the values
# are the number of users that have done
# that job.



#
# 4)
# Create a function, called "most_popular_job"
# that has one parameter: a list of CV's, and
# returns a tuple (str, int) that represents
# the title of the most popular job and the number
# of times it was held by people on the site.
#
# HINT: You should probably use your "job_counts"
# function!
#
# HINT: You can use the method '.items' on
# dictionaries to iterate over them like a
# list of tuples.



############################################
############################################
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
############################################
############################################


#
# 5)
# Create a class called "User"
#
# The class should be instantiated
# with one attribute: "name"
# which is a string.
#
#
#
# 6)
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
# 7)
# Modify the "add_score" method
# so that it throws an error if the
# "score" it is given is not an integer
# or is negative.
#
#
#
# 8)
# Create a "top_score" method
# that has one parameter: "level"
# and returns the user's top score
# for that level.
#
# If the user has no score for that
# level, the method should return None


#
# 9)
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
# 10)
# Now modify the function "top_player"
# so that it returns None if given a level
# that no player has played


#
# 11)
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
