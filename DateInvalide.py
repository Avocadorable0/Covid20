class DateInvalide(Exception):
    def __init__(self, date1, date2):
        self.date1 = date1
        self.date2 = date2
        self.message = "Erreur sur la date"
        super().__init__(self.message)

    def __str__(self):
        return self.message
