import datetime


class Repositorio:
    def __init__(self):
        self.equipamentos = [
            {"id": 1, "nome": "Notebook Dell",  "tipo": "notebook", "disponivel": True},
            {"id": 2, "nome": "Projetor Epson", "tipo": "projetor", "disponivel": True},
            {"id": 3, "nome": "Cabo HDMI",      "tipo": "cabo",      "disponivel": True},
        ]
        self.emprestimos_registrados = []


class Notificador:
    def notificar_emprestimo(self, email, data_devolucao):
        print(f"[EMAIL] {email} — empréstimo até {data_devolucao}")

    def notificar_devolucao(self, email, multa):
        print(f"[EMAIL] {email} — multa R${multa:.2f}")

    def notificar_atraso(self, email):
        print(f"[EMAIL] {email} — você está em atraso!")


class Sistema:

    def __init__(self, repositorio, notificador):
        self.repositorio = repositorio
        self.notificador = notificador

    def registrar(self, equipamento_id, usuario_nome, usuario_email, dias):
        equipamento = None

        for e in self.repositorio.equipamentos:
            if e["id"] == equipamento_id:
                equipamento = e
                break

        if equipamento is None or not equipamento["disponivel"]:
            print("Equipamento inválido ou indisponível")
            return False

        data_emprestimo = datetime.date.today()
        data_devolucao = data_emprestimo + datetime.timedelta(days=dias)

        emprestimo = {
            "id": len(self.repositorio.emprestimos_registrados) + 1,
            "equipamento_id": equipamento_id,
            "equipamento_nome": equipamento["nome"],
            "tipo": equipamento["tipo"],
            "usuario_nome": usuario_nome,
            "usuario_email": usuario_email,
            "data_emprestimo": data_emprestimo,
            "data_devolucao": data_devolucao,
            "devolvido": False,
        }

        self.repositorio.emprestimos_registrados.append(emprestimo)
        equipamento["disponivel"] = False

        self.notificador.notificar_emprestimo(
            usuario_email,
            data_devolucao
        )

        return True

    def devolver(self, emprestimo_id):
        emprestimo = None

        for e in self.repositorio.emprestimos_registrados:
            if e["id"] == emprestimo_id:
                emprestimo = e
                break

        if emprestimo is None or emprestimo["devolvido"]:
            print("Empréstimo inválido ou já devolvido")
            return

        emprestimo["devolvido"] = True

        hoje = datetime.date.today()
        atraso = (hoje - emprestimo["data_devolucao"]).days

        multa = 0

        if atraso > 0:
            if emprestimo["tipo"] == "notebook":
                multa = atraso * 10.0
            elif emprestimo["tipo"] == "projetor":
                multa = atraso * 15.0
            elif emprestimo["tipo"] == "cabo":
                multa = atraso * 2.0

        for e in self.repositorio.equipamentos:
            if e["id"] == emprestimo["equipamento_id"]:
                e["disponivel"] = True

        self.notificador.notificar_devolucao(
            emprestimo["usuario_email"],
            multa
        )

        print(f"Devolução registrada. Multa: R${multa:.2f}")

    def listar_atrasados(self):
        hoje = datetime.date.today()

        for e in self.repositorio.emprestimos_registrados:
            if not e["devolvido"] and e["data_devolucao"] < hoje:

                atraso = (hoje - e["data_devolucao"]).days

                multa = 0

                if e["tipo"] == "notebook":
                    multa = atraso * 10.0
                elif e["tipo"] == "projetor":
                    multa = atraso * 15.0
                elif e["tipo"] == "cabo":
                    multa = atraso * 2.0

                print(f"{e['usuario_nome']} — {atraso} dias — R${multa:.2f}")

                self.notificador.notificar_atraso(
                    e["usuario_email"]
                )


def main():

    repositorio = Repositorio()
    notificador = Notificador()

    s = Sistema(repositorio, notificador)

    while True:
        print("\n1-Registrar  2-Devolver  3-Atrasados  0-Sair")

        op = input("Opção: ")

        if op == "1":
            s.registrar(
                int(input("ID equipamento: ")),
                input("Nome: "),
                input("Email: "),
                int(input("Dias: "))
            )

        elif op == "2":
            s.devolver(int(input("ID empréstimo: ")))

        elif op == "3":
            s.listar_atrasados()

        elif op == "0":
            break


if __name__ == "__main__":
    main()