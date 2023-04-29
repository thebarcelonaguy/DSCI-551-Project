# JobTracker class
class JobTracker:
    def _init_(self):
        self.tasks = []
        self.task_trackers = []
    
    def submit_job(self, task):
        self.tasks.append(task)
        self.assign_task(task)
    
    def assign_task(self, task):
        for tracker in self.task_trackers:
            if tracker.is_available():
                tracker.assign_task(task)
                return
    
    def register_task_tracker(self, tracker):
        self.task_trackers.append(tracker)

