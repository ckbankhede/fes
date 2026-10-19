dict={"Max":90,"Neha":80,"Arav":92,"John":82,"Alex":91}
average=0
for names in dict:
    average=average+dict[names]
average=average/len(dict)
top_scorer=""
top_score=0
for names in dict:
    if dict[names]>top_score:
        top_score=dict[names]
        top_scorer=names
print("top score:",top_score)
print("Top Scorer:",top_scorer)
user_input=input("State a student name:")
print(user_input,dict.get(user_input))