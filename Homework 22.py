import array as arr
print("====SCHOOL SNACK COUNTER====")
snack_box={"chocolate","chips","candy","gum"}
snack_box_2={"Orange","chocolate","gum"}
print("The snack box includes:",snack_box)
print("The snack box 2 includes:",snack_box_2)
snack_box.add("apple")
print("Updated snack box:",snack_box)
shared_snacks=snack_box.intersection(snack_box_2)
print("Both snack boxes include:",shared_snacks)
snack_array=arr.array(["i","3","9","2","3"])
no_of_3s_in_array=snack_array.count(3)
print("No. of 3s in snack array",no_of_3s_in_array)
snack_array.reverse()
print("Reversed snack array:",snack_array)