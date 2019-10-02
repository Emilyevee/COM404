looking = input ("where should i look")
if looking == "in the bedroom":
    print ("where in the bedroom should i look?")
    bedroom = input()
    if bedroom == "under the bed":
        print ("found some shoes but no battery")

if looking == "in the bathrom":
    print ("where in the bathroom should i look")
    bathroom = input()
    if bathroom == "in the bathtub":
        print ("found a rubber duck but no battery")
    else:
        print ("it is wet but i found no battery.")

if looking == "in the lab":
    print ("where in the lab should i look")
    lab = input ()
    if lab == "on the table":
        print ("yes i found my battery")
    else:
        print ("found some tools but no battery")

