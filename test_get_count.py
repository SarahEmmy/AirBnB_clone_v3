#!/usr/bin/python3
from models import storage
from models.state import State

if __name__ == "__main__":
    print("All objects: {}".format(storage.count()))
    print("State objects: {}".format(storage.count(State)))

    first_state_id = list(storage.all(State).values())[0].id
    first_state = storage.get(State, first_state_id)
    print("First state: [{}] ({}) {}".format(type(first_state).__name__, first_state_id, first_state.to_dict()))
