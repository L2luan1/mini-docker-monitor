"#Mini Docker Monitor" 
# Mini Docker Monitor

Este projeto é um monitor simples de containers Docker desenvolvido em Python utilizando o Docker SDK. Ele permite:
- Listar containers ativos.
- Monitorar o uso de recursos como CPU, memória e rede.

## 🛠 Funcionalidades

1. **Listar Containers**:
   - Exibe todos os containers ativos no Docker.
   - Uso:
     ```bash
     python monitor.py --list
     ```

2. **Monitorar Recursos**:
   - Monitora consumo de CPU, memória e rede dos containers.
   - Uso:
     ```bash
     python monitor.py --monitor
     ```

## 📂 Estrutura do Código

- `monitor.py`: Contém o código principal para listar e monitorar containers.
- `README.md`: Documento de descrição do projeto.

## 🚀 Como começar

1. Instale o Python na sua máquina.
2. Instale o Docker e certifique-se de que está em execução.
3. Instale o Docker SDK com:
   ```bash
   pip install Docker


---

### 🖥 **Passo 2: Salvar e testar**
1. Após escrever o conteúdo no editor, salve o arquivo.
2. Você pode visualizar o `README.md` diretamente no GitHub após enviar o projeto.

---

### 🚦 **Passo 3: Subir para o GitHub**
1. Adicione o `README.md` ao Git:
   ```bash
   git add README.md