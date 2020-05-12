
import mysql.connector



con= mysql.connector.connect(
        
        user= 'ardit700_student',
        password = 'ardit700_student',
        host= '108.167.140.122',
        database = 'ardit700_pm1database'
        )

cursor = con.cursor()

word= input('Enter the word you wnat to know meaning of : ')
query= cursor.execute("SELECT * FROM Dictionary WHERE Expression = '%s'" % word)
results = cursor.fetchall()



if results:
    for item in results:
        print(item[1])
else:
    print('No results found')
  
