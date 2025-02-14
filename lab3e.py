#!/usr/bin/env python3

my_list = [100, 200, 300, 'six hundred']

def give_list():
    return my_list

def give_first_item():
    return str(my_list[0])

def give_first_and_last_item():
    return [my_list[0], my_list[-1]]

def give_second_and_third_item():
    return [my_list[1], my_list[2]]

if __name__ == '__main__':
    print(give_list())
    print(give_first_item())
    print(give_first_and_last_item())
    print(give_second_and_third_item())

courses = ['uli101', 'ops235', 'ops335', 'ops445', 'ops535', 'ops635']
print(courses[0])
courses[0] = 'eac150'
print(courses[0])
print(courses)

courses.append('ops235')
print(courses)

courses.insert(0, 'hwd101')
print(courses)

courses.remove('ops335')
print(courses)

sorted_courses = courses.copy()
sorted_courses.sort()
print(courses)
print(sorted_courses)

list_of_numbers = [1, 5, 2, 6, 8, 5, 10, 2]
print("List length is " + str(len(list_of_numbers)) +
      ", smallest element in the list is " + str(min(list_of_numbers)) +
      ", largest element in the list is " + str(max(list_of_numbers)))
