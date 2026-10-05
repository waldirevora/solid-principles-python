'''
SINGLE RESPONSIBILITY PRINCIPLE

O código foi organizado seguindo o Princípio da Responsabilidade Única.

Cada classe possui uma responsabilidade específica, separando o gerenciamento
de tarefas, a conexão com a API, o envio de notificações e a geração de relatórios.
'''

# Responsabilidade: conexão com a API
class ApiConnection:
    def connect_api(self):
        pass


# Responsabilidade: gerenciamento das tarefas
class TaskHandler:
    def create_task(self):
        pass

    def update_task(self):
        pass

    def remove_task(self):
        pass


# Responsabilidade: envio de notificações
class NotificationService:
    def send_notification(self):
        pass


# Responsabilidade: geração e envio de relatórios
class ReportService:
    def generate_report(self):
        pass

    def send_report(self):
        pass