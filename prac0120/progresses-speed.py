def solution(progresses, speeds):
    answer = []

    list_of_days = []
    for i, progress in enumerate(progresses):
        amount = 100-progress
        if amount % speeds[i] != 0:
            days = amount // speeds[i] + 1
        else:
            days = amount / speeds[i]
        list_of_days.append(days)

    list_of_idx = []
    max_now = 0.0

    for i, days in enumerate(list_of_days):
        if max_now < days:
            list_of_idx.append(i)
            max_now = days

    answer = []
    for i, idx in enumerate(list_of_idx):
        if i != len(list_of_idx)-1:
            answer.append(list_of_idx[i+1]-idx)
        else:
            answer.append(len(progresses)-idx)


    print(answer)


progresses1 = [93, 30, 55]
progresses2 = [95, 90, 99, 99, 80, 99]

speeds1 = [1, 30, 5]
speeds2 = [1, 1, 1, 1, 1, 1]

# [2, 1]
solution(progresses1, speeds1)
solution(progresses2, speeds2)




