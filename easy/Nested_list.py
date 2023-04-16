"""
Given the names and grades for each student in a class of N students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

ex)
records = [["chi",20.0],["beta",50.0],["alpha",50.0]]
The ordered list of scores is [20.0,50.0], so the second lowest score is 50.0. There are two students with that score:["beta","alpha"] . Ordered alphabetically, the names are printed as:

The first line contains an integer, N , the number of students.
The 2N subsequent lines describe each student over 2 lines.
- The first line contains a student's name.
- The second line contains their grade.
input:

5
Harry
37.21
Berry
37.21
Tina
37.2
Akriti
41
Harsh
39

output:
Berry
Harry

"""
if __name__ == '__main__':
    
    stu_arr = []
    stu_dict = {}
    for _ in range(int(input())):
        name = input()
        score = float(input())
        if score not in stu_dict:
            stu_dict[score] = [name]
        else:
            stu_dict[score].append(name)
        #stu_arr.append([name,score])
        
    #first,second = 0, 0
    #for stu in stu_arr:
    #    if stu[1] > first:
    #        second = first
    #        first = stu[1]
    
    score_arr = list(stu_dict.keys())
    score_arr.sort()
    second = score_arr[1]
    stu_dict[second].sort()
    for name in stu_dict[second]:
        print(name)
        