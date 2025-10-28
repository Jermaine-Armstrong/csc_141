import greetings
greetings.greet_user("Prahfit")

from greetings import greet_user
greet_user("Prahfit")

from greetings import greet_user as fn
fn("Prahfit")

import greetings as mn
mn.greet_user("Prahfit")

from greetings import *
greet_user("Prahfit")
