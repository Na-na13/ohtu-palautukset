from matchers import And, HasAtLeast, PlaysIn, All, Not, HasFewerThan, Or

class QueryBuilder:
    def __init__(self, matcher=All()):
        self._matcher = matcher

    def build(self):
        return And(self._matcher)

    def playsIn(self, team):
        #return QueryBuilder(PlaysIn(team))
        self._matcher = And(self._matcher, PlaysIn(team))
        return self

    def hasAtLeast(self, value, attr):
        #return QueryBuilder(HasAtLeast(value,attr))
        self._matcher = And(self._matcher, HasAtLeast(value, attr))
        return self

    def hasFewerThan(self, value, attr):
        #return QueryBuilder(HasFewerThan(value, attr))
        self._matcher = And(self._matcher, HasFewerThan(value, attr))
        return self
