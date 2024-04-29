'''
1. Implement a Lecture class that describes a presentation. When instantiated, the class must take three arguments
in the following order:

topic - topic of speech
start_time — start time of the performance as a string in HH:MM format
duration — duration of the speech as a string in HH:MM format
2. Also implement the Conference class, which describes a conference lasting one day. The conference is a set of
sequential presentations. When instantiated, the class must not accept any arguments.

The Conference class must have four instance methods:

add() is a method that takes a speech as an argument and adds it to the conference. If a performance overlaps in time
with other performances, a ValueError exception must be raised with the text:
It is not possible to hold a performance at this time.
total() - method that returns the total duration of all speeches in the conference as a string in the format HH:MM
longest_lecture() - a method that returns the duration of the longest lecture in the conference as a string in the
format HH:MM
longest_break() - a method that returns the duration of the longest break between speeches in a conference as a string
in the format HH:MM
'''

from datetime import datetime, timedelta


class Lecture:
    def __init__(self, topic: str, start_time: str, duration: str) -> None:
        self.topic = topic
        self.start_time = datetime.strptime(start_time, "%H:%M")
        self.duration = datetime.strptime(duration, "%H:%M")
        self.end_time = self.start_time + timedelta(hours=self.duration.hour, minutes=self.duration.minute)


class Conference:
    def __init__(self) -> None:
        self.lectures = []

    def add(self, other: Lecture) -> None:
        for lecture in self.lectures:
            if lecture.start_time <= other.start_time < lecture.end_time or other.start_time <= lecture.start_time < other.end_time:
                raise ValueError("It is not possible to hold a performance at this time")
        self.lectures.append(other)

    def total(self) -> str:
        return self.timedelta_format(
            sum((lecture.end_time - lecture.start_time for lecture in self.lectures), start=timedelta()))

    def longest_lecture(self) -> str:
        return self.timedelta_format(max(lecture.end_time - lecture.start_time for lecture in self.lectures))

    def longest_break(self) -> str:
        self.lectures.sort(key=lambda lecture: lecture.start_time)
        return self.timedelta_format(
            max(self.lectures[i + 1].start_time - self.lectures[i].end_time for i in range(len(self.lectures) - 1)))

    @staticmethod
    def timedelta_format(delta: timedelta) -> str:
        return (datetime(1, 1, 1) + delta).strftime("%H:%M")

# Example
conference = Conference()

conference.add(Lecture('Prime Numbers', '08:00', '01:30'))
conference.add(Lecture('Life after ChatGPT', '10:00', '02:00'))
conference.add(Lecture('Ant Colony Algorithm', '13:30', '01:50'))
print(conference.total())
print(conference.longest_lecture())
print(conference.longest_break())

# Output
# 05:20
# 02:00
# 01:30