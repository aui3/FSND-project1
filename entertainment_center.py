import media
import fresh_tomatoes

#set up movie information
national_treasure = media.Movie ("National Treasure","Cage plays Benjamin Franklin Gates, a historian and amateur cryptologist searching for a lost treasure of precious metals, jewelry, artwork and other artifacts that was accumulated into a single massive stockpile by looters and warriors over many millennia starting in Ancient Egypt, later rediscovered by warriors who form themselves into the Knights Templar to protect the treasure, eventually hidden by American Freemasons during the American Revolutionary War.", "http://upload.wikimedia.org/wikipedia/en/1/12/Movie_national_treasure.JPG","https://www.youtube.com/watch?v=mcf4tXYjaxo", 2000)

kings_speech = media.Movie ("The King's Speech", "The King's Speech is a 2010 British historical drama film directed by Tom Hooper and written by David Seidler. Colin Firth plays King George VI who, to cope with a stammer, sees Lionel Logue, an Australian speech and language therapist played by Geoffrey Rush. The men become friends as they work together, and after his brother abdicates the throne, the new King relies on Logue to help him make his first wartime radio broadcast on Britain's declaration of war on Germany in 1939.", "http://upload.wikimedia.org/wikipedia/en/a/a0/Kings_speech_ver3.jpg","https://www.youtube.com/watch?v=pzI4D6dyp_o", 2010)

the_judge = media.Movie ("The Judge", "The Judge is a 2014 American drama film directed by David Dobkin. The film stars Robert Downey, Jr., Robert Duvall, Vera Farmiga, Vincent D'Onofrio, Jeremy Strong, Dax Shepard, and Billy Bob Thornton. The film was released in the United States on October 10, 2014. It received mixed reviews; critics praised the performances of Downey and Duvall and Thomas Newman's score, but criticized the formulaic nature of its script and the lack of development for its supporting characters.", "http://upload.wikimedia.org/wikipedia/en/6/61/The_Judge_2014_film_poster.jpg","https://www.youtube.com/watch?v=ZBvK6ni97W8", 2014)

imitation_game = media.Movie ("The Imitation Game", "The Imitation Game is a 2014 historical thriller film directed by Morten Tyldum, with a screenplay by Graham Moore loosely based on the biography Alan Turing: The Enigma by Andrew Hodges. It stars Benedict Cumberbatch as the British cryptanalyst Alan Turing, who helped solve the Enigma code during the Second World War and was later prosecuted for homosexuality.", "http://upload.wikimedia.org/wikipedia/en/5/5e/The_Imitation_Game_poster.jpg","https://www.youtube.com/watch?v=ZRzZX2aN3I0", 2008)

twenty_one = media.Movie ("Twenty One", "21 is a 2008 American heist drama film directed by Robert Luketic and stars Jim Sturgess, Kevin Spacey, Laurence Fishburne, Kate Bosworth, Liza Lapira, Jacob Pitts, and Aaron Yoo. The film is inspired by the true story of the MIT Blackjack Team as told in Bringing Down the House, the best-selling book by Ben Mezrich.", "http://upload.wikimedia.org/wikipedia/en/a/a8/21_%282008_film%29.jpg","https://www.youtube.com/watch?v=mcf4tXYjaxo", 2000)

#array of movie names
movies = [national_treasure , kings_speech , the_judge , imitation_game , twenty_one]
fresh_tomatoes.open_movies_page(movies);
