from flask import Flask, render_template, request, redirect, url_for, flash
from app import app, mysql

@app.route('/')
def home():
    cur = mysql.connection.cursor()
    cur.execute("SELECT  * FROM studentsdata")
    data = cur.fetchall()
    cur.close()


    return render_template('index.html', studentsdata=data )



@app.route('/insert', methods = ['POST'])
def insert():

    if request.method == "POST":
        flash("Data Saved Successfully")
        id_number = request.form['id_number']
        fname = request.form['fname']
        lname = request.form['lname']
        gender = request.form['gender']
        age = request.form['age']
        year = request.form['year']
        college = request.form['college']
        department = request.form['department']
        course = request.form['course']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO studentsdata (id_number, fname, lname, gender, age, year, college, department, course) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)", (id_number, fname, lname, gender, age, year, college, department, course))
        cur.execute("INSERT INTO collegedata (id_number,college, department, course) VALUES (%s, %s,%s,%s)", (id_number, college, department, course))
        mysql.connection.commit()
        return redirect(url_for('home'))


@app.route('/delete/<string:id_number>', methods = ['GET'])
def delete(id_number):
    flash("Student Record Has Been Deleted Successfully")
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM studentsdata WHERE id_number=%s", (id_number,))
    cur.execute("DELETE FROM collegedata WHERE id_number=%s", (id_number,))
    mysql.connection.commit()
    return redirect(url_for('home'))





@app.route('/update',methods=['POST'])
def update():

    if request.method == 'POST':
        id_number = request.form['id_number']
        fname = request.form['fname']
        lname = request.form['lname']
        
        age = request.form['age']
        year = request.form['year']
        college = request.form['college']
        department = request.form['department']
        course = request.form['course']
        cur = mysql.connection.cursor()
        cur.execute("""
               UPDATE studentsdata
               SET fname=%s, lname=%s, age=%s, year=%s, college=%s, department=%s, course=%s
               WHERE id_number=%s
            """, (fname, lname, age, year, college, department, course, id_number))
        cur.execute("""
               UPDATE collegedata
               SET college=%s, department=%s, course=%s
               WHERE id_number=%s
            """, (college, department, course, id_number))
        flash("Data Updated Successfully")
        mysql.connection.commit()
        return redirect(url_for('home'))


@app.route('/search', methods=['POST','GET'])
def search():

    if request.method == 'POST':
        search = request.form['search']
        cur = mysql.connection.cursor()
        cur.execute("""SELECT * FROM studentsdata WHERE id_number=%s or fname=%s or lname=%s or gender=%s or age=%s or college=%s or department=%s or course=%s """,
            (search,search,search,search,search,search,search,search));
        searchData = cur.fetchall()
        cur.close()
        return render_template('index.html',studentsdata=searchData)



@app.route('/list')
def list():

    cur = mysql.connection.cursor()
    cur.execute("SELECT  * FROM schooldata")
    data3 = cur.fetchall()
    cur.close()

    return render_template('list.html', schooldata=data3)


@app.route('/sorted')
def sorted():
    return render_template('sorted.html')

@app.route('/coet')
def coet():
    return render_template('coet.html')

@app.route('/chemical engineering and technology department')
def chemEng():
    return render_template('chemEng.html')

@app.route('/electrical and electronics engineering and technology department')
def elecEng():
    return render_template('elecdept.html')

@app.route('/mechanical engineering and technology department')
def mechEng():
    return render_template('mechanicalEng.html')

@app.route('/civil engineering department')
def civilEng():
    return render_template('civilEng.html')

@app.route('/materials and resources engineering and technology department')
def materialsEng():
    return render_template('materialsEng.html')

@app.route('/COET Graduate Programs Department')
def gradcoet():
    return render_template('gradcoet.html')


@app.route('/cass')
def cass():
    return render_template('cass.html')

@app.route('/Psychology Department')
def psych():
    return render_template('psych.html')

@app.route('/English Department')
def english():
    return render_template('english.html')

@app.route('/Departamento ng Filipino at ibang mga Wika')
def filipino():
    return render_template('filipino.html')

@app.route('/History Department')
def history():
    return render_template('history.html')

@app.route('/Political Science Department')
def polsci():
    return render_template('polsci.html')

@app.route('/Sociology Department')
def sociology():
    return render_template('sociology.html')

@app.route('/Philosophy and Humanities Department')
def philosophy():
    return render_template('philosophy.html')

@app.route('/CASS Graduate Programs')
def gradcass():
    return render_template('gradcass.html')

@app.route('/csm')
def csm():
    return render_template('csm.html')

@app.route('/Biological Sciences Department')
def biology():
    return render_template('biology.html')

@app.route('/Mathematics and Statistics Department')
def mathstat():
    return render_template('mathstat.html')

@app.route('/Chemistry Department')
def chem():
    return render_template('chem.html')

@app.route('/Physics Department')
def physics():
    return render_template('physics.html')

@app.route('/CSM Graduate Programs Department')
def gradcsm():
    return render_template('gradcsm.html')

@app.route('/ccs')
def ccs():
    return render_template('ccs.html')

@app.route('/Computer Science Department')
def comsci():
    return render_template('comsci.html')

@app.route('/Information Technology Department')
def itdept():
    return render_template('itdept.html')

@app.route('/Computer Applications Department')
def comapp():
    return render_template('comapp.html')

@app.route('/CCS Graduate Programs Department')
def gradccs():
    return render_template('gradccs.html')

@app.route('/cbaa')
def cbaa():
    return render_template('cbaa.html')

@app.route('/Accountancy Department')
def accountancy():
    return render_template('accountancy.html')

@app.route('/Economics Department')
def economics():
    return render_template('economics.html')

@app.route('/Marketing Department')
def marketing():
    return render_template('marketing.html')

@app.route('/Hospitality and Tourism Management Department')
def hospitalityAndTourism():
    return render_template('hospitality.html')

@app.route('/CBAA Graduate Programs Department')
def gradcbaa():
    return render_template('gradcbaa.html')

@app.route('/ced')
def ced():
    return render_template('ced.html')

@app.route('/Science and Mathematics Education Department')
def scimath():
    return render_template('scimath.html')

@app.route('/Physical Education Department')
def pe():
    return render_template('pe.html')

@app.route('/CED Graduate Programs Department')
def gradced():
    return render_template('gradced.html')

@app.route('/Professional Education Department')
def ped():
    return render_template('ped.html')

@app.route('/Technology Teacher Education Department')
def tted():
    return render_template('tted.html')

@app.route('/con')
def con():
    return render_template('colnur.html')

@app.route('/Nursing Department')
def nursing():
    return render_template('nursing.html')


@app.route('/searchlist', methods=['POST','GET'])
def searchlist():

    if request.method == 'POST':
        searchlist = request.form['searchlist']
        cur = mysql.connection.cursor()
        cur.execute("""SELECT * FROM schooldata WHERE college=%s or department=%s or course=%s""",
            (searchlist,searchlist, searchlist));
        searchData2 = cur.fetchall()
        cur.close()
        return render_template('list.html',schooldata=searchData2)