from flask import Flask, request, redirect, render_template
from datetime import datetime
from random import randrange

class App(Flask):
    def __init__(self):
        super().__init__(__name__)

        self.posts = []
        self.ids = []

        self.add_url_rule('/', 'index', self.index)
        self.add_url_rule('/create', 'create', self.create)
        self.add_url_rule('/delete/', 'delete', self.delete)

    def index(self):
        return render_template('index.html', todo_posts = self.posts)

    def create(self):
        post_content = request.args.get('content')
        now = datetime.now()
        date_created = f'{now.day}-{now.month}-{now.year} {now.hour}:{now.minute}:{now.second}'
        id = randrange(1, 501)
        while id in self.ids:
            id = randrange(1, 501)
        self.ids.append(id)
        print(self.ids)

        self.posts.append({
            'content': post_content,
            'date-created': date_created,
            'id': id
        })

        return redirect('/')

    def delete(self):
        id = request.args.get('id')
        try:
            id = int(id)
            del self.ids[self.ids.index(id)]
            for i, j in enumerate(self.posts):
                if j['id'] == id:
                    index = i
            del self.posts[index]
        except Exception as e:
            print(e)
            return f'<h2>Error</h2><p>id {id} is not a valid id.</p>'
        return redirect('/')

if __name__ == '__main__':
    App().run(host = '127.0.0.1', port = 5000)
