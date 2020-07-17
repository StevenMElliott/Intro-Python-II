from room import Room
from player import Player

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", ["key", "skull"]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#reusable text prompts
direction_prompt = "Select direction of travel: (n)orth, (e)ast, (s)outh, (w)est: \n"
empty_direction = "There is nothing in that direction."

#New player starting outside
current_room = room['outside']
np = Player(current_room)
print(np)
p_input = (input(f"{direction_prompt}")).lower()


while(p_input != "q"):
    #movement block for n, e, s, w
    if p_input == "n":
        #test to make sure the room exists
        test_room = current_room.n_to
        #doesn't go there if it doesn't exist
        if test_room == None:
            print(f"{empty_direction}")
            p_input = (input(f"{direction_prompt}")).lower()
        #moves player north
        else:
            current_room = current_room.n_to
            np = Player(current_room)
            print(np.current_room)
            p_input = (input(f"{direction_prompt}")).lower()
    elif p_input == "e":
        test_room = current_room.e_to
        if test_room == None:
            print(f"{empty_direction}")
            p_input = (input(f"{direction_prompt}")).lower()
        else:
            current_room = current_room.e_to
            np = Player(current_room)
            print(np.current_room)
            p_input = (input(f"{direction_prompt}")).lower()
    elif p_input == "s":
        test_room = current_room.s_to
        if test_room == None:
            print(f"{empty_direction}")
            p_input = (input(f"{direction_prompt}")).lower()
        else:
            current_room = current_room.s_to
            np = Player(current_room)
            print(np.current_room)
            p_input = (input(f"{direction_prompt}")).lower()
    elif p_input == "w":
        test_room = current_room.w_to
        if test_room == None:
            print(f"{empty_direction}")
            p_input = (input(f"{direction_prompt}")).lower()
        else:
            current_room = current_room.w_to
            np = Player(current_room)
            print(np.current_room)
            p_input = (input(f"{direction_prompt}")).lower()
    #search room
    elif p_input == "search":
        print(current_room.items)
        p_input = (input(f"{direction_prompt}")).lower()
    #get item from room
    elif p_input.find("get") != -1:
        transaction = p_input.split()
        # if len(transaction) == 1:
        #     print("get what?")
        #     p_input = (input(f"{direction_prompt}")).lower()
        if transaction[1] in current_room.items:
            np.items.append(transaction[1])
            current_room.items.remove(transaction[1])
            print(np)
            p_input = (input(f"{direction_prompt}")).lower()
        else:
            print(f"{transaction} not found in {np.current_room}.\n")
            p_input = (input(f"{direction_prompt}")).lower()
    #drop item into room
    elif p_input.find("drop") != -1:
        transaction = p_input.split()
        if len(transaction) !=1:
            if transaction[1] in np.items:
                current_room.items.append(transaction[1])
                np.items.remove(transaction[1])
                print(f"Dropped {transaction[1]} in {current_room}\n")
                p_input = (input(f"{direction_prompt}")).lower()
            else:
                print(f"Unable to drop.\n")
                p_input = (input(f"{direction_prompt}")).lower()
        else:
            print(f"Unable to drop.\n")
            p_input = (input(f"{direction_prompt}")).lower()

    else:
        print(f"\n{p_input} ain't no direction I ever heard of.")
        print("Are you some extra dimentional being?")
        p_input = (input(f"{direction_prompt}")).lower()


# Make a new player object that is currently in the 'outside' room.

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.