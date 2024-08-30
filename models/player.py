"""
This module defines the Player class used to represent player information.
"""

class Player:
    """
    A class to represent a player.

    Attributes:
    id (int): The player's ID.
    firstName (str): The player's first name.
    lastName (str): The player's last name.
    fullName (str): The player's full name.
    displayName (str): The player's display name.
    shortName (str): The player's short name.
    weight (int): The player's weight.
    displayWeight (str): The player's display weight.
    height (int): The player's height.
    displayHeight (str): The player's display height.
    age (int): The player's age.
    dateOfBirth (str): The player's date of birth.
    debutYear (int): The player's debut year.
    links (list): Links related to the player.
    birthPlace (str): The player's birth place.
    college (str): The player's college.
    slug (str): The player's slug.
    headshot (str): The player's headshot URL.
    jersey (str): The player's jersey number.
    position (str): The player's position.
    injuries (list): The player's injuries.
    linked (list): Linked information.
    team (dict): The player's current team.
    teams (list): The player's previous teams.
    statistics (dict): The player's statistics.
    notes (list): Notes about the player.
    contracts (list): The player's contracts.
    experience (int): The player's experience.
    collegeAthlete (bool): Whether the player is a college athlete.
    active (bool): Whether the player is active.
    eventLog (list): The player's event log.
    draft (dict): The player's draft information.
    status (str): The player's status.
    """

    def __init__(
        self,
        id: int,
        firstName: str,
        lastName: str,
        fullName: str,
        displayName: str,
        shortName: str,
        weight: int,
        displayWeight: str,
        height: int,
        displayHeight: str,
        age: int,
        dateOfBirth: str,
        debutYear: int,
        links: list,
        birthPlace: str,
        college: str,
        slug: str,
        headshot: str,
        jersey: str,
        position: str,
        injuries: list,
        linked: list,
        team: dict,
        teams: list,
        statistics: dict,
        notes: list,
        contracts: list,
        experience: int,
        collegeAthlete: bool,
        active: bool,
        eventLog: list,
        draft: dict,
        status: str,
    ):
        """
        Constructs all the necessary attributes for the player object.
        """
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

    def to_dict(self) -> dict:
        """
        Converts the player object to a dictionary.

        Returns:
        dict: A dictionary representation of the player object.
        """
        return self.__dict__