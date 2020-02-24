voters_roll = [1,2,3,1,1,4,4]
voters_roll = [str(i) for i in voters_roll]

def audit(voters_roll):
    riggers = []
    for voter in voters_roll:
        if voters_roll.count(voter) > 1 and voter not in riggers:
            riggers.append(voter)

    for rigger in riggers:
        print(rigger, "appears",voters_roll.count(rigger),"times")

audit(voters_roll)
