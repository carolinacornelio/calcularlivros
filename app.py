from flask import Flask, render_template, request
from datetime import datetime, timedelta

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        pages = int(request.form['pages'])
        days = int(request.form['days'])
        start_day = int(request.form['startDay'])
        
        today = datetime.today()
        start_date = datetime(today.year, today.month, start_day)
        end_date = start_date + timedelta(days=days-1)
        
        pags_dia = (pages // days) + (1 if pages % days else 0)
        
        reading_schedule = []
        current_page = 0
        for d in range(days):
            current_date = start_date + timedelta(days=d)
            current_page += pags_dia
            if current_page > pages:
                current_page = pages
            reading_schedule.append({
                'date': current_date.strftime('%d/%m/%Y'),
                'page': current_page
            })
        
        return render_template('index.html', 
                               start_date=start_date.strftime('%d/%m/%Y'), 
                               end_date=end_date.strftime('%d/%m/%Y'), 
                               days=days, 
                               pags_dia=pags_dia, 
                               reading_schedule=reading_schedule)
    
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)