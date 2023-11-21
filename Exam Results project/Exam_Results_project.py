def calculate_subject_grade(test_results, c_barrier, b_barrier, a_barrier):
    average_score = sum(test_results) / len(test_results)
    total_marks = sum(test_results)
    if average_score >= a_barrier:
        return "A", total_marks
    elif average_score >= b_barrier:
        return "B", total_marks
    elif average_score >= c_barrier:
        return "C", total_marks
    else:
        return "Fail", total_marks
 
 
def english_grade(test1, test2):
    return calculate_subject_grade([test1, test2], 64, 84, 104)
 
 
def maths_grade(test1, test2, test3):
    return calculate_subject_grade([test1, test2, test3], 56, 64, 78)
 
 
def science_grade(test1, test2, test3):
    return calculate_subject_grade([test1, test2, test3], 96, 113, 128)
 
 
def main():
    english_test1 = int(input("Enter English Test 1 score: "))
    english_test2 = int(input("Enter English Test 2 score: "))

    maths_test1 = int(input("Enter Maths Test 1 score: "))
    maths_test2 = int(input("Enter Maths Test 2 score: "))
    maths_test3 = int(input("Enter Maths Test 3 score: "))

    science_test1 = int(input("Enter Science Test 1 score: "))
    science_test2 = int(input("Enter Science Test 2 score: "))
    science_test3 = int(input("Enter Science Test 3 score: "))

    english_result, english_total_marks = english_grade(english_test1, english_test2)
    maths_result, maths_total_marks = maths_grade(maths_test1, maths_test2, maths_test3)
    science_result, science_total_marks = science_grade(science_test1, science_test2, science_test3)

    print(f"\nEnglish Grade: {english_result} | Total Marks: {english_total_marks}/240")
    print(f"Maths Grade: {maths_result} | Total Marks: {maths_total_marks}/300")
    print(f"Science Grade: {science_result} | Total Marks: {science_total_marks}/450")
 
 
if __name__ == "__main__":
    main()