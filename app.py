from flask import Flask, render_template, request
from datetime import datetime, timedelta

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        pags = int(request.form['pages'])
        dias = int(request.form['days'])
        comeco = int(request.form['startDay'])
        mes = int(request.form['startMonth'])

        today = datetime.today()
        inicio = datetime(today.year, mes, comeco)
        final = inicio + timedelta(days=dias-1)

        pags_dia = (pags // dias) + (1 if pags % dias else 0)

        lista = []
        pag_atual = 0
        for d in range(dias):
            data_atual = inicio + timedelta(days=d)
            pag_atual += pags_dia
            if pag_atual > pags:
                pag_atual = pags
            lista.append({
                'date': data_atual.strftime('%d/%m/%Y'),
                'page': pag_atual
            })

        return render_template('table.html',
                               inicio=inicio.strftime('%d/%m/%Y'),
                               final=final.strftime('%d/%m/%Y'),
                               dias=dias,
                               pags_dia=pags_dia,
                               lista=lista)

    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)
