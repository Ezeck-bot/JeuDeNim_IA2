from nim import available_actions


def test_empty_board_falsy():
    empty_board = ()

    assert not available_actions(empty_board)


def test_empty_board_empty():
    empty_board = ()
    assert len(available_actions(empty_board)) == 0


def test_documented_example():
    assert {(0, 1), (1, 1), (0, 2)} == set(available_actions([2, 1, 0, 0]))


# TODO: test_available_actions (10 points)
#   Ajouter des tests pour les cas-limites de available_actions
def test_une_pile_avec_un_objet():
    assert set(available_actions((1,))) == {(0, 1)}


def test_plusieurs_piles_sans_doublons():
    actions = available_actions((3, 2, 1))

    assert set(actions) == {
        (0, 1),
        (0, 2),
        (0, 3),
        (1, 1),
        (1, 2),
        (2, 1),
    }
    assert len(actions) == len(set(actions))


def test_piles_vides_ignorees():
    assert set(available_actions((0, 2))) == {(1, 1), (1, 2)}


def test_toutes_les_piles_vides():
    assert not available_actions((0, 0))


def test_nombre_d_actions_egale_la_somme_des_piles():
    board = (4, 0, 2, 5)

    assert len(available_actions(board)) == sum(board)
