from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import random

def scroll_suave(navegador, duracao=3):
    """Rola a página suavemente até o final e volta ao topo"""
    altura_total = navegador.execute_script("return document.body.scrollHeight")
    passos = 50
    for i in range(passos):
        navegador.execute_script(f"window.scrollTo(0, {(altura_total/ passos)*(i+1)})")
        time.sleep(duracao / passos)
    time.sleep(random.uniform(0.5, 1.5))  # pausa aleatória
    # volta ao topo
    for i in range(passos):
        navegador.execute_script(f"window.scrollTo(0, {altura_total - (altura_total/ passos)*(i+1)})")
        time.sleep(duracao / passos)
    time.sleep(random.uniform(0.5, 1.5))

def automacao_github_site():
    print("Iniciando o navegador...")
    servico = Service(ChromeDriverManager().install())
    navegador = webdriver.Chrome(service=servico)
    navegador.maximize_window()

    # ===============================
    # Acessa sua aba de Repositories
    # ===============================
    url_repos = "https://github.com/pauloalexandredeoliveira?tab=repositories"
    navegador.get(url_repos)
    time.sleep(random.uniform(2, 4))

    # ===============================
    # Clica em todos os repositórios da lista
    # ===============================
    repositorios = navegador.find_elements(By.XPATH, "//li[@itemprop='owns']//h3/a")
    print(f"{len(repositorios)} repositórios encontrados.")

    for repo in repositorios:
        nome_repo = repo.text
        print(f"Abrindo repositório: {nome_repo}")
        repo.click()
        time.sleep(random.uniform(2, 4))
        scroll_suave(navegador, duracao=5)
        navegador.back()  # volta para a lista de repositórios
        time.sleep(random.uniform(2, 4))
        repositorios = navegador.find_elements(By.XPATH, "//li[@itemprop='owns']//h3/a")  # atualiza lista

    # ===============================
    # Acessa seu site Monteiros-Doces-Gourmet
    # ===============================
    site_doces = "https://pauloalexandredeoliveira.github.io/Monteiros-Doces-Gourmet/"
    print(f"Acessando site: {site_doces}")
    navegador.get(site_doces)
    time.sleep(random.uniform(2, 4))
    scroll_suave(navegador, duracao=7)

    # ===============================
    # Finaliza
    # ===============================
    navegador.quit()
    print("Automação concluída!")

if __name__ == "__main__":
    automacao_github_site()
