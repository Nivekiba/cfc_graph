# Composante fortement connexe

Ce code est fait à titre éducatif. Il permet de déterminer les composantes fortement connexe d'un graphe

## Utilisation

Pour déterminer les CFC d'un graphe vous devez renseigner le graphe dans le fichier json ```graph.json``` sous forme de liste d'adjence
C'est-à-dire que chaque clé du fichier json est un sommet et le tableau associé à ce sommet est un tableau des suivants
Par exemple le graphe suivant:

![Graphe](graphe_exemple.png)

Aura pour representation en liste d'adjacence:

```
{
  '1': ['2'],
  '2': ['4'],
  '3': ['2', '4'],
  '4': ['3']
}
```

Et c'est donc cette representation qui est mise dans le fichier json.
Ainsi vous pouvez donc lancer le code de recherche des CFC de votre graphe

```
py cfc.py
```
