def organize_sales(ticket_log):
    cinema_dict = {}
    for line in ticket_log:
        splitted_line = line.split('::')
        movie_title = splitted_line[0]
        show_time = splitted_line[1]
        price = int(splitted_line[2])
        if movie_title not in cinema_dict:
            cinema_dict[movie_title] = []
        cinema_dict[movie_title].append((show_time,price))
    return cinema_dict
def calculate_box_office(cinema_dict):
    for movie_title, details in cinema_dict.items():
        total = 0
        for detail in details:
            total += detail[1]
        print(f'{movie_title} : {total} tickets sold')
ticket_log = [
    "Avatar::10:00AM::50",
    "Titanic::11:00AM::30",
    "Avatar::2:00PM::100",
    "StarWars::1:00PM::80",
    "Titanic::4:00PM::40",
    "StarWars::5:00PM::120"
]
cinema_dict = organize_sales(ticket_log)
calculate_box_office(cinema_dict)

    
        




