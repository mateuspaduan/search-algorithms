## EPC1 - Solution

1. **Teste de objetivo** -> `FindPath.ObjectiveTest()`: Retorna True se o estado atual é igual ao próximo
**Sucessor** -> `FindPath.ExpandSolution`: Retorna todos os possíveis estados sucessores do atual

2. 
```python
nodes = ['S. R. Sapucaí', 'Pouso Alegre', 'Cambuí', 'Congonhal', 'Camanducaia', 'Borda da Mata',
        'Ipuiúna', 'Bragança Paulista', 'Jacutinga', 'Andradas', 'Atibaia', 'Itapira',
        'Esp. Santo Pinhal', 'Mogi-Guaçu', 'Mogi Mirim', 'Campinas']

edges = [('S. R. Sapucaí', 'Pouso Alegre'), 

        ('Pouso Alegre', 'Cambuí'), ('Cambuí', 'Camanducaia'), ('Camanducaia', 'Bragança Paulista'),
        ('Bragança Paulista', 'Atibaia'), ('Atibaia', 'Campinas'),

        ('Pouso Alegre', 'Borda da Mata'), ('Borda da Mata', 'Jacutinga'), ('Jacutinga', 'Itapira'),
        ('Itapira', 'Campinas'),

        ('Pouso Alegre', 'Congonhal'), ('Congonhal', 'Ipuiúna'), ('Ipuiúna', 'Andradas'), ('Andradas', 'Esp. Santo Pinhal'), ('Esp. Santo Pinhal', 'Mogi-Guaçu'), ('Mogi-Guaçu', 'Mogi Mirim'), ('Mogi Mirim', 'Campinas')
        ]
```

3. [Link for answer on google sheets](https://docs.google.com/spreadsheets/d/1VjdI6rGqSYkzphPShVxeJZG1QmXFsd4paxaL1iQzwpU/edit?usp=sharing)

4.