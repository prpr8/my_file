initial = {
    "A":"on table",
    "B":"on table",
    "C":"on table"
    
}

Goal = [("A","B"),
        ("B","C")]

while Goal:
    x,y = Goal.pop()
    if initial[x]==y:
        print(f"{x} is already on {y}")
        
    else:
        print(f"pickup {x} ")
        print(f"stack on {y}")
        initial[x]=y
        
print(f"final state is {initial}")