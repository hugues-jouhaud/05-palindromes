#### Fonction secondaire


def ispalindrome(p):
    """Test de vérification d'un palyndrome"""
    txtinverse = p[::-1]
    if txtinverse == p :
        return True
    return False

#### Fonction principale


def main():
    """Test sur des mots"""
    # vos appels à la fonction secondaire ici

    for s in ["radar", "kayak", "level", "rotor", "civique", "deifie"]:
        print(s, ispalindrome(s))


if __name__ == "__main__":
    main()