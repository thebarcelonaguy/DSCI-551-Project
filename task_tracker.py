# TaskTracker class
class TaskTracker:
    def _init_(self):
        self.tasks = []
        self.is_busy = False
    
    def is_available(self):
        return not self.is_busy
    
    def assign_task(self, task):
        self.tasks.append(task)
        self.is_busy = True
        self.execute_task(task)
    
    def execute_task(self, task):
        self.tasks.remove(task)
        self.is_busy = False