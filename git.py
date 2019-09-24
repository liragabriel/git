<<<<<<< HEAD
#--------------------------------------------
#
# API -> https://github.com/PyGithub/PyGithub
#
#           by Gabriel Lira @ 2019
#
#--------------------------------------------
=======
"""
    API -> https://github.com/PyGithub/PyGithub
               Gabriel Lira © 2019
"""
>>>>>>> b3d0082cc5c94274bd1e0f4a1fa30769f7f9f65e

from github import Github
from flask import Flask, render_template

app = Flask(__name__)

class Git:

    def __init__(self, username, password):

        self.username = username
        self.password = password

    #-----------------------------------------
    # Retorna todos os repositórios do usuário
    #-----------------------------------------
    def lista_repositorios(self):

        g = Github(self.username, self.password)

        for repo in g.get_user().get_repos():
            print(repo.name)

    #------------------------------------------------
    # Retorna todos os arquivos dentro do repositório
    #------------------------------------------------
    def arquivos_repositorio(self, repo):

        g = Github(self.username, self.password)
        r = g.get_repo(self.username+'/'+repo)

        contents = r.get_contents('')
        while len(contents) > 1:
            file_content = contents.pop(0)
            if file_content.type == 'dir':
                contents.extend(r.get_contents(file_content.path))
            else:
                print(file_content)

""" Rotas """

@app.route('/')
def inicio():
    return render_template('test.html')

if __name__ == '__main__':
    app.run(debug=True)
