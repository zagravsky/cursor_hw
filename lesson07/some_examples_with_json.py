import json

if __name__ == "__main__":
    # Load data from file to local variable
    our_data = json.load(open("some_data.json", "r"))
    print(our_data)
    print(type(our_data))
    # Change some field to new value
    our_data[0]["week"] = 56
    # Save data from variable to new file
    json.dump(our_data, open("new_file.json", "w"))
    for topic in our_data:
        # Iterate trow our_data to see type of values
        print(topic)
        print(type(topic))
        for key, val in topic.items():
            print(f"Key {key} {val}, Type {type(val)}")
    # Convert dict to json format string
    our_str = json.dumps(our_data)
    print(our_str)
    print(type(json.loads(our_str)))
    print(type(our_str))

