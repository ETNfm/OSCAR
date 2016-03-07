SOURCES:
https://en.wikipedia.org/wiki/Levenshtein_distance




SELECT user_id,
       show_id,
       name,
       type,
       display_name,
       day,
       time,
       frequency
FROM shows
JOIN shows_users ON shows.id = shows_users.show_id
JOIN users on shows_users.user_id = users.id\G





*************************** 183. row ***************************
     user_id: 6630
     show_id: 774
        name: The Noble Gathering
        type: Trance
     user_id: 6630
     show_id: 774
display_name: The Noble Six
         day: 3
        time: 13:00:00
   frequency: 1
*************************** 184. row ***************************
     user_id: 6631
     show_id: 775
        name: This Is Waves
        type: Trance
     user_id: 6631
     show_id: 775
display_name: Eich
         day: 2
        time: 14:00:00
   frequency: 2
*************************** 185. row ***************************
     user_id: 6633
     show_id: 776
        name: Trance Only
        type: Trance
     user_id: 6633
     show_id: 776
display_name: 9Axis
         day: 3
        time: 14:00:00
   frequency: 0
*************************** 186. row ***************************
     user_id: 6633
     show_id: 777
        name: Entrance to Soul
        type: Trance
     user_id: 6633
     show_id: 777
display_name: 9Axis
         day: 5
        time: 14:00:00
   frequency: 4
186 rows in set (0.00 sec)






*************************************************************************************
*************************************************************************************

SELECT user_id, show_id, name, type, user_id, show_id, display_name, day, time, frequency
FROM shows
JOIN shows_users ON shows.id = shows_users.show_id
JOIN users on shows_users.user_id = users.id
WHERE type = 'House'
ORDER BY frequency DESC\G

*************************** 126. row ***************************
     user_id: 6623
     show_id: 765
        name: Subterranean Sessions
        type: House
     user_id: 6623
     show_id: 765
display_name: Chris Pfaff
         day: 2
        time: 22:00:00
   frequency: 0
*************************** 127. row ***************************
     user_id: 452
     show_id: 420
        name: Reverend Chachi @ Dizzy Bitch Recordings
        type: House
     user_id: 452
     show_id: 420
display_name: MT Chachi
         day: 3
        time: 16:00:00
   frequency: 0
*************************** 128. row ***************************
     user_id: 6626
     show_id: 768
        name: TheRemixLabel
        type: House
     user_id: 6626
     show_id: 768
display_name: Cristian Paduraru
         day: 5
        time: 12:00:00
   frequency: 0
128 rows in set (0.00 sec)

