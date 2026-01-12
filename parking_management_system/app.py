from flask import Flask, render_template, request, redirect, url_for, flash
import uuid
import datetime
import mysql.connector

app = Flask(__name__)
app.secret_key = 'secret-key'

# Function to get fresh DB connection and cursor
def get_db_connection():
    conn = mysql.connector.connect(
        host="localhost",
        user="USER",
        password="PASSWORD",
        database="DB_NAME"
    )
    return conn, conn.cursor()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/enter', methods=['GET', 'POST'])
def enter():
    if request.method == 'POST':
        car_type = request.form['car_type']
        car_no = request.form['car_no']
        unique_code = str(uuid.uuid4())[:8]
        entry_time = datetime.datetime.now()

        db, cursor = get_db_connection()
        try:
            # Check if the car is already parked
            cursor.execute("""
                SELECT id FROM ParkingRecords
                WHERE car_no = %s AND exit_time IS NULL
            """, (car_no,))
            existing = cursor.fetchone()

            if existing:
                flash("This car is already parked. Please exit before entering again.", "error")
                return redirect(url_for('enter'))

            # Insert new entry
            cursor.execute("""
                INSERT INTO ParkingRecords (car_no, car_type, unique_code, entry_time)
                VALUES (%s, %s, %s, %s)
            """, (car_no, car_type, unique_code, entry_time))
            db.commit()
        except mysql.connector.Error as err:
            flash(f"Database Error: {str(err)}", "error")
            return redirect(url_for('enter'))
        finally:
            cursor.close()
            db.close()

        return render_template('entry_result.html', unique_code=unique_code)
    return render_template('enter.html')

@app.route('/exit', methods=['GET', 'POST'])
def exit():
    if request.method == 'POST':
        car_no = request.form['car_no']
        unique_code = request.form['unique_code']
        exit_time = datetime.datetime.now()

        db, cursor = get_db_connection()
        try:
            cursor.execute("""
                SELECT id, entry_time FROM ParkingRecords 
                WHERE car_no = %s AND unique_code = %s AND exit_time IS NULL
            """, (car_no, unique_code))
            result = cursor.fetchone()

            if result:
                car_id, entry_time = result
                duration = (exit_time - entry_time).seconds // 60
                charge = duration * 2

                cursor.execute("""
                    UPDATE ParkingRecords
                    SET exit_time = %s, charge = %s
                    WHERE id = %s
                """, (exit_time, charge, car_id))
                db.commit()
                return render_template('exit_result.html', duration=duration, charge=charge)
            else:
                flash("Invalid Car Number or Unique Code.", "error")
                return redirect(url_for('exit'))
        except mysql.connector.Error as err:
            flash(f"Database error: {err}", "error")
            return redirect(url_for('exit'))
        finally:
            cursor.close()
            db.close()
    return render_template('exit.html')

if __name__ == '__main__':
    app.run(port = 5000, debug=True)

