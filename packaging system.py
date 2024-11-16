n=int(input("number of items\n"))

total_weight=0
pack_count=0
pack_list=[]

for i in range(n):
    item_weight=int(input("please enter weight of the item"))
    if item_weight==0:
        print("invalid input")
        break

    if item_weight>10:
        print("invalid. Please enter a number between 0 and 10")
        continue

    if item_weight+total_weight<20:
        total_weight+=item_weight
        continue

    elif item_weight+total_weight==20:
        total_weight+=item_weight
        pack_list.append(total_weight)
        pack_count+=1
        print(f"package {pack_count} with total weight of {total_weight} will be sent")
        total_weight=0
        # print(total_weight)
    elif item_weight+total_weight>20:
        if  (total_weight!=0):
            pack_count+=1
            print(f"package {pack_count} will be sent with total weight of {total_weight}")
            pack_list.append(total_weight)
            total_weight=0
            total_weight+=item_weight
            continue

if total_weight<20:
    # pack_count+=1
    # print(f"package {pack_count} with total weight of {total_weight}")
    pack_list.append(total_weight)
# print(pack_list)
print(f"the total number of packages sent is {len(pack_list)} with total weight of {sum(pack_list)}")
# This is calculated as the number of packages sent multiplied by 20 kg, minus the total weight of packages sent.
print(f"the total unused capacity is {len(pack_list)*20-(sum(pack_list))}")
# print(total_weight)



