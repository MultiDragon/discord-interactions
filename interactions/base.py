import logging

__all__ = (
    "get_logger",
    "__version__",
    "__authors__",
)

__version__ = "4.3.0-rc.1"

__authors__ = {
    "current": [
        {"name": "DeltaX<@DeltaXWizard>", "status": "Project Maintainer"},
        {"name": "EdVraz<@EdVraz>", "status": "Developer"},
        {"name": "Astrea<@Astrea49>", "status": "Developer"},
        {"name": "Toricane<@Toricane>", "status": "Developer"},
    ],
    "old": [
        {"name": "James Walston<@jameswalston>"},
        {"name": "Daniel Allen<@LordOfPolls>"},
        {"name": "eunwoo1104<@eunwoo1104>"},
    ],
}


get_logger = logging.getLogger
