from matchers import And, HasAtLeast, PlaysIn, All, Not, HasFewerThan, Or

class QueryBuilder:
    def __init__(self):
        self._matcher = All()

    def build(self):
        return_query = self._matcher
        self._matcher = All()
        return return_query

    def playsIn(self, team):
        self._matcher = And(self._matcher, PlaysIn(team))
        return self

    def hasAtLeast(self, value, attr):
        self._matcher = And(self._matcher, HasAtLeast(value, attr))
        return self

    def hasFewerThan(self, value, attr):
        self._matcher = And(self._matcher, HasFewerThan(value, attr))
        return self

    def oneOf(self, *matchers):
        self._matcher = Or(*matchers)
        return self
