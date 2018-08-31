## EPC2 - Solution

1) **Teste de objetivo** - `FindPath.ObjectiveTest`: Retorna True se o estado atual é igual ao próximo\
**Sucessor** - `FindPath.ExpandSolution`: Retorna todos os possíveis estados sucessores do atual\
**Heurística** - `FindPath.Heuristic`: Retorna a distância em linha reta entre a cidade atual e o destino.

2)
```python
custo_linha_reta = {
    ('S. R. Sapucaí', 'Campinas'): 165,
    ('Pouso Alegre', 'Campinas'): 137,
    ('Cambuí', 'Campinas'): 108,
    ('Congonhal', 'Campinas'): 135,
    ('Camanducaia', 'Campinas'): 97,
    ('Borda da Mata', 'Campinas'): 117,
    ('Bragança Paulista', 'Campinas'): 54,
    ('Ipuiúna', 'Campinas'): 139,
    ('Jacutinga', 'Campinas'): 84,
    ('Andradas', 'Campinas'): 106,
    ('Atibaia', 'Campinas'): 57,
    ('Itapira', 'Campinas'): 58,
    ('Esp. Santo Pinhal', 'Campinas'): 86,
    ('Mogi-Guaçu', 'Campinas'): 62,
    ('Mogi Mirim', 'Campinas'): 54,
    ('Campinas', 'Campinas'): 0,
}
```

3)
```python
nodes = [
    'S. R. Sapucaí', 'Pouso Alegre', 'Cambuí',
    'Congonhal', 'Camanducaia', 'Borda da Mata',
    'Ipuiúna', 'Bragança Paulista', 'Jacutinga',
    'Andradas', 'Atibaia', 'Itapira', 'Esp. Santo Pinhal',
    'Mogi-Guaçu', 'Mogi Mirim', 'Campinas'
]

edges = [
    ('S. R. Sapucaí',     'Pouso Alegre'),      ('Pouso Alegre',      'S. R. Sapucaí'),
    ('Pouso Alegre',      'Cambuí'),            ('Cambuí',            'Pouso Alegre'),
    ('Cambuí',            'Camanducaia'),       ('Camanducaia',       'Cambuí'),
    ('Camanducaia',       'Bragança Paulista'), ('Bragança Paulista', 'Camanducaia'),
    ('Bragança Paulista', 'Atibaia'),           ('Atibaia',           'Bragança Paulista'),
    ('Bragança Paulista', 'Itapira'),           ('Itapira',           'Bragança Paulista'),
    ('Atibaia',           'Campinas'),          ('Campinas',          'Atibaia'),
    ('Pouso Alegre',      'Borda da Mata'),     ('Borda da Mata',     'Pouso Alegre'),
    ('Borda da Mata',     'Jacutinga'),         ('Jacutinga',         'Borda da Mata'),
    ('Jacutinga',         'Itapira'),           ('Itapira',           'Jacutinga'),
    ('Itapira',           'Campinas'),          ('Campinas',          'Itapira'),
    ('Pouso Alegre',      'Congonhal'),         ('Congonhal',         'Pouso Alegre'),
    ('Congonhal',         'Ipuiúna'),           ('Ipuiúna',           'Congonhal'),
    ('Ipuiúna',           'Andradas'),          ('Andradas',          'Ipuiúna'),
    ('Andradas',          'Esp. Santo Pinhal'), ('Esp. Santo Pinhal', 'Andradas'),
    ('Esp. Santo Pinhal', 'Mogi-Guaçu'),        ('Mogi-Guaçu',        'Esp. Santo Pinhal'),
    ('Mogi-Guaçu',        'Mogi Mirim'),        ('Mogi Mirim',        'Mogi-Guaçu'),
    ('Mogi Mirim',        'Campinas'),          ('Campinas',          'Mogi Mirim'),
]
```

4) a) A função `ObjectiveTest` verifica se um estado representa o estado objetivo simplesmente comparando o atual com o objetivo.

Exemplo:
```python
ObjectiveTest("Santa Rita", "Campinas") -> False
ObjectiveTest("Pouso Alegre", "Campinas") -> False
ObjectiveTest("Cambuí", "Campinas") -> False
ObjectiveTest("Camanducaia", "Campinas") -> False
ObjectiveTest("Bragança Paulista", "Campinas") -> False
ObjectiveTest("Atibaia", "Campinas") -> False
ObjectiveTest("Campinas", "Campinas") -> True
```

5) a) A função `Heuristic` receberá como parâmetros: `current = "Pouso Alegre"`  e `target = "Campinas"`. Ao dar um `.get()` no dicionário `custo_linha_reta` com esses parâmetros, receberá `137`, que é a distância em linha reta entre Pouso Alegre e Campinas, e o valor que será retornado pela função.\
b) PathFindingWithCostExample.py: `Pouso Alegre -> Cambuí -> Camanducaia -> Bragança Paulista -> Atibaia -> Campinas`\
PathFindingExample.py: `S. R. Sapucaí -> Pouso Alegre -> Borda da Mata -> Jacutinga -> Itapira -> Campinas`

6) Mudanças para adaptar o código para funcionar como um algoritmo A*: [commit diff](https://github.com/mugbug/search-algorithms/commit/b77932edf52ae54bd69afac9f78c1d8b9367f386)

7) **A*:** Distância final entre Pouso Alegre e Campinas: 225.00km\
**Busca gulosa:** Distância final entre Pouso Alegre e Campinas: 225.00km