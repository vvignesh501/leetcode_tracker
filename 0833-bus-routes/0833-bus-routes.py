class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:

        if source == target:
            return 0

        buses_and_routes = defaultdict(list)
        for bus, stops in enumerate(routes):
            for stop in stops:
                buses_and_routes[stop].append(bus)
        
        # BFS setup
        visited_buses = set()
        visited_stops = set([source])
        q = deque()
        
        # Start with all buses that can be boarded from source
        for bus in buses_and_routes[source]:
            q.append((bus, 1))  # (bus index, buses taken so far)
            visited_buses.add(bus)
        
        # BFS
        while q:
            bus, buses_taken = q.popleft()
            
            # Check all stops this bus goes through
            for stop in routes[bus]:
                if stop == target:
                    return buses_taken
                
                # For each stop, try to board new buses
                for next_bus in buses_and_routes[stop]:
                    if next_bus not in visited_buses:
                        visited_buses.add(next_bus)
                        q.append((next_bus, buses_taken + 1))
        
        return -1


# Time: O(M)
# Space: O(M + N) where \U0001d440 = ∑len(route) = total stops across all routes,
# \U0001d441=number of buses