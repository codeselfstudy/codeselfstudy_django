from codeselfstudy.settings import CACHE_BUSTER


def add_cachebuster_to_context(request):
    """Makes a {{ cache_buster }} variable available to all templates."""
    return {
        "cache_buster": CACHE_BUSTER
    }
