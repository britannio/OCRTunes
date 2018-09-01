###OCRTunes###
import sqlite3 #imports the sqlite3 module to allow external databased to be used.
import ast # save eval of dictionaries

db = sqlite3.connect('database.db') #Creates a sqlite3 database
cursor = db.cursor() #assign a cursor to the database

cursor.execute('''CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY, name TEXT, password TEXT, date INTEGER,
                   month INTEGER, year INTEGER, favouriteArtist TEXT, favouriteGenre TEXT, playlists TEXT)''')
#Creates a users table in the main databse
cursor.execute('''DROP TABLE IF EXISTS songLibrary''')
# deletes the previous song library to prevent duplicate songs from being added to the song library
cursor.execute('''CREATE TABLE IF NOT EXISTS songLibrary(id INTEGER PRIMARY KEY, title TEXT, artist TEXT, genre TEXT, length INTEGER)''')
# Creates the songLibrary table in the main database

#adds all songs into the songLibrary table in the main database
#song length is in seconds
cursor.execute('''INSERT INTO songLibrary(title, artist, genre, length) VALUES ('I Miss You', 'Clean Bandit', 'pop', 206)''')
cursor.execute('''INSERT INTO songLibrary(title, artist, genre, length) VALUES ('Wolves', 'Selena Gomez', 'pop', 198)''')
cursor.execute('''INSERT INTO songLibrary(title, artist, genre, length) VALUES ('Dusk Till Dawn', 'ZAYN', 'pop', 239)''')
cursor.execute('''INSERT INTO songLibrary(title, artist, genre, length) VALUES ('Juicy', 'BIG', 'hip-hop', 207)''')
cursor.execute('''INSERT INTO songLibrary(title, artist, genre, length) VALUES ('In Da Club', '50 Cent', 'hip-hop', 242)''')                                                                             
cursor.execute('''INSERT INTO songLibrary(title, artist, genre, length) VALUES ('Gucci Gang', 'Lil Pump', 'hip-hop', 188)''')
cursor.execute('''INSERT INTO songLibrary(title, artist, genre, length) VALUES ('Rockstar', 'Post Malone', 'hip-hop', 229)''')
cursor.execute('''INSERT INTO songLibrary(title, artist, genre, length) VALUES ('It Takes Two', 'Rob Base', 'hip-hop', 239) ''')
cursor.execute('''INSERT INTO songLibrary(title, artist, genre, length) VALUES ('Jump Around', 'House of Pain', 'hip-hop', 203) ''')
cursor.execute('''INSERT INTO songLibrary(title, artist, genre, length) VALUES ('Bartier Cardi', 'Cardi B', 'hip-hop', 196) ''')
cursor.execute('''INSERT INTO songLibrary(title, artist, genre, length) VALUES ('Cradle Song', 'The Choir', 'classical', 243) ''')
cursor.execute('''INSERT INTO songLibrary(title, artist, genre, length) VALUES ('Clair De Lune', 'Cinema Classics', 'classical', 181) ''')
cursor.execute('''INSERT INTO songLibrary(title, artist, genre, length) VALUES ('Perfect', 'Ed Sheeran', 'pop', 198  )''')
cursor.execute('''INSERT INTO songLibrary(title, artist, genre, length) VALUES ('Havana', 'Camila Cabello', 'pop', 185)''')
cursor.execute('''INSERT INTO songLibrary(title, artist, genre, length) VALUES ('New Rules', 'Dua Lipa', 'pop', 241) ''')
cursor.execute('''INSERT INTO songLibrary(title, artist, genre, length) VALUES ('Closer', 'The Chainsmokers', 'pop', 192) ''')
cursor.execute('''INSERT INTO songLibrary(title, artist, genre, length) VALUES ('Too Good at Goodbyes', 'Sam Smith', 'pop', 181) ''')
cursor.execute('''INSERT INTO songLibrary(title, artist, genre, length) VALUES ('End Game', 'Taylor Swift', 'pop', 229 )''')
cursor.execute('''INSERT INTO songLibrary(title, artist, genre, length) VALUES ('Sorry Not Sorry', 'Demi Lovato', 'pop', 202 )''')
cursor.execute('''INSERT INTO songLibrary(title, artist, genre, length) VALUES ('Mi Gente', 'J Balvin', 'pop', 183 )''')
cursor.execute('''INSERT INTO songLibrary(title, artist, genre, length) VALUES ('It Aint Me', 'Kygo', 'pop', 223 )''')
cursor.execute('''INSERT INTO songLibrary(title, artist, genre, length) VALUES ('Wolves', 'Marshmello', 'pop', 216 )''')
db.commit() # saves the database after a change has been made i.e. songs have been added to the SongLibary
                                                                               
name = '' #global variable to store the name of the user currently logged in.
#This allows any subroutine with global access to this variable to check the name of the user.
admin = False # global variable to store the state of the users access level(False = standard user, True = OCRTunes Creator)
playlist = {}

def home():
    #login,signup and artist/genre viewing takes place here
    

   
    print('Would you like to:')
    print('1. Login')
    print('2. Signup')
    print('3. View available artists and genres')

    while True:
        try:
            choice = int(input(':')) ##unfinished
        except ValueError:
            print('Please enter a number')
            continue
        
        if choice == 1:
            login()
        elif choice == 2:
            create_account()
        elif choice == 3:
            view_artists_and_genres()
        else:
            print(str(choice) + 'isn\'t an option')
            
#End of home() 
    
def create_account():
    #account creation takes place here
    print('\nCreate Account')
    print('----------------')
    while True:
        nameTaken = False

        print('Please enter an alphanumeric username between 1 and 20 characters?')
        name = str(input(':')).strip().lower()

        if len(name) >= 1 and len(name) <= 20 and name.isalnum():

            cursor.execute('''SELECT name FROM users''')
            for row in cursor:
                if name == row[0]:
                    print('Name taken')
                    nameTaken = True
                else:
                    pass
                    #name is unique
            else:
                if nameTaken:
                    continue
                else:
                    break

        else:
            print('''Something went wrong \n please make sure that your name is: \nBetween 1 and to characters long and only contains letters and numbers''')

    print('Hello', name, 'Please enter yor date of birth in the following format dd/mm/yy eg. 31/12/2000')
    while True:
        try:
            dob = str(input(':'))
            dobList = dob.split('/')
        except:
            print('make sure you use the correect format dd/mm/yy')

        try:
            date = int(dobList[0])
            month = int(dobList[1])
            year = int(dobList[2])
        except:
            print('Make sure that you use whole numbers')
            continue
            

        if len(dobList) == 3 : #'and dobList' checks if the variable is empty
            
            #date = int(dobList[0])
            if date < 1 or date > 31:
                print('The date must be between 1 and 31')
                continue

            #month = int(dobList[1])
            if month < 1 or month > 12:
                print('The month must be between 1 and 12')
                continue

            #year = int(dobList[2])
            if year < 1900 or year > 2100:
                print('Please enter a valid year')
                continue
            break #goal
                
        else:
            print('make sure you use the correct format dd/mm/yy')
            continue

    while True: #validates the password
        print('Please create a password using the following criteria:')
        print('-At least 5 characters \n-Contains letters and numbers/symbols')
        password = str(input(':')).strip()
        if len(password) >= 5 and password.isalpha() == False:
            break
        else:
            print('Invalid password')

    while True: #validates the favourite artist
        print('Please enter the full name of your favourite artist(Must be in the song library)')
        favouriteArtist = str(input(':')).lower()
        cursor.execute('''SELECT artist FROM songLibrary''')
        artists = []
        for row in cursor:
            artists.append(row[0].lower())

        if favouriteArtist in artists:
            break
        else:
            print('Unfortunately',favouriteArtist, 'isn\'t in the song library.')
            
    while True: #validates the favourite genre
        print('Please enter your favourite genre(Must be in the song library)')
        favouriteGenre = str(input(':')).lower()
        cursor.execute('''SELECT genre FROM songLibrary''')
        genres = []
        for row in cursor:
            genres.append(row[0].lower())

        if favouriteGenre in genres:
            break
        else:
            print('The genre', favouriteGenre, 'isn\'t in the song library.')
    
    cursor.execute('''INSERT INTO users(name, password, date, month, year, favouriteArtist, favouriteGenre, playlists)
                   VALUES (?, ?, ?, ?, ?, ?, ?, ?)''',  (name, password, date, month, year, favouriteArtist, favouriteGenre, '{}'))
    db.commit()
    print('You have successfully created an account')
    home()

        
#End of create_account()          
        

def login():
    #user login takes place here
    global name
    global admin
    print('\nLogin')
    print('------')
    print('Please enter your:')
    name = str(input('Username:'))
    password = str(input('Password:'))
    if name == 'admin' and password == '@dmiN':
        admin = True
        options()
    else:
        admin = False
        
    cursor.execute('''SELECT password FROM users WHERE name=?''', (name,))
    for row in cursor:
        if password == row[0]:
            options()
    else:
        print('Incorrect name or password\n')
        login()
#End of login()

    
def view_artists_and_genres():
    #This subroutine allows the user to view a list of all the artists and genres present in the song library
    #This is helpful for new users who aren't aware of the artists and genres supported on this platform.
    artists = []
    genres = []
    cursor.execute('''SELECT artist, genre FROM songLibrary ''')
    for row in cursor:
        if row[0] not in artists:
            artists.append(row[0])
            
        if row[1] not in genres:
            genres.append(row[1])
    print('\nArtists')
    print('-------')
    for x in artists:
        print(x)
    
    print('\nGenres')
    print('------')
    for x in genres:
        print(x)
    print()
    home()
#End of viewArtistsAndGenres

def options():
    #This subroutine allows the user to choose what they would like to do after logging in
    global name
    global admin
    print('\nMENU | Logged in as: ' + name)
    print('-----------------------------------')
    print('Would you like to:')
    print('1). View all songs in the song library')
    print('2). Manually create a playlist')
    print('3). Automatically create a playlist')
    print('4). View a playlist')
    print('5). View and save all songs made by an artist')
    print('6). Sign out')
    if admin:
        print('7). View Average song length of every genre')

    while True:
        try:
           choice = int(input(':'))
        except ValueError:
            print('You must enter a number')
            continue

        if choice == 1:
            view_song_library()
        elif choice == 2:
            create_playlist()
        elif choice == 3:
            generate_playlist()
        elif choice == 4:
            view_playlist()
        elif choice == 5:
            save_artist_song()
        elif choice == 6:
            home()
        elif choice == 7 and admin:
              average_song_length()
        else:
            print(str(choice) + ' isn\'t an option')
#End of options()

def edit_artist():
    #This subroutine allows the user to edit their favourite Artist
    global name
    #global cursor
    print('Change Favourite Artist | Logged in as: ' + name)
    print('-----------------------')
    while True: #validates the favourite artist
        print('Please enter the full name of your favourite artist(Must be in the song library)')
        favouriteArtist = str(input(':')).lower()
        cursor.execute('''SELECT artist FROM songLibrary''')
        artists = []
        for row in cursor:
            artists.append(row[0].lower())

        if favouriteArtist in artists:
            break
        else:
            print('Unfortunately',favouriteArtist, 'isn\'t in the song library.')
    cursor.execute('''UPDATE users SET favouriteArtist =? WHERE name=?''', (favouriteArtist, name,))

def edit_genre():
    #This subroutine allows the user toedit their favourite genre
    global name
    #global cursor
    print('Change Favourite genre | Logged in as: ' + name)
    while True: #validates the favourite genre
        print('Please enter your favourite genre(Must be in the song library)')
        favouriteGenre = str(input(':')).lower()
        cursor.execute('''SELECT genre FROM songLibrary''')
        genres = []
        for row in cursor:
            genres.append(row[0].lower())

        if favouriteGenre in genres:
            break
        else:
            print('Unfortunately',favouriteGenre, 'isn\'t in the song library.')
    cursor.execute('''UPDATE users SET favouriteGenre=? WHERE name=?''', (favouriteGenre, name,))    
    

def view_song_library():
    #This subroutine allows the user toview an alphabetical list of all the
    #songs in the song library
    global name
    print('View an alphabetical list of \nall the songs in the song library | Logged in as: ' + name)
    print('------------------------------------------')
    cursor.execute('''SELECT title, artist, length FROM songLibrary ORDER by title ASC''') 
    for row in cursor:
        minutes = str(row[2] // 60) + ':' + str(row[2] % 60)
        print(row[0], 'by', row[1], 'length:', minutes) 
    options()
    
    
def create_playlist():
    #This subroutine allows the user to create a playlist
    global name
    print('Create a playlist | Logged in as: ' + name)
    print('---------------------------------------------------')
    songId = [] #array to store the id of all the songs added to the playlits
    playlists = {}
    while True: #validates the newly created playlist name
        print('Enter the name of your playlist')
        playlistName = str(input(':'))
        cursor.execute('''SELECT playlists FROM users WHERE name=? ''', (name,)) #retrieves all playlists the user has created.
        for row in cursor:
            playlists = ast.literal_eval(row[0]) #used to make the dictionary be recognised as a dictionary not a string.
            
        if playlistName in playlists: #checks if the playlist name exists
            print('Playlist name taken')
            continue
        else:
            break
    
        
    
    while True: #validates the song being added
        print('Enter the name of the artist followed by the song name(separated by a comma and case sensitive) ')
        print('e.g. Clean Bandit, I Miss You')
        
        try:
            artistSong = str(input(':')).strip().split(',')
            songId.append(cursor.execute('''SELECT id FROM songLibrary WHERE artist=? AND title=? ''', (artistSong[0],artistSong[1].strip(),) ).fetchone()[0])
        except:
            print('Invalid Input, song is possibly not present in the song library')
            continue
            
        print('Would you like to add another song?')
        print('1). Yes')
        print('2). No')
        choice = int(input(':'))
        if choice == 1:
            continue
        elif choice == 2:
            break
        else:
            print('Invalid input')
            break

    playlists[playlistName] = songId
    cursor.execute('''UPDATE users SET playlists=? WHERE name=?''', (str(playlists), name,))
    db.commit()
    print('Playlist created successfully')
    
    options()
    

def view_playlist():
    #This subroutine allows the user to view all their playlists
    global name
    print('View a playlist | Logged in as: ' + name)
    print('------------------------------------------')
    print('Avaliable Playlists:')
    playlists = ast.literal_eval(cursor.execute('''SELECT playlists FROM users WHERE name=? ''', (name,)).fetchone()[0])
    for playlist in playlists:
        print(playlist)
    print('Enter the name of the playlist you would like to view')
    playlistName = str(input(':'))
    if playlistName in playlists:
        print('Songs in :' + playlistName)
        print('--------------------------')
        playlistArray = playlists[playlistName]
        for itemId in playlistArray:
            cursor.execute('''SELECT title, artist, length FROM songLibrary WHERE id=?''', (int(itemId),) )
            songInfo = cursor.fetchone()
            print(songInfo[0] + ' by ' + songInfo[1] + ' length: ' + str(songInfo[2] // 60) + ':' + str(songInfo[2] % 60))

    options()
        

def generate_playlist():
    #This subroutine allows the user to automatically generate a playlist based
    #on a certain criterea
    global name
    print('Automatically generate a playlist | Logged in as: ' + name)
    print('-----------------------------------------------------------------')
    print('Would you like to generate a playlist based on:')
    print('1). A specified length')
    print('2). A chosen genre')
    while True:
        try:
            choice = int(input(':'))
        except ValueError:
            print('Please enter a number')
            continue
        except:
            print('Invalid Input')
            continue
        
        if choice == 1:
            playlist_by_length()
        elif choice == 2:
            playlist_by_genre()
        else:
            print('Invalid input')
            continue

def playlist_by_length():
    global name
    print('Enter the length of the playlist you would like to create in minutes(at least 5 minutes)')
    while True: #validates the playlist length inputted 
        try:
            chosenLength = int(input(':')) * 60
            break
        except ValueError:
            print('Please enter a number')
            continue
        except:
            print('Invalid input')
            continue

    if chosenLength / 60 < 5:
        print('Playlist length must be at least 5 minutes')
        playlist_by_length()
    
    songId = [] #array to store the id of all the songs added to the playlits
    totalLength = 0
    playlists = {}
    while True: #validates the newly created playlist name
        print('Enter the name of your playlist')
        playlistName = str(input(':'))
        cursor.execute('''SELECT playlists FROM users WHERE name=? ''', (name,)) #retrieves all playlists the user has created.
        for row in cursor:
            playlists = ast.literal_eval(row[0]) #used to make the dictionary be recognised as a dictionary not a string.
            
        if playlistName in playlists: #checks if the playlist name exists
            print('Playlist name taken')
            continue
        else:
            break
    cursor.execute('''SELECT id,length FROM songLibrary ORDER BY length ASC ''')
        
    for row in cursor:
        if totalLength + row[1] <= chosenLength:
            songId.append(row[0])
            totalLength = totalLength + row[1]
        else:
            break
    playlists[playlistName] = songId
    cursor.execute('''UPDATE users SET playlists=? WHERE name=?''', (str(playlists), name,))
    db.commit()
    print(playlistName + ' created successfully')
    options()
    
def playlist_by_genre():
    global name
    counter = 0 #counter variable to store the amount of songs added to the playlist
    while True: #validates the genre entered
        print('Enter the genre you would like to create a playlist for(must be in the song library)')
        chosenGenre = str(input(':')).lower()
        cursor.execute('''SELECT genre FROM songLibrary''')
        genres = []
        for row in cursor:
            genres.append(row[0].lower())

        if chosenGenre in genres:
            break
        else:
            print('Unfortunately',chosenGenre, 'isn\'t in the song library.')
            continue
    
    songId = [] #array to store the id of all the songs added to the playlits
    playlists = {}
    while True: #validates the newly created playlist name
        print('Enter the name of your playlist')
        playlistName = str(input(':'))
        cursor.execute('''SELECT playlists FROM users WHERE name=? ''', (name,)) #retrieves all playlists the user has created.
        for row in cursor:
            playlists = ast.literal_eval(row[0]) #used to make the dictionary be recognised as a dictionary not a string.
            
        if playlistName in playlists: #checks if the playlist name exists
            print('Playlist name taken')
            continue
        else:
            break

    
    cursor.execute('''SELECT id FROM songLibrary WHERE genre=? ''', (chosenGenre,))
    for row in cursor:
        if counter < 5:
            songId.append(row[0])
        else:
            break
        counter = counter + 1
    playlists[playlistName] = songId
    cursor.execute('''UPDATE users SET playlists=? WHERE name=? ''', (str(playlists), name,))
    print(playlistName + ' created successfully')
    options()
    

def save_artist_song():
    #This subroutine allows the user to save all songs by a specific artist to a text file
    global name
    print('Save all songs made by an artist | Logged in as: ' + name)
    print('--------------------------------------------------------------')
    print('Enter an artist name(Case sensitive)')
    artistsInLibrary = []
    songsByArtist = []
    while True:#firstly check if the artist is in the song library
        chosenArtist = str(input(':'))
        cursor.execute('''SELECT artist FROM songLibrary''')
        for row in cursor:
            artistsInLibrary.append(str(row[0]))
        if chosenArtist in artistsInLibrary:
            break
        else:
            print('Unfortunately',chosenArtist, 'isn\'t in the song library.')
            
    #then find all the songs made by that artist
    cursor.execute('''SELECT title FROM songLibrary WHERE artist=?''', (chosenArtist,))
    for row in cursor:
        if str(row[0]).lower() not in songsByArtist:
            songsByArtist.append(str(row[0]))
               
    file = open(chosenArtist + '.txt', 'w')
        
    print('The song/s made by ' + chosenArtist + ' are:')
    print('-------------------------------')
    for song in songsByArtist:
        print(song)
        file.write(song + '\n')
    file.close()

    options()
            

    
def average_song_length():
    #This subroutine allows the creators of OCRTunes to view the average length of all the songs in every genre
    global name 
    print('Average song length in each genre | Logged in as: ' + name)
    print('--------------------------------------------------------------')

    genres = []
    cursor.execute('''SELECT genre FROM songLibrary''')
    for row in cursor:
        if row[0] not in genres:
            genres.append(row[0])

    for genre in genres:

        length = 0
        totalSongs = 0
        cursor.execute('''SELECT length FROM songLibrary WHERE genre=? ''', (genre,))
        for row in cursor:
            length = length + row[0]
            totalSongs = totalSongs + 1
        mean = length // totalSongs
        meanInMinutes = str(mean // 60) + ':' + str(mean % 60)
        print('Genre: ' + genre + ' Length: ' + meanInMinutes) #average length of songs in genre
        
print('Welcome to ')
print('     ____     _____   _____      _______                              ')
print('    / __ \   / ____| |  __ \    |__   __|                             ')
print('   | |  | | | |      | |__) |      | |     _   _   _ __     ___   ___ ')
print('   | |  | | | |      |  _  /       | |    | | | | | \'_ \   / _ \ / __| ')
print('   | |__| | | |____  | | \ \       | |    | |_| | | | | | |  __/ \__ \ ')
print('    \____/   \_____| |_|  \_\      |_|     \__,_| |_| |_|  \___| |___/ \n')
#Font sourced from http://patorjk.com/software/taag
print('The industry leading online music streaming service :) \n')   

home()

