## EPC2 - Solution

1) **Teste de objetivo** -> `FindPath.ObjectiveTest`: Retorna True se o estado atual é igual ao próximo\
**Sucessor** -> `FindPath.ExpandSolution`: Retorna todos os possíveis estados sucessores do atual
**Heurística** -> `FindPath.Heuristic`: Retorna a distância em linha reta entre a cidade atual e o destino.

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
    ('Bragança Paulista', 'Itapira'): ,
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
    ('S. R. Sapucaí', 'Pouso Alegre'),
    ('Pouso Alegre', 'Cambuí'),
    ('Cambuí', 'Camanducaia'),
    ('Camanducaia', 'Bragança Paulista'),
    ('Bragança Paulista', 'Atibaia'),
    ('Bragança Paulista', 'Itapira'),
    ('Atibaia', 'Campinas'),
    ('Pouso Alegre', 'Borda da Mata'),
    ('Borda da Mata', 'Jacutinga'),
    ('Jacutinga', 'Itapira'),
    ('Itapira', 'Campinas'),
    ('Pouso Alegre', 'Congonhal'),
    ('Congonhal', 'Ipuiúna'),
    ('Ipuiúna', 'Andradas'),
    ('Andradas', 'Esp. Santo Pinhal'),
    ('Esp. Santo Pinhal', 'Mogi-Guaçu'),
    ('Mogi-Guaçu', 'Mogi Mirim'),
    ('Mogi Mirim', 'Campinas'),
]
```

4. a) A função `ObjectiveTest` 
