from Skill_Factory import SkillFactory

factory = SkillFactory()

skill1 = factory.create("dmg", "Fireball", 10)

print(f'This is a {skill1.getType()} skill, name is {skill1.getName()} with {skill1.getPower()} power')