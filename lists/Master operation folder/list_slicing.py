myList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# --- Full Slice ---
newList1 = myList[0:10:1]

# --- Standard Slices ---
newList2 = myList[2:6]
newList3 = myList[-8:-4]

# --- Omitted Start/End ---
newList4 = myList[:6]
newList5 = myList[6:]

# --- Out of bounds slice (Returns empty list) ---
newList6 = myList[10:20]

# --- Step Slicing ---
newList7 = myList[1:10:2]

# --- Reverse Slicing ---
newList_reverse = myList[::-1]