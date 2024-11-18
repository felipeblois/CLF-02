from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

questions = [
    {
        "question": "O que é computação em nuvem?",
        "options": [
            "A) Faça backup de arquivos armazenados em dispositivos móveis e desktop para evitar a perda de dados",
            "B) Implantação de aplicativos conectados à infraestrutura local",
            "C) Execução de código sem a necessidade de gerenciar ou provisionar servidores",
            "D) Fornecimento sob demanda de recursos e aplicações de TI pela internet com o modelo de pagamento conforme o uso",
        ],
        "answer": "D) Fornecimento sob demanda de recursos e aplicações de TI pela internet com o modelo de pagamento conforme o uso",
    },
    {
        "question": "Você deseja usar uma instância do Amazon EC2 para uma carga de trabalho de processamento em lote. Qual seria o melhor tipo de instância do Amazon EC2 a ser usado?",
        "options": [
            "A) Uso geral",
            "B) Otimizada para memória",
            "C) Otimizada para computação",
            "D) Otimizada para armazenamento",
        ],
        "answer": "C) Otimizada para computação",
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
        "question": "Quais são as opções de duração do contrato para instâncias reservadas do Amazon EC2? (Selecione DUAS opções.)",
        "options": [
            "A) 1 ano",
            "B) 3 ano",
            "C) 2 ano",
            "D) 4 ano",
        ],
        "answer": ["A) 1 ano","B) 3 ano",]
    },
    {
        "question": "Você tem uma carga de trabalho que será executada por um total de seis meses e consegue suportar interrupções. Qual seria a opção de compra mais econômica do Amazon EC2?",
        "options": [
            "A) Instância reservada",
            "B) Instância spot",
            "C) Instância dedicada",
            "D) Instância sob demanda",
        ],
        "answer": "B) Instância spot",
    },
    {
        "question": "Qual processo é um exemplo do Elastic Load Balancing?",
        "options": [
            "A) Garantir que nenhuma instância única do Amazon EC2 tenha que suportar a carga de trabalho completa sozinha",
            "B) Remover instâncias desnecessárias do Amazon EC2 quando a demanda está baixa",
            "C) Adicionar uma segunda instância do Amazon EC2 durante a venda popular de uma loja on-line",
            "D) Ajustar automaticamente o número de instâncias do Amazon EC2 para atender à demanda",
        ],
        "answer": "A) Garantir que nenhuma instância única do Amazon EC2 tenha que suportar a carga de trabalho completa sozinha",
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
        "question": "Você deseja implantar e gerenciar aplicativos em contêineres. Qual serviço você deve usar?",
        "options": [
            "A) AWS Lambda",
            "B) Amazon Simple Notification Service (Amazon SNS)",
            "C) Amazon Simple Queue Service (Amazon SQS)",
            "D) Amazon Elastic Kubernetes Service (Amazon EKS)",
        ],
        "answer": "D) Amazon Elastic Kubernetes Service (Amazon EKS)",
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
        "question": "Qual declaração é VERDADEIRA para a infraestrutura global da AWS?",
        "options": [
            "A) Uma Região consiste em uma única Zona de Disponibilidade",
            "B) Uma Zona de Disponibilidade consiste em duas ou mais Regiões",
            "C) Uma Região consiste em três ou mais Zonas de Disponibilidade",
            "D) Uma Zona de Disponibilidade consiste em uma única Região",
        ],
        "answer": "C) Uma Região consiste em três ou mais Zonas de Disponibilidade",
    },
    {
        "question": "Quais fatores devem ser considerados ao selecionar uma Região? (Selecione DUAS opções.)",
        "options": [
            "A) Conformidade com governança de dados e requisitos legais",
            "B) Proximidade com os clientes",
            "C) Acesso a suporte técnico 24 horas por dia",
            "D) Capacidade de atribuir permissões personalizadas a diferentes usuários",
            "E) Acesso à AWS Command Line Interface (AWS CLI)",
        ],
        "answer": ["B) Proximidade com os clientes","A) Conformidade com governança de dados e requisitos legais",]
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
        "question": "Qual declaração descreve melhor o Amazon CloudFront?",
        "options": [
            "A) Um serviço que permite executar a infraestrutura em uma abordagem de nuvem híbrida",
            "B) Um mecanismo de computação sem servidor para contêineres",
            "C) Um serviço que permite enviar e receber mensagens entre componentes de software por uma fila",
            "D) Um serviço global de entrega de conteúdo",
        ],
        "answer": "D) Um serviço global de entrega de conteúdo",
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
        "question": "Qual site o Amazon CloudFront usa para armazenar cópias de conteúdo em cache para entregá-los mais rapidamente aos usuários em qualquer local?",
        "options": [
            "A) Região",
            "B) Zona de Disponibilidade",
            "C) Local de borda",
            "D) Origem",
        ],
        "answer": "C) Local de borda",
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
        "question": "Qual ação você pode executar com o AWS Outposts?",
        "options": [
            "A) Automatizar ações para serviços e aplicações da AWS por meio de scripts",
            "B) Acessar assistentes e fluxos de trabalho automatizados para executar tarefas nos serviços da AWS",
            "C) Desenvolver aplicações da AWS em linguagens de programação compatíveis.",
            "D) Estender a infraestrutura e os serviços da AWS para diferentes locais, incluindo um data center on-premises.",
        ],
        "answer": "D) Estender a infraestrutura e os serviços da AWS para diferentes locais, incluindo um data center on-premises.",
    },
    {
        "question": "Sua empresa tem um aplicativo que usa instâncias do Amazon EC2 para executar o site voltado para o cliente e instâncias de banco de dados do Amazon RDS para armazenar informações pessoais dos clientes. Como o desenvolvedor deve configurar a VPC de acordo com as práticas recomendadas?",
        "options": [
            "A) Colocar as instâncias do Amazon EC2 em uma sub-rede privada e as instâncias de bancos de dados do Amazon RDS em uma sub-rede pública.",
            "B) Colocar as instâncias do Amazon EC2 em uma sub-rede pública e as instâncias de bancos de dados do Amazon RDS em uma sub-rede privada.",
            "C) Colocar as instâncias do Amazon EC2 e as instâncias de bancos de dados do Amazon RDS em uma sub-rede pública.",
            "D) Colocar as instâncias do Amazon EC2 e as instâncias de bancos de dados do Amazon RDS em uma sub-rede privada.",
        ],
        "answer": "B) Colocar as instâncias do Amazon EC2 em uma sub-rede pública e as instâncias de bancos de dados do Amazon RDS em uma sub-rede privada.",
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
        "question": "Qual componente pode ser usado para estabelecer uma conexão privada dedicada entre o data center da sua empresa e a AWS?",
        "options": [
            "A) Sub-rede privada",
            "B) DNS",
            "C) AWS Direct Connect",
            "D) Gateway privado virtual",
        ],
        "answer": "C) AWS Direct Connect",
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
        "question": "Qual declaração descreve melhor os grupos de segurança?",
        "options": [
            "A) Eles são stateful e negam todo o tráfego de entrada por padrão.",
            "B) Eles são stateful e permitem todo o tráfego de entrada por padrão.",
            "C) Eles são stateless e negam todo o tráfego de entrada por padrão.",
            "D) Eles são stateless e permitem todo o tráfego de entrada por padrão.",
        ],
        "answer": "A) Eles são stateful e negam todo o tráfego de entrada por padrão.",
    },
    {
        "question": "Qual componente é usado para conectar uma VPC à internet?",
        "options": [
            "A) Sub-rede pública",
            "B) Local de borda",
            "C) Grupo de segurança",
            "D) Gateway de internet",
        ],
        "answer": "D) Gateway de internet",
    },
    {
        "question": "Qual serviço é usado para gerenciar os registros de DNS para nomes de domínio?",
        "options": [
            "A) Amazon Virtual Private Cloud",
            "B) AWS Direct Connect",
            "C) Amazon CloudFront",
            "D) Amazon Route 53",
        ],
        "answer": "D) Amazon Route 53",
    },
{
        "question": "Quais storage classes do Amazon S3 são otimizadas para dados de arquivamento? (Selecione DUAS opções.)",
        "options": [
            "A) Amazon S3 Standard",
            "B) Amazon S3 Glacier Flexible Retrieval",
            "C) Amazon S3 Intelligent-Tiering",
            "D) Amazon S3 Standard-IA",
            "E) Amazon S3 Glacier Deep Archive",
        ],
        "answer": [
            "B) Amazon S3 Glacier Flexible Retrieval",
            "E) Amazon S3 Glacier Deep Archive",
        ],
    },
    {
        "question": "Qual(ais) afirmação(ões) é(são) VERDADEIRA(S) sobre os volumes do Amazon EBS e sistemas de arquivos do Amazon Elastic File System?",
        "options": [
            "A) Os volumes do EBS armazenam dados em uma única Zona de Disponibilidade. Os sistemas de arquivos do Amazon EFS armazenam dados em várias Zonas de Disponibilidade.",
            "B) Os volumes do EBS armazenam dados em várias Zonas de Disponibilidade. Os sistemas de arquivos do Amazon EFS armazenam dados em uma única Zona de Disponibilidade.",
            "C) Os volumes do EBS e os sistemas de arquivos do Amazon EFS armazenam dados em uma única Zona de Disponibilidade.",
            "D) Os volumes do EBS e os sistemas de arquivos do Amazon Elastic File System armazenam dados em várias Zonas de Disponibilidade.",
        ],
        "answer": "A) Os volumes do EBS armazenam dados em uma única Zona de Disponibilidade. Os sistemas de arquivos do Amazon EFS armazenam dados em várias Zonas de Disponibilidade.",
    },
    {
        "question": "Você quer armazenar dados em um serviço de armazenamento de objetos. Qual serviço da AWS é o melhor para esse tipo de armazenamento?",
        "options": [
            "A) Amazon Managed Blockchain",
            "B) Amazon Elastic File System (Amazon EFS)",
            "C) Amazon Elastic Block Store (Amazon EBS)",
            "D) Amazon Simple Storage Service (Amazon S3)",
        ],
        "answer": "D) Amazon Simple Storage Service (Amazon S3)",
    },
    {
        "question": "Qual afirmação melhor descreve o Amazon DynamoDB?",
        "options": [
            "A) Um serviço que permite executar bancos de dados relacionais na nuvem AWS",
            "B) Um serviço de banco de dados de chave-valor sem servidor",
            "C) Um serviço que você pode usar para migrar bancos de dados relacionais e não relacionais e outros tipos de armazenamentos de dados",
            "D) Banco de dados relacional de nível empresarial",
        ],
        "answer": "B) Um serviço de banco de dados de chave-valor sem servidor",
    },
    {
        "question": "Qual serviço é usado para consultar e analisar dados em um data warehouse?",
        "options": [
            "A) Amazon Redshift",
            "B) Amazon Neptune",
            "C) Amazon DocumentDB",
            "D) Amazon ElastiCache",
        ],
        "answer": "A) Amazon Redshift",
    },
{
        "question": "Qual afirmativa descreve melhor uma política do IAM?",
        "options": [
            "A) Um processo de autenticação que adiciona uma camada de proteção para sua conta AWS",
            "B) Um documento que concede ou nega permissões para serviços e recursos AWS",
            "C) Uma identidade que você pode assumir para obter acesso temporário a permissões",
            "D) A identidade que é estabelecida quando você cria pela primeira vez uma conta AWS",
        ],
        "answer": "B) Um documento que concede ou nega permissões para serviços e recursos AWS",
    },
    {
        "question": "Um funcionário precisa de acesso temporário para criar vários buckets do Amazon S3. Qual opção seria a melhor escolha para essa tarefa?",
        "options": [
            "A) Usuário-raiz da conta AWS",
            "B) Grupo do IAM",
            "C) Função do IAM",
            "D) Política de controle de serviço (SCP)",
        ],
        "answer": "C) Função do IAM",
    },
    {
        "question": "Qual afirmativa melhor descreve o princípio de menor privilégio?",
        "options": [
            "A) Adicionar um usuário do IAM em pelo menos um grupo do IAM",
            "B) Verificar as permissões de um pacote em relação a uma lista de controle de acesso",
            "C) Conceder apenas as permissões necessárias para executar tarefas específicas",
            "D) Executar um ataque de negação de serviço originado de pelo menos um dispositivo",
        ],
        "answer": "C) Conceder apenas as permissões necessárias para executar tarefas específicas",
    },
    {
        "question": "Qual serviço ajuda a proteger suas aplicações contra ataques distribuídos de negação de serviço (DDoS)?",
        "options": [
            "A) Amazon GuardDuty",
            "B) Amazon Inspector",
            "C) AWS Artifact",
            "D) AWS Shield",
        ],
        "answer": "D) AWS Shield",
    },
    {
        "question": "Qual tarefa o AWS Key Management Service (AWS KMS) pode executar?",
        "options": [
            "A) Configurar uma autenticação multifator (MFA).",
            "B) Atualizar a senha do usuário-raiz da conta AWS.",
            "C) Criar chaves de criptografia.",
            "D) Atribuir permissões a usuários e grupos.",
        ],
        "answer": "C) Criar chaves de criptografia.",
    },
{
        "question": "Quais ações você pode executar usando o Amazon CloudWatch? (Selecione DUAS opções.)",
        "options": [
            "A) Monitorar a utilização e o desempenho de seus recursos",
            "B) Receber orientações em tempo real para melhorar seu ambiente AWS",
            "C) Comparar sua infraestrutura com as práticas recomendadas da AWS em cinco categorias",
            "D) Acessar métricas em um único painel",
            "E) Detectar automaticamente atividades da conta incomuns",
        ],
        "answer": [
            "A) Monitorar a utilização e o desempenho de seus recursos",
            "D) Acessar métricas em um único painel",
        ],
    },
    {
        "question": "Qual serviço permite que você reveja a segurança de seus buckets do Amazon S3 verificando permissões de acesso aberto?",
        "options": [
            "A) Amazon CloudWatch",
            "B) AWS CloudTrail",
            "C) AWS Trusted Advisor",
            "D) Amazon GuardDuty",
        ],
        "answer": "C) AWS Trusted Advisor",
    },
    {
        "question": "Quais categorias estão inclusas no painel do AWS Trusted Advisor? (Selecione DUAS opções.)",
        "options": [
            "A) Confiabilidade",
            "B) Desempenho",
            "C) Dimensionamento",
            "D) Elasticidade",
            "E) Tolerância a falhas",
        ],
        "answer": [
            "B) Desempenho",
            "E) Tolerância a falhas",
        ],
    },
{
        "question": "Qual ação você pode executar com a cobrança consolidada?",
        "options": [
            "A) Analisar o custo em que seu uso previsto da AWS incorrerá até o final do mês.",
            "B) Criar uma estimativa de custo para seus casos de uso na AWS.",
            "C) Combinar o uso entre contas para obter descontos de preços por volume.",
            "D) Visualizar e gerenciar os custos e o uso da AWS ao longo do tempo.",
        ],
        "answer": "C) Combinar o uso entre contas para obter descontos de preços por volume.",
    },
    {
        "question": "Qual ferramenta de definição de preço é usada para visualizar, entender e gerenciar o custo e o uso da AWS ao longo do tempo?",
        "options": [
            "A) Calculadora de Preços da AWS",
            "B) AWS Budgets",
            "C) AWS Cost Explorer",
            "D) Nível gratuito da AWS",
        ],
        "answer": "C) AWS Cost Explorer",
    },
    {
        "question": "Qual ferramenta de preços permite receber alertas quando o uso do serviço excede um limite que você definiu?",
        "options": [
            "A) Painel de cobrança no console de gerenciamento da AWS",
            "B) AWS Budgets",
            "C) Nível gratuito da AWS",
            "D) AWS Cost Explorer",
        ],
        "answer": "B) AWS Budgets",
    },
    {
        "question": "Sua empresa deseja ter suporte de um technical account manager (TAM) da AWS. Qual plano de suporte você deve escolher?",
        "options": [
            "A) Desenvolvedor",
            "B) Empresarial de Grande Porte",
            "C) Basic",
            "D) Empresarial",
        ],
        "answer": "B) Empresarial de Grande Porte",
    },
    {
        "question": "Qual serviço ou recurso é usado para encontrar software de terceiros que pode ser executado na AWS?",
        "options": [
            "A) AWS Marketplace",
            "B) Nível gratuito da AWS",
            "C) AWS Support",
            "D) Painel de cobrança no console de gerenciamento da AWS",
        ],
        "answer": "A) AWS Marketplace",
    },
 {
        "question": "Qual perspectiva do AWS Cloud Adoption Framework ajuda você a estruturar a seleção e a implementação de permissões?",
        "options": [
            "A) Perspectiva de governança",
            "B) Perspectiva de segurança",
            "C) Perspectiva de operações",
            "D) Perspectiva de negócio",
        ],
        "answer": "B) Perspectiva de segurança",
    },
    {
        "question": "Quais estratégias fazem parte das seis estratégias de migração de aplicativo? (Selecione DUAS opções.)",
        "options": [
            "A) Revisitar",
            "B) Reter",
            "C) Lembrar",
            "D) Redesenvolver",
            "E) Redefinir hospedagem",
        ],
        "answer": ["B) Reter", "E) Redefinir hospedagem",]
    },
    {
        "question": "Qual é a capacidade de armazenamento do AWS Snowmobile?",
        "options": [
            "A) 40 PB",
            "B) 60 PB",
            "C) 80 PB",
            "D) 100 PB",
        ],
        "answer": "D) 100 PB",
    },
    {
        "question": "Qual declaração descreve melhor o Amazon Lex?",
        "options": [
            "A) Um serviço para criação de interfaces de conversação usando voz e texto",
            "B) Um serviço de machine learning que extrai automaticamente texto e dados de documentos digitalizados",
            "C) Um serviço de banco de dados de documentos compatível com cargas de trabalho do MongoDB",
            "D) Um serviço que identifica atividades on-line potencialmente fraudulentas",
        ],
        "answer": "A) Um serviço para criação de interfaces de conversação usando voz e texto",
    },
    {
        "question": "Qual pilar do AWS Well-Architected Framework inclui a capacidade de executar cargas de trabalho de maneira eficaz e obter informações sobre as operações?",
        "options": [
            "A) Otimização de custos",
            "B) Excelência operacional",
            "C) Eficiência de desempenho",
            "D) Confiabilidade",
        ],
        "answer": "B) Excelência operacional",
    },
    {
        "question": "Quais são os benefícios da computação em nuvem? (Selecione DUAS opções.)",
        "options": [
            "A) Aumente a velocidade e a agilidade.",
            "B) Beneficiar-se de economias de escala.",
            "C) Trocar despesa variável por despesa antecipada.",
            "D) Manter a capacidade da infraestrutura.",
            "E) Parar de gastar dinheiro com execução e manutenção de data centers.",
        ],
        "answer": ["A) Aumente a velocidade e a agilidade.", "E) Parar de gastar dinheiro com execução e manutenção de data centers.",],
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
