"""AmritaBot template."""

from typing import ClassVar, Literal

from amctl.templating import BaseTemplate, TmplField, field

__template_ignore___: Literal[False] = False


class ambotTemplate(BaseTemplate):
    """Minimal Python package scaffold template."""

    __template_name__: str = "ambot"
    __template_description__: str = "Template for AmritaBot creation."
    __core_package__: str = "amrita"
    __versions__: tuple[str, ...] = ("1.3.0", "1.2.1", "1.2.0", "1.0.0")
    __tmpl_fields__: ClassVar[dict[str, TmplField]] = {
        "description": field(
            default="My awesome robot.",
            description="Short project description",
        ),
    }

    def on_create(self, project_dir, name, version=None, **fields):
        """Render template with amctl metadata embedded."""
        super().on_create(project_dir, name, version=version, **fields)

    # TODO: Bot management commands


__template_export__ = ambotTemplate
