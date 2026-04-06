def find_section_index(section_names, section_name):
    for i in range(len(section_names)):
        if section_names[i] == section_name:
            return i
    return -1
    
def process_booking(initial_sections, initial_seats, operations):
    section_names=initial_sections[:]
    seats_available=initial_seats[:]
    print('Initial state:')
    print(f'   Sections: {section_names} ')
    print(f'   Seats: {seats_available}\n')
    print('Processing operations:')

    for op_num in range(len(operations)):
        operation = operations[op_num]
        command , name = operation[0] , operation[1]

        index = find_section_index(section_names, name)

        if command == 'ADD_SECTION':
            capacity = operation[2]
            if index == -1:
                section_names.append(name)
                seats_available.append(capacity)
                print(f'{op_num+1}. ADD_SECTION {name} {capacity} : Added new section')
            else:
                print(f"{op_num+1}. ADD_SECTION {name} {capacity}: Already exists (no change)")

        elif command == 'BOOK':
            num = operation[2]
            if index == -1:
                print(f'{op_num+1}. BOOK {name} {num}: Failed (section not found ) ')
            elif seats_available[index] < num:
                print(f"{op_num+1}. BOOK {name} {num}: Failed (only {seats_available[index]} available)")
            else:
                old = seats_available[index]
                seats_available[index] -= num
                print(f'{op_num+1}. BOOK {name} {num}: {old} -> {seats_available[index]} ')

        elif command == 'CANCEL':
            num = operation[2]
            if index == -1:
                print(f'{op_num+1}. CANCEL {name} {num}: Failed (section not found) ')
            else:
                old = seats_available[index]
                seats_available[index] += num
                print(f'{op_num+1}. CANCEL {name} {num}: {old} -> {seats_available[index]}')
    print(f'\nFinal state:')
    print(f'  Sections: {section_names}')
    print(f'  Seats: {seats_available}')
    return section_names, seats_available

sections = ["Orchestra", "Mezzanine", "Balcony"]
seats = [50, 75, 100]
booking_operations = [
    ["BOOK", "Mezzanine", 10],
    ["BOOK", "Orchestra", 60],
    ["CANCEL", "Balcony", 5],
    ["ADD_SECTION", "Box Seats", 12],
    ["BOOK", "Orchestra", 20]
]

final_sections, final_seats = process_booking(sections, seats, booking_operations)


