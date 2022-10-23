class EventManager:
    registeredCallback = {}

    EVENT_COLLISION = 1
    EVENT_GOAL = 2

    def registerCallback(self, callback, event):
        self.registeredCallback[event] = callback

    def dispatchEvent(self, event):
        if event in self.registeredCallback:
            self.registeredCallback[event]()