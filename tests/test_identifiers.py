"""Tests for canonical requirement identifiers."""

from spec_ep.export import SPEC_ID
from spec_ep.extractor_utils import extract_identifier_notes
from spec_ep.load import load_text
from spec_ep.paths import repo_root


def test_identifiers_are_extractable() -> None:
    """IDENTIFIERS.md contains extractable canonical identifiers."""
    root = repo_root()
    requirements = extract_identifier_notes(
        load_text(root / "IDENTIFIERS.md"),
        expected_prefix=SPEC_ID,
    )

    assert requirements


def test_identifiers_use_expected_prefix() -> None:
    """All canonical identifiers use the prefix."""
    root = repo_root()
    requirements = extract_identifier_notes(
        load_text(root / "IDENTIFIERS.md"),
        expected_prefix=SPEC_ID,
    )

    for requirement in requirements:
        assert requirement.id.startswith("EP.")


def test_identifiers_are_unique() -> None:
    """Canonical identifiers are unique."""
    root = repo_root()
    requirements = extract_identifier_notes(
        load_text(root / "IDENTIFIERS.md"),
        expected_prefix=SPEC_ID,
    )

    identifiers = [requirement.id for requirement in requirements]

    assert len(identifiers) == len(set(identifiers))


def test_identifiers_are_alphabetical() -> None:
    """Canonical identifiers are listed alphabetically."""
    root = repo_root()
    requirements = extract_identifier_notes(
        load_text(root / "IDENTIFIERS.md"),
        expected_prefix=SPEC_ID,
    )

    identifiers = [requirement.id for requirement in requirements]

    assert identifiers == sorted(identifiers)


def test_each_identifier_has_one_note() -> None:
    """Each canonical identifier has one non-empty note."""
    root = repo_root()
    requirements = extract_identifier_notes(
        load_text(root / "IDENTIFIERS.md"),
        expected_prefix=SPEC_ID,
    )

    for requirement in requirements:
        assert requirement.note
        assert requirement.normative_source == f"SPEC.md#{requirement.id}"
