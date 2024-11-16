uiz Interativo para Certificação AWS Certified Cloud Practitioner

Este projeto é uma aplicação web interativa criada em Python com Flask. Ele simula um questionário baseado na prova de certificação AWS Certified Cloud Practitioner, ajudando no preparo para o exame por meio de 120 questões abrangentes.

Estrutura do Projeto

Diretórios e Arquivos Necessários

	1.	Diretório principal do projeto
	•	Crie um diretório para o projeto e navegue até ele:
    mkdir aws_certification_quiz
    cd aws_certification_quiz
	2.	Arquivos principais
	•	Crie os seguintes arquivos dentro do diretório:
	•	app.py: Contém o código principal da aplicação Flask.
	•	templates/: Diretório onde ficarão os arquivos HTML.
	•	templates/index.html: Página principal do questionário.
	•	templates/summary.html: Página de resumo de desempenho.
	•	static/: Diretório para arquivos estáticos como CSS, imagens, etc.
	•	static/styles.css: Arquivo CSS para personalizar o layout.

Configuração do Ambiente

1.	Instalar o Python e criar um ambiente virtual
	•	Certifique-se de que você tem o Python instalado:
    python3 --version
    •	Crie e ative um ambiente virtual:
    python3 -m venv venv
    source venv/bin/activate
2.	Instalar as dependências
	•	Instale o Flask para executar o projeto:
    pip install flask

Estrutura do Projeto Final

Seu diretório deve ter a seguinte estrutura:
aws_certification_quiz/
│
├── app.py
├── templates/
│   ├── index.html
│   ├── summary.html
├── static/
│   ├── styles.css

Execução da Aplicação

1.	Executar o servidor Flask
	•	No terminal, na raiz do projeto, execute:
    python app.py
2.	Acessar no navegador
	•	Acesse a aplicação pelo navegador em:
    http://127.0.0.1:5000
3.	Navegar pelo questionário
	•	Responda às perguntas, confira as respostas e veja o resumo do desempenho ao final.

Personalização

	1.	Adicionar novas questões
	•	No arquivo app.py, localize a variável questions e adicione suas próprias questões seguindo o formato fornecido.
	2.	Modificar o layout
	•	Edite o arquivo static/styles.css para personalizar as cores, fontes e design.

Colaboração

Sinta-se à vontade para contribuir com melhorias no código, novas perguntas ou funcionalidades. Faça um fork do repositório, implemente suas alterações e envie um pull request.

Divirta-se aprendendo e conquiste sua certificação AWS! 🚀