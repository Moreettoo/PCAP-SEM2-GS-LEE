import json
from classes import Perfil, Competencia, Carreira 

def salvar_json(dados, arquivo):
    with open(arquivo, 'w') as f:
        json.dump(dados, f)

def carregar_json(arquivo):
    try:
        with open(arquivo, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return [] 

def gerar_recomendacoes(perfil, carreiras):
    recomendacoes = []
    for carreira in carreiras:
        compatibilidade = 0
        total = 0
        for comp, nivel in carreira.competencias_necessarias.items():
            if comp in perfil.competencias:
                if perfil.competencias[comp] >= nivel:
                    compatibilidade += 1
            total += 1
        if compatibilidade / total >= 0.7: 
            recomendacoes.append(carreira.nome)
    return recomendacoes

def menu():
    perfis = carregar_json('perfis.json')
    carreiras = carregar_json('carreiras.json')
    
    perfis_obj = [Perfil(p['nome'], p['competencias']) for p in perfis]
    carreiras_obj = [Carreira(c['nome'], c['competencias_necessarias']) for c in carreiras]
    
    while True:
        print("\n--- Sistema de Orientação de Carreiras ---")
        print("1. Cadastrar Perfil")
        print("2. Ver Recomendações")
        print("3. Sair")
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            nome = input("Nome do perfil: ")
            competencias = {}
            print("Digite competências (ex: logica 8, criatividade 7). Digite 'fim' para parar.")
            while True:
                entrada = input("Competência e nível: ")
                if entrada == "fim":
                    break
                partes = entrada.split()
                if len(partes) == 2:
                    competencias[partes[0]] = int(partes[1])
            perfil = Perfil(nome, competencias)
            perfis_obj.append(perfil)
            perfis.append({"nome": nome, "competencias": competencias})
            salvar_json(perfis, 'perfis.json')
            print("Perfil cadastrado!")
        
        elif opcao == "2":
            nome = input("Nome do perfil para recomendações: ")
            perfil = None
            for p in perfis_obj:
                if p.nome == nome:
                    perfil = p
                    break
            if perfil:
                recs = gerar_recomendacoes(perfil, carreiras_obj)
                if recs:
                    print("Carreiras recomendadas:")
                    for r in recs:
                        print("- " + r)
                else:
                    print("Nenhuma carreira recomendada. Melhore suas competências!")
            else:
                print("Perfil não encontrado.")
        
        elif opcao == "3":
            break
        else:
            print("Opção inválida.")

carreiras_iniciais = [
    {"nome": "Desenvolvedor de Software", "competencias_necessarias": {"logica": 8, "criatividade": 6}},
    {"nome": "Designer Gráfico", "competencias_necessarias": {"criatividade": 9, "adaptabilidade": 7}},
    {"nome": "Gerente de Projetos", "competencias_necessarias": {"colaboracao": 8, "adaptabilidade": 7}}
]
salvar_json(carreiras_iniciais, 'carreiras.json')

if __name__ == "__main__":
    menu()