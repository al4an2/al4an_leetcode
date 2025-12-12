class Solution:
    def countMentions(self, numberOfUsers: int, events: list[list[str]]) -> list[int]:
        counter = [0] * numberOfUsers
        user_status = [0] * numberOfUsers
        events.sort(key= lambda x: (int(x[1]), x[0]== "MESSAGE"))
        for event in events:
            current_time = int(event[1])
            if event[0] == "MESSAGE":
                if event[2] == "ALL":
                    for user in range(numberOfUsers):
                        counter[user] += 1
                elif event[2] == "HERE":
                    for idx, time in enumerate(user_status):
                        if time <= current_time:
                            counter[idx] += 1
                else:
                    for user_id in event[2].split(" "):
                        counter[int(user_id[2:])] += 1
            
            else:
                user_status[int(event[2])] = current_time + 60
            
        return counter