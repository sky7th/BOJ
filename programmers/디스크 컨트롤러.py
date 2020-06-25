import heapq


def solution(jobs):
    answer = 0
    last_time, now_time = -1, 0
    waiting_tasks = []
    count = 0
    while count < len(jobs):
        for index, job in enumerate(jobs):
            request_time, running_time = job
            if last_time < request_time <= now_time:
                heapq.heappush(waiting_tasks, (running_time, index))

        if not waiting_tasks:
            now_time += 1
            continue

        _, task_index = heapq.heappop(waiting_tasks)
        task_request_time, task_running_time = jobs[task_index]
        task_total_time = now_time + task_running_time - task_request_time
        answer += task_total_time

        last_time = now_time
        now_time += task_running_time
        count += 1

    return answer // len(jobs)