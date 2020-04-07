# �־��� stones ���� num ���� ����� �� �ִ°��� Ȯ���ϴ� �Լ�
# k: �ִ� ���� �� �ִ� ��
# def check_possible(stones, check_num, k):
#     # 1) check_num-1 ���� �ǳ� �� ���ٸ��� ����
#     stones_remain = [max(0, stone-(check_num-1)) for stone in stones]
#     # print(stones_remain)
    
#     # 2) ���� ���ٸ����� �Ѹ��� �� �ǳʷ��� �ǳʾ� �� ĭ ����Ʈ
#     stones_remain_ind_list = [ind for ind, val in enumerate(stones_remain) if val > 0]
#     if len(stones_remain_ind_list) == 0:
#         return False
    
#     step_list = [stones_remain_ind_list[i] - stones_remain_ind_list[i-1] for i in range(1, len(stones_remain_ind_list))]
#     # print(step_list)
#     step_list.append(stones_remain_ind_list[0] + 1)
#     step_list.append(len(stones_remain_ind_list) - stones_remain_ind_list[-1])
    
#     if max(step_list) > k:
#         return False
#     return True

def check_possible(stones, check_num, k):
    now = -1
    for i in range(len(stones)):
        if (stones[i] - (check_num-1)) > 0:
            if i-now > k:
                return False
            now = i
    if (len(stones) - now) > k:
        return False
    else:
        return True
    
def solution(stones, k):
    
    if min(stones) == max(stones):
        return min(stones)
    
    # binary search
    answer = 0
    lower_limit, upper_limit = 0, max(stones)     
    while lower_limit <= upper_limit:
        # print('---')
        # print(lower_limit, upper_limit)
        check_num = (upper_limit + lower_limit) // 2
        # print(check_num)
        check_result = check_possible(stones, check_num, k)
        # print(check_result)
        if check_result == True:
            answer = check_num
            lower_limit = check_num + 1
        else:
            upper_limit = check_num - 1
    return answer