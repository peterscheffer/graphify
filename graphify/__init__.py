"""graphify - extract · build · cluster · analyze · report."""


def __getattr__(name):
    # Lazy imports so `graphify install` works before heavy deps are in place.
    _EXPORT_MODULE = "graphify.export"
    _ANALYZE_MODULE = "graphify.analyze"
    _BUILD_MODULE = "graphify.build"
    _CLUSTER_MODULE = "graphify.cluster"
    _EXTRACT_MODULE = "graphify.extract"
    _REPORT_MODULE = "graphify.report"
    _WIKI_MODULE = "graphify.wiki"
    _map = {
        "extract": (_EXTRACT_MODULE, "extract"),
        "collect_files": (_EXTRACT_MODULE, "collect_files"),
        "build_from_json": (_BUILD_MODULE, "build_from_json"),
        "cluster": (_CLUSTER_MODULE, "cluster"),
        "score_all": (_CLUSTER_MODULE, "score_all"),
        "cohesion_score": (_CLUSTER_MODULE, "cohesion_score"),
        "god_nodes": (_ANALYZE_MODULE, "god_nodes"),
        "surprising_connections": (_ANALYZE_MODULE, "surprising_connections"),
        "suggest_questions": (_ANALYZE_MODULE, "suggest_questions"),
        "generate": (_REPORT_MODULE, "generate"),
        "to_json": (_EXPORT_MODULE, "to_json"),
        "to_html": (_EXPORT_MODULE, "to_html"),
        "to_svg": (_EXPORT_MODULE, "to_svg"),
        "to_canvas": (_EXPORT_MODULE, "to_canvas"),
        "to_wiki": (_WIKI_MODULE, "to_wiki"),
    }
    if name in _map:
        import importlib
        mod_name, attr = _map[name]
        mod = importlib.import_module(mod_name)
        return getattr(mod, attr)
    raise AttributeError(f"module 'graphify' has no attribute {name!r}")
