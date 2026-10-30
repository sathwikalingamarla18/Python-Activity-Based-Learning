### Problem Statement
To develop a Python program using nested lists to represent multiple classrooms and their seating positions. The program should allocate students to available seats, preserve reserved seats, detect duplicate student assignments, and calculate the number of vacant seats in each classroom. The program helps manage classroom seating efficiently and prevents seat allocation errors.

### Algorithm:
1.Start the program.
2. Initialize the classroom seating arrangement.
3.Create a list of students waiting for seats.
4. Check each seat in every classroom.
5. If a seat is empty and a student is available, assign the student to that seat.
6. Display the updated seating arrangement.
7. Count the remaining empty seats.
8. Stop the program.
### Flowchart
```mermaid
flowchart TD
    A([Start]) --> B[Initialize classrooms using nested lists]
    B --> C[Mark available and reserved seats]
    C --> D[Enter student details]
    D --> E[Select a classroom and seat]
    E --> F{Is the seat reserved?}

    F -- Yes --> G[Preserve reserved seat]
    G --> N{Are more students to allocate?}

    F -- No --> H{Is the seat already occupied?}
    H -- Yes --> I[Reject allocation]
    I --> N

    H -- No --> J{Is the student already assigned?}
    J -- Yes --> K[Report duplicate assignment]
    K --> N

    J -- No --> L[Allocate student to the seat]
    L --> N

    N -- Yes --> D
    N -- No --> O[Count occupied and vacant seats]
    O --> P[Calculate vacant capacity for each classroom]
    P --> Q[Display seating and occupancy details]
    Q --> R([Stop])
```
### Code
seats = [["A", "RESERVED", ""], ["B", "", "C"]]

students = ["Ravi", "Maya"]

i = 0

while i < len(seats):
    
    j = 0
    
    while j < len(seats[i]):
        
        if seats[i][j] == "":
            
            if students:
        
                seats[i][j] = students.pop(0)
    
        j += 1

    i += 1

print(seats)

print("Vacant:", sum(row.count("") for row in seats))

### Sample Input
Classroom Seats:

[
    
    ["A", "RESERVED", ""],

    ["B", "", "C"]
]

Students to Allocate:

["Ravi", "Maya"]

### Sample Output
[['A', 'RESERVED', 'Ravi'], ['B', 'Maya', 'C']]

Vacant: 0




