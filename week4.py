from collections import deque
class Attraction:
    def _init_(self, name):
        self.name = name
        self.queue = deque()

    def add_guest(self, guest):
        self.queue.append(guest)
        print(f"{guest} joined the queue for {self.name}")

    def serve_guest(self):
        if not self.queue:
            print(f"No guests in the queue for {self.name}")
            return
        guest = self.queue.popleft()
        print(f"{guest} is now being served at {self.name}")

class ThemePark:
    def _init_(self):
        self.attractions = {}

    def add_attraction(self, name):
        attraction = Attraction(name)
        self.attractions[name] = attraction

    def reserve_ticket(self, guest, attraction_name):
        if attraction_name not in self.attractions:
            print(f"Attraction '{attraction_name}' not found")
            return
        self.attractions[attraction_name].add_guest(guest)

    def serve_guest_at_attraction(self, attraction_name):
        if attraction_name not in self.attractions:
            print(f"Attraction '{attraction_name}' not found")
            return
        self.attractions[attraction_name].serve_guest()

# Example usage
theme_park = ThemePark()
theme_park.add_attraction("Roller Coaster")
theme_park.add_attraction("Ferris Wheel")

theme_park.reserve_ticket("Alice", "Roller Coaster")
theme_park.reserve_ticket("Bob", "Roller Coaster")
theme_park.reserve_ticket("Carol", "Ferris Wheel")

theme_park.serve_guest_at_attraction("Roller Coaster")
theme_park.serve_guest_at_attraction("Roller Coaster")
theme_park.serve_guest_at_attraction("Ferris Wheel")
