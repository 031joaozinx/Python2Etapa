# Atividade Aula 12 — Model, Controller e View (StreamFlix)

**Disciplina:** Python / Flask  
**Profª:** Janaína Duarte  
**Projeto:** `flask/Aula12/`  
**Objetivo:** Explorar o código, localizar arquivos e explicar o que cada camada faz.

---

## Como responder

1. Abra a pasta `flask/Aula12/` no editor ou GitHub.
2. Navegue pelas pastas `models/`, `controllers/` e `views/`.
3. Rode o site (`python app.py`) quando a pergunta pedir para testar no navegador.
4. Responda com **caminho do arquivo** + **explicação em suas palavras**.

**Identificação**

- Nome: Joao Lucas Santos
- Turma: 3b1

---

## Bloco A — Model (perguntas 1 a 10)

**1.** Em qual pasta ficam as classes que representam tabelas do banco SQLite? Cite o caminho.
Pasta models/.Caminho: flask/Aula12/models/

**2.** Qual é o nome do arquivo de banco criado quando o app roda? Em qual arquivo Python essa configuração está?
Arquivo streamflix.db (ou database.db). A configuração está no arquivo raiz flask/Aula12/app.py

**3.** Quais classes Model existem no projeto (nome das classes)? Em quais arquivos `.py` cada uma está?
FilmeFavorito no arquivo models/filme_favorito.py
HistoricoBusca no arquivo models/historico_busca.py

**4.** De qual superclasse `FilmeFavorito` e `HistoricoBusca` herdam? O que elas ganham automaticamente por herança (cite 3 campos)?
 Herdam de db.Model. Elas ganham os campos id, titulo e data_criacao (ou criado_em)

**5.** Qual é o `__tablename__` da tabela de favoritos? Por que usamos `__tablename__` em vez de só o nome da classe?
filmes_favoritos
Usamos Para definir explicitamente o nome da tabela física em letras minúsculas e plural no banco de dados, evitando que o framework crie a tabela com o nome exato da classe em CamelCase.

**6.** No model `FilmeFavorito`, qual coluna guarda o id do filme vindo da API TMDB? Ela tem alguma restrição especial (`unique`, `nullable`)?
 Guarda na coluna tmdb_id (ou filme_id). Ela possui as restrições unique=True e nullable=False

**7.** Abra `models/filme_favorito.py`. O que o método `@classmethod adicionar` faz passo a passo? O que acontece se o filme já existir nos favoritos?
1-Recebe os dados do filme
2-Faz uma busca com query.filter_by para ver se o ID já existe
3-Se já existir: Ignora a inserção ou retorna o objeto existente
4-Se não existir: Cria a instância, adiciona com db.session.add() e salva com db.session.commit().

**8.** Onde está o método que lista as últimas 8 buscas? Qual é o nome da classe e do método?
Classe: HistoricoBusca
Método: listar_recentes (ou obter_ultimas)
Arquivo: models/historico_busca.py

**9.** O model grava dados da API TMDB inteira ou só alguns campos espelhados? Cite 4 campos salvos em `FilmeFavorito`.
Só alguns campos espelhados. Quatro campos salvos: tmdb_id, titulo, cartaz_path (ou poster_path) e nota_avaliacao

**10.** Em `models/__init__.py`, o que é exportado além de `db`? Por que o controller importa `from models import FilmeFavorito` em vez de importar o arquivo inteiro da pasta?
Exporta as classes FilmeFavorito e HistoricoBusca. O controller importa direto do __init__.py para manter o código limpo e centralizado, evitando caminhos longos de arquivos individuais.

---

## Bloco B — Controller (perguntas 11 a 20)

**11.** Quantos Blueprints existem no projeto? Cite o **nome** de cada um e o **url_prefix** (se tiver).
Existe 3 Blueprints
filmes_bp (prefixo /filmes)
favoritos_bp (prefixo /favoritos)
main_bp ou home_bp (prefixo /)

**12.** Em qual arquivo está a rota `/filmes/populares`? Qual é o nome da função Python que responde essa URL?
Arquivo: controllers/filmes_controller.py 
Função: def populares():

**13.** O que a função `populares()` faz antes de chamar `render_template`? Cite duas chamadas (Model, Service ou API).
Chama tmdb_api.obter_populares() para buscar os dados na API externa
Chama FilmeFavorito.query.all() para verificar quais já estão favoritados

**14.** Quando o usuário busca um filme em `/filmes/buscar`, qual controller registra o termo no banco? Qual model é usado e em qual linha aproximada?
 O filmes_controller.py. Usa o model HistoricoBusca na linha aproximada 20.

**15.** Abra `controllers/favoritos_controller.py`. Qual método HTTP é exigido para adicionar favorito (`GET` ou `POST`)? Qual a URL completa de exemplo para adicionar o filme id 550?
Método: POST
URL: http://127.0.0

**16.** No `filmes_controller.py`, rota `detalhe(filme_id)`: o que acontece se `api.detalhe(filme_id)` retornar `None`?
 O controller faz uma checagem if filme is None: e dispara a função abort(404), exibindo uma página de erro.

**17.** Onde os Blueprints são **registrados** no Flask? Cite o arquivo e o comando usado (3 registros).
app.register_blueprint(main_bp)
app.register_blueprint(filmes_bp)
app.register_blueprint(favoritos_bp)


**18.** Qual controller cuida da página inicial `/`? Quais variáveis ele envia para o template `index.html`?
controllers/main_controller.py (ou home_controller.py). Envia as variáveis populares (lista de filmes) e historico (últimas buscas).

**19.** A pasta `services/tmdb_api.py` é Model, Controller ou View? Justifique: quem chama essa classe e para quê?
 uma classe de Serviço/Helper. Quem chama são os Controllers para fazer as requisições HTTP e entregar os dados do TMDB formatados

**20.** No controller de busca, de onde vem o termo digitado quando o usuário usa o formulário da home (`index.html`)? É `request.form` ou `request.args`? Explique a diferença nesse projeto.
Vem de request.args. O formulário usa o método GET, enviando o termo visível na URL (ex: ?q=termo), por isso acessamos via request.args.get(). O request.form seria usado apenas se o método fosse POST

---

## Bloco C — View (perguntas 21 a 30)

**21.** Onde ficam os templates HTML? Qual caminho completo da pasta?
Pasta de visualização
Caminho: flask/Aula12/views/templates/

**22.** Qual template é a “base” de todas as páginas (layout com menu)? Como os outros templates usam esse layout (qual comando Jinja)?
Template base: views/templates/layout.html. Os outros usam o comando Jinja {% extends 'layout.html' %}

**23.** Abra `views/templates/layout.html`. Liste os 5 links do menu e o `url_for` de cada um.
Home: {{ url_for('main.index') }}
Populares: {{ url_for('filmes.populares') }}
Favoritos: {{ url_for('favoritos.lista') }}
Histórico: {{ url_for('main.historico') }}
Sobre: {{ url_for('main.sobre') }}

**24.** Qual arquivo HTML exibe a seção **“Onde assistir (Brasil)”**? De onde vem a variável `streaming` usada nessa tela?
Arquivo: views/templates/filmes/detalhe.html
Origem: Vem do controller de detalhes, que puxa os dados de provedores da API do TMDB filtrados para a região do Brasil (BR)

**25.** O arquivo `filmes/_card.html` é uma página inteira ou um pedaço reutilizado? Quem inclui esse arquivo e com qual tag Jinja?
    É um pedaço reutilizável (parcial). É incluído por páginas como index.html usando a tag {% include 'filmes/_card.html' %}

**26.** Em `filmes/detalhe.html`, como a View sabe se o filme já está nos favoritos? Qual variável booleana/objeto controla o botão “Salvar” vs “Remover”?
Através de uma busca prévia no banco feita pelo controller. A variável que controla o botão é a booleana favoritado (usando {% if favoritado %})

**27.** Onde está o CSS do site? Como o `layout.html` carrega esse arquivo (função Flask/Jinja)?
Fica em views/static/css/style.css. O layout.html carrega usando: {{ url_for('static', filename='css/style.css') }}

**28.** Na listagem de favoritos (`favoritos/lista.html`), qual loop Jinja percorre os registros? Cite 3 campos exibidos na tabela.
Loop: {% for filme in favoritos %}
Campos: filme.titulo, filme.nota_avaliacao e filme.data_criacao

**29.** O que significa `{% if modo_demo %}` no layout? Quem disponibiliza essa variável para **todos** os templates?
Significa uma condicional para ativar o modo de demonstração do site. Quem disponibiliza para todos os templates é o @app.context_processor no arquivo app.py

**30.** Desenhe ou descreva o fluxo completo quando o aluno clica em **“Salvar favorito”** no detalhe do filme, indicando **View → Controller → Model** (e redirect de volta). Cite arquivos envolvidos.
View (filmes/detalhe.html): Usuário clica em "Salvar" e envia um formulário POST.
Controller (controllers/favoritos_controller.py): Recebe a requisição e os dados do filme.
Model (models/filme_favorito.py): O controller executa FilmeFavorito.adicionar(), que grava no banco streamflix.db.
Redirect: O controller executa um redirect(url_for('filmes.detalhe')) atualizando a tela do usuário.

---

## Entrega

- Arquivo `.txt` ou `.md` com as 30 respostas 

**Critério:** respostas que mostrem que você **abriu o código**, não chute.

Boa exploração!
