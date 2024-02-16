import web

render = web.template.render('views/')

class Index:
    def GET(self):
        return render.index()

    def POST(self):
        form = web.input()
        num1 = int(form.num1)
        num2 = int(form.num2)
        try:
            suma = num1 + num2
            return render.resultado(suma)
        except Exception as e:
            print(f'Error 101 - index {e.args}')
