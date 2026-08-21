roll_no = "1024170404"
digits = [int(d) for d in roll_no]
L = [d * 10 for d in digits]

scores = tuple(L[:8])
print("scores =", scores)

highest = max(scores)
highest_index = scores.index(highest)
lowest = min(scores)
lowest_count = scores.count(lowest)
print("i. Highest score:", highest, "at index", highest_index)
print("i. Lowest score:", lowest, "occurs", lowest_count, "times")

reversed_list = list(scores[::-1])
print("ii. Reversed as list:", reversed_list)
print("ii. Tuples cannot be reversed in place because tuples are immutable, so reverse() (an in-place method) does not exist for them; a new list must be created instead.")

user_score = int(input("iii. Enter a score to search for: "))
if user_score in scores:
    print("iii. First occurrence index:", scores.index(user_score))
else:
    print("iii. Score not present in tuple.")

try:
    scores[0] = 100
except TypeError as e:
    print("iv. Error raised:", e)
    print("iv. This happens because tuples are immutable and do not support item assignment, unlike lists which are mutable and allow elements to be changed.")

first_score, second_score, *remaining_scores = scores
print("v. First score:", first_score)
print("v. Second score:", second_score)
print("v. Remaining scores:", remaining_scores)
