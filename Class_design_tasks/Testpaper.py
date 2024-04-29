'''
In this task, you need to implement the Testpaper class, which will allow you to create exam tests. Each test must be
created based on a topic, a pattern of correct answers and a minimum percentage of correct solutions:

testpaper1 = Testpaper('Maths', ['1A', '2C', '3D', '4A', '5A'], '60%')
testpaper2 = Testpaper('Chemistry', ['1C', '2C', '3D', '4A'], '75%')
testpaper3 = Testpaper('Computing', ['1D', '2C', '3C', '4B', '5D', '6C', '7A'], '75%')
The created tests must be taken by a student - an instance of the Student class. It should have a take_test() method
that takes a test and the student's answers to that test as arguments:

student1 = Student()
student2 = Student()

student1.take_test(testpaper1, ['1A', '2D', '3D', '4A', '5A'])
student2.take_test(testpaper2, ['1C', '2D', '3A', '4C'])
student2.take_test(testpaper3, ['1A', '2C', '3A', '4C', '5D', '6C', '7B'])
Test results should be available in the form of a dictionary, the key in which is the topic of the test, and the value
is the test result (passed or failed) and the percentage of correct solutions:

print(student1.tests_taken) # {'Maths': 'Passed! (80%)'}
print(student2.tests_taken) # {'Chemistry': 'Failed! (25%)', 'Computing': 'Failed! (43%)'}
If the student has not yet taken any tests, the tests_taken attribute should contain the line No tests taken:

student3 = Student()

print(student3.tests_taken) # No tests taken
'''

class Testpaper:
    def __init__(self, topic, answers, passing_grade):
        self.topic = topic
        self.answers = answers
        self.passing_grade = passing_grade

class Student:
    def __init__(self):
        self.tests = {}
        self.tests_taken = "No tests taken"

    def take_test(self, testpaper, student_answers):
        correct_answers = sum([1 for ans in student_answers if ans in testpaper.answers])
        total_questions = len(testpaper.answers)
        percentage = (correct_answers / total_questions) * 100
        result = "Passed!" if percentage >= int(testpaper.passing_grade[:-1]) else "Failed!"
        self.tests[testpaper.topic] = f"{result} ({round(percentage)}%)"
        self.tests_taken = self.tests