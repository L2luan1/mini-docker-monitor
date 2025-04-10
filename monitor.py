
import docker

def list_containers():
    """
    Lista os containers ativos no Docker.
    """
    try:
        client = docker.from_env()  # Conecta ao Docker
        containers = client.containers.list()  # Lista os containers ativos
        if containers:
            print("Containers ativos:")
            for container in containers:
                print(f"- Nome: {container.name}, ID: {container.id[:12]}, Status: {container.status}")
        else:
            print("Nenhum container ativo no momento.")
    except Exception as e:
        print(f"Erro ao acessar o Docker: {e}")

if __name__ == "__main__":
    list_containers()

    import docker

def monitor_resources():
    """
    Monitorar o consumo de recursos dos containers ativos.
    """
    try:
        client = docker.from_env()
        containers = client.containers.list()
        if containers:
            print("Monitorando recursos dos containers ativos:")
            for container in containers:
                stats = container.stats(stream=False)  # Obtém dados de estatísticas do container
                cpu_usage = stats["cpu_stats"]["cpu_usage"]["total_usage"]
                memory_usage = stats["memory_stats"]["usage"]
                network_rx = stats["networks"]["eth0"]["rx_bytes"]
                network_tx = stats["networks"]["eth0"]["tx_bytes"]
                print(f"- Nome: {container.name}")
                print(f"  CPU: {cpu_usage} nanosegundos")
                print(f"  Memória: {memory_usage / 1024:.2f} KB")
                print(f"  Rede (Recebido): {network_rx / 1024:.2f} KB")
                print(f"  Rede (Enviado): {network_tx / 1024:.2f} KB\n")
        else:
            print("Nenhum container ativo no momento para monitorar.")
    except Exception as e:
        print(f"Erro ao acessar o Docker: {e}")

if __name__ == "__main__":
    monitor_resources()