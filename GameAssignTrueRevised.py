#Ken gains 3 skill points per level. He wants to master 5 different skills. 
#Each skill takes 5 skill points to master, and he is at level 3 already.
#Ken only wants to learn skills that will do at least 1000 damage after putting 5 skill points into them.
#Here are the skills. Thrust, DashAttack, Thrash, OverheadSwing & Behead
#All of this is accounting for Ken being level 10.
def menu():
    print("[1]Ken is still too weak")
    print("[2]Ken is of average strength")
    print("[3]Ken is very powerful")
    print("[0]System error")
Ken_level = int(input("Enter your level: "))
while Ken_level < 15 and Ken_level > 0:
    print("Ken is still too weak")
if Ken_level < 25:
    print("Ken is average")
elif Ken_level >= 25:
    print("Ken is very powerful")
else:                                                       
    print("System error")

Behead_masterylevel = 5
OverheadSwing_masterylevel = 5
Thrash_masterylevel = 5
Thrust_masterylevel = 5
DashAttack_masterylevel = 5
Ken_skillpoints = Ken_level*3
Thrust_damage = Ken_level*35 + Thrust_masterylevel*100
DashAttack_damage = Ken_level*40 + DashAttack_masterylevel*90
Thrash_damage = Ken_level*45 + Thrash_masterylevel*80
OverheadSwing_damage = Ken_level*50 + OverheadSwing_masterylevel*100
Behead_damage = Ken_level*40 + Behead_masterylevel*85
#Find the damage of all skills
print("Ken has accumulated this many skill points" ,Ken_skillpoints)
#Ken has 30 skill points, enough to learn every skill. 
#Ken only wants the skills that do over 1000 damage at skill level 5. Determine the skills that do.
print("The damage of Thrash is" ,Thrash_damage)
print("The damage of Thrust is" ,Thrust_damage)
print("The damage of Dash Attack is"  ,DashAttack_damage)
print("The damage of Behead is" ,Behead_damage)
print("The damage of Overhead Swing is" ,OverheadSwing_damage)
#Only OverheadSwing did enough damage. 
#For all skills to do enough damage, lets find out what level Ken has to be by adjusting variables.
if Behead_damage >= 1000 and OverheadSwing_damage >= 1000 and DashAttack_damage >= 1000 and Thrust_damage >= 1000 and Thrash_damage >= 1000:
    print("This is the level where Ken can do good damage with any skill")
else:
    print("Ken is too weak, he has a lot of growing to do.")
#Ken can do good damage at level 15
#What skill does the most damage at level 25? Ken will get new sets of skills at level 30
#Because of this, Ken has decided to invest only in the 3 skills that do the highest damage.
#Find out what those skills are.