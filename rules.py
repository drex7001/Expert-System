from experta import *

class WellnessRules(KnowledgeEngine):
    @Rule(AND(Fact(age=P(lambda x: x > 25)),
              Fact(bmi=P(lambda x: x < 25))))
    def nutrition_advice_good(self):
        self.declare(Fact(nutrition_advice="good"))

    @Rule(AND(Fact(age=P(lambda x: x >= 18 and x <= 65)),
              Fact(bmi=P(lambda x: x >= 18.5 and x <= 30))))
    def nutrition_advice_average(self):
        self.declare(Fact(nutrition_advice="average"))

    @Rule(AND(Fact(age=P(lambda x: x < 18)),
              Fact(bmi=P(lambda x: x > 30))))
    def nutrition_advice_poor(self):
        self.declare(Fact(nutrition_advice="poor"))

    @Rule(Fact(stress_level=P(lambda x: x < 4)))
    def exercise_advice_good(self):
        self.declare(Fact(exercise_advice="good"))

    @Rule(Fact(stress_level=P(lambda x: x >= 4 and x <= 7)))
    def exercise_advice_average(self):
        self.declare(Fact(exercise_advice="average"))

    @Rule(Fact(stress_level=P(lambda x: x > 7)))
    def exercise_advice_poor(self):
        self.declare(Fact(exercise_advice="poor"))

    @Rule(AND(Fact(stress_level=P(lambda x: x > 7)),
              Fact(focus_level=P(lambda x: x > 7))))
    def mental_wellness_advice_good(self):
        self.declare(Fact(mental_wellness_advice="good"))

    @Rule(AND(Fact(stress_level=P(lambda x: x >= 4 and x <= 7)),
              Fact(focus_level=P(lambda x: x >= 4 and x <= 7))))
    def mental_wellness_advice_average(self):
        self.declare(Fact(mental_wellness_advice="average"))

    @Rule(AND(Fact(stress_level=P(lambda x: x < 4)),
              Fact(focus_level=P(lambda x: x < 4))))
    def mental_wellness_advice_poor(self):
        self.declare(Fact(mental_wellness_advice="poor"))