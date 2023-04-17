"""
The provided code stub will read in a dictionary containing key/value pairs of name:[marks] for a list of students. Print the average of the marks array for the student name provided, showing 2 places after the decimal.

The first line contains the integer N , the number of students' records. The next n lines contain the names and marks obtained by a student, each value separated by a space. The final line contains query_name, the name of a student to query.

ex)
input:
3
Krishna 67 68 69
Arjun 70 98 63
Malika 52 56 60
Malika

output:
56.00

(52+56+60)/3
"""
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    avg = sum(student_marks[query_name])/3
    print(format(avg,".2f"))
    
    