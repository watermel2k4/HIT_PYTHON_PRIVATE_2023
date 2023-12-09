class Job():
    def __init__(self,id,name,branch,salary):
        self.id = id
        self.name = name
        self.branch = branch
        self.salary = salary
        self.skills = []
    def evaluate(self):
        average_score = self.evaluate_average()
        if average_score > 9.0:
            return "Rất phù hợp"
        elif average_score > 7.0:
            return "Phù hợp"
        elif average_score > 5.0:
            return "Tạm được"
        elif average_score > 3.0:
            lacking_skills = [skill for skill, score in self.get_skills().items() if score < 4.0]
            return f"Cần bổ sung kiến thức: {', '.join(lacking_skills)}"
        else:
            return "Cần học lại kiến thức base"
    def __str__(self):
        return f'ID: {self.id} - Name: {self.name} - Branch: {self.branch} - Salary: {self.salary}'
    def get_skills(self):
        return {}
class AI(Job):
    def __init__(self, id, name, branch, salary, Pythonskill, MLskill, DeepSkill, MathSkill):
        Job.__init__(self,id, name, branch, salary)
        self.Pythonskill = Pythonskill
        self.MLskill = MLskill
        self.DeepSkill = DeepSkill
        self.MathSkill = MathSkill
    def evaluate_average(self):
        return (self.Pythonskill + self.MLskill +  self.DeepSkill +  self.MathSkill) / 4
    def __str__(self) -> str:
        return Job.__str__(self) + f' - Evaluate: {self.evaluate()}'
    def get_skills(self):
        return {
            'Python Skill': self.Pythonskill,
            'ML Skill': self.MLskill,
            'Deep Skill': self.DeepSkill,
            'Math Skill': self.MathSkill
        }
class Backend(Job):
    def __init__(self, id, name, branch, salary, SQLskill, OOPskill, Apiskill, Javaskill):
        Job.__init__(self,id, name, branch, salary)
        self.SQLskill = SQLskill
        self.OOPskill = OOPskill
        self.Apiskill = Apiskill
        self.Javaskill = Javaskill
    def evaluate_average(self):
        return (self.SQLskill + self.OOPskill +  self.Apiskill +  self.Javaskill) / 4
    def __str__(self) -> str:
        return Job.__str__(self) + f' - Evaluate: {self.evaluate()}'
    def get_skills(self):
        return {
            'SQL Skill': self.SQLskill,
            'OOP Skill': self.OOPskill,
            'Api Skill': self.Apiskill,
            'Java Skill': self.Javaskill
        }
class Frontend(Job):
    def __init__(self, id, name, branch, salary, Htmlskill, Cssskill, Nodejsskill, UX, UI):
        Job.__init__(self,id, name, branch, salary)
        self.Htmlskill = Htmlskill
        self.Cssskill = Cssskill
        self.Nodejsskill = Nodejsskill
        self.UX = UX
        self.UI = UI
    def evaluate_average(self):
        return (self.Htmlskill + self.Cssskill + self.Nodejsskill + self.UX + self.UI) / 5
    def __str__(self) -> str:
        return Job.__str__(self) + f' - Evaluate: {self.evaluate()}'
    def get_skills(self):
        return {
            'Html Skill': self.Htmlskill,
            'Css Skill': self.Cssskill,
            'Nodejs Skill': self.Nodejsskill,
            'UX': self.UX,
            'UI': self.UI
        }
class Fullstack(Backend, Frontend):
    def __init__(self, id, name, branch, salary, SQLskill, OOPskill, Apiskill, Javaskill, Htmlskill, Cssskill, Nodejsskill, UX, UI):
        Backend.__init__(self, id, name, branch, salary, SQLskill, OOPskill, Apiskill, Javaskill)
        Frontend.__init__(self, id, name, branch, salary, Htmlskill, Cssskill, Nodejsskill, UX, UI)

    def evaluate_average(self):
        # You can choose how to calculate the average based on both Backend and Frontend skills
        # For example, you might want to calculate the average of all skills combined.
        backend_average = Backend.evaluate_average(self)
        frontend_average = Frontend.evaluate_average(self)
        return (backend_average + frontend_average) / 2
    def __str__(self) -> str:
        return Job.__str__(self) + f' - Evaluate: {self.evaluate()}'
    def get_skills(self):
        backend_skills = Backend.get_skills(self)
        frontend_skills = Frontend.get_skills(self)
        return {**backend_skills, **frontend_skills}
ai = AI(Pythonskill=5, MLskill=2, DeepSkill=5, MathSkill=1, id=1, name='Data Scientist', branch='AI', salary=30000000)
be = Backend(SQLskill=10, OOPskill=8, Apiskill=7, Javaskill=9, id=2, name='Backend Developer', branch='IT', salary=25000000)
ft = Frontend(Htmlskill=3, Cssskill=8, Nodejsskill=7, UX=8, UI=9, id=3, name='Frontend Developer', branch='IT', salary=20000000)
fs = Fullstack(
    id=4, name='Fullstack Developer', branch='IT', salary=30000000,
    SQLskill=10, OOPskill=8, Apiskill=7, Javaskill=9,
    Htmlskill=7, Cssskill=8, Nodejsskill=7, UX=8, UI=9
)
print(ai)
print(be)
print(ft)
print(fs)



