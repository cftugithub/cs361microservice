## cs361microservice
This program will read a list of job applicants from "applicants.csv" and then provide an output CSV file based on a request from another program. The user can request either a certain number of applicants of any profession, or a certain number of applicants for a specific profession.<br>

The output CSV file will contain the applicant name, email, profession, resume and cover letter.


### Requesting Data
To request data, write the request to the "request.txt" file.

#### Requesting a number of applicants of any type
To request a certain number of applicants, write "get {x}" where x is the number of applicants.<br>

For example, "get 5" will return 5 applicants.<br>

If the number requested is greater than the number of available applicants, all applicants will be returned.

#### Requesting a number of applicants of a specific type
To request a certain number of applicants of a specific type, write "get {x} {type}" where "x" is the number of applicants and "type" is the type of applicant.<br>

For example, "get 5 Detective" will return 5 applicants with Detective as their profession.<br>

If the number requested is greater than the number of available applicants, all applicants will be returned.




### Receiving Data
The requested output will be written to the "output.csv" file.

#### Sample output
##### get 5
name,email,profession,resume,cover_letter<br>
Chie Satonaka,chie.satonaka@email.com,Kung-Fu Martial Artist,4 years martial arts experience.,I am a very good martial artist.<br>
Yosuke Hanamura,yosuke.hanamura@email.com,Store Employee,3 years retail experience.,I am a very good store employee.<br>
Naoto Shirogane,naoto.shirogane@email.com,Detective,2 years experience detecting.,I’m a great detective.<br>
Yukiko Amagi,yukiko.amagi@email.com,Inn Owner,10 years experience with hospitality.,I am a very good inn manager.<br>
Rise Kujikawa,rise.kujikawa@email.com,Idol Singer,5 years experience singing.,I am a very good singer.<br>

##### get 5 Handyman
name,email,profession,resume,cover_letter<br>
John Adams,john.adams@email.com,Handyman,10 years experience repairing appliances.,I am very good at fixing things.<br>


### Diagram
![Blank diagram](https://user-images.githubusercontent.com/85588796/199160677-c2d9864a-1ad9-46cc-ac8e-1af993880c8b.png)


