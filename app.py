from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

questions = [
    {
        "question": "Qual das seguintes opções NÃO é uma característica da computação em nuvem?",
        "options": [
            "A) Escalabilidade sob demanda",
            "B) Alto custo inicial de hardware",
            "C) Modelo de pagamento conforme o uso",
            "D) Elasticidade",
        ],
        "answer": "B) Alto custo inicial de hardware",
    },
    {
        "question": "Qual é o modelo de implantação em que os serviços de nuvem são fornecidos em uma rede privada usada exclusivamente por uma única organização?",
        "options": [
            "A) Nuvem Pública",
            "B) Nuvem Privada",
            "C) Nuvem Híbrida",
            "D) Nuvem Comunitária",
        ],
        "answer": "B) Nuvem Privada",
    },
    {
        "question": "Qual benefício da computação em nuvem permite que você aumente ou diminua os recursos de TI conforme necessário para atender à demanda?",
        "options": [
            "A) Elasticidade",
            "B) Confiabilidade",
            "C) Segurança",
            "D) CapEx reduzido",
        ],
        "answer": "A) Elasticidade",
    },
    {
        "question": "Qual modelo de serviço de computação em nuvem fornece ao cliente a capacidade de implantar e gerenciar suas próprias aplicações usando infraestrutura de terceiros?",
        "options": [
            "A) Software como Serviço (SaaS)",
            "B) Plataforma como Serviço (PaaS)",
            "C) Infraestrutura como Serviço (IaaS)",
            "D) Função como Serviço (FaaS)",
        ],
        "answer": "C) Infraestrutura como Serviço (IaaS)",
    },
    {
        "question": "Qual dos seguintes é um exemplo de serviço PaaS na AWS?",
        "options": [
            "A) Amazon EC2",
            "B) AWS Lambda",
            "C) Amazon S3",
            "D) AWS Elastic Beanstalk",
        ],
        "answer": "D) AWS Elastic Beanstalk",
    },
    {
        "question": "Qual é um benefício econômico chave da computação em nuvem?",
        "options": [
            "A) Investimento significativo em hardware",
            "B) Custos operacionais imprevisíveis",
            "C) Economia de escala",
            "D) Contratos de longo prazo",
        ],
        "answer": "C) Economia de escala",
    },
    {
        "question": "O que significa dizer que a nuvem é “elástica”?",
        "options": [
            "A) A capacidade de expandir rapidamente o espaço de armazenamento físico",
            "B) A capacidade de otimizar custos ao comprar hardware",
            "C) A capacidade de provisionar e liberar recursos de computação automaticamente para atender à demanda",
            "D) A capacidade de reduzir a complexidade da rede",
        ],
        "answer": "C) A capacidade de provisionar e liberar recursos de computação automaticamente para atender à demanda",
    },
    {
        "question": "Qual das seguintes opções descreve melhor o modelo de responsabilidade compartilhada na nuvem?",
        "options": [
            "A) O cliente é totalmente responsável pela segurança na nuvem",
            "B) O provedor de nuvem é totalmente responsável pela segurança na nuvem",
            "C) O provedor de nuvem e o cliente compartilham responsabilidades específicas pela segurança",
            "D) Nenhuma responsabilidade de segurança é necessária na nuvem",
        ],
        "answer": "C) O provedor de nuvem e o cliente compartilham responsabilidades específicas pela segurança",
    },
    {
        "question": "Qual é uma vantagem de usar serviços de nuvem em relação a um data center tradicional?",
        "options": [
            "A) Maior investimento inicial",
            "B) Maior tempo para provisionar recursos",
            "C) Escalabilidade limitada",
            "D) Capacidade de ir ao mercado mais rapidamente",
        ],
        "answer": "D) Capacidade de ir ao mercado mais rapidamente",
    },
    {
        "question": "O que é o modelo de precificação “pay-as-you-go” na AWS?",
        "options": [
            "A) Pagar antecipadamente por todos os serviços",
            "B) Pagar apenas pelos serviços que você usa, quando os usa",
            "C) Pagar uma taxa fixa mensal independentemente do uso",
            "D) Pagar taxas adicionais por suporte técnico",
        ],
        "answer": "B) Pagar apenas pelos serviços que você usa, quando os usa",
    },
    {
        "question": "Qual modelo de serviço permite que os clientes da AWS usem apenas recursos de armazenamento sem se preocupar com a infraestrutura subjacente?",
        "options": [
            "A) IaaS",
            "B) PaaS",
            "C) SaaS",
            "D) StaaS (Storage as a Service)",
        ],
        "answer": "A) IaaS",
    },
    {
        "question": "O que é computação sem servidor (serverless computing)?",
        "options": [
            "A) Computação que não requer servidores físicos",
            "B) Modelo de execução no qual o provedor de nuvem gerencia a alocação de recursos automaticamente",
            "C) Serviços que exigem que os clientes gerenciem servidores virtuais",
            "D) Uma abordagem para eliminar completamente o uso de servidores em TI",
        ],
        "answer": "B) Modelo de execução no qual o provedor de nuvem gerencia a alocação de recursos automaticamente",
    },
    {
        "question": "Qual das seguintes é uma característica de um modelo de nuvem híbrida?",
        "options": [
            "A) Uso exclusivo de serviços de nuvem pública",
            "B) Combinação de nuvem privada e nuvem pública",
            "C) Uso de serviços de nuvem em uma única região geográfica",
            "D) Uso de vários provedores de nuvem pública",
        ],
        "answer": "B) Combinação de nuvem privada e nuvem pública",
    },
    {
        "question": "O que é escalabilidade horizontal na computação em nuvem?",
        "options": [
            "A) Aumentar a capacidade de um servidor adicionando mais recursos (CPU, RAM)",
            "B) Aumentar o número de servidores para distribuir a carga",
            "C) Diminuir o número de servidores para economizar custos",
            "D) Reduzir a capacidade de um servidor removendo recursos",
        ],
        "answer": "B) Aumentar o número de servidores para distribuir a carga",
    },
    {
        "question": "Qual termo descreve a capacidade de recuperar rapidamente de falhas e continuar operando?",
        "options": [
            "A) Elasticidade",
            "B) Resiliência",
            "C) Escalabilidade",
            "D) Disponibilidade",
        ],
        "answer": "B) Resiliência",
    },
    {
        "question": "Qual serviço da AWS ajuda a migrar bancos de dados para a nuvem com tempo de inatividade mínimo?",
        "options": [
            "A) AWS Snowball",
            "B) AWS Database Migration Service (DMS)",
            "C) AWS Data Pipeline",
            "D) AWS Migration Hub",
        ],
        "answer": "B) AWS Database Migration Service (DMS)",
    },
    {
        "question": "Qual é o principal benefício de usar serviços gerenciados na nuvem?",
        "options": [
            "A) Controle total sobre a infraestrutura subjacente",
            "B) Redução da sobrecarga operacional e de manutenção",
            "C) Necessidade de gerenciar atualizações e patches manualmente",
            "D) Maior complexidade na configuração",
        ],
        "answer": "B) Redução da sobrecarga operacional e de manutenção",
    },
    {
        "question": "O que significa “economia de escala” no contexto da computação em nuvem?",
        "options": [
            "A) A capacidade de obter descontos significativos comprando hardware em massa",
            "B) A capacidade de reduzir custos operacionais ao compartilhar recursos em larga escala",
            "C) A capacidade de aumentar os preços conforme a demanda aumenta",
            "D) A capacidade de reduzir a qualidade do serviço para economizar custos",
        ],
        "answer": "B) A capacidade de reduzir custos operacionais ao compartilhar recursos em larga escala",
    },
    {
        "question": "Qual modelo de implantação de nuvem oferece serviços a várias organizações que compartilham requisitos específicos?",
        "options": [
            "A) Nuvem Pública",
            "B) Nuvem Privada",
            "C) Nuvem Comunitária",
            "D) Nuvem Híbrida",
        ],
        "answer": "C) Nuvem Comunitária",
    },
    {
        "question": "Qual benefício da computação em nuvem ajuda a melhorar o desempenho e reduzir a latência para usuários finais globalmente?",
        "options": [
            "A) Elasticidade",
            "B) Serviços gerenciados",
            "C) Distribuição geográfica de recursos",
            "D) Custos iniciais elevados",
        ],
        "answer": "C) Distribuição geográfica de recursos",
    },
    {
        "question": "O que é um data center tradicional?",
        "options": [
            "A) Um conjunto de servidores em nuvem gerenciados por um provedor de serviços",
            "B) Um local físico onde servidores e outros componentes de hardware são mantidos e operados pela própria organização",
            "C) Um serviço virtual que simula hardware físico",
            "D) Um ambiente de desenvolvimento hospedado na nuvem",
        ],
        "answer": "B) Um local físico onde servidores e outros componentes de hardware são mantidos e operados pela própria organização",
    },
    {
        "question": "Qual é a definição de “latência” em redes e computação em nuvem?",
        "options": [
            "A) A quantidade de dados que podem ser transferidos por segundo",
            "B) O atraso total entre o envio de uma solicitação e o recebimento da resposta",
            "C) A capacidade máxima de armazenamento disponível",
            "D) A taxa de erros em uma rede",
        ],
        "answer": "B) O atraso total entre o envio de uma solicitação e o recebimento da resposta",
    },
    {
        "question": "Qual dos seguintes NÃO é um modelo de serviço de computação em nuvem?",
        "options": [
            "A) Software como Serviço (SaaS)",
            "B) Infraestrutura como Serviço (IaaS)",
            "C) Plataforma como Serviço (PaaS)",
            "D) Rede como Serviço (NaaS)",
        ],
        "answer": "D) Rede como Serviço (NaaS)",
    },
    {
        "question": "Como a computação em nuvem pode ajudar as empresas a serem mais ágeis?",
        "options": [
            "A) Aumentando os custos de TI",
            "B) Prolongando os ciclos de lançamento de produtos",
            "C) Facilitando a rápida experimentação e implantação de novas soluções",
            "D) Reduzindo a capacidade de resposta às mudanças do mercado",
        ],
        "answer": "C) Facilitando a rápida experimentação e implantação de novas soluções",
    },
    {
        "question": "O que é um “data lake” na computação em nuvem?",
        "options": [
            "A) Um repositório centralizado que permite armazenar todos os dados estruturados e não estruturados em qualquer escala",
            "B) Um banco de dados relacional tradicional",
            "C) Um serviço de backup em nuvem para dados críticos",
            "D) Uma ferramenta para análise em tempo real de dados financeiros",
        ],
        "answer": "A) Um repositório centralizado que permite armazenar todos os dados estruturados e não estruturados em qualquer escala",
    },
    {
        "question": "Qual serviço da AWS permite executar código sem provisionar ou gerenciar servidores?",
        "options": [
            "A) AWS Elastic Beanstalk",
            "B) Amazon EC2",
            "C) AWS Lambda",
            "D) Amazon Lightsail",
        ],
        "answer": "C) AWS Lambda",
    },
    {
        "question": "Qual é a principal responsabilidade do cliente no modelo de responsabilidade compartilhada?",
        "options": [
            "A) Segurança da nuvem",
            "B) Segurança dentro da nuvem",
            "C) Manutenção dos data centers físicos",
            "D) Garantir a disponibilidade dos serviços da AWS",
        ],
        "answer": "B) Segurança dentro da nuvem",
    },
    {
        "question": "O que é um “microserviço” em arquitetura de software?",
        "options": [
            "A) Uma grande aplicação monolítica",
            "B) Um padrão de arquitetura que divide uma aplicação em pequenos serviços independentes",
            "C) Um tipo de servidor físico de pequeno porte",
            "D) Uma ferramenta para monitorar desempenho de aplicações",
        ],
        "answer": "B) Um padrão de arquitetura que divide uma aplicação em pequenos serviços independentes",
    },
    {
        "question": "Qual benefício da computação em nuvem permite que as organizações evitem investimentos de capital em hardware?",
        "options": [
            "A) Elasticidade",
            "B) Modelo de pagamento antecipado",
            "C) Redução de CapEx (Capital Expenditure)",
            "D) Aumento de OpEx (Operational Expenditure)",
        ],
        "answer": "C) Redução de CapEx (Capital Expenditure)",
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
        "question": "O que é uma “política” no contexto do AWS IAM?",
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
        "question": "Qual serviço da AWS permite que você crie e gerencie chaves de criptografia para proteger dados em repouso?",
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
        "question": "O que é uma “função” no AWS IAM?",
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
        "question": "O que é o princípio do “menor privilégio” na segurança da informação?",
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
            "A) Um portal que fornece acesso sob demanda a relatórios de conformidade da AWS",
            "B) Um serviço para monitorar a saúde dos serviços da AWS",
            "C) Uma ferramenta para gerenciar pipelines de implantação",
            "D) Um serviço de gerenciamento de identidades",
        ],
        "answer": "A) Um portal que fornece acesso sob demanda a relatórios de conformidade da AWS",
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
        "question": "Qual serviço ajuda a identificar e proteger dados confidenciais armazenados no Amazon S3 usando machine learning?",
        "options": [
            "A) Amazon Macie",
            "B) Amazon GuardDuty",
            "C) AWS Shield",
            "D) AWS WAF",
        ],
        "answer": "A) Amazon Macie",
    },
    {
        "question": "O que é criptografia em repouso?",
        "options": [
            "A) Criptografar dados enquanto eles estão sendo transmitidos pela rede",
            "B) Criptografar dados armazenados em mídia física ou lógica",
            "C) Criptografar apenas as senhas dos usuários",
            "D) Criptografar dados após a exclusão",
        ],
        "answer": "B) Criptografar dados armazenados em mídia física ou lógica",
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
        "question": "O que é o Amazon VPC (Virtual Private Cloud)?",
        "options": [
            "A) Um serviço que permite criar uma rede virtual isolada dentro da nuvem AWS",
            "B) Um serviço de armazenamento em bloco",
            "C) Um serviço de computação sem servidor",
            "D) Um serviço para entrega de conteúdo global",
        ],
        "answer": "A) Um serviço que permite criar uma rede virtual isolada dentro da nuvem AWS",
    },
    {
        "question": "Qual serviço permite conectar sua rede local à nuvem AWS de forma segura e privada?",
        "options": [
            "A) Amazon Route 53",
            "B) AWS Direct Connect",
            "C) AWS VPN",
            "D) Amazon CloudFront",
        ],
        "answer": "B) AWS Direct Connect",
    },
    {
        "question": "O que é um Security Group no Amazon VPC?",
        "options": [
            "A) Um firewall virtual que controla o tráfego de entrada e saída das instâncias",
            "B) Um grupo de usuários no IAM",
            "C) Uma política de segurança para S3",
            "D) Uma ferramenta para monitorar custos",
        ],
        "answer": "A) Um firewall virtual que controla o tráfego de entrada e saída das instâncias",
    },
    {
        "question": "Qual é a função das Network ACLs (Listas de Controle de Acesso de Rede) no Amazon VPC?",
        "options": [
            "A) Controlar o acesso aos recursos do IAM",
            "B) Fornecer controle de tráfego no nível da sub-rede",
            "C) Gerenciar chaves de criptografia",
            "D) Monitorar atividades de rede",
        ],
        "answer": "B) Fornecer controle de tráfego no nível da sub-rede",
    },
    {
        "question": "Qual serviço da AWS permite que você automatize a avaliação, auditoria e avaliação de configurações de recursos?",
        "options": [
            "A) AWS Config",
            "B) AWS CloudTrail",
            "C) Amazon CloudWatch",
            "D) AWS Trusted Advisor",
        ],
        "answer": "A) AWS Config",
    },
    {
        "question": "O que é o AWS Trusted Advisor?",
        "options": [
            "A) Um serviço que fornece recomendações para ajudar a seguir as melhores práticas da AWS",
            "B) Um firewall de rede",
            "C) Um serviço para criar pipelines de implantação",
            "D) Uma ferramenta para gerenciar funções do IAM",
        ],
        "answer": "A) Um serviço que fornece recomendações para ajudar a seguir as melhores práticas da AWS",
    },
    {
        "question": "Qual das seguintes práticas ajuda a proteger contas da AWS?",
        "options": [
            "A) Compartilhar credenciais com a equipe inteira",
            "B) Usar senhas fortes e habilitar MFA",
            "C) Desabilitar logs de auditoria",
            "D) Utilizar apenas a conta root para todas as atividades",
        ],
        "answer": "B) Usar senhas fortes e habilitar MFA",
    },
    {
        "question": "O que é o princípio da “defesa em profundidade” na segurança da informação?",
        "options": [
            "A) Usar uma única camada de segurança para simplificar o gerenciamento",
            "B) Implementar várias camadas de segurança para proteger recursos",
            "C) Delegar toda a segurança ao provedor de nuvem",
            "D) Focar apenas na segurança física dos data centers",
        ],
        "answer": "B) Implementar várias camadas de segurança para proteger recursos",
    },
    {
        "question": "Qual serviço permite gerenciar identidades federadas e SSO (Single Sign-On) para aplicações corporativas?",
        "options": [
            "A) AWS Single Sign-On (SSO)",
            "B) AWS IAM",
            "C) Amazon Cognito",
            "D) AWS Directory Service",
        ],
        "answer": "A) AWS Single Sign-On (SSO)",
    },
    {
        "question": "O que é o Amazon Detective?",
        "options": [
            "A) Um serviço que ajuda a analisar, investigar e identificar a causa raiz de potenciais problemas de segurança",
            "B) Uma ferramenta para criar dashboards personalizados",
            "C) Um serviço de armazenamento em cache",
            "D) Um serviço para entrega de conteúdo",
        ],
        "answer": "A) Um serviço que ajuda a analisar, investigar e identificar a causa raiz de potenciais problemas de segurança",
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
        "question": "O que são “Regiões” na AWS?",
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
    "question": "Qual serviço da AWS permite criar identidades digitais e credenciais temporárias para usuários móveis e web?",
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
    "question": "Qual serviço da AWS é um serviço de computação que permite que você execute instâncias de máquinas virtuais na nuvem?",
    "options": [
        "A) Amazon EC2",
        "B) AWS Lambda",
        "C) Amazon S3",
        "D) Amazon RDS",
    ],
    "answer": "A) Amazon EC2",
},
{
    "question": "O que é o Amazon S3?",
    "options": [
        "A) Um serviço de armazenamento em bloco",
        "B) Um serviço de banco de dados relacional",
        "C) Um serviço de armazenamento de objetos escalável e durável",
        "D) Um serviço de entrega de conteúdo",
    ],
    "answer": "C) Um serviço de armazenamento de objetos escalável e durável",
},
{
    "question": "Qual serviço é usado para gerenciar contêineres Docker na AWS?",
    "options": [
        "A) AWS Fargate",
        "B) Amazon ECS (Elastic Container Service)",
        "C) Amazon EKS (Elastic Kubernetes Service)",
        "D) Todas as opções acima",
    ],
    "answer": "D) Todas as opções acima",
},
{
    "question": "O que é o Amazon RDS?",
    "options": [
        "A) Um serviço de banco de dados relacional gerenciado",
        "B) Um serviço de armazenamento em cache",
        "C) Um serviço de computação sem servidor",
        "D) Um serviço de balanceamento de carga",
    ],
    "answer": "A) Um serviço de banco de dados relacional gerenciado",
},
{
    "question": "Qual serviço da AWS oferece distribuição global de conteúdo para sites e aplicações?",
    "options": [
        "A) Amazon CloudFront",
        "B) Amazon Route 53",
        "C) AWS Direct Connect",
        "D) AWS VPN",
    ],
    "answer": "A) Amazon CloudFront",
},
{
    "question": "O que é o AWS Elastic Beanstalk?",
    "options": [
        "A) Um serviço para implantar e escalar aplicações web e serviços com facilidade",
        "B) Um serviço de computação sem servidor",
        "C) Um serviço de monitoramento de aplicações",
        "D) Um serviço de gerenciamento de identidades",
    ],
    "answer": "A) Um serviço para implantar e escalar aplicações web e serviços com facilidade",
},
{
    "question": "Qual serviço permite orquestrar fluxos de trabalho complexos com etapas dependentes?",
    "options": [
        "A) AWS Step Functions",
        "B) Amazon SQS",
        "C) Amazon SNS",
        "D) AWS Glue",
    ],
    "answer": "A) AWS Step Functions",
},
{
    "question": "O que é o Amazon DynamoDB?",
    "options": [
        "A) Um serviço de banco de dados relacional",
        "B) Um serviço de banco de dados NoSQL rápido e flexível",
        "C) Um serviço de armazenamento em bloco",
        "D) Um serviço de data warehouse",
    ],
    "answer": "B) Um serviço de banco de dados NoSQL rápido e flexível",
},
{
    "question": "Qual serviço é usado para gerenciar filas de mensagens entre sistemas distribuídos?",
    "options": [
        "A) Amazon SQS (Simple Queue Service)",
        "B) Amazon SNS (Simple Notification Service)",
        "C) Amazon MQ",
        "D) AWS EventBridge",
    ],
    "answer": "A) Amazon SQS (Simple Queue Service)",
},
{
    "question": "Qual serviço permite implantar aplicações em dispositivos de borda e conectá-los à nuvem AWS?",
    "options": [
        "A) AWS IoT Core",
        "B) AWS Greengrass",
        "C) Amazon Connect",
        "D) Amazon Kinesis",
    ],
    "answer": "B) AWS Greengrass",
},
{
    "question": "O que é o Amazon EMR (Elastic MapReduce)?",
    "options": [
        "A) Um serviço para executar cargas de trabalho de Big Data usando frameworks como Hadoop e Spark",
        "B) Um serviço de entrega de conteúdo",
        "C) Um serviço de computação sem servidor",
        "D) Um serviço de monitoramento de aplicações",
    ],
    "answer": "A) Um serviço para executar cargas de trabalho de Big Data usando frameworks como Hadoop e Spark",
},
{
    "question": "Qual serviço da AWS permite gerenciar infraestrutura como código?",
    "options": [
        "A) AWS CloudFormation",
        "B) AWS CodeCommit",
        "C) AWS CodeDeploy",
        "D) AWS CodePipeline",
    ],
    "answer": "A) AWS CloudFormation",
},
{
    "question": "Qual serviço oferece uma solução de armazenamento de arquivos totalmente gerenciada para uso com instâncias do Amazon EC2?",
    "options": [
        "A) Amazon EFS (Elastic File System)",
        "B) Amazon S3",
        "C) Amazon EBS (Elastic Block Store)",
        "D) Amazon Glacier",
    ],
    "answer": "A) Amazon EFS (Elastic File System)",
},
{
    "question": "O que é o Amazon Kinesis?",
    "options": [
        "A) Um serviço para processamento de dados em streaming em tempo real",
        "B) Um serviço de banco de dados relacional",
        "C) Um serviço de computação sem servidor",
        "D) Um serviço de monitoramento de aplicações",
    ],
    "answer": "A) Um serviço para processamento de dados em streaming em tempo real",
},
{
    "question": "Qual serviço é usado para enviar notificações para usuários ou sistemas usando diferentes protocolos, como SMS, e-mail ou HTTP?",
    "options": [
        "A) Amazon SNS (Simple Notification Service)",
        "B) Amazon SQS",
        "C) AWS Lambda",
        "D) Amazon SES (Simple Email Service)",
    ],
    "answer": "A) Amazon SNS (Simple Notification Service)",
},
{
    "question": "O que é o AWS CodeCommit?",
    "options": [
        "A) Um serviço de controle de código-fonte gerenciado que hospeda repositórios Git",
        "B) Uma ferramenta para implantar código em instâncias EC2",
        "C) Um serviço de compilação e teste contínuo",
        "D) Um serviço de entrega de código automatizada",
    ],
    "answer": "A) Um serviço de controle de código-fonte gerenciado que hospeda repositórios Git",
},
{
    "question": "Qual serviço da AWS permite criar APIs escaláveis e seguras para aplicações?",
    "options": [
        "A) Amazon API Gateway",
        "B) AWS AppSync",
        "C) AWS Lambda",
        "D) AWS Amplify",
    ],
    "answer": "A) Amazon API Gateway",
},
{
    "question": "O que é o Amazon Lightsail?",
    "options": [
        "A) Um serviço que facilita o início rápido na nuvem com servidores virtuais, armazenamento, bancos de dados e networking simplificados",
        "B) Um serviço de balanceamento de carga",
        "C) Um serviço de armazenamento em bloco",
        "D) Um serviço de banco de dados NoSQL",
    ],
    "answer": "A) Um serviço que facilita o início rápido na nuvem com servidores virtuais, armazenamento, bancos de dados e networking simplificados",
},
{
    "question": "Qual serviço da AWS é usado para carregar grandes volumes de dados para a nuvem usando dispositivos físicos?",
    "options": [
        "A) AWS Snowball",
        "B) AWS Data Pipeline",
        "C) AWS Direct Connect",
        "D) AWS Storage Gateway",
    ],
    "answer": "A) AWS Snowball",
},
{
    "question": "O que é o Amazon Aurora?",
    "options": [
        "A) Um banco de dados relacional compatível com MySQL e PostgreSQL, criado para a nuvem",
        "B) Um serviço de banco de dados NoSQL",
        "C) Um serviço de cache em memória",
        "D) Um serviço de monitoramento de aplicações",
    ],
    "answer": "A) Um banco de dados relacional compatível com MySQL e PostgreSQL, criado para a nuvem",
},
{
    "question": "Qual serviço permite adicionar facilmente recursos de inteligência artificial às aplicações, como reconhecimento de imagem e análise de texto?",
    "options": [
        "A) Amazon SageMaker",
        "B) Amazon Rekognition",
        "C) Amazon Comprehend",
        "D) Todas as opções acima",
    ],
    "answer": "D) Todas as opções acima",
},
{
    "question": "O que é o AWS Glue?",
    "options": [
        "A) Um serviço de integração de dados totalmente gerenciado para preparação e carregamento de dados",
        "B) Um serviço de computação sem servidor",
        "C) Um serviço de armazenamento em cache",
        "D) Um serviço de balanceamento de carga",
    ],
    "answer": "A) Um serviço de integração de dados totalmente gerenciado para preparação e carregamento de dados",
},
{
    "question": "Qual serviço da AWS é usado para monitorar e gerenciar recursos em tempo real?",
    "options": [
        "A) Amazon CloudWatch",
        "B) AWS CloudTrail",
        "C) AWS Config",
        "D) AWS X-Ray",
    ],
    "answer": "A) Amazon CloudWatch",
},
{
    "question": "O que é o AWS Batch?",
    "options": [
        "A) Um serviço que permite executar trabalhos de computação em lote em escala",
        "B) Um serviço de banco de dados NoSQL",
        "C) Um serviço de armazenamento de objetos",
        "D) Um serviço de entrega de conteúdo",
    ],
    "answer": "A) Um serviço que permite executar trabalhos de computação em lote em escala",
},
{
    "question": "Qual serviço permite gerenciar certificados SSL/TLS para proteger aplicações web?",
    "options": [
        "A) AWS Certificate Manager (ACM)",
        "B) AWS Secrets Manager",
        "C) AWS KMS",
        "D) AWS Shield",
    ],
    "answer": "A) AWS Certificate Manager (ACM)",
},
{
    "question": "O que é o Amazon FSx?",
    "options": [
        "A) Um serviço que fornece sistemas de arquivos totalmente gerenciados otimizados para diferentes cargas de trabalho",
        "B) Um serviço de banco de dados relacional",
        "C) Um serviço de computação sem servidor",
        "D) Um serviço de armazenamento em bloco",
    ],
    "answer": "A) Um serviço que fornece sistemas de arquivos totalmente gerenciados otimizados para diferentes cargas de trabalho",
},
{
    "question": "Qual serviço da AWS permite que você execute código em resposta a eventos sem provisionar ou gerenciar servidores?",
    "options": [
        "A) AWS Lambda",
        "B) Amazon EC2",
        "C) AWS Elastic Beanstalk",
        "D) AWS Batch",
    ],
    "answer": "A) AWS Lambda",
},
{
    "question": "O que é o Amazon Elasticache?",
    "options": [
        "A) Um serviço de cache em memória gerenciado que suporta Redis e Memcached",
        "B) Um serviço de banco de dados relacional",
        "C) Um serviço de armazenamento em bloco",
        "D) Um serviço de entrega de conteúdo",
    ],
    "answer": "A) Um serviço de cache em memória gerenciado que suporta Redis e Memcached",
},
{
    "question": "Qual serviço da AWS oferece um ambiente de desenvolvimento integrado (IDE) baseado na web?",
    "options": [
        "A) AWS Cloud9",
        "B) AWS CodeCommit",
        "C) AWS CodeBuild",
        "D) AWS CodeDeploy",
    ],
    "answer": "A) AWS Cloud9",
},
{
    "question": "O que é o Amazon MQ?",
    "options": [
        "A) Um serviço de mensagem gerenciado compatível com protocolos padrão do setor",
        "B) Um serviço de monitoramento de aplicações",
        "C) Um serviço de banco de dados relacional",
        "D) Um serviço de armazenamento em bloco",
    ],
    "answer": "A) Um serviço de mensagem gerenciado compatível com protocolos padrão do setor",
},
{
    "question": "Qual serviço permite que você implante e gerencie clusters Kubernetes na AWS?",
    "options": [
        "A) Amazon EKS (Elastic Kubernetes Service)",
        "B) Amazon ECS",
        "C) AWS Fargate",
        "D) AWS Lambda",
    ],
    "answer": "A) Amazon EKS (Elastic Kubernetes Service)",
},
{
    "question": "O que é o AWS OpsWorks?",
    "options": [
        "A) Um serviço de gerenciamento de configuração que usa Chef e Puppet",
        "B) Um serviço de monitoramento de aplicações",
        "C) Um serviço de entrega de conteúdo",
        "D) Um serviço de computação sem servidor",
    ],
    "answer": "A) Um serviço de gerenciamento de configuração que usa Chef e Puppet",
},
{
    "question": "Qual serviço da AWS é usado para gerenciamento de identidades e acesso para aplicações móveis e web?",
    "options": [
        "A) Amazon Cognito",
        "B) AWS IAM",
        "C) AWS Directory Service",
        "D) AWS SSO",
    ],
    "answer": "A) Amazon Cognito",
},
{
    "question": "O que é o AWS Elastic Transcoder?",
    "options": [
        "A) Um serviço para transcodificação de arquivos de mídia em diferentes formatos",
        "B) Um serviço de armazenamento em cache",
        "C) Um serviço de banco de dados NoSQL",
        "D) Um serviço de monitoramento de aplicações",
    ],
    "answer": "A) Um serviço para transcodificação de arquivos de mídia em diferentes formatos",
},
{
    "question": "Qual serviço da AWS facilita a transferência de grandes quantidades de dados para o Amazon S3 através da Internet?",
    "options": [
        "A) AWS Transfer for SFTP",
        "B) AWS DataSync",
        "C) AWS Snowball",
        "D) AWS Storage Gateway",
    ],
    "answer": "B) AWS DataSync",
},
{
    "question": "O que é o AWS CodePipeline?",
    "options": [
        "A) Um serviço que automatiza pipelines de entrega contínua",
        "B) Um serviço de controle de código-fonte",
        "C) Um serviço de compilação e teste contínuo",
        "D) Um serviço de implantação automatizada",
    ],
    "answer": "A) Um serviço que automatiza pipelines de entrega contínua",
},
{
    "question": "Qual serviço é usado para enviar e receber e-mails em escala?",
    "options": [
        "A) Amazon SES (Simple Email Service)",
        "B) Amazon SNS",
        "C) Amazon SQS",
        "D) AWS Lambda",
    ],
    "answer": "A) Amazon SES (Simple Email Service)",
},
{
    "question": "O que é o Amazon Cognito Identity Pools?",
    "options": [
        "A) Um recurso que permite fornecer acesso aos usuários aos serviços da AWS diretamente",
        "B) Um serviço de banco de dados relacional",
        "C) Um serviço de computação sem servidor",
        "D) Um serviço de entrega de conteúdo",
    ],
    "answer": "A) Um recurso que permite fornecer acesso aos usuários aos serviços da AWS diretamente",
},
{
    "question": "Qual serviço permite que você descubra, classifique e proteja dados confidenciais armazenados no Amazon S3?",
    "options": [
        "A) Amazon Macie",
        "B) AWS Shield",
        "C) AWS WAF",
        "D) AWS Config",
    ],
    "answer": "A) Amazon Macie",
},
{
    "question": "O que é o AWS Amplify?",
    "options": [
        "A) Um conjunto de ferramentas e serviços para desenvolver aplicações web e móveis escaláveis e seguras",
        "B) Um serviço de banco de dados NoSQL",
        "C) Um serviço de armazenamento em bloco",
        "D) Um serviço de monitoramento de aplicações",
    ],
    "answer": "A) Um conjunto de ferramentas e serviços para desenvolver aplicações web e móveis escaláveis e seguras",
},
{
    "question": "Qual serviço permite hospedar repositórios de pacotes privados e públicos para armazenamento e gerenciamento de artefatos?",
    "options": [
        "A) AWS CodeArtifact",
        "B) AWS CodeCommit",
        "C) AWS CodeBuild",
        "D) AWS CodeDeploy",
    ],
    "answer": "A) AWS CodeArtifact",
},
{
    "question": "O que é o Amazon WorkSpaces?",
    "options": [
        "A) Um serviço de desktop como serviço que permite provisionar desktops virtuais na nuvem",
        "B) Um serviço de armazenamento em bloco",
        "C) Um serviço de banco de dados relacional",
        "D) Um serviço de monitoramento de aplicações",
    ],
    "answer": "A) Um serviço de desktop como serviço que permite provisionar desktops virtuais na nuvem",
},
{
    "question": "Qual serviço da AWS permite gerenciar logs e métricas de recursos e aplicações?",
    "options": [
        "A) Amazon CloudWatch",
        "B) AWS CloudTrail",
        "C) AWS Config",
        "D) AWS X-Ray",
    ],
    "answer": "A) Amazon CloudWatch",
},
{
    "question": "O que é o AWS Artifact?",
    "options": [
        "A) Um portal que fornece acesso a relatórios de conformidade e acordos legais",
        "B) Um serviço de monitoramento de aplicações",
        "C) Um serviço de armazenamento em cache",
        "D) Um serviço de entrega de conteúdo",
    ],
    "answer": "A) Um portal que fornece acesso a relatórios de conformidade e acordos legais",
},
{
    "question": "Qual é o modelo de precificação padrão para serviços da AWS?",
    "options": [
        "A) Contratos de longo prazo com pagamento antecipado",
        "B) Pagamento conforme o uso (pay-as-you-go)",
        "C) Taxa mensal fixa",
        "D) Pagamento apenas no final do contrato",
    ],
    "answer": "B) Pagamento conforme o uso (pay-as-you-go)",
},
{
    "question": "O que são as instâncias reservadas do Amazon EC2?",
    "options": [
        "A) Instâncias que podem ser usadas apenas durante horários específicos",
        "B) Opções de compra que oferecem desconto significativo em troca de um compromisso de uso por um ou três anos",
        "C) Instâncias que são lançadas sob demanda sem compromisso de tempo",
        "D) Instâncias que são interrompidas quando a demanda é alta",
    ],
    "answer": "B) Opções de compra que oferecem desconto significativo em troca de um compromisso de uso por um ou três anos",
},
{
    "question": "Qual ferramenta da AWS permite estimar os custos mensais dos serviços antes de usá-los?",
    "options": [
        "A) AWS Cost Explorer",
        "B) AWS Pricing Calculator",
        "C) AWS Budgets",
        "D) AWS Cost and Usage Reports",
    ],
    "answer": "B) AWS Pricing Calculator",
},
{
    "question": "O que é o AWS Free Tier?",
    "options": [
        "A) Um nível de serviço que oferece uso gratuito ilimitado de todos os serviços da AWS",
        "B) Um nível de serviço que oferece certos recursos gratuitos por 12 meses e outros sempre gratuitos dentro de limites especificados",
        "C) Uma oferta promocional disponível apenas para clientes empresariais",
        "D) Uma opção de suporte premium",
    ],
    "answer": "B) Um nível de serviço que oferece certos recursos gratuitos por 12 meses e outros sempre gratuitos dentro de limites especificados",
},
{
    "question": "Qual opção de suporte da AWS oferece acesso 24/7 ao suporte técnico por telefone e chat, bem como um gerente técnico de conta designado?",
    "options": [
        "A) Suporte Básico",
        "B) Suporte Desenvolvedor",
        "C) Suporte Business",
        "D) Suporte Enterprise",
    ],
    "answer": "D) Suporte Enterprise",
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
    "question": "Qual serviço da AWS é ideal para criar dashboards e relatórios interativos a partir de dados armazenados no Amazon S3?",
    "options": [
        "A) Amazon QuickSight",
        "B) AWS Glue",
        "C) Amazon Athena",
        "D) Amazon Redshift",
    ],
    "answer": "A) Amazon QuickSight",
},
{
    "question": "O que é o AWS Backup?",
    "options": [
        "A) Um serviço que automatiza o backup de dados em serviços da AWS",
        "B) Um serviço de recuperação de desastres",
        "C) Um serviço de armazenamento em cache",
        "D) Um serviço para migrar bancos de dados para a nuvem",
    ],
    "answer": "A) Um serviço que automatiza o backup de dados em serviços da AWS",
},
{
    "question": "Qual serviço da AWS ajuda a gerenciar e controlar o uso de recursos e custos em várias contas da AWS?",
    "options": [
        "A) AWS Organizations",
        "B) AWS Cost Explorer",
        "C) AWS Billing Dashboard",
        "D) AWS Control Tower",
    ],
    "answer": "D) AWS Control Tower",
},
{
    "question": "O que é o Amazon Timestream?",
    "options": [
        "A) Um banco de dados para dados de séries temporais totalmente gerenciado",
        "B) Um serviço de monitoramento de aplicações",
        "C) Um serviço de processamento em tempo real",
        "D) Um serviço para armazenar dados em cache",
    ],
    "answer": "A) Um banco de dados para dados de séries temporais totalmente gerenciado",
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
