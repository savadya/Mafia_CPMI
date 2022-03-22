class Players:
    def __init__(self, id, role):
        self.id = id
        self.role = role

    def role_replacement(self, role):
        self.role = role

    def get_role(self):
        return self.role
