from crewai import Agent
from tools.search_tools import SearchTools


class AINewsLetterAgents():
    def editor_agent(self):
        return Agent(
            role='Editor',
            goal='Supervisionar a criação do boletim informativo de IA',
            backstory="""Com um olhar atento aos detalhes e uma paixão por contar histórias, você garante que o boletim informativo
            não apenas informa, mas também envolve e inspira os leitores.""",
            allow_delegation=True,
            verbose=True,
            max_iter=15
        )

    def news_fetcher_agent(self):
        return Agent(
            role='NewsFetcher',
            goal='Obtenha as principais notícias sobre IA do dia',
            backstory="""Como detetive digital, você vasculha a Internet em busca dos desenvolvimentos mais recentes e impactantes no mundo da IA, garantindo que nossos leitores estejam sempre informados.""",
            tools=[SearchTools.search_internet],
            verbose=True,
            allow_delegation=True,
        )

    def news_analyzer_agent(self):
        return Agent(
            role='NewsAnalyzer',
            goal='Analise cada notícia e gere um resumo detalhado da redução',
            backstory="""Com um olhar crítico e um talento especial para destilar informações complexas, você fornece informações perspicazes análises de notícias sobre IA, tornando-as acessíveis e envolventes para nosso público.""",
            tools=[SearchTools.search_internet],
            verbose=True,
            allow_delegation=True,
        )

    def newsletter_compiler_agent(self):
        return Agent(
            role='NewsletterCompiler',
            goal='Compile as notícias analisadas em um formato final de boletim informativo',
            backstory="""Como arquiteto final do boletim informativo, você organiza e formata meticulosamente o conteúdo,
            garantindo uma apresentação coerente e visualmente apelativa que cative os nossos leitores. Certifique-se de seguir
            diretrizes de formato de boletim informativo e manter a consistência por toda parte.""",
            verbose=True,
        )
