# Name: Ashton Alston
# Date: 1/10/24
# Description: 
# This Python script creates a simple text-based adventure game where players navigate 
# through different rooms, interact with items, and solve puzzles using commands like 
# "go," "look," and "take." The game features room transitions, item handling, and 
# secret room reveals, providing a foundation for a basic text adventure experience.
#######################################################################################
import time
# the blueprint for a room
class Room:
    # the constructor
    def __init__(self, name):
        # rooms have a name, exits (e.g., south), exit locations
        # (e.g., to the south is room n), items (e.g., table), item
        # descriptions (for each item), and grabbables (things that
        # can be taken into inventory)
        self.name = name
        self.exits = []
        self.exitLocations = []
        self.items = []
        self.itemDescriptions = []
        self.grabbables = []
        self.grabbablesDescriptions = []
        

    # getters and setters for the instance variables
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def exits(self):
        return self._exits

    @exits.setter
    def exits(self, value):
        self._exits = value

    @property
    def exitLocations(self):
        return self._exitLocations

    @exitLocations.setter
    def exitLocations(self, value):
        self._exitLocations = value

    @property
    def items(self):
        return self._items

    @items.setter
    def items(self, value):
        self._items = value

    @property
    def itemDescriptions(self):
        return self._itemDescriptions

    @itemDescriptions.setter
    def itemDescriptions(self, value):
        self._itemDescriptions = value

    @property
    def grabbables(self):
        return self._grabbables

    @grabbables.setter
    def grabbables(self, value):
        self._grabbables = value
    @property
    def grabbablesDescriptions(self):
        return self._grabbablesDescriptions
    
    @grabbablesDescriptions.setter
    def grabbablesDescriptions(self,value):
        self._grabbablesDescriptions = value
    # adds an exit to the room
    # the exit is a string (e.g., north)
    # the room is an instance of a room
    def addExit(self, exit, room):
        # append the exit and room to the appropriate lists
        self._exits.append(exit)
        self._exitLocations.append(room)

    # adds an item to the room
    # the item is a string (e.g., table)
    # the desc is a string that describes the item (e.g., it is made of wood)
    def addItem(self, item, desc):
        # append the item and description to the appropriate lists
        self._items.append(item)
        self._itemDescriptions.append(desc)

    # adds a grabbable item to the room
    # the item is a string (e.g., key)
    def addGrabbable(self, item, desc):
        # append the item to the list
        self._grabbables.append(item)
        self._grabbablesDescriptions.append(desc)

    def modItemDiscript(self, item, newdesc):
        if item in self.items:
            item_index = self.items.index(item)
            self.itemDescriptions[item_index]= newdesc


    # removes a grabbable item from the room
    # the item is a string (e.g., key)
        # removes a grabbable item from the room
# the item is a string (e.g., key)
    def delGrabbable(self, item):
        # check if the item is in the list
        if item in self._grabbables:
            # remove the item from the list
            self._grabbables.remove(item)

            # check if there's a corresponding item description
            if item in self._items:
                # find the index of the corresponding item
                item_index = self._items.index(item)

                # check if the index is within the range of item descriptions
                if item_index < len(self._itemDescriptions):
                    # remove the corresponding item description
                    del self._items[item_index]
                    del self._itemDescriptions[item_index]
    def moveItem(self, item):
        # Check if the item is in the room
        if item in self._items:
            # Find the index of the corresponding item
            item_index = self._items.index(item)

            # Check if the index is within the range of item descriptions
            if item_index < len(self._itemDescriptions):
                # Get the description of the item
                item_description = self._itemDescriptions[item_index]

                # Check if the moved item is a bookshelf
                if "bookshelves" in item.lower():
                    return "It looks like another exit to the south!"
                else:
                    return "Everything looks normal."

        return "There is no {} here.".format(item)
    


    # returns a string description of the room
    # returns a string description of the room
    def __str__(self):
        # first, the room name
        s = "You are in {}.\n".format(self.name)

        # next, the items in the room
        s += "You see: " + ", ".join(self.items) + "\n"

        # next, the exits from the room
        s += "Exits: "
        for exit in self.exits:
            s += exit + " "

        return s


def createRooms():
    # create the rooms and give them meaningful names
    r1 = Room("Room 1")
    r2 = Room("Room 2")
    r3 = Room("Room 3")
    r4 = Room("Room 4")
    
    

    # add exits to room 1
    r1.addExit("east", r2)  # -> to the east of room 1 is room 2
    r1.addExit("south", r3)

    # add grabbables to room 1
    r1.addGrabbable("key", "Just an ordinary key")

    # add items to room 1
    r1.addItem("chair", "It is made of wicker and no one is sitting on it.")
    r1.addItem("table", "It is made of oak. A golden key rests on it.")

    # add exits to room 2
    r2.addExit("west", r1)
    r2.addExit("south", r4)

    # add items to room 2
    r2.addItem("rug", "It is nice and Indian. It also needs to be vacuumed.")
    r2.addItem("fireplace", "It is full of ashes.There is no chimney.")
    r2.addItem("cat", "Very fluffy, potentially cuddley.")

    # add exits to room 3
    r3.addExit("north", r1)
    r3.addExit("east", r4)


    # add grabbables to room 3
    r3.addGrabbable("book","4568...I belong on the bookshelves..or behind it? ")

    # add items to room 3
    r3.addItem("bookshelves", "They are empty. Go figure.")
    r3.addItem("statue", "There is nothing special about it.")
    r3.addItem("desk", "The statue is resting on it. So is a book.")
    r3.addItem("pickle-jar", "Yeah I would not touch that.")

    # add exits to room 4
    r4.addExit("north", r2)
    r4.addExit("west", r3)
    r4.addExit("south", None)  # DEATH!

    # add grabbables to room 4
    r4.addGrabbable("6-pack","It looks expired, but im not sure.")
    r4.addGrabbable("tiny-book", "4599")

    # add items to room 4
    r4.addItem("alpaca", "The alpaca is very cute. His breathe stinks but there is a tiny-book around his neck!")
    r4.addItem("brew_rig", "Gourd is brewing some sort of oatmeal stout on the brew rig. A 6-pack is resting beside it.")
    r4.addItem("robert", "He is facing the corner and chained. I wouldn't look at him")
    # set room 1 as the current room at the beginning of the game
    currentRoom = r1
    return currentRoom

def death():   
    print(" " * 17 + "u" * 7)
    print(" " * 13 + "u" * 2 + "$" * 11 + "u" * 2)
    print(" " * 10 + "u" * 2 + "$" * 17 + "u" * 2)
    print(" " * 9 + "u" + "$" * 21 + "u")
    print(" " * 8 + "u" + "$" * 23 + "u")
    print(" " * 7 + "u" + "$" * 25 + "u")
    print(" " * 7 + "u" + "$" * 25 + "u")
    print(" " * 7 + "u" + "$" * 6 + "\"" + " " * 3 + "\"" + "$" * 3 +
          "\"" + " " * 3 + "\"" + "$" * 6 + "u")
    print(" " * 7 + "\"" + "$" * 4 + "\"" + " " * 6 + "u$u" + " " * 7
          + "$" * 4 + "\"")
    print(" " * 8 + "$" * 3 + "u" + " " * 7 + "u$u" + " " * 7 + "u" +
          "$" * 3)
    print(" " * 8 + "$" * 3 + "u" + " " * 6 + "u" + "$" * 3 + "u" + "" * 6 + "u" + "$" * 3)
    print(" " * 9 + "\"" + "$" * 4 + "u" * 2 + "$" * 3 + " " * 3 +
          "$" * 3 + "u" * 2 + "$" * 4 + "\"")
    print(" " * 10 + "\"" + "$" * 7 + "\"" + " " * 3 + "\"" + "$" * 7
          + "\"")
    print(" " * 12 + "u" + "$" * 7 + "u" + "$" * 7 + "u")
    print(" " * 13 + "u$\"$\"$\"$\"$\"$\"$u")
    print(" " * 2 + "u" * 3 + " " * 8 + "$" * 2 + "u$ $ $ $ $u" + "$"
          * 2 + " " * 7 + "u" * 3)
    print(" u" + "$" * 4 + " " * 8 + "$" * 5 + "u$u$u" + "$" * 3 + " " * 7 + "u" + "$" * 4)
    print(" " * 2 + "$" * 5 + "u" * 2 + " " * 6 + "\"" + "$" * 9 +
          "\"" + " " * 5 + "u" * 2 + "$" * 6)
    print("u" + "$" * 11 + "u" * 2 + " " * 4 + "\"" * 5 + " " * 4 +
          "u" * 4 + "$" * 10)
    print("$" * 4 + "\"" * 3 + "$" * 10 + "u" * 3 + " " * 3 + "u" * 2
          + "$" * 9 + "\"" * 3 + "$" * 3 + "\"")
    print(" " + "\"" * 3 + " " * 6 + "\"" * 2 + "$" * 11 + "u" * 2 +
          " " + "\"" * 2 + "$" + "\"" * 3)
    print(" " * 11 + "u" * 4 + " \"\"" + "$" * 10 + "u" * 3)
    print(" " * 2 + "u" + "$" * 3 + "u" * 3 + "$" * 9 + "u" * 2 +
          " \"\"" + "$" * 11 + "u" * 3 + "$" * 3)
    print(" " * 2 + "$" * 10 + "\"" * 4 + " " * 11 + "\"\"" + "$" *
          11 + "\"")
    print(" " * 3 + "\"" + "$" * 5 + "\"" + " " * 22 + "\"\"" + "$" *
          4 + "\"\"")
    print(" " * 5 + "$" * 3 + "\"" + " " * 25 + "$" * 4 + "\"")
    19
    
def win():
    print("Congratulations! You have successfully completed the game.")
    print("You are a master adventurer!")
    print("Thanks for playing. See you next time!")
    exit()  # This will exit the game

    


# Main
# ...

# Main
inventory = []
inventoryDesc = []

currentRoom = createRooms()

# play forever (well, at least until the player dies or asks to quit)
while True:
    # set the status so the player has situational awareness
    # the status has room and inventory information
    status = "{}\nYou are carrying: {}\n".format(currentRoom, inventory)

    # if the current room is None, then the player is dead
    # this only happens if the player goes south when in room 4
    if currentRoom is None:
        status = "You are dead."

    # display the status
    print("========================================================")
    print(status)

    # if the current room is None (and the player is dead), exit the game
    if currentRoom is None:
        death()
        break

    # prompt for player input
    # the game supports a simple language of <verb> <noun>
    # valid verbs are go, look, take, and help
    action = input("What to do? ")
    # set the user's input to lowercase to make it easier to compare
    # the verb and noun to known values
    action = action.lower()

    # exit the game if the player wants to leave (supports quit, exit, and bye)
    if action in ["quit", "exit", "bye"]:
        print("See you later!")
        break

    # set a default response
    response = "I don't understand. Try 'help' for available commands."

    # split the user input into words (words are separated by spaces)
    words = action.split()

    # the game only understands two-word inputs
    if len(words) == 2:
        # isolate the verb and noun
        verb = words[0]
        noun = words[1]

        # the verb is: go
        if verb == "go":
            # set a default response
            response = "Invalid exit."

            # check for valid exits in the current room
            for i in range(len(currentRoom.exits)):
                # a valid exit is found
                if noun == currentRoom.exits[i]:
                    # change the current room to the one that is
                    # associated with the specified exit
                    currentRoom = currentRoom.exitLocations[i]
                    # set the response (success)
                    response = "Room changed."
                    # no need to check any more exits
                    break
            else:
                response = "Invalid exit. Try a different direction."

        # the verb is: look
        elif verb == "look":
            # set a default response
            response = "I don't see that item."
            if noun == "robert":
                death()
                exit()
            # check for valid items in the current room
            for i in range(len(currentRoom.items)):
        # a valid item is found
                if noun == currentRoom.items[i]:
                    # set the response to the item's description
                    response = currentRoom.itemDescriptions[i]
                    break

            # check for valid items in the inventory
            for i in range(len(inventory)):
                if noun == inventory[i]:
                    response = inventoryDesc[i]
                    break

            

        # the verb is: take
        elif verb == "take":
            response = "I dont see that item"
            for grabbable in currentRoom.grabbables:
                if noun == grabbable:
                    description = currentRoom.grabbablesDescriptions[currentRoom.grabbables.index(grabbable)]
                    inventoryDesc.append(description)
                    currentRoom.delGrabbable(grabbable)
                    inventory.append(grabbable)

                    currentRoom.modItemDiscript(grabbable, "The item you took is gone. Nothing extraordinary here.")
                    response = "Item Grabbed"
                    #Change item description after grabbable is picked up
                    if "key" in inventory:
                        currentRoom.modItemDiscript("table", "Just a normal table.")
                    if "book" in inventory:
                        currentRoom.modItemDiscript("desk", "Nothings here except a statue.")
                    if "bible" in inventory:
                        currentRoom.modItemDiscript("lion", "Please don't go near him again")
                    if "tiny-book" in inventory:
                        currentRoom.modItemDiscript("alpaca", "Cool guy, to be honest. Sorry about taking the tiny-book")
                    if "6-pack" in inventory:
                        currentRoom.modItemDiscript("brew_rig", "Just a brew rig now.")



        
        # ...
        # In the game loop, handle the "move" verb
# ...
        elif verb == "move":
            # set a default response
            response = "I don't see that item."

            # check for valid items in the current room
            for i in range(len(currentRoom.items)):
                # a valid item is found
                if noun == currentRoom.items[i]:
                    # Check if the moved item is a bookshelf
                    if "bookshelves" in noun.lower():
                        # Remove the bookshelves from the room
                        currentRoom.delGrabbable(noun)

                        # Create a new room for the Secret Room
                        secret_room = Room("Secret Room")
                        secret_room.addExit("north", currentRoom)  # Create a connection back to the original room
                        currentRoom.addExit("south", secret_room)  # Create a connection to the Secret Room

                        # Add a painting to the Secret Room
                        secret_room.addItem("painting", "A mysterious painting hangs on the wall. It kinda crooked. It needs to be moved.")

                        # Add a sleeping lion to the Secret Room
                        secret_room.addItem("lion", "A majestic lion is peacefully sleeping in the corner.There is a bible next to him.")
                        secret_room.addGrabbable("bible", "1984")

                        # Set the response to the result of moving the item (success)
                        response = "The bookshelves move, revealing a secret room to the south."
                    else: 
                        response = "Everything looks normal."

                       
                        

                    if "painting" in noun:
                        print("It looks like a trap door! I think it needs a code")
                        paswd = input("Enter a 4 digit code:")
                        if paswd == "4599": 
                            win()
                        else:
                            print("That's not right. Go back and search for the correct code. Sometimes the truth...stinks?")
                            print("Just move the painting once more to try again!")
                            time.sleep(8)
                            break
                        

                    # no need to check any more items
                    break
        


    elif action == "help":
        response = "Valid commands are: go <direction>, look <item>, take <item>, move <item>, quit, exit, bye, help."

    # display the response
    print("\n{}".format(response))
