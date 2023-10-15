from mylib.logic.business_logic import wiki


def test_wiki():
    assert "god" in wiki()
