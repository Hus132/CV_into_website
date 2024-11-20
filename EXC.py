num_of_items=int(input("please enter the number of items to be shipped\n"))
total_weight=0
pack_count=0
item_count=0
package_list=[]
for i in range(num_of_items):
    item_weight=int(input("please enter the weight of the item"))
    if item_weight==0:
        print("invalid weight")
        break

    if item_weight>10:
        print(("invalid weight given. Please enter a weight between 1 and 10."))
        continue
    else:
        if item_weight + total_weight<20:
            package_list.append(item_weight)
        elif item_weight + total_weight>=20:
            total_weight+=item_weight

            pack_count+=1
            package_list.append(item_weight)
            print(f"{pack_count} package will be sent with weight of {total_weight}")

if (total_weight<20):
    print(f"package with {total_weight} is sent")

print(package_list)














    # if item_weight>20:
    #     pack_num+=1
    #     item_count+=1
    #     print(f"package with weight {item_weight} and {item_count} items will be sent")
    #     break
    #
    # if item_weight+total_weight<20:
    #     total_weight+=item_weight
    #
    # if item_weight+total_weight>20:
    #     pack_num+=1
    #     total_weight+=item_weight
    #     print(f"package with weight {total_weight} will be sent")







