from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

questions = [
    {
        "question": "Qual das seguintes opções NÃO é uma característica fundamental da computação em nuvem?",
        "options": [
            "A) Escalabilidade sob demanda",
            "B) Investimento inicial elevado em hardware",
            "C) Pagamento conforme o uso",
            "D) Elasticidade",
        ],
        "answer": "B) Investimento inicial elevado em hardware",
    },
    {
        "question": "O que significa 'elasticidade' na computação em nuvem?",
        "options": [
            "A) Capacidade de aumentar ou diminuir recursos automaticamente conforme a demanda",
            "B) Capacidade de reduzir custos fixos",
            "C) Capacidade de manter os mesmos recursos independentemente da demanda",
            "D) Capacidade de garantir segurança dos dados",
        ],
        "answer": "A) Capacidade de aumentar ou diminuir recursos automaticamente conforme a demanda",
    },
    {
        "question": "Qual modelo de serviço de nuvem oferece a infraestrutura básica como serviços, incluindo servidores virtuais, armazenamento e redes?",
        "options": [
            "A) Software como Serviço (SaaS)",
            "B) Plataforma como Serviço (PaaS)",
            "C) Infraestrutura como Serviço (IaaS)",
            "D) Função como Serviço (FaaS)",
        ],
        "answer": "C) Infraestrutura como Serviço (IaaS)",
    },
    {
        "question": "Qual é a principal vantagem de utilizar serviços gerenciados na nuvem?",
        "options": [
            "A) Controle total sobre a infraestrutura física",
            "B) Redução da sobrecarga operacional e de manutenção",
            "C) Necessidade de gerenciar atualizações manualmente",
            "D) Aumento da complexidade da configuração",
        ],
        "answer": "B) Redução da sobrecarga operacional e de manutenção",
    },
    {
        "question": "Qual dos seguintes NÃO é um modelo de implantação de nuvem?",
        "options": [
            "A) Nuvem Pública",
            "B) Nuvem Privada",
            "C) Nuvem Comunitária",
            "D) Nuvem Global",
        ],
        "answer": "D) Nuvem Global",
    },
    {
        "question": "O que é um 'data lake' na computação em nuvem?",
        "options": [
            "A) Um banco de dados relacional tradicional",
            "B) Um repositório centralizado que permite armazenar todos os dados estruturados e não estruturados em qualquer escala",
            "C) Um serviço de backup em nuvem",
            "D) Uma ferramenta para análise em tempo real de dados financeiros",
        ],
        "answer": "B) Um repositório centralizado que permite armazenar todos os dados estruturados e não estruturados em qualquer escala",
    },
    {
        "question": "Qual é o principal benefício da computação em nuvem para startups?",
        "options": [
            "A) Investimento inicial elevado",
            "B) Flexibilidade para escalar conforme o crescimento",
            "C) Dependência de infraestrutura física",
            "D) Custos fixos altos",
        ],
        "answer": "B) Flexibilidade para escalar conforme o crescimento",
    },
    {
        "question": "O que é 'pay-as-you-go' na AWS?",
        "options": [
            "A) Pagar antecipadamente por todos os serviços",
            "B) Pagar apenas pelos serviços que você usa, quando os usa",
            "C) Pagar uma taxa fixa mensal independentemente do uso",
            "D) Pagar taxas adicionais por suporte técnico",
        ],
        "answer": "B) Pagar apenas pelos serviços que você usa, quando os usa",
    },
    {
        "question": "Qual serviço da AWS permite executar código sem provisionar ou gerenciar servidores?",
        "options": [
            "A) Amazon EC2",
            "B) AWS Lambda",
            "C) Amazon S3",
            "D) AWS Elastic Beanstalk",
        ],
        "answer": "B) AWS Lambda",
    },
    {
        "question": "Qual é o principal diferencial da computação sem servidor (serverless computing)?",
        "options": [
            "A) Controle total sobre a infraestrutura do servidor",
            "B) Gerenciamento automático de recursos pelo provedor de nuvem",
            "C) Necessidade de gerenciar atualizações de software",
            "D) Menor segurança dos dados",
        ],
        "answer": "B) Gerenciamento automático de recursos pelo provedor de nuvem",
    },
{
        "question": "O que é uma VPC (Virtual Private Cloud) na AWS?",
        "options": [
            "A) Um serviço de armazenamento em bloco",
            "B) Um serviço que permite criar uma rede virtual isolada dentro da nuvem AWS",
            "C) Um serviço de entrega de conteúdo",
            "D) Um serviço de computação sem servidor",
        ],
        "answer": "B) Um serviço que permite criar uma rede virtual isolada dentro da nuvem AWS",
    },
    {
        "question": "Qual dos seguintes é um exemplo de serviço SaaS na AWS?",
        "options": [
            "A) Amazon EC2",
            "B) Amazon RDS",
            "C) Amazon WorkSpaces",
            "D) AWS Lambda",
        ],
        "answer": "C) Amazon WorkSpaces",
    },
    {
        "question": "O que é 'capex' em termos de computação em nuvem?",
        "options": [
            "A) Despesas operacionais contínuas",
            "B) Investimento em despesas de capital",
            "C) Custos relacionados a serviços gerenciados",
            "D) Gastos com marketing",
        ],
        "answer": "B) Investimento em despesas de capital",
    },
    {
        "question": "Qual é a principal diferença entre IaaS e PaaS?",
        "options": [
            "A) IaaS fornece software completo, enquanto PaaS fornece infraestrutura básica",
            "B) IaaS fornece infraestrutura básica, enquanto PaaS fornece plataforma para desenvolvimento",
            "C) IaaS é gratuito, enquanto PaaS é pago",
            "D) IaaS não é escalável, enquanto PaaS é",
        ],
        "answer": "B) IaaS fornece infraestrutura básica, enquanto PaaS fornece plataforma para desenvolvimento",
    },
    {
        "question": "Qual serviço da AWS permite a criação e gerenciamento de identidades e permissões de usuários?",
        "options": [
            "A) Amazon Cognito",
            "B) AWS IAM",
            "C) AWS Organizations",
            "D) AWS SSO",
        ],
        "answer": "B) AWS IAM",
    },
    {
        "question": "O que é 'economia de escala' na computação em nuvem?",
        "options": [
            "A) A capacidade de obter descontos significativos comprando hardware em massa",
            "B) A capacidade de reduzir custos operacionais ao compartilhar recursos em larga escala",
            "C) A capacidade de aumentar os preços conforme a demanda aumenta",
            "D) A capacidade de reduzir a qualidade do serviço para economizar custos",
        ],
        "answer": "B) A capacidade de reduzir custos operacionais ao compartilhar recursos em larga escala",
    },
    {
        "question": "Qual serviço da AWS é usado para gerenciar usuários e permissões de acesso aos recursos da AWS?",
        "options": [
            "A) AWS Identity and Access Management (IAM)",
            "B) AWS Organizations",
            "C) AWS Config",
            "D) AWS Certificate Manager",
        ],
        "answer": "A) AWS Identity and Access Management (IAM)",
    },
    {
        "question": "O que é uma 'política' no contexto do AWS IAM?",
        "options": [
            "A) Uma ferramenta para monitorar o uso dos recursos da AWS",
            "B) Um documento que define permissões para usuários ou grupos",
            "C) Um serviço que provisiona recursos automaticamente",
            "D) Um programa de treinamento em segurança",
        ],
        "answer": "B) Um documento que define permissões para usuários ou grupos",
    },
    {
        "question": "Qual recurso do IAM permite aplicar políticas de segurança em um grupo de contas da AWS?",
        "options": [
            "A) Grupos IAM",
            "B) Funções IAM",
            "C) AWS Organizations",
            "D) Usuários IAM",
        ],
        "answer": "C) AWS Organizations",
    },
    {
        "question": "O que é o AWS Shield?",
        "options": [
            "A) Um serviço que protege aplicações web contra ataques DDoS",
            "B) Um firewall para filtrar tráfego de entrada e saída",
            "C) Um serviço para gerenciamento de chaves de criptografia",
            "D) Uma solução de autenticação multifator",
        ],
        "answer": "A) Um serviço que protege aplicações web contra ataques DDoS",
    },
 {
        "question": "Qual serviço da AWS permite criar e gerenciar chaves de criptografia para proteger dados em repouso?",
        "options": [
            "A) AWS Key Management Service (KMS)",
            "B) AWS Secrets Manager",
            "C) AWS Certificate Manager",
            "D) Amazon GuardDuty",
        ],
        "answer": "A) AWS Key Management Service (KMS)",
    },
    {
        "question": "O que é o Amazon GuardDuty?",
        "options": [
            "A) Um serviço de detecção de ameaças que monitora continuamente atividades maliciosas e comportamentos não autorizados",
            "B) Um serviço de autenticação de usuários",
            "C) Um serviço de gerenciamento de identidades",
            "D) Um serviço para criptografar dados em trânsito",
        ],
        "answer": "A) Um serviço de detecção de ameaças que monitora continuamente atividades maliciosas e comportamentos não autorizados",
    },
    {
        "question": "Qual é o principal benefício de usar o AWS CloudTrail?",
        "options": [
            "A) Monitorar o desempenho das aplicações",
            "B) Rastrear o histórico de chamadas de API e atividades da conta",
            "C) Proteger aplicações contra ataques DDoS",
            "D) Gerenciar chaves de criptografia",
        ],
        "answer": "B) Rastrear o histórico de chamadas de API e atividades da conta",
    },
    {
        "question": "O que é o Amazon Inspector?",
        "options": [
            "A) Um serviço que avalia a segurança e conformidade das aplicações implantadas na AWS",
            "B) Um serviço de gerenciamento de chaves",
            "C) Uma ferramenta para monitorar custos",
            "D) Um serviço para criar pipelines de CI/CD",
        ],
        "answer": "A) Um serviço que avalia a segurança e conformidade das aplicações implantadas na AWS",
    },
    {
        "question": "Qual serviço da AWS permite definir uma política de controle de serviço (SCP) para gerenciar permissões em uma organização?",
        "options": [
            "A) AWS IAM",
            "B) AWS Organizations",
            "C) AWS Config",
            "D) Amazon Cognito",
        ],
        "answer": "B) AWS Organizations",
    },
    {
        "question": "O que é uma 'função' no AWS IAM?",
        "options": [
            "A) Um conjunto de permissões temporárias que um usuário ou serviço pode assumir",
            "B) Um grupo de usuários com políticas associadas",
            "C) Um recurso para monitorar atividades na conta",
            "D) Um serviço para gerenciar chaves de criptografia",
        ],
        "answer": "A) Um conjunto de permissões temporárias que um usuário ou serviço pode assumir",
    },
    {
        "question": "Qual serviço ajuda a proteger aplicações web contra explorações comuns na camada de aplicação, como SQL injection e cross-site scripting?",
        "options": [
            "A) AWS WAF (Web Application Firewall)",
            "B) Amazon Macie",
            "C) AWS Shield",
            "D) AWS Firewall Manager",
        ],
        "answer": "A) AWS WAF (Web Application Firewall)",
    },
    {
        "question": "O que é o princípio do 'menor privilégio' na segurança da informação?",
        "options": [
            "A) Conceder aos usuários todas as permissões possíveis para facilitar o acesso",
            "B) Conceder apenas as permissões necessárias para realizar as tarefas atribuídas",
            "C) Remover todas as permissões de todos os usuários",
            "D) Compartilhar credenciais entre usuários para simplificar o gerenciamento",
        ],
        "answer": "B) Conceder apenas as permissões necessárias para realizar as tarefas atribuídas",
    },
    {
        "question": "Qual ferramenta pode ser usada para verificar se os recursos da AWS estão em conformidade com as melhores práticas e políticas internas?",
        "options": [
            "A) AWS Trusted Advisor",
            "B) AWS Config",
            "C) Amazon Inspector",
            "D) AWS CloudTrail",
        ],
        "answer": "B) AWS Config",
    },
    {
        "question": "Qual serviço da AWS oferece autenticação e gerenciamento de usuários para aplicações web e móveis?",
        "options": [
            "A) AWS IAM",
            "B) Amazon Cognito",
            "C) AWS Directory Service",
            "D) AWS SSO (Single Sign-On)",
        ],
        "answer": "B) Amazon Cognito",
    },
{
        "question": "O que é o AWS Artifact?",
        "options": [
            "A) Um serviço para monitorar a saúde dos serviços da AWS",
            "B) Um portal que fornece acesso sob demanda a relatórios de conformidade da AWS",
            "C) Uma ferramenta para gerenciar pipelines de implantação",
            "D) Um serviço de gerenciamento de identidades",
        ],
        "answer": "B) Um portal que fornece acesso sob demanda a relatórios de conformidade da AWS",
    },
    {
        "question": "Qual serviço da AWS pode ser usado para armazenar e gerenciar segredos, como credenciais de banco de dados e chaves de API?",
        "options": [
            "A) AWS Secrets Manager",
            "B) AWS KMS",
            "C) AWS Certificate Manager",
            "D) Amazon Macie",
        ],
        "answer": "A) AWS Secrets Manager",
    },
    {
        "question": "Qual recurso do IAM permite que você exija autenticação multifator (MFA) para aumentar a segurança?",
        "options": [
            "A) Políticas IAM",
            "B) Grupos IAM",
            "C) Funções IAM",
            "D) Políticas de Senha",
        ],
        "answer": "D) Políticas de Senha",
    },
    {
        "question": "O que é o AWS Security Hub?",
        "options": [
            "A) Um serviço que fornece uma visão abrangente da postura de segurança em todas as contas da AWS",
            "B) Uma ferramenta para gerenciar funções do IAM",
            "C) Um serviço de firewall de rede",
            "D) Um serviço para configurar balanceadores de carga",
        ],
        "answer": "A) Um serviço que fornece uma visão abrangente da postura de segurança em todas as contas da AWS",
    },
    {
        "question": "Qual serviço da AWS permite que você monitore a atividade de DNS para detectar comportamentos maliciosos?",
        "options": [
            "A) Amazon Route 53",
            "B) Amazon GuardDuty",
            "C) AWS Shield",
            "D) AWS WAF",
        ],
        "answer": "B) Amazon GuardDuty",
    },
    {
        "question": "O que são 'Regiões' na AWS?",
        "options": [
            "A) Conjuntos de data centers distribuídos globalmente que operam de forma independente",
            "B) Data centers redundantes em uma única localização",
            "C) Serviços de computação sem servidor",
            "D) Ferramentas de gerenciamento de custos",
        ],
        "answer": "A) Conjuntos de data centers distribuídos globalmente que operam de forma independente",
    },
    {
        "question": "Por que é importante escolher a região correta ao implantar recursos na AWS?",
        "options": [
            "A) Para obter melhores preços e latência mais baixa",
            "B) Porque todos os recursos estão disponíveis em todas as regiões",
            "C) Porque as regiões determinam a quantidade de armazenamento disponível",
            "D) Porque as regiões não afetam o desempenho",
        ],
        "answer": "A) Para obter melhores preços e latência mais baixa",
    },
    {
        "question": "Qual dos seguintes é um exemplo de responsabilidade do cliente no modelo de responsabilidade compartilhada?",
        "options": [
            "A) Segurança dos data centers físicos",
            "B) Gerenciamento das políticas do IAM",
            "C) Manutenção da infraestrutura subjacente",
            "D) Disponibilidade dos serviços da AWS",
        ],
        "answer": "B) Gerenciamento das políticas do IAM",
    },
    {
        "question": "Qual serviço da AWS permite que você crie identidades digitais e credenciais temporárias para usuários móveis e web?",
        "options": [
            "A) Amazon Cognito",
            "B) AWS IAM",
            "C) AWS SSO",
            "D) AWS Directory Service",
        ],
        "answer": "A) Amazon Cognito",
    },
    {
        "question": "O que é o AWS Firewall Manager?",
        "options": [
            "A) Um serviço que facilita a configuração e o gerenciamento centralizado de regras de firewall em várias contas e aplicações",
            "B) Um serviço para gerenciar chaves de criptografia",
            "C) Uma ferramenta para monitorar custos",
            "D) Um serviço de autenticação multifator",
        ],
        "answer": "A) Um serviço que facilita a configuração e o gerenciamento centralizado de regras de firewall em várias contas e aplicações",
    },
{
        "question": "Qual serviço da AWS permite a implementação de políticas de conformidade e auditoria para recursos da AWS?",
        "options": [
            "A) AWS Config",
            "B) AWS CloudTrail",
            "C) AWS Trusted Advisor",
            "D) AWS Security Hub",
        ],
        "answer": "A) AWS Config",
    },
    {
        "question": "O que é criptografia em trânsito?",
        "options": [
            "A) Criptografar dados enquanto estão sendo transmitidos pela rede",
            "B) Criptografar dados armazenados em mídia física ou lógica",
            "C) Criptografar apenas as senhas dos usuários",
            "D) Criptografar dados após a exclusão",
        ],
        "answer": "A) Criptografar dados enquanto estão sendo transmitidos pela rede",
    },
    {
        "question": "Qual serviço da AWS permite monitorar e gerenciar eventos e logs para identificar atividades suspeitas?",
        "options": [
            "A) Amazon GuardDuty",
            "B) AWS Shield",
            "C) AWS WAF",
            "D) AWS Firewall Manager",
        ],
        "answer": "A) Amazon GuardDuty",
    },
    {
        "question": "Qual serviço da AWS é usado para implementar e gerenciar políticas de segurança para múltiplas contas?",
        "options": [
            "A) AWS Organizations",
            "B) AWS IAM",
            "C) AWS Config",
            "D) AWS Security Hub",
        ],
        "answer": "A) AWS Organizations",
    },
    {
        "question": "O que é o Amazon Macie?",
        "options": [
            "A) Um serviço que usa machine learning para descobrir, classificar e proteger dados confidenciais na AWS",
            "B) Um serviço de gerenciamento de chaves",
            "C) Um serviço de monitoramento de aplicações",
            "D) Um serviço de entrega de conteúdo",
        ],
        "answer": "A) Um serviço que usa machine learning para descobrir, classificar e proteger dados confidenciais na AWS",
    },
    {
        "question": "Qual serviço da AWS permite configurar regras de firewall em nível de aplicação?",
        "options": [
            "A) AWS WAF",
            "B) AWS Shield",
            "C) AWS Firewall Manager",
            "D) Amazon GuardDuty",
        ],
        "answer": "A) AWS WAF",
    },
    {
        "question": "O que é o AWS Single Sign-On (SSO)?",
        "options": [
            "A) Um serviço para gerenciar chaves de criptografia",
            "B) Um serviço que permite gerenciar acesso centralizado a múltiplos aplicativos",
            "C) Um serviço de monitoramento de aplicações",
            "D) Um serviço para entrega de conteúdo",
        ],
        "answer": "B) Um serviço que permite gerenciar acesso centralizado a múltiplos aplicativos",
    },
    {
        "question": "Qual é a finalidade principal do AWS Certificate Manager (ACM)?",
        "options": [
            "A) Gerenciar políticas de segurança",
            "B) Provisionar, gerenciar e implantar certificados SSL/TLS",
            "C) Monitorar logs de segurança",
            "D) Gerenciar identidades de usuários",
        ],
        "answer": "B) Provisionar, gerenciar e implantar certificados SSL/TLS",
    },
    {
        "question": "O que é o AWS Secrets Manager?",
        "options": [
            "A) Um serviço para gerenciar e rotacionar segredos, como credenciais de banco de dados e chaves de API",
            "B) Um serviço de monitoramento de atividades",
            "C) Um serviço de entrega de conteúdo",
            "D) Um serviço de backup de dados",
        ],
        "answer": "A) Um serviço para gerenciar e rotacionar segredos, como credenciais de banco de dados e chaves de API",
    },
    {
        "question": "Qual serviço da AWS ajuda a proteger aplicações contra vulnerabilidades conhecidas?",
        "options": [
            "A) Amazon Inspector",
            "B) AWS Shield",
            "C) AWS WAF",
            "D) AWS Firewall Manager",
        ],
        "answer": "A) Amazon Inspector",
    },
{
        "question": "O que é o AWS Artifact?",
        "options": [
            "A) Um serviço para monitorar a saúde dos serviços da AWS",
            "B) Um portal que fornece acesso a relatórios de conformidade e acordos legais",
            "C) Uma ferramenta para gerenciar pipelines de implantação",
            "D) Um serviço de gerenciamento de identidades",
        ],
        "answer": "B) Um portal que fornece acesso a relatórios de conformidade e acordos legais",
    },
    {
        "question": "Qual serviço da AWS permite gerenciar identidades federadas e SSO (Single Sign-On) para aplicações corporativas?",
        "options": [
            "A) AWS Single Sign-On (SSO)",
            "B) AWS IAM",
            "C) Amazon Cognito",
            "D) AWS Directory Service",
        ],
        "answer": "A) AWS Single Sign-On (SSO)",
    },
    {
        "question": "O que é o AWS Trusted Advisor?",
        "options": [
            "A) Um serviço que fornece recomendações para otimizar recursos, melhorar desempenho, aumentar a segurança e reduzir custos",
            "B) Um serviço de monitoramento de aplicações",
            "C) Um serviço de entrega de conteúdo",
            "D) Um serviço de armazenamento em cache",
        ],
        "answer": "A) Um serviço que fornece recomendações para otimizar recursos, melhorar desempenho, aumentar a segurança e reduzir custos",
    },
    {
        "question": "Qual dos seguintes é um benefício de usar o AWS CloudHSM?",
        "options": [
            "A) Gerenciamento de chaves de criptografia em hardware dedicado",
            "B) Serviço de detecção de ameaças",
            "C) Armazenamento de objetos altamente durável",
            "D) Balanceamento de carga de aplicações web",
        ],
        "answer": "A) Gerenciamento de chaves de criptografia em hardware dedicado",
    },
    {
        "question": "Qual serviço da AWS permite criar e gerenciar políticas de segurança para proteger recursos em múltiplas contas?",
        "options": [
            "A) AWS Security Hub",
            "B) AWS Firewall Manager",
            "C) AWS WAF",
            "D) Amazon GuardDuty",
        ],
        "answer": "B) AWS Firewall Manager",
    },
    {
        "question": "O que é o AWS KMS (Key Management Service)?",
        "options": [
            "A) Um serviço para monitorar atividades na conta",
            "B) Um serviço gerenciado que facilita a criação e o controle de chaves de criptografia",
            "C) Um serviço de entrega de conteúdo",
            "D) Uma ferramenta para gerenciar identidades",
        ],
        "answer": "B) Um serviço gerenciado que facilita a criação e o controle de chaves de criptografia",
    },
    {
        "question": "Qual serviço da AWS permite realizar análises de comportamento de rede para identificar atividades suspeitas?",
        "options": [
            "A) Amazon GuardDuty",
            "B) AWS Shield",
            "C) AWS WAF",
            "D) AWS Firewall Manager",
        ],
        "answer": "A) Amazon GuardDuty",
    },
    {
        "question": "O que é o princípio da 'defesa em profundidade' na segurança da informação?",
        "options": [
            "A) Usar uma única camada de segurança para simplificar o gerenciamento",
            "B) Implementar várias camadas de segurança para proteger recursos",
            "C) Delegar toda a segurança ao provedor de nuvem",
            "D) Focar apenas na segurança física dos data centers",
        ],
        "answer": "B) Implementar várias camadas de segurança para proteger recursos",
    },
    {
        "question": "Qual serviço da AWS permite que você monitore e gerencie conformidade contínua dos recursos da AWS?",
        "options": [
            "A) AWS Config",
            "B) AWS CloudTrail",
            "C) AWS Security Hub",
            "D) AWS Trusted Advisor",
        ],
        "answer": "C) AWS Security Hub",
    },
    {
        "question": "Qual serviço da AWS permite automatizar a aplicação de patches de segurança em suas instâncias?",
        "options": [
            "A) AWS Systems Manager Patch Manager",
            "B) AWS Config",
            "C) AWS CloudTrail",
            "D) Amazon Inspector",
        ],
        "answer": "A) AWS Systems Manager Patch Manager",
    },
]

@app.route("/", methods=["GET", "POST"])
def quiz():
    # Index da pergunta atual e estado do questionário
    question_index = int(request.args.get("q", 0))
    user_answers = request.args.getlist("answers", type=str)
    feedback_list = request.args.getlist("feedback", type=str)

    # Processar envio da resposta
    if request.method == "POST":
        selected_option = request.form.get("option")
        correct_answer = questions[question_index]["answer"]
        feedback = ""

        if selected_option == correct_answer:
            feedback = "Correto! A resposta é: " + correct_answer
        else:
            feedback = f"Errado! A resposta correta é: {correct_answer}"

        # Atualizar listas de respostas e feedback
        user_answers.append(selected_option)
        feedback_list.append(feedback)

        # Verificar se há mais perguntas
        if question_index + 1 < len(questions):
            return redirect(
                url_for(
                    "quiz",
                    q=question_index + 1,
                    answers=user_answers,
                    feedback=feedback_list,
                )
            )
        else:
            # Fim do questionário, redirecionar para o resumo
            return redirect(
                url_for(
                    "result",
                    answers=user_answers,
                    feedback=feedback_list,
                )
            )

    # Renderizar a pergunta atual
    question = questions[question_index]
    return render_template(
        "quiz.html",
        question=question,
        question_index=question_index,
        answers=user_answers,
        feedback=feedback_list,
        total_questions=len(questions),
    )


@app.route("/result", methods=["GET"])
def result():
    user_answers = request.args.getlist("answers", type=str)
    feedback_list = request.args.getlist("feedback", type=str)
    correct_answers = sum(
        1
        for i, answer in enumerate(user_answers)
        if answer == questions[i]["answer"]
    )
    incorrect_answers = len(user_answers) - correct_answers

    return render_template(
        "result.html",
        total_questions=len(questions),
        correct_answers=correct_answers,
        incorrect_answers=incorrect_answers,
        feedback_list=feedback_list,
    )


if __name__ == "__main__":
    app.run(debug=True)
