# create and initialize three name variables
# (name1, name2, name3)
name1 = "BossLady"
name2 = "BossMan"
name3 = "Screams"
name4 = "Doctor"
name5 = "ReeKid"
name6 = "RandomMan"
name7 = "RandomKid"
name8 = "RandomLady"
name9 = "RandomRunner"
name10 = "Player222"



# create and initialize three score variables
# (score1, score2, score3)
score1 = 1000
score2 = 995
score3 = 990
score4 = 985
score5 = 980
score6 = 975
score7 = 970
score8 = 965
score9 = 960
score10 = 400



# print a title for the high scores list
print("      High Scores")
print("----------------------")

# Line between each of the scores.
spacerline = "----------------------"

# print each of the three score lines in the pattern "name = score"
table = str.format('''{0:^12} = {11:4}
{10}
{1:^12} = {12:4}
{10}
{2:^12} = {13:4}
{10}
{3:^12} = {14:4}
{10}
{4:^12} = {15:4}
{10}
{5:^12} = {16:4}
{10}
{6:^12} = {17:4}
{10}
{7:^12} = {18:4}
{10}
{8:^12} = {19:4}
{10}
{9:^12} = {20:4}
{10}''',name1,name2,name3,name4,name5,name6,name7,name8,name9,name10,spacerline,score1,score2,score3,score4,score5,score6,score7,score8,score9,score10)
print(table)
