Walking=(1,0,1,1,0,1)
Good=0
Bad=0
for i in Walking:
    if(Walking[i]==0):
        Good+=1
    else:
        Bad+=1
if Good>Bad:
    print("Your doing great on your walking.")
else:
    print("You are not doing that well in walking.")