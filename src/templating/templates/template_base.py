from abc import ABC, abstractmethod

import templating.escapers as esc

class TemplateBase(ABC):

    @property
    @abstractmethod
    def name(self) -> str:
        pass

    @property
    @abstractmethod
    def template_path(self) -> str:
        pass

    @property
    @abstractmethod
    def help(self) -> str:
        pass

    @property
    @abstractmethod
    def escaper(self) -> esc.Escaper:
        pass
