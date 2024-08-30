class Player:
    def __init__(self, id, firstName, lastName, fullName, displayName, shortName, weight, displayWeight, height, displayHeight, age, dateOfBirth, debutYear, links, birthPlace, college, slug, headshot, jersey, position, injuries, linked, team, teams, statistics, notes, contracts, experience, collegeAthlete, active, eventLog, draft, status):
        self.id = id
        self.firstName = firstName
        self.lastName = lastName
        self.fullName = fullName
        self.displayName = displayName
        self.shortName = shortName
        self.weight = weight
        self.displayWeight = displayWeight
        self.height = height
        self.displayHeight = displayHeight
        self.age = age
        self.dateOfBirth = dateOfBirth
        self.debutYear = debutYear
        self.links = links
        self.birthPlace = birthPlace
        self.college = college
        self.slug = slug
        self.headshot = headshot
        self.jersey = jersey
        self.position = position
        self.injuries = injuries
        self.linked = linked
        self.team = team
        self.teams = teams
        self.statistics = statistics
        self.notes = notes
        self.contracts = contracts
        self.experience = experience
        self.collegeAthlete = collegeAthlete
        self.active = active
        self.eventLog = eventLog
        self.draft = draft
        self.status = status
    def to_dict(self):
        return self.__dict__