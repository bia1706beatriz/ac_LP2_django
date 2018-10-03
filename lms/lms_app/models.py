from django.db import models
from lms_app.professor import *
from lms_app.disciplina import *
from lms_app.disciofertada import *
from lms_app.aluno import *

'''
class Professor(models.Model):
    def __str__(self):
        return self.nome +self.email

    def save(self):
        #print('estou salvando!')
        if(self.login == ''):
            raise Exception('login nao enviado')

        if (self.email == ''):
            self.email = 'email nao fornecido'
        
        if(len(Professor.objects.filter(login = self.login)) > 0):
            raise Exception('login ja utilizado')


        super(Professor,self).save()

    nome = models.TextField(max_length=255)
    email = models.TextField(max_length=255)
    celular = models.TextField(max_length=20)
    login = models.TextField(max_length=20)
    senha = models.TextField(max_length=20)



class Disciplina(models.Model):
    def __str__(self):
        return self.ementa + " "+self.nome

    def save(self):
        if (len(Disciplina.objects.filter(nome = self.nome)) >=1):
                raise Exception('')
        super(Disciplina,self).save()

    nome = models.TextField(max_length=50)
    ementa = models.TextField(max_length=5000)

class DisciplinaOfertada(models.Model):
    def __str__(self):
        return self.curso

    def save(self):
        if self.curso not in ['ADS', 'SI', 'BD']:
            raise Exception('')
        if (len(DisciplinaOfertada.objects.filter(ano=self.ano ,semestre=self.semestre, turma=self.turma, curso=self.curso , disciplina=self.disciplina)) >=1):
            raise Exception("")
        if self.professor != self.disciplina:
            raise Exception("")

        super(DisciplinaOfertada,self).save()

    curso = models.TextField(max_length=255)
    turma = models.TextField(max_length=5)
    ano = models.IntegerField() #um inteiro, representa um ano
    semestre = models.IntegerField() #um inteiro, 1 para primeiro sem e 2 para segundo
    professor = models.IntegerField() #id de um professor valido
    disciplina = models.IntegerField() #id de uma disciplina valida

'''