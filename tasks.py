from crewai import Task
from datetime import datetime


class AINewsLetterTasks():
    def fetch_news_task(self, agent):
        return Task(
            description=f'Obtenha as principais notícias sobre IA das últimas 24 horas. A hora atual é {datetime.now()}.',
            agent=agent,
            async_execution=True,
            expected_output="""Uma lista dos principais títulos de notícias sobre IA, URLs e um breve resumo de cada história das últimas 24 horas. 
                Examplo Output: 
                [
                    {  'title': 'IA ganha destaque em comerciais do Super Bowl', 
                    'url': 'https://example.com/story1', 
                    'summary': 'A IA causou impacto nos comerciais do Super Bowl deste ano...'
                    }, 
                    {{...}}
                ]
            """
        )

    def analyze_news_task(self, agent, context):
        return Task(
            description='Analise cada notícia e garanta que haja pelo menos 5 artigos bem formatados',
            agent=agent,
            async_execution=True,
            context=context,
            expected_output="""Uma análise formatada para cada notícia, incluindo um resumo, marcadores detalhados,
                e uma seção "Por que é importante". Deverão ser no mínimo 5 artigos, cada um seguindo o formato adequado.
                Exemplo Output: 
                '## IA ganha destaque em comerciais do Super Bowl\n\n
                **O resumo:
                ** A IA causou impacto nos comerciais do Super Bowl deste ano...\n\n
                **Os detalhes:**\n\n
                - O spot Copilot da Microsoft apresentou seu assistente de IA...\n\n
                **Por que isso importa:** Embora os anúncios relacionados à IA tenham crescido desenfreadamente no ano passado, sua presença no Super Bowl é um grande momento popular.\n\n'
            """
        )

    def compile_newsletter_task(self, agent, context, callback_function):
        return Task(
            description='Compilar a newsletter',
            agent=agent,
            context=context,
            expected_output="""Uma newsletter completa em formato markdown, com estilo e layout consistentes.
                Examplo Output: 
                '# Principais histórias em IA hoje:\\n\\n
                - IA ganha destaque em comerciais do Super Bowl\\n
                - Altman busca TRILHÕES para iniciativa global de chips de IA\\n\\n

                ## IA ganha destaque em comerciais do Super Bowl\\n\\n
                **O resumo:** A IA causou impacto nos comerciais do Super Bowl deste ano...\\n\\n
                **Os detalhes:**...\\n\\n
                **Por que isso importa::**...\\n\\n
                ## Altman busca TRILHÕES para iniciativa global de chips de IA\\n\\n
                **O resumo:** O CEO da OpenAI, Sam Altman, está supostamente tentando levantar TRILHÕES de dólares...\\n\\n'
                **Os detalhes:**...\\n\\n
                **Por que isso importa::**...\\n\\n
            """,
            callback=callback_function
        )
