# Frog generator

# prérequis
Python3 et quelques modules :
* PIL
* random
* glob
* time

un amour des grenouilles


# version API
Je me a disposition une version API en bonus : [ici](https://unicolo.re/api/frog)
![et une grenouille !](https://unicolo.re/api/frog)

# Idée
je suis tombé sur une générateur de grenouilles très simpliste (au niveau du générateur et au niveau du design : [ici](https://frogitivity2.tumblr.com/post/185637054685/ready-to-start-yes-no)) et je me suis dit que je voulais la même chose ! Mais je ne sais pas dessiner...

2 jours plus tard j'avais une version 1 qui me donnait des grenouilles un peu moche.

Dans la version que je presente ici, les paramètres sont pour la plupart ajuster selon des intervales empiriques. j'en ai généré des grenouilles avant de faire un dépot git...

# Génération
La génération est faites en python a partir d'un ensemble de classes. le générateur prends en compte les `seed` pour avoir une grenouille unique. Il gère : la forme, la couleure, les yeux, le nez, la bouche et le chapeau.

la génération peut être faite selon différentes tailles (par defaut 1000×1000)

je ne promet rien mais je vais essayer de faire une documentation dans le code de `frog.py`

le fichier `generator.py` fabrique une grille de X×Y grenouilles avec fond transparent ET un gif avec fond noir des-dites grenouilles

# Art
Pour les bouches et les chapeaux, les formes sont trop complexes à générer mathématiquement : je fais donc appel au travail d'un ami !

Du taf de kalitey : je vous ordonne d'aller jeter un oeil !

unicolor-dream
[ galerie tumblr ](https://unicolor-dream.tumblr.com/)
[ galerie unicolore ](https://gallery.unicolo.re)



