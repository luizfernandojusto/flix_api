from django.core.management.base import BaseCommand
import csv
from datetime import datetime

from autor.models import Autor


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument(
            "file_name", type=str, help="Nome do arquivo CSV com autores"
        )

    def handle(self, *args, **options):
        file_name = options["file_name"]

        with open(file_name, "r", encoding="utf-8") as file:
            leitura = csv.DictReader(file)
            for r in leitura:
                nome = r["Nome"]
                data_nascimento = datetime.strptime(
                    r["Data de Nascimento"], "%Y-%m-%d"
                ).date()
                nacionalidade = r["Nacionalidade"]

                self.stdout.write(self.style.NOTICE(nome))

                Autor(
                    nome=nome,
                    data_nascimento=data_nascimento,
                    nacionalidade=nacionalidade,
                ).save()

            self.stdout.write(self.style.SUCCESS("AUTORES IMPORTADO COM SUCESSO"))
