from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import FileWriterTool
from dotenv import load_dotenv

load_dotenv()

@CrewBase
class Stepbytep():
	"""Stepbytep crew"""

	agents_config = 'config/agents.yaml'
	tasks_config = 'config/tasks.yaml'

	@agent
	def blog_generator(self) -> Agent:
		return Agent(
			config=self.agents_config['blog_generator'],
			verbose=True
		)

	@agent
	def file_writer(self) -> Agent:
		return Agent(
			config=self.agents_config['file_writer'],
			tools=[FileWriterTool()],
			verbose=True
		)

	@task
	def generate_blog_task(self) -> Task:
		return Task(
			config=self.tasks_config['ai_blog_write_task'],
			agent=self.blog_generator()
		)

	@task
	def write_file_task(self) -> Task:
		return Task(
			config=self.tasks_config['file_write_task'],
			agent=self.file_writer()
		)

	@crew
	def crew(self) -> Crew:
		"""Creates the Stepbytep crew"""
		return Crew(
			agents=self.agents,
			tasks=self.tasks,
			process=Process.sequential,
			verbose=True,
		)
