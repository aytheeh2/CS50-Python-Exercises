from twttr import shorten

def test_shorten():
    assert shorten("Twitter") == "Twttr"
    assert shorten("AppleOu")=="ppl"
    assert shorten("Twi123ttEr") == "Tw123ttr"
    assert shorten("Twit..?er") == "Twt..?r"
