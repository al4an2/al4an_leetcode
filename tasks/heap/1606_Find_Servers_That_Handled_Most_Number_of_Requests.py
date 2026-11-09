import heapq


class Solution:
    def busiestServers(self, k: int, arrival: list[int], load: list[int]) -> list[int]:
        free_services = [i for i in range(k)]
        responce_count = [0] * k

        heapq.heapify(free_services)

        busy_services = []

        for idx, start in enumerate(arrival):
            while busy_services and busy_services[0][0] <= start:
                service = heapq.heappop(busy_services)

                server_id = service[1]

                target = idx % k
                if server_id < target:
                    heapq.heappush(free_services, server_id + k)
                else:
                    heapq.heappush(free_services, server_id) 

            if not free_services:
                continue

            while free_services and free_services[0] < idx:
                old_server = heapq.heappop(free_services)
                heapq.heappush(free_services, old_server + k)

            server = heapq.heappop(free_services)
            responce_count[server % k] += 1

            busy_time = start + load[idx]
            heapq.heappush(busy_services, (busy_time, server))
        
        max_request = max(responce_count)

        return [idx for idx in range(k) if responce_count[idx] == max_request]