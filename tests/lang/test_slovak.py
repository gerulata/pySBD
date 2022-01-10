# -*- coding: utf-8 -*-
import pytest

GOLDEN_SK_RULES_TEST_CASES = [
    ("Ide o majiteľov firmy ABTrade s. r. o., ktorí stoja aj za ďalšími spoločnosťami, napr. XYZCorp a.s.",
     ["Ide o majiteľov firmy ABTrade s. r. o., ktorí stoja aj za ďalšími spoločnosťami, napr. XYZCorp a.s."]),
    ("„Prieskumy beriem na ľahkú váhu. V podstate ma to nezaujíma,“ reagoval Matovič na prieskum agentúry Focus.",
     ["„Prieskumy beriem na ľahkú váhu. V podstate ma to nezaujíma,“ reagoval Matovič na prieskum agentúry Focus."]),
    ("Toto sa mi podarilo až na 10. pokus, ale stálo to za to.",
     ["Toto sa mi podarilo až na 10. pokus, ale stálo to za to."]),
    ("Ide o príslušníkov XII. Pluku špeciálneho určenia.",
     ["Ide o príslušníkov XII. Pluku špeciálneho určenia."]),
    ("Spoločnosť bola založená 7. Apríla 2020, na zmluve však figuruje dátum 20. marec 2020.",
     ["Spoločnosť bola založená 7. Apríla 2020, na zmluve však figuruje dátum 20. marec 2020."]),
    # Test numbered lists with periods
    ("1. Prvý bod. 2. Druhý bod.",
     ["1. Prvý bod.", "2. Druhý bod."]),
    ("1) Prvý bod. 2) Druhý bod.",
     ["1) Prvý bod.", "2) Druhý bod."]),
    ("• 1. Prvý bod. • 2. Prvý bod",
     ["• 1. Prvý bod.", "• 2. Prvý bod"]),
    # Test bugs on special characters followed by numbers with periods
    ("FCL VW DNV: V3. minúte sme dali gól",
     ["FCL VW DNV: V3. minúte sme dali gól"]),
    ("Oslávili sme naše 25. výročie.",
     ["Oslávili sme naše 25. výročie."])
]


@pytest.mark.parametrize('text,expected_sents', GOLDEN_SK_RULES_TEST_CASES)
def test_sk_sbd(sk_default_fixture, text, expected_sents):
    """Slovak language SBD tests"""
    segments = sk_default_fixture.segment(text)
    segments = [s.strip() for s in segments]
    assert segments == expected_sents
