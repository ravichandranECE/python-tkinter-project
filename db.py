import sqlite3

class database:
    def __init__(self,db):
        self.con=sqlite3.connect(db)
        self.cur=self.con.cursor()
        sql="""
        CREATE TABLE IF NOT EXISTS employees(
            id integer primary key,
            name text,
            age text,
            dept text,
            clg text
        )
        """
        self.cur.execute(sql)
        self.con.commit()

        #insert funt
    def insert(self,name,age,department,clg):
        self.cur.execute("insert into employees values(NULL,?,?,?,?)",
                         (name,age,department,clg))
        self.con.commit()

#fetch fun
    def fetch(self):
        self.cur.execute("SELECT * from employees")
        rows=self.cur.fetchall()
        #print(rows)
        return rows
# delete funt
    def remove(self,id):
        self.cur.execute("delete from employees where id=?",
                         (id,))
        self.con.commit()

    def update(self, id, name, age, dept, clg):
        self.cur.execute("update employees set name=?, age=?, dept=?, clg=? where id=?",
                         (name, age, dept, clg, id))
        self.con.commit()

#upd  ate funct



o = database("employees.db")

#o.insert("ravi", "21", "ece", "ssm")
#o.fetch()
#o.remove("8")
o.update("1","ram", "21","tdctgj", "tdhyf")