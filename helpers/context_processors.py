from django.conf import settings


def add_cachebuster_to_context(request):
    """Makes a {{ cache_buster }} variable available to all templates."""
    return {"cache_buster": settings.CACHE_BUSTER}
