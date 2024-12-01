# -*- coding: utf-8 -*-
"""
Created on Mon Nov 25 17:19:14 2024

@author: Bruno O. e Enzo C.
"""

class Library(object):
    """Tentativa de criar uma biblioteca"""
    
    def __init__(self):
        """Criar uma lista sem elementos"""
        self.livros = {}
        self.livros_emprestados = {}
            
    def getBooks(self):
        """Mostrar quais livros estão na biblioteca"""
        livros_disponíveis = [livro for livro, disponível in self.livros if disponível = True]
        for livro in Library().livros:
            print(Library().livros[livro])
                    
    def add_Book(self, livro):
        """Adicionar livros na biblioteca"""
        self.livros[livro] = True
        print('O livro "' + livro + ' "foi adicionado na biblioteca!')
        print(Library().livros)
        
    def remove_Book(self, livro):
        """Remover livros da biblioteca"""
        print("Livro {} removido da biblioteca!".format(livro))
        if livro in self.livros:
            self.livros.remove(livro)
            print(Library().livros_emprestados)
        else:
            print('O livro {} não está na biblioteca!'.format(livro))
    
    def borrow_Book(self, livro, nome):
        """Emprestar um livro da biblioteca"""
        if livro in Library().livros and Library().livros[livro]:
            print('O usuario {:1} está emprestando o livro {:2} da biblioteca!'.format(nome, livro))
            self.livros[livro] = False
            self.livros_emprestados.append(livro)
            
            
        
class User(object):
    """Usuários para interagir com a biblioteca"""
    
    def __init__(self, nome):
        """Criar uma lista para registrar usuários"""
        self.user = nome
        self.emprestados = []
    
    def borrow(self, livro, Library):
        """Emprestar um livro da biblioteca"""
        print("Emprestando o livro {}!".format(livro))
        Library.borrow_Book(self, livro, User().user)
        self.emprestados.append(livro)
        
    
l = Library()
l.getBooks()
l.add_Book("To Kill a Mockingbird")
l.getBooks()
l.add_Book("1984")
l.getBooks()
"""u = User("Bob")
print(u.user)
u.borrow("To Kill a Mockingbird", Library)"""
