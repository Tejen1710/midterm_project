"""Unit tests for the dynamic help registry (Decorator pattern)."""

from app.help_registry import register_command, build_help


def test_register_and_build_help():
    """Ensure commands register and appear in help text."""
    @register_command("foo", "Foo does something.")
    def _foo():  # dummy function
        pass

    help_text = build_help(extra_sections=["Extra"])
    # Verify command registration worked
    assert "foo" in help_text
    assert "Foo does something." in help_text
    assert "Extra" in help_text
