def shortest_step(goal_num: int) -> int:
    # write your code here
    step_counter = 0

    def divide(value):
        counter = 0
        print(value, value % 2)
        while value % 2 == 0:
            value = value / 2
            counter += 1
        return counter

    def plus(value):
        counter = 0
        print(value, value % 2)
        while value % 2 != 0:
            value -= 1
            counter += 1

            print(">>", value, value % 2)
        return counter

    while goal_num > 1:
        step_counter += divide(goal_num)
        step_counter += plus(goal_num)



    return step_counter


print(shortest_step(1000))
