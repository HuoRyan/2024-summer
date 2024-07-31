def build_attraction_dict(filename):
    attraction_dict = {}
    with open (filename, "r") as file:
        for line in file:
            attraction, province = line.strip().split(",")
            attraction_dict[attraction] = province
    return attraction_dict