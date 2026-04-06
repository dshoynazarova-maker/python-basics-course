def calculate_price_per_ticket(event_tuple):
    tickets_sold = event_tuple[2]
    revenue_generated = event_tuple[3]
    return revenue_generated / tickets_sold

def find_top_earning_event(events):
    top_revenue = -1
    top_event_id = ""
    for event_id, _, _, revenue in events:
        if revenue > top_revenue:
            top_revenue = revenue
            top_event_id = event_id
        elif revenue == top_revenue:
            if event_id < top_event_id:
                top_event_id = event_id
    return top_event_id

def get_events_by_artist(events, artist_name):
    event_ids = []
    for event_id, artist, _, _ in events:
        if artist == artist_name:
            event_ids.append(event_id)

    return sorted(event_ids)

def get_artist_sales_summary(events):
    summary_list = []
    for _, artist, sold, _ in events:
        found = False
        for i in range(len(summary_list)):
            current_artist = summary_list[i][0]
            if current_artist == artist:
                summary_list[i][1] += sold
                found = True
                break
        if not found:
            summary_list.append([artist, sold])
    final_summary_tuples = [(artist, sold) for artist, sold in summary_list]
    return sorted(final_summary_tuples)

def analyze_ticket_sales(events):
    top_earning_event_id = find_top_earning_event(events)
    imagine_dragons_events = get_events_by_artist(events, 'Imagine Dragons')
    artist_summary = get_artist_sales_summary(events)

    return (top_earning_event_id, imagine_dragons_events, artist_summary)

events = [
        ('EV101', 'The Killers', 5000, 375000),
        ('EV205', 'Imagine Dragons', 8000, 600000),
        ('EV102', 'The Killers', 4500, 360000),
        ('EV301', 'Coldplay', 10000, 950000),
        ('EV206', 'Imagine Dragons', 8500, 680000)
    ]
summary_results = analyze_ticket_sales(events)
print(summary_results)

