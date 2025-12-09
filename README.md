# 🎬 Knowledge Graph de Filmes

## 📋 Sobre o Projeto

Este projeto implementa um **Knowledge Graph (Grafo de Conhecimento)** totalmente do zero, sem usar bibliotecas prontas de grafos. O sistema modela relações entre filmes, diretores, atores e gêneros cinematográficos, permitindo:

- ✅ Criar e manipular um grafo de conhecimento (implementação própria)
- 🔍 Consultar entidades e relacionamentos
- 📊 Realizar análises de centralidade (algoritmos implementados manualmente)
- 🗺️ Encontrar caminhos entre entidades usando BFS
- 📈 Visualizar o grafo de forma interativa em HTML
- 🌐 Exportar visualização interativa e navegável no navegador

**Base de Conhecimento:**
- 37 nós (entidades)
- 37 arestas (relacionamentos)
- 10 filmes clássicos
- 8 diretores renomados
- 13 atores famosos
- 6 gêneros cinematográficos

---

## 🚀 Como Executar

### Pré-requisitos

- Python 3.8 ou superior
- pip (gerenciador de pacotes Python)

### 1️⃣ Clone ou baixe o projeto

```bash
# Se estiver no GitHub:
git clone https://github.com/seu-usuario/knowledge-graph-filmes.git
cd knowledge-graph-filmes

# Ou simplesmente extraia o arquivo ZIP
```

### 2️⃣ Crie um ambiente virtual (recomendado)

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate
```

### 3️⃣ Instale as dependências

```bash
pip install -r requirements.txt
```

### 4️⃣ Execute o programa

```bash
python movie_knowledge_graph
```

O programa irá:
1. Criar a base de conhecimento
2. Executar análises de centralidade
3. Gerar um arquivo HTML interativo em `outputs/interactive_graph.html`
4. Abrir automaticamente o grafo interativo no navegador

---

## 📦 Dependências

O projeto utiliza as seguintes bibliotecas:

```
pandas>=2.0.0          # Manipulação de dados em tabelas
pyvis>=0.3.2           # Visualização interativa em HTML
```

**Nota importante:** Este projeto NÃO usa NetworkX ou outras bibliotecas de grafos. Toda a estrutura de grafo e algoritmos foram implementados do zero!

---

## 🎯 Funcionalidades Implementadas

### ⚠️ IMPORTANTE: Implementação do Zero

**Este projeto NÃO usa bibliotecas prontas de grafos!** Toda a estrutura e algoritmos foram implementados manualmente:

- ✅ **Estrutura de Grafo**: Lista de adjacências com dicionários Python
- ✅ **BFS (Busca em Largura)**: Para encontrar caminho mais curto
- ✅ **Degree Centrality**: Cálculo manual usando fórmula matemática
- ✅ **Betweenness Centrality**: Algoritmo de Brandes implementado do zero
- ✅ **Closeness Centrality**: BFS + cálculo de distâncias médias
- ✅ **Operações CRUD**: Adicionar/remover nós e arestas
- ✅ **Visualização Interativa**: Grafo navegável em HTML usando Pyvis

**Apenas Pyvis é usado para visualização HTML** (não faz cálculos de grafo).

### Manipulação do Grafo

```python
kg = MovieKnowledgeGraph()

# Adicionar elementos
kg.add_node('Titanic', node_type='movie')
kg.add_edge('Titanic', 'James Cameron', 'directed_by')

# Remover elementos
kg.remove_node('Titanic')
kg.remove_edge('Inception', 'Leonardo DiCaprio')
```

### Consultas

```python
# Consultar informações de um nó
kg.query_node('Christopher Nolan')

# Verificar relacionamento entre dois nós
kg.query_relationship('The Matrix', 'Keanu Reeves')

# Encontrar caminho mais curto
kg.find_shortest_path('The Godfather', 'Sci-Fi')

# Listar todos os nós
kg.list_all_nodes()

# Listar tipos de relacionamentos
kg.list_all_relationships()
```

### Análises

```python
# Estatísticas gerais
kg.get_statistics()

# Análise de centralidade
kg.centrality_analysis()

# Visualização interativa (HTML)
kg.visualize_interactive(output_file='outputs/interactive_graph.html')
```

**Recursos da Visualização Interativa:**
- 🖱️ **Arraste os nós** para reorganizar o grafo
- 🔍 **Zoom** com a roda do mouse
- 🎨 **Cores diferentes** para cada tipo de entidade (filmes, atores, diretores, gêneros)
- 📋 **Informações ao passar o mouse** sobre nós e arestas
- 🌐 **Navegável no navegador** - funciona offline após gerado

---

## 📊 Exemplo de Saída

Ao executar o programa, você verá:

```
MOVIE KNOWLEDGE GRAPH

Graph created: 37 nodes, 37 edges

Query 1 - Node info (Andrei Tarkovsky):
  Degree: 4
  Neighbors: Stalker, Mirror, Solaris...

Query 2 - Relationship (Stalker -> Andrei Tarkovsky):
  directed_by

Query 3 - Shortest path (Stalker -> Mulholland Drive):
  Stalker -> Andrei Tarkovsky -> Mulholland Drive

Query 4 - Top 5 Degree Centrality:
  Andrei Tarkovsky: 0.111
  Ingmar Bergman: 0.083
  Marcello Mastroianni: 0.083
  ...

Generating interactive visualization...
Saved: outputs/interactive_graph.html
```

Uma visualização interativa será gerada e aberta automaticamente no seu navegador!

---

## 📁 Estrutura do Projeto

```
KnowledgeGraphs/
│
├── movie_knowledge_graph      # Código principal (sem extensão .py)
├── requirements.txt           # Dependências (pandas e pyvis)
├── README.md                  # Este arquivo
│
├── lib/                       # Bibliotecas JavaScript para visualização
│   ├── bindings/
│   │   └── utils.js
│   ├── tom-select/
│   └── vis-9.1.2/
│
└── outputs/                   # Saídas geradas (criada automaticamente)
    └── interactive_graph.html # Visualização interativa do grafo
```

---

## 🎓 Conceitos Abordados

Este projeto demonstra:

1. **Knowledge Graphs**: Representação semântica de conhecimento
2. **Teoria de Grafos**: Nós, arestas, caminhos, centralidade
3. **Estruturas de Dados**: Implementação de grafos com dicionários
4. **Algoritmos de Grafos**:
   - BFS (Busca em Largura)
   - Cálculos de centralidade (Degree, Betweenness, Closeness)
   - Algoritmo de Brandes
5. **Visualização Interativa**: Grafos navegáveis em HTML
6. **Python Avançado**: Classes, dicionários, collections.deque

---

## 🔧 Personalização

### Adicionar seus próprios filmes

Edite a função `create_base_knowledge()` no arquivo `movie_knowledge_graph`:

```python
head = [
    # Adicione seus filmes aqui
    'Seu Filme', 'Seu Filme', ...
]

relation = [
    'directed_by', 'stars', ...
]

tail = [
    'Seu Diretor', 'Seu Ator', ...
]
```

### Alterar cores da visualização

Na função `visualize_interactive()`:

```python
# Personalize as cores por tipo de nó
node_colors = {
    'movie': '#FF6B6B',      # Vermelho para filmes
    'actor': '#4ECDC4',      # Azul para atores
    'director': '#FFE66D',   # Amarelo para diretores
    'genre': '#95E1D3'       # Verde para gêneros
}
```

---

## 📖 Documentação Adicional

- **Pyvis Documentation**: https://pyvis.readthedocs.io/
- **Pandas Documentation**: https://pandas.pydata.org/docs/
- **Tutorial Original**: Lopez Yse, D. "Knowledge Graphs from scratch with Python"

---

## 🐛 Troubleshooting

### Erro: "ModuleNotFoundError: No module named 'pandas'" ou 'pyvis'

**Solução:** Instale as dependências:
```bash
pip install -r requirements.txt
```

### Erro: "ValueError: Invalid node"

**Solução:** Verifique se o nó existe antes de consultar:
```python
kg.list_all_nodes()  # Veja os nós disponíveis
```

### O arquivo HTML não abre automaticamente

**Solução:** Abra manualmente o arquivo:
```bash
# Windows
start outputs\interactive_graph.html

# Linux/Mac
open outputs/interactive_graph.html
```

Ou simplesmente navegue até a pasta `outputs/` e dê duplo clique em `interactive_graph.html`

---

## 👨‍💻 Autor

**Gabriel Lins Alves do Nascimento**
- 🐙 GitHub: [@gabriel1ns](https://github.com/gabriel1ns)
- 📁 Repositório: [KnowledgeGraphs](https://github.com/gabriel1ns/KnowledgeGraphs)