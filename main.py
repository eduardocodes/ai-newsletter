from crewai import Crew, Process
from agents import AINewsLetterAgents
from file_io import save_markdown
from tasks import AINewsLetterTasks
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()

# Agents e Tasks
agents = AINewsLetterAgents()
tasks = AINewsLetterTasks()

# Instanciar ChatGPT
OpenaiGPT4 = ChatOpenAI(
    model="gpt-4"
)

# Configurar agents
editor = agents.editor_agent()
news_fetcher = agents.news_fetcher_agent()
news_analyzer = agents.news_analyzer_agent()
newsletter_compiler = agents.newsletter_compiler_agent()

# Configurar tasks
fetch_news_task = tasks.fetch_news_task(news_fetcher)
analyze_news_task = tasks.analyze_news_task(news_analyzer, [fetch_news_task])
compile_newsletter_task = tasks.compile_newsletter_task(
    newsletter_compiler, [analyze_news_task], save_markdown)

# Configurar crew
crew = Crew(
    agents=[editor, news_fetcher, news_analyzer, newsletter_compiler],
    tasks=[fetch_news_task, analyze_news_task, compile_newsletter_task],
    process=Process.hierarchical,
    manager_llm=OpenaiGPT4,
    verbose=2
)

# Iniciar trabalho em equipe
results = crew.kickoff()

# Printar os resultados
print('Results:')
print(results)
