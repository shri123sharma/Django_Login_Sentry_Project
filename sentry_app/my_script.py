def add_fish_to_aquarium(fish_list):
    if len(fish_list) > 10:
        raise ValueError("A maximum of 10 fish can be added to the aquarium")
    return {"tank_a": fish_list}

if __name__=="__main__":
    print(add_fish_to_aquarium(fish_list=['shark','tuna']))