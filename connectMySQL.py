import MySQLdb

try:
    conn = MySQLdb.connect(host='localhost', user='root', passwd='', port=3306)
    cur = conn.cursor()

    # cur.execute('create database if not exists python')
    conn.select_db('python')
    # cur.execute('create table test(id int,info varchar(20))')

    value = [1, 'hi rollen']
    cur.execute('insert into test values(%s,%s)', value)
    '''
    values=[]
    for i in range(20):
        values.append((i,'hi rollen'+str(i)))
         
    cur.executemany('insert into test values(%s,%s)',values)
 
    cur.execute('update test set info="I am rollen" where id=3')
    '''
    conn.commit()
    cur.close()
    conn.close()
    print 'insert success'

except MySQLdb.Error, e:
    print "Mysql Error %d: %s" % (e.args[0], e.args[1])



# create table novel(id int unsigned not null auto_increment primary key,title char(100) not null,link text, author char(30) ,nums int unsigned ,category char(20) ,update_time int unsigned ,section text);
