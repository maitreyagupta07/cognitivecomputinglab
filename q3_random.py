import random
from collections import Counter

roll_no = 1024170404
random.seed(roll_no)

nums = [random.randint(100, 900) for _ in range(100)]
print("i. Random list:", nums)

odd_count = sum(1 for n in nums if n % 2 != 0)
print("ii. Odd count:", odd_count)

even_count = sum(1 for n in nums if n % 2 == 0)
print("iii. Even count:", even_count)


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


prime_list = [n for n in nums if is_prime(n)]
print("iv. Prime count:", len(prime_list))
print("iv. Prime numbers found:", prime_list)

counts = Counter(nums)
most_common_num, most_common_freq = counts.most_common(1)[0]
print("v. Most frequent number:", most_common_num, "occurs", most_common_freq, "times")
