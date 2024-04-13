class Acount:
    def __init__(self, name, silvers, golds, rubins, powers, personages, skins):
        self.name = name
        self.silvers = silvers
        self.golds = golds
        self.rubins = rubins
        self.powers = powers
        self.personages = personages
        self.skins = skins
    def add(self, prize):
        if type(prize) == tuple:
            if prize[0] == 'silver':
                self.silvers += prize[1]
            elif prize[0] == 'gold':
                self.golds += prize[1]
            elif prize[1] == 'rubin':
                self.rubins += prize[1]
        elif type(prize) == 'personage':
            self.personages.append(prize)
        elif type(prize) == 'skin':
            self.skins.append(prize)