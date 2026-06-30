# --- Basic Repetition ---
base_list = [1, 2, 3]
result1 = base_list * 3
result2 = 3 * base_list

# Note: Adding an integer to a list causes a TypeError
# error_list = [1, 2, 3]
# number = 4
# result_error = error_list + number

# --- Repetition by 0 and Negative Numbers ---
list_zeros = [4, 5, 6]
res_zero = list_zeros * 0
res_neg = list_zeros * -1

# --- Repetition by 1 ---
list_one = [1, 2, 3, 4, 5]
res_one = list_one * 1

# Note: Multiplying two lists causes a TypeError
# list_err1 = [1, 2, 3]
# list_err2 = [4, 5, 6]
# res_err = list_err1 * list_err2