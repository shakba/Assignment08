#------------------------------------------#
# Title: CD_Inventory.py
# Desc: Assignnment 08 working with classes
# Change Log: (Who, When, What)
#shakedbason, 2020-Aug-30, created file
#shakedbason, 2020-Aug-30, added modified
#------------------------------------------#

import pickle

# -- DATA -- #
strFileName = 'cdInventory.dat'
lstOfCDObjects = []
lstIdIndex = []

class CD:
    """Stores data about a CD:

    properties:
        cd_id: (int) with CD ID
        cd_title: (string) with the title of the CD
        cd_artist: (string) with the artist of the CD
    methods:

    """
    #Make all attributes private.
    def __init__(self, cd_id, cd_title, cd_artist):

        self.__cdId = int(cd_id)
        self.__cdTitle = cd_title.title()
        self.__cdArtist = cd_artist.title()
        
    @property
    def cd_Id(self):
        return self.__cdId

    @cd_Id.setter
    def cd_Id(self, newId):
        self.__cdId = int(newId)

    @property
    def cd_Title(self):
        return self.__cdTitle

    @cd_Title.setter
    def cd_Title(self, newTitle):
        self.__cdTitle = newTitle

    @property
    def cd_Artist(self):
        return self.__cdArtist

    @cd_Artist.setter
    def cd_Artist(self, newArtist):
        self.__cdArtist = newArtist

    def __str__(self):
        return f'{self.cd_Id}\t{self.cd_Title} (by:{self.cd_Artist})'

# -- PROCESSING -- #
class FileIO:
    """Processes data to and from file:

    properties:

    methods:
        save_inventory(file_name, lst_Inventory): -> None
        load_inventory(file_name): -> (a list of CD objects)

    """
    @staticmethod
    def load_inventory(file_name):
        """Function manage data ingestion from file to a list of dictionaries
        Reads data from binary file and use pickle 
        Args:
            file_name (string type)
            table (list of objects)
        Returns:
            None.
        """
        with open(file_name, 'rb') as objFile:
            val = pickle.load(objFile)
            print('\nCdInventory loaded\n')
            return val

    @staticmethod
    def save_inventory(file_name, table):
        """Function writes and add data to file
        appends data
        Args:
            file_name (string type)
            table (list of objects)
        Returns:
            None.
        """
        with open(file_name, 'wb') as objFile:
            pickle.dump(table, objFile)
        print('\nCDInventory saved\n')

# -- PRESENTATION (Input/Output) -- #
class IO:
    """Handling Input / Output"""
    @staticmethod
    def print_menu():
        """Displays a menu by user choice 
        Args:
            None.
        Returns:
            None.
        """

        print('Menu\n\n[l] load Inventory from file\n[a] Add CD\n[i] Display Current Inventory')
        print('[d] delete CD from Inventory\n[s] Save Inventory to file\n[x] exit\n')

    @staticmethod
    def menu_choice():
        """Gets user input for menu selection
        Args:
            None.
        Returns:
            choice (string): a lower case sting of the users input out of the choices l, a, i, d, s or x
        """
        choice = ' '
        while choice not in ['l', 'a', 'i', 'd', 's', 'x']:
            choice = input('Which operation would you like to perform? [l, a, i, d, s or x]: ').lower().strip()
        print()  # Add extra space for layout
        return choice

    @staticmethod
    def show_inventory(table):
        """Displays current inventory table
        Args:
            table (list of CD objects): list data structure (list of CD objects) that holds the data during runtime.
        Returns:
            None.
        """
        print('======= The Current Inventory: =======')
        print('ID\tCD Title (by: Artist)\n')
        for row in table:
            # Prints the CD object based on __str__ method
            print(row)
        print('======================================')

    @staticmethod
    def addItem():
        """Function to get user input for ID, title, and artist
        
        Args:
            None.
            
        Returns:
            StrID (string)
            Strtitle (string)
            StArtist (string)
        """
        strID = input('Enter ID: ').strip()
        strTitle = input('What is the CD\'s title? ').strip()
        stArtist = input('What is the Artist\'s name? ').strip()
        return strID, strTitle, stArtist

    @staticmethod
    def delItem(intIDDel, table, spotId):
        """Function to DELETE existing data from table.
        
        Args:
            idRemove (int): ID to remove CD data
            table (list of dic): 2D data structure
            spotId(List)
            
        Returns:
            None
        """             
        intRowNr = -1
        blnCDRemoved = False
        for row in spotId:
            intRowNr += 1
            if intIDDel == row:
                del table[intRowNr]
                blnCDRemoved = True
                break
        if blnCDRemoved:
            print('The CD was removed')
        else:
            print('Could not find this CD!')

# -- Main Body of Script -- #
# 2. start main loop
while True:
    # 2.1 Display Menu to user and get choice
    IO.print_menu()
    strChoice = IO.menu_choice()

    # 3. Process menu selection
    # 3.1 process exit first
    if strChoice == 'x':
        break

    # 3.2 process load inventory
    if strChoice == 'l':
        print('WARNING: If you continue, all unsaved data will be lost and the Inventory re-loaded from file.')
        strYesNo = input('type \'yes\' to continue and reload from file. otherwise reload will be canceled: ')
        if strYesNo.lower() == 'yes':
            print('reloading...')
            lstOfCDObjects.clear()
            cdFile = FileIO.load_inventory(strFileName)
            lstOfCDObjects.extend(cdFile)
            IO.show_inventory(lstOfCDObjects)
        else:
            input('canceling... Inventory data NOT reloaded. Press [ENTER] to continue to the menu.')
            IO.show_inventory(lstOfCDObjects)
        continue  # start loop back at top.

    # 3.3 process add a CD
    elif strChoice == 'a':
        # 3.3.1 Ask user for new ID, CD Title and Artist
        userID, userTitle, userArtist = IO.addItem()

        # Check for blank fields
        if(not userID or not userTitle or not userArtist):
            print("Cannot leave ID, CD Title or Artist Name field blank!\n")
            continue
        newCD = CD(userID, userTitle, userArtist)
        lstOfCDObjects.append(newCD)
        IO.show_inventory(lstOfCDObjects)
    # 3.4 process display current inventory
        
    elif strChoice == 'i':
        IO.show_inventory(lstOfCDObjects)

    # 3.5 process delete a CD
    elif strChoice == 'd':
        # 3.5.1 get Userinput for which CD to delete
        # 3.5.1.1 display Inventory to user
        IO.show_inventory(lstOfCDObjects)
        # 3.5.1.2 ask user which ID to remove
        try:
            intIdSel = int(input('Which ID would you like to delete ? ').strip())
        except ValueError:
            print('\ID CAN NOT BE STRING!\n')
            continue
        lstIdIndex.clear()
        for row in lstOfCDObjects:
            lstIdIndex.append(row.cd_Id)
        # 3.5.2 search thru table and delete CD
        IO.delItem(intIdSel, lstOfCDObjects, lstIdIndex)
        IO.show_inventory(lstOfCDObjects)
    # 3.6 process save inventory to file
        
    elif strChoice == 's':
        # 3.6.1 Display current inventory and ask user for confirmation to save
        IO.show_inventory(lstOfCDObjects)
        strYesNo = input('Save this inventory to file? [y/n] ').strip().lower()
        # 3.6.2 Process choice
        if strYesNo == 'y':
            # 3.6.2.1 save data
            FileIO.save_inventory(strFileName,lstOfCDObjects)
        else:
            input('The inventory was NOT saved to file. Press [ENTER] to return to the menu.')
    # 3.7 catch-all should not be possible, as user choice gets vetted in IO, but to be save:
    else:
        print('General Error')