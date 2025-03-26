class person:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def display_info(self):
        print(f"Nome: {self.nome}, Idade: {self.idade}")


class Student(person):
    def __init__(self, nome, idade, curso):
        super().__init__(nome, idade)
        self.curso = curso

    def display_info(self):
       print(f'Nome: {self.nome}, Idade: {self.idade}, Curso: {self.curso}')



p = person("João", 30)
p.display_info()

s = Student("Maria", 20, "Engenharia")
s.display_info()




