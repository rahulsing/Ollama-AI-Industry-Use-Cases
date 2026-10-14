"""Discover industry folders (NN_name/ with a catalog.py) and load their catalogs.

Each industry folder contains:
  catalog.py   DOMAIN, CATEGORIES, USE_CASES
  business.py  INDUSTRY_101, AREAS, GLOSSARY, BUSINESS, FLOWS, ASK (optional)
  NN_slug/app.py for every use case
"""

import importlib.util
import re
from pathlib import Path
from types import SimpleNamespace

ROOT = Path(__file__).resolve().parents[1]


def _load(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def load_domains() -> list[SimpleNamespace]:
    domains = []
    for folder in sorted(p for p in ROOT.iterdir() if p.is_dir() and re.match(r"\d{2}_", p.name)):
        if not (folder / "catalog.py").exists():
            continue
        catalog = _load(folder / "catalog.py", f"{folder.name}_catalog")
        business = _load(folder / "business.py", f"{folder.name}_business")
        domains.append(SimpleNamespace(
            folder=folder.name, path=folder, **catalog.DOMAIN,
            categories=catalog.CATEGORIES, use_cases=catalog.USE_CASES,
            industry_101=business.INDUSTRY_101, areas=business.AREAS,
            glossary=business.GLOSSARY, business=business.BUSINESS, flows=business.FLOWS, ask=getattr(business, "ASK", {}),
        ))
    return domains


def load_labs() -> list[dict]:
    """Hands-on labs from labs/catalog.py (kept apart from the industry use cases)."""
    path = ROOT / "labs" / "catalog.py"
    return _load(path, "labs_catalog").LABS if path.exists() else []
