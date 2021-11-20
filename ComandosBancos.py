from BancoDados import Banco

class Usuarios(object):


  def __init__(self, parceiro = "", senha = "", usuario = "",
  filial = ""):
    self.info = {}
    #self.idusuario = idusuario
    self.parceiro = parceiro
    self.senha = senha
    self.usuario = usuario
    self.filial = filial
    #self.usuario = usuario
    #self.senha = senha


  def insertUser(self):

    banco = Banco()
    try:
      c = banco.conexao.cursor()

      c.execute("insert into lojas (parceiro, senha, usuario, filial) values ('" +
      self.parceiro + "', '" + self.senha + "', '" +
      self.usuario + "', '" + self.filial + "' )")

      banco.conexao.commit()
      c.close()

      return "Usuário cadastrado com sucesso!"
    except:
      return "Ocorreu um erro na inserção do usuário"

  def updateUser(self):

    banco = Banco()
    try:

        c = banco.conexao.cursor()

        c.execute("update lojas set parceiro = '" + self.parceiro + "',  senha = '" + self.senha + "', usuario = '" + self.usuario +
        "', filial = '" + self.filial + " ")

        banco.conexao.commit()
        c.close()

        return "Usuário atualizado com sucesso!"
    except:
        return "Ocorreu um erro na alteração do usuário"

  def deleteUser(self):

    banco = Banco()
    try:

        c = banco.conexao.cursor()

        c.execute("delete from lojas where placa = '" + self.placa + "' ")

        banco.conexao.commit()
        c.close()

        return "Usuário excluído com sucesso!"
    except:
        return "Ocorreu um erro na exclusão do usuário"

  def selectUser(self, parceiro):
    banco = Banco()
    try:

        c = banco.conexao.cursor()

        c.execute("select * from lojas where placa = '" + placa + "' ")

        for linha in c:
            self.placa = linha[0]
            self.modelo = linha[1]
            self.cor = linha[2]
            self.ano = linha[3]
            #self.usuario = linha[4]
            #self.senha = linha[5]

        c.close()

        return "Busca feita com sucesso!"
    except:
        return "Ocorreu um erro na busca do usuário"
