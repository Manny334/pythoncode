# THe parameter weekday is true if it is a weekday, and the parameter vacation is true if we are on
# vacation. We sleep in if it not a weekday, or vacation. Return true if we sleep in
def sleep_in(weekday, vacation):
    if not weekday or vacation:
        return True
    else:
        return False

