#include <iostream>

using namespace std;

int main() {
    int numSubjects;
    cout << "Enter the number of subjects: ";
    cin >> numSubjects;

    double totalCredits = 0.0;
    double totalGradePoints = 0.0;

    for (int i = 1; i <= numSubjects; i++) {
        cout << "\nSubject " << i << ":\n";
        double credits;
        cout << "Enter the credits for subject " << i << ": ";
        cin >> credits;

        double grade;
        cout << "Enter the grade for subject " << i << ": ";
        cin >> grade;

        double gradePoints = credits * grade;
        totalCredits += credits;
        totalGradePoints += gradePoints;
    }

    double cgpa = totalGradePoints / totalCredits;

    cout << "\nCGPA: " << cgpa << endl;

    return 0;
}

