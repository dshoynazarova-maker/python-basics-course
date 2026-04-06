def catalog_animals(tag_data):
    animal_catalog = {}
    for dic in tag_data:
        for id , name in dic.items():
            id = dic['chip_id']
            name = dic['species']
            animal_catalog[id]=name
    return animal_catalog

def process_sightings(animal_catalog, detected_chips):
    unseen_animals = set()
    unknown_signals = set()
    c_animals = set([id for id, name in animal_catalog.items()])
    detected_chips_set = set(detected_chips)
    unseen_animals = c_animals - detected_chips_set
    unknown_signals = detected_chips_set - c_animals
    return unseen_animals, unknown_signals
    
def alert_missing(animal_catalog, unseen_set):
    report = [f"NOT SEEN: {animal_catalog[chip_id]} (ID: {chip_id})" for chip_id in unseen_set]
    return sorted(report, key=lambda x: x.split(": ")[1].split(" (ID: ")[0])

tags = [
    {'chip_id': "WOLF-01", 'species': "Grey Wolf"},
    {'chip_id': "BEAR-09", 'species': "Brown Bear"},
    {'chip_id': "DEER-55", 'species': "Elk"}
]
sightings = ["WOLF-01", "DEER-55", "UFO-99"]

animal_catalog = catalog_animals(tags)
unseen_animals, unknown_signals = process_sightings(animal_catalog, sightings)
report = alert_missing(animal_catalog, unseen_animals)

print(f"Unseen Animals: {unseen_animals}")     
print(f"Unknown Signals: {unknown_signals}")
print(f"Report: {report}")