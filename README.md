#       O sistema de academia a seguir, serve para gerenciamento de alunos e professores de uma certa academia,
#   ele tem a opção de cadastrar aluno, professores e admins. Apenas o admin pode ver, cadastrar e editar professores e alunos.
#   quando um aluno é cadastrado o admin pode matriculado em um esporte e adicionar ou não um professor a ele. quando um professor
#   é cadastrado, ele ganha um 'usuario" e "senha" e pode fazer login em uma interface exclusiva para professores, nela ele pode ver
#    seus alunos e adicionar um treino para cada, o professor também pode fazer a edição de seu perfil de professor.
#   
#       Esse programa foi desenvolvido com um banco de dado postgress em um servidor localhost, para seu funcionamento deve ser criado
#   o mesmo em sua máquina local e editar a classe "config" no arquivo db.py. Nessa mesma pasta há o arquivo academia.sql ele deve ser usado
#   para criar o database
#
#   O arquivo Main faz toda a aplicação rodar
#
#   usuario inicial: "usuario": admin, "senha": admin