def insertion_sort(InputList):
   for i in range(1, len(InputList)):
      nxt_element = InputList[i]
      j = i - 1
      while (j >= 0) and (InputList[j] > nxt_element):
         InputList[j + 1] = InputList[j]
         j -= 1
      InputList[j + 1] = nxt_element

# List to be sorted
list = [19, 2, 31, 45, 30, 11, 121, 27]
# Perform insertion sort on the list
insertion_sort(list)
# Print the sorted list
print(list)